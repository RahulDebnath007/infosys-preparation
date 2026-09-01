# Maximum Score Subsequence

## 📌 Problem Statement

You are given an array of integers `A`.

We need to select a **subsequence** of the array such that:

1. The selected elements maintain their original order.
2. Every two consecutive selected elements satisfy at least one of the following relationships:

```text
x = 2y
x = 3y
x = y + 1
x = y - 1
x = y / 2
x = y / 3
```

The **score** of a selected element is equal to its number of divisors.

Therefore:

```text
Score = sum of number of divisors of selected elements
```

The objective is to find the **maximum possible score**.

---

# 🧠 Understanding the Problem

Suppose we have:

```text
A = [2, 3, 4, 5]
```

We can select:

```text
2 → 3 → 4 → 5
```

because:

```text
3 = 2 + 1
4 = 3 + 1
5 = 4 + 1
```

The score is:

```text
divisors(2) + divisors(3) + divisors(4) + divisors(5)
```

Number of divisors:

```text
2 → 2
3 → 2
4 → 3
5 → 2
```

Therefore:

```text
Score = 2 + 2 + 3 + 2
      = 9
```

---

# 💡 Key Observation

This is a **Dynamic Programming on Subsequence** problem.

For every current value:

```text
x = A[i]
```

we need to know:

> What is the best score of a valid subsequence that can come immediately before `x`?

Instead of checking every previous element, we determine exactly which values can be connected to `x`.

---

# 🔗 Finding Compatible Previous Values

The allowed relationships are:

```text
x = 2y
x = 3y
x = y + 1
x = y - 1
x = y / 2
x = y / 3
```

We rearrange these equations to find possible values of `y`.

For the current value `x`, possible previous values are:

```text
x - 1
x + 1
2x
3x
x / 2
x / 3
```

The division cases are valid only when the division produces an integer.

Therefore:

```python
if x % 2 == 0:
    x // 2
```

and:

```python
if x % 3 == 0:
    x // 3
```

---

# 🎯 Pattern Used

## Dynamic Programming + HashMap

The main pattern is:

```text
DP on Subsequence
        +
HashMap
```

We use a HashMap to store the best score associated with every value.

---

# 🧠 DP State

We maintain:

```python
best[value]
```

where:

> `best[value]` represents the maximum score of a valid subsequence ending with `value`.

For example:

```text
best[2] = 2
best[3] = 4
best[4] = 7
```

means:

```text
Best subsequence ending at 2 → score 2
Best subsequence ending at 3 → score 4
Best subsequence ending at 4 → score 7
```

---

# 🔄 DP Transition

For every current value `x`:

```text
x = A[i]
```

find all compatible previous values:

```text
x - 1
x + 1
2x
3x
x / 2
x / 3
```

Then:

```text
previous = maximum(best[y])
```

for all compatible `y`.

Finally:

```text
current_score = previous + divisor_count(x)
```

So the main DP formula is:

```text
dp[x] =
    divisor_count(x)
    +
    max(best[compatible values])
```

---

# 🧱 Starting a New Subsequence

The current element does not necessarily need to extend an existing subsequence.

It can start a new subsequence by itself.

Therefore:

```python
previous = 0
```

If no compatible previous value exists:

```text
current_score = divisor_count(x)
```

---

# 🔢 Counting Divisors

We need the number of divisors for every selected number.

A naive approach would check:

```text
1 → x
```

This takes:

```text
O(x)
```

which is inefficient.

Instead, we only check up to:

```text
√x
```

because divisors come in pairs.

For example:

```text
12
```

has divisor pairs:

```text
1 × 12
2 × 6
3 × 4
```

So we only need to check:

```text
1, 2, 3
```

---

# ⚡ Optimized Divisor Counting

```python
from math import isqrt

def divisor_count(x):
    count = 0

    for d in range(1, isqrt(x) + 1):
        if x % d == 0:
            count += 1

            if d * d != x:
                count += 1

    return count
```

### Why `d * d != x`?

If `x` is a perfect square, the divisor pair contains the same number twice.

For example:

```text
9 = 3 × 3
```

We should count `3` only once.

Therefore:

```python
if d * d != x:
    count += 1
```

prevents double counting.

---

# 🔍 Example — Divisor Count

For:

```text
x = 12
```

Check values up to:

```text
√12 ≈ 3
```

### `d = 1`

```text
12 % 1 == 0
```

Divisors:

```text
1 and 12
```

