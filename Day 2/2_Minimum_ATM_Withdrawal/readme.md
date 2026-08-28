# 💳 Minimum ATM Withdrawals

A sliding-window / two-pointer solution to the classic "take from either end" array problem.

## Problem

There's an ATM represented by an array of numbers. You can withdraw money only from the **left end** or the **right end** of the array. Given a target amount `X`, find the **minimum number of withdrawals** needed to withdraw **exactly** `X`.

If it's impossible, output `-1`.

### Input Format

```
N
a[0] a[1] ... a[N-1]
X
```

- Line 1: integer `N` — size of the array
- Line 2: `N` space-separated integers — the ATM array
- Line 3: integer `X` — the required withdrawal amount

### Output Format

A single integer: the minimum number of withdrawals, or `-1` if impossible.

### Example

**Input**
```
5
1 1 4 2 3
5
```

**Output**
```
2
```

## Constraints

- `1 ≤ N ≤ 10⁵`
- `1 ≤ ATM[i] ≤ 10⁵`
- `1 ≤ X ≤ 10⁹`

## Key Insight

Trying every combination of left/right picks is complicated and slow. Instead, **reverse the perspective**:

> Whatever you *don't* withdraw stays behind as one continuous subarray in the middle.

So:

```
Total = Withdrawn + Remaining
target = Total - X
```

The problem becomes: **find the longest contiguous subarray whose sum equals `target`.**

If the longest such subarray has length `maxLen`:

```
Minimum Withdrawals = N - maxLen
```

Since all `ATM[i] ≥ 1`, the classic positive-sum **sliding window** technique applies directly.

## Algorithm

1. Compute `total = sum(atm)`.
2. Compute `target = total - X`.
   - If `target < 0` → `X > total`, impossible → return `-1`.
   - If `target == 0` → the entire array must be withdrawn → return `N`.
3. Slide a window `[left, right]` across the array, tracking `currSum`:
   - Expand by moving `right` forward, adding `atm[right]`.
   - While `currSum > target`, shrink from the left.
   - Whenever `currSum == target`, update `maxLen = max(maxLen, right - left + 1)`.
4. If no window ever matched `target`, return `-1`.
5. Otherwise return `N - maxLen`.

### Why Sliding Window Works

Because every element is positive:
- Moving `right` forward only **increases** the sum.
- Moving `left` forward only **decreases** the sum.

This monotonic behavior means both pointers only ever move forward — never backward — giving an efficient single pass.

## Dry Run

```
ATM = [1, 1, 4, 2, 3], X = 5
total = 11
target = 11 - 5 = 6
```

| right | atm[right] | currSum | action | window | maxLen |
|-------|-----------|---------|--------|--------|--------|
| 0 | 1 | 1 | expand | [1] | -1 |
| 1 | 1 | 2 | expand | [1,1] | -1 |
| 2 | 4 | 6 | match! | [1,1,4] | 3 |
| 3 | 2 | 8→7→6 | shrink twice, match | [4,2] | 3 |
| 4 | 3 | 9→5 | shrink | [2,3]... | 3 |

`maxLen = 3` → `answer = 5 - 3 = 2`

This corresponds to withdrawing `3 + 2 = 5` from the right end in 2 withdrawals.

## Solution (Python 3)

```python
def minWithdrawals(atm, X):
    total = sum(atm)
    target = total - X

    # X is greater than the total available amount
    if target < 0:
        return -1

    # X equals the total amount
    if target == 0:
        return len(atm)

    n = len(atm)
    left = 0
    currSum = 0
    maxLen = -1

    # Find the longest subarray with sum = target
    for right in range(n):
        currSum += atm[right]

        while currSum > target and left <= right:
            currSum -= atm[left]
            left += 1

        if currSum == target:
            maxLen = max(maxLen, right - left + 1)

    # No subarray with the required sum
    if maxLen == -1:
        return -1

    return n - maxLen


if __name__ == "__main__":
    n = int(input().strip())

    atm = list(map(int, input().split()))

    while len(atm) < n:
        atm.extend(map(int, input().split()))

    X = int(input().strip())

    print(minWithdrawals(atm, X))
```

## Complexity

| | Complexity |
|---|---|
| Time | `O(N)` — both pointers move forward only, each at most `N` steps |
| Space (auxiliary) | `O(1)` |
| Space (including input) | `O(N)` |

## Edge Cases

| Case | Example | Result |
|---|---|---|
| `X > total` | `ATM=[1,2,3]`, `X=10` | `-1` (impossible) |
| `X == total` | `ATM=[1,2,3]`, `X=6` | `3` (withdraw everything) |
| No valid subarray sums to `target` | `ATM=[2,4,6]`, `X=5` | `-1` |

## Common Mistakes

- **Brute-forcing every left/right combination** — this is `O(N²)` or worse and too slow for `N ≤ 10⁵`.
- **Confusing `target` with `X`** — remember `target = total - X`, not `X` itself.
- **Finding *any* matching subarray instead of the longest one** — a longer remaining subarray means fewer elements removed, i.e. fewer withdrawals.
- **Applying this sliding-window approach to arrays with negative numbers** — it relies on all values being positive so the sum changes monotonically as pointers move.

## Pattern Recognition

| Clue in the problem | What to think |
|---|---|
| "Take elements from either end" | 🔄 Reverse the perspective |
| Need an exact amount `X` | 🎯 Target sum |
| Elements removed from ends | 🧩 What remains is one middle subarray |
| Minimize withdrawals | 📏 Maximize remaining length |
| All values positive | 🪟 Sliding window applies |

## One-Line Memory Trick

> `total - X → longest subarray → N - maxLen`

This is a classic **Two Pointers + Sliding Window + Problem Transformation** exercise.