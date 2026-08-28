# ⚖️ Equal Sum Swaps

## Problem

Given two warehouses `A` and `B` of crate weights, find all pairs `(a, b)` — `a` from `A`, `b` from `B` — such that swapping `a` and `b` makes the total weight of both warehouses equal.

Output rules:
- Pairs where `a × b` is **even** are listed first.
- Pairs where `a × b` is **odd** are listed after.
- If no valid pair exists, print `-1`.

### Input Format
```
Line 1: space-separated integers for warehouse A
Line 2: space-separated integers for warehouse B
```

### Output Format
```
a,b,a,b,...
```
(comma-separated, even-product pairs first, then odd-product pairs; `-1` if none)

### Example
```
Input:
8 7
4 3

Output:
8,4,7,3
```

### Constraints
- `1 ≤ |A|, |B| ≤ 10^5`

---

## Key Insight

Let `sumA = sum(A)`, `sumB = sum(B)`. Swapping `a` and `b` gives:

```
sumA - a + b = sumB - b + a
```

Solving:

```
sumA - sumB = 2(a - b)
diff = sumA - sumB
a - b = diff / 2  →  target = diff // 2
b = a - target
```

**If `diff` is odd, no valid pair can exist** (target wouldn't be an integer) → print `-1`.

## Efficient Approach

Brute force (`O(|A| × |B|)`) is too slow for `10^5` elements. Instead:

1. Compute `target = (sumA - sumB) // 2`.
2. Build `setB = set(B)` for O(1) lookups.
3. For each `a` in `A`, compute `b = a - target` and check if `b` is in `setB`.
4. Classify each valid pair by whether `a × b` is even or odd.
5. Print even-product pairs, then odd-product pairs. If none found, print `-1`.

## Solution (Python 3)

```python
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sumA, sumB = sum(A), sum(B)
diff = sumA - sumB

if diff % 2 != 0:
    print(-1)
    exit()

target = diff // 2
setB = set(B)

even_pairs = []
odd_pairs = []

for a in A:
    b = a - target
    if b in setB:
        pair = f"{a},{b}"
        if (a * b) % 2 == 0:
            even_pairs.append(pair)
        else:
            odd_pairs.append(pair)

if not even_pairs and not odd_pairs:
    print(-1)
else:
    print(",".join(even_pairs + odd_pairs))
```

## Complexity

| | Complexity |
|---|---|
| Time | `O(|A| + |B|)` |
| Space | `O(|B| + P)` where `P` = number of valid output pairs |

## Common Mistakes

- ❌ Brute-force nested loops (`O(N²)`) — use a hash set instead.
- ❌ Skipping the `diff % 2 != 0` check before dividing.
- ❌ Using `b = a + target` instead of `b = a - target`.
- ❌ Printing odd-product pairs before even-product pairs.

## Pattern Summary

**Equal sums → derive difference → required `b` → set lookup → classify even/odd.**

A Math + Hashing + Array Traversal pattern common in coding assessments.