Count:

```text
2
```

### `d = 2`

Divisors:

```text
2 and 6
```

Count:

```text
4
```

### `d = 3`

Divisors:

```text
3 and 4
```

Count:

```text
6
```

Therefore:

```text
divisor_count(12) = 6
```

---

# 💻 Python 3 Solution

```python
from math import isqrt


def divisor_count(x):
    count = 0

    for d in range(1, isqrt(x) + 1):
        if x % d == 0:
            count += 1

            if d * d != x:
                count += 1

    return count


def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    best = {}
    answer = 0

    for x in arr:

        # Possible previous values
        candidates = [
            x - 1,
            x + 1,
            2 * x,
            3 * x
        ]

        if x % 2 == 0:
            candidates.append(x // 2)

        if x % 3 == 0:
            candidates.append(x // 3)

        previous = 0

        # Find the best compatible subsequence
        for y in candidates:
            previous = max(previous, best.get(y, 0))

        # Add the contribution of the current value
        current = previous + divisor_count(x)

        # Store the best score ending with x
        best[x] = max(best.get(x, 0), current)

        # Update global maximum
        answer = max(answer, current)

    print(answer)


solve()
```

---

# 🔎 Code Explanation

## Step 1 — Read Input

```python
n = int(input())
arr = list(map(int, input().split()))
```

We read the number of elements and the array.

---

## Step 2 — Create DP HashMap

```python
best = {}
```

This stores:

```text
value → maximum score ending with that value
```

---

## Step 3 — Process Array from Left to Right

```python
for x in arr:
```

This is critical because the selected elements must form a **subsequence**.

Processing from left to right guarantees that we only use DP states created by elements appearing earlier in the array.

---

# Step 4 — Generate Compatible Values

```python
candidates = [
    x - 1,
    x + 1,
    2 * x,
    3 * x
]
```

Then handle the division cases:

```python
if x % 2 == 0:
    candidates.append(x // 2)

if x % 3 == 0:
    candidates.append(x // 3)
```

---

# Step 5 — Find the Best Previous State

```python
previous = 0

for y in candidates:
    previous = max(previous, best.get(y, 0))
```

`best.get(y, 0)` means:

```text
If y exists:
    return best[y]

Otherwise:
    return 0
```

We take the maximum because we want the highest possible score.

---

# Step 6 — Calculate Current Score

```python
current = previous + divisor_count(x)
```

The current number contributes its number of divisors.

For example:

```text
previous = 7
divisor_count(12) = 6
```

then:

```text
current = 7 + 6
        = 13
```

---

# Step 7 — Update DP

```python
best[x] = max(best.get(x, 0), current)
```

If `x` has already appeared, we keep whichever subsequence gives the better score.

---

# Step 8 — Update Answer

```python
answer = max(answer, current)
```

The optimal subsequence can end at any element, so we keep the global maximum.

---

# 🚶 Example Walkthrough

Consider:

```text
A = [2, 3, 4, 5]
```

### Process `2`

No compatible previous element exists.

```text
divisor_count(2) = 2
```

Therefore:

```text
best[2] = 2
```

---

### Process `3`

Compatible previous values:

```text
2, 4, 6, 9
```

`2` exists:

```text
best[2] = 2
```

Divisor count:

```text
divisor_count(3) = 2
```

Therefore:

```text
current = 2 + 2
        = 4
```

```text
best[3] = 4
```

---

### Process `4`

Compatible previous values include:

```text
3
5
8
12
2
```

Existing states:

```text
best[3] = 4
best[2] = 2
```

Best previous score:

```text
4
```

Divisor count:

```text
divisor_count(4) = 3
```

Therefore:

```text
current = 4 + 3
        = 7
```

```text
best[4] = 7
```

---

### Process `5`

Compatible previous value:

```text
4
```

We have:

```text
best[4] = 7
```

Divisor count:

```text
divisor_count(5) = 2
```

Therefore:

```text
current = 7 + 2
        = 9
```

Final answer:

```text
9
```

---

# 📊 DP Table

For:

```text
A = [2, 3, 4, 5]
```

| Current Value | Divisor Count | Best Previous Score | Current Score |
| ------------: | ------------: | ------------------: | ------------: |
|           `2` |             2 |                   0 |             2 |
|           `3` |             2 |                   2 |             4 |
|           `4` |             3 |                   4 |             7 |
|           `5` |             2 |                   7 |             9 |

Therefore:

```text
Maximum Score = 9
```

---

# 🔥 Why This Is DP

At every element, we are asking:

> What is the best answer I can get if this element is the last element of my subsequence?

That is exactly a DP state.

The state is:

```text
best[x]
```

and the transition is:

```text
best[x] =
divisor_count(x)
+
best compatible previous state
```

---

# ⚡ Why HashMap Is Important

Without a HashMap, we might search all previous elements for every `x`.

That could take:

```text
O(N²)
```

With:

```python
best.get(y, 0)
```

we can directly find the best score associated with a value.

There are only a constant number of compatible values for each `x`.

Therefore, the DP portion takes approximately:

```text
O(N)
```

---

# ⚠️ Common Mistakes

## 1. Sorting the Array

Do **not** sort the array.

The problem requires a subsequence, so the original order must be preserved.

---

## 2. Checking Every Previous Element

Avoid:

```text
For every x:
    scan all previous elements
```

This leads to:

```text
O(N²)
```

Generate only the six possible compatible values.

---

## 3. Forgetting the Division Conditions

Do not blindly use:

```python
x // 2
x // 3
```

For example:

```text
5 // 2 = 2
```

but:

```text
5 / 2 = 2.5
```

So `2` is not a valid candidate from the `x / 2` relationship.

Use:

```python
if x % 2 == 0:
```

and:

```python
if x % 3 == 0:
```

---

## 4. Counting Divisors in O(x)

Checking all values from `1` to `x` is unnecessary.

Use the square-root technique:

```text
O(√x)
```

---

## 5. Overwriting a Better DP State

Do not blindly write:

```python
best[x] = current
```

because `x` can appear multiple times.

Instead:

```python
best[x] = max(best.get(x, 0), current)
```

---

# 📈 Complexity Analysis

Let:

```text
N = number of elements
M = maximum value in the array
```

### DP Complexity

For every element, we check at most six compatible values.

HashMap lookup is:

```text
O(1)
```

on average.

Therefore:

```text
DP Time = O(N)
```

### Divisor Counting

For every element `x`, divisor counting takes:

```text
O(√x)
```

Therefore, in the worst case:

```text
O(N√M)
```

### Overall

```text
Time Complexity:  O(N√M)
Space Complexity: O(N)
```

The `O(N)` space is used by the `best` HashMap.

---

# 🧠 Pattern Recognition

This problem combines several important DSA patterns.

### Pattern 1 — DP on Subsequence

If you see:

```text
Select elements
+
Maintain original order
+
Maximize score
```

think:

```text
Dynamic Programming
```

---

### Pattern 2 — DP by Value

Instead of:

```text
dp[i]
```

we maintain:

```text
best[value]
```

because the compatibility condition depends on the **value** of the previous element.

---

### Pattern 3 — HashMap DP

If only a small number of previous values can connect to the current value, store DP results in a HashMap.

---

### Pattern 4 — Number Theory

The score depends on the number of divisors, so use:

```text
Divisor counting → √N optimization
```

---

# 🔑 Key Takeaways

1. Process the array **left to right** to preserve subsequence order.

2. For current `x`, possible previous values are:

```text
x - 1
x + 1
2x
3x
x/2
x/3
```

3. Store the best score for each value:

```python
best[x]
```

4. Calculate:

```text
current =
best compatible score
+
number of divisors of x
```

5. Count divisors using the square-root technique.

6. Use a HashMap to avoid an `O(N²)` search.

---

# 🎯 Final Mental Model

```text
              Current x
                  ↓
       Find compatible values
                  ↓
     ┌────┬────┬────┬────┬────┬────┐
     ↓    ↓    ↓    ↓    ↓    ↓
    x-1  x+1   2x   3x  x/2  x/3
     └────┴────┴────┴────┴────┴────┘
                  ↓
          Check best[value]
                  ↓
        Take maximum previous
                  ↓
       + divisor_count(x)
                  ↓
             best[x]
                  ↓
          Update answer
```

The core formula to remember is:

```text
best[x] = divisor_count(x) + max(best[compatible values])
```

## 🚀 One-Line Exam Recall

> **For every element `x`, find the best DP score among its six compatible previous values, add the number of divisors of `x`, and store the result in a HashMap.**

### Pattern

```text
Dynamic Programming + HashMap
```

### Supporting Technique

```text
Divisor Counting using √N
```

### Complexity

```text
Time  → O(N√M)
Space → O(N)
```
