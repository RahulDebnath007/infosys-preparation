# Maximum Total Value After Decreasing

## 📌 Problem Statement

You are given `N` items, each having an initial value.

You must choose **exactly one item every day**.

After each day:

* Every item that has not been chosen decreases by `1`.
* An item's value cannot go below `0`.
* The value obtained from an item is the value it has **when it is chosen**.

The goal is to maximize the **total value collected** after choosing one item per day.

---

# 🧠 Understanding the Problem

Suppose:

```text
A = [5, 3, 2]
```

We have three days and must choose one item each day.

The best strategy is to choose the largest available value first.

### Day 1

Choose:

```text
5
```

Contribution:

```text
5
```

The remaining values decrease by `1`:

```text
3 → 2
2 → 1
```

### Day 2

Choose the largest remaining value:

```text
2
```

Contribution:

```text
2
```

The last item decreases:

```text
1 → 0
```

### Day 3

Choose:

```text
0
```

Contribution:

```text
0
```

Total:

```text
5 + 2 + 0 = 7
```

Therefore:

```text
Answer = 7
```

---

# 💡 Key Observation

The optimal strategy is:

> **Always choose the largest value available.**

Why?

If we choose a smaller value while a larger value is available, the larger value will lose `1` before we eventually use it.

Suppose:

```text
a > b
```

If we choose `b` first:

```text
b + max(0, a - 1)
```

If we choose `a` first:

```text
a + max(0, b - 1)
```

Choosing `a` first is never worse.

Therefore, the largest value should always be selected first.

This gives us a **Greedy** solution.

---

# 🎯 Pattern Used

## Greedy + Sorting

The problem follows this pattern:

```text
Greedy
   +
Sorting
```

We sort all values in descending order.

Then:

```text
Largest value → Day 0
Second largest → Day 1
Third largest → Day 2
...
```

---

# 🔄 Important Formula

Suppose an item has initial value:

```text
value
```

and we select it on:

```text
day
```

Since it loses `1` for every previous day:

```text
remaining value = value - day
```

But the value cannot become negative.

Therefore:

```python
max(0, value - day)
```

is the contribution of that item.

So the total answer is:

```text
sum(max(0, A[i] - i))
```

after sorting `A` in descending order.

---

# 🔍 Example

Consider:

```text
A = [5, 3, 2]
```

After sorting:

```text
[5, 3, 2]
```

Calculate each contribution:

| Day | Initial Value | Decrease | Final Value | Contribution |
| --: | ------------: | -------: | ----------: | -----------: |
|   0 |             5 |        0 |           5 |            5 |
|   1 |             3 |        1 |           2 |            2 |
|   2 |             2 |        2 |           0 |            0 |

Therefore:

```text
5 + 2 + 0 = 7
```

---

# 💻 Python 3 Solution

```python
def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    # Choose larger values earlier
    arr.sort(reverse=True)

    MOD = 10**9 + 7
    answer = 0

    for day, value in enumerate(arr):
        answer += max(0, value - day)

    print(answer % MOD)


solve()
```

---

# 🔍 Code Explanation

## Step 1 — Read Input

```python
n = int(input())
arr = list(map(int, input().split()))
```

We read:

```text
n → number of items
arr → initial values
```

---

# Step 2 — Sort in Descending Order

```python
arr.sort(reverse=True)
```

For example:

```text
Before:

[3, 5, 2, 8]

After:

[8, 5, 3, 2]
```

This means the largest item is selected first.

---

# Step 3 — Process Each Day

```python
for day, value in enumerate(arr):
```

`enumerate()` gives us:

```text
day
value
```

For example:

```text
day = 0 → first item
day = 1 → second item
day = 2 → third item
```

---

# Step 4 — Calculate Remaining Value

```python
max(0, value - day)
```

If:

```text
value = 5
day = 2
```

then:

```text
5 - 2 = 3
```

Contribution:

```text
3
```

If:

```text
value = 2
day = 5
```

then:

```text
2 - 5 = -3
```

But values cannot become negative.

Therefore:

```text
max(0, -3) = 0
```

---

# Step 5 — Add to Answer

```python
answer += max(0, value - day)
```

We add each item's value at the time it is selected.

---

# Step 6 — Apply Modulo

```python
print(answer % MOD)
```

where:

```python
MOD = 10**9 + 7
```

The modulo keeps the final result within the required range.

---

# 🚶 Example Walkthrough

Consider:

```text
A = [5, 3, 2]
```

### Initial Array

```text
[5, 3, 2]
```

Already sorted.

---

### Day 0

Choose:

```text
5
```

Contribution:

```text
5 - 0 = 5
```

---

### Day 1

The value `3` has decreased by one:

```text
3 - 1 = 2
```

Contribution:

```text
2
```

---

### Day 2

The value `2` has decreased twice:

```text
2 - 2 = 0
```

Contribution:

```text
0
```

---

### Total

```text
5 + 2 + 0
= 7
```

Therefore:

```text
Answer = 7
```

---

# 📊 Dry Run

For:

```text
A = [8, 5, 3, 2]
```

| Day | Value | `value - day` | Contribution |
| --: | ----: | ------------: | -----------: |
|   0 |     8 |             8 |            8 |
|   1 |     5 |             4 |            4 |
|   2 |     3 |             1 |            1 |
|   3 |     2 |            -1 |            0 |

Total:

```text
8 + 4 + 1 + 0 = 13
```

So:

```text
Answer = 13
```

---

# 🧠 Why Sorting Works

The decrease happens based on **time**.

An item selected later has suffered more decreases.

Therefore, expensive items should be used as early as possible.

Consider:

```text
A = [10, 2]
```

### Correct order

Choose `10` first:

```text
10 + 1 = 11
```

### Wrong order

Choose `2` first:

```text
2 + 9 = 11
```

Here both happen to produce the same result.

But generally, choosing the larger value first is never worse.

For example:

```text
A = [10, 1, 1]
```

Largest-first:

```text
10 + 0 + 0 = 10
```

Any ordering cannot improve upon using the largest available value first.

The exchange argument is the reason the greedy strategy is valid.

---

# 🔄 Exchange Argument

Suppose two values are:

```text
a > b
```

and we have two consecutive days.

### Option 1 — Larger value first

```text
a + max(0, b - 1)
```

### Option 2 — Smaller value first

```text
b + max(0, a - 1)
```

If both values remain positive:

```text
Option 1 = a + b - 1
Option 2 = b + a - 1
```

They are equal.

If the smaller value reaches zero:

```text
Option 1 = a
Option 2 = b + (a - 1)
```

Since:

```text
a > b
```

choosing the larger value first is at least as good.

Therefore, larger values can safely be moved earlier.

Repeating this argument means the array can be sorted in descending order.

---

# ⚠️ Common Mistakes

## 1. Sorting in Ascending Order

Incorrect:

```python
arr.sort()
```

This selects smaller values first and allows larger values to decrease unnecessarily.

Use:

```python
arr.sort(reverse=True)
```

---

## 2. Forgetting the Decrease

Do not simply calculate:

```python
sum(arr)
```

The values decrease based on the day they are selected.

The correct contribution is:

```python
value - day
```

---

## 3. Allowing Negative Values

Incorrect:

```python
answer += value - day
```

This could add negative values.

Use:

```python
answer += max(0, value - day)
```

because an item's value stops decreasing at zero.

---

## 4. Confusing Index With Day

Fortunately, after sorting, the index represents the day:

```python
for day, value in enumerate(arr):
```

So:

```text
index 0 → day 0
index 1 → day 1
index 2 → day 2
```

---

# 🧩 Pattern Recognition

This is a classic **Greedy + Sorting** problem.

Look for this pattern when:

* You have multiple items/jobs.
* Their value decreases as time passes.
* You must choose one item per time step.
* Choosing an item earlier prevents it from losing as much value.
* The largest/currently most valuable item should be prioritized.

Typical thought process:

```text
Value changes with time
        ↓
Who should be selected first?
        ↓
Largest value
        ↓
Sort descending
        ↓
Apply time-based decrease
```

---

# 📈 Complexity Analysis

Let:

```text
N = number of items
```

### Sorting

```text
O(N log N)
```

because we sort the array.

### Traversal

```text
O(N)
```

because every item is processed exactly once.

Therefore:

```text
Overall Time Complexity = O(N log N)
```

---

## Space Complexity

Python's sorting uses additional internal memory.

For the algorithm itself, we only maintain a few variables.

Conceptually:

```text
Extra Space = O(1)
```

excluding the sorting implementation's internal memory.

---

# 🔑 Key Takeaways

### 1. Choose the largest value first

```text
Largest → earliest day
```

### 2. Sort descending

```python
arr.sort(reverse=True)
```

### 3. Account for the number of previous days

```python
value - day
```

### 4. Never allow negative contribution

```python
max(0, value - day)
```

### 5. Sum all contributions

```python
answer += max(0, value - day)
```

### 6. Apply modulo at the end

```python
answer % (10**9 + 7)
```

---

# 🎯 Final Mental Model

Think of the problem as:

```text
             ITEMS
               ↓
       Sort largest → smallest
               ↓
        Day 0 → largest
        Day 1 → second largest
        Day 2 → third largest
               ↓
       value - day
               ↓
        max(0, value-day)
               ↓
          Add contribution
               ↓
             ANSWER
```

The core formula is:

```text
answer = Σ max(0, sorted_array[i] - i)
```

where the array is sorted in descending order.

---

# 🚀 One-Line Exam Recall

> **Sort the values in descending order, choose one per day, and add `max(0, value - day)` for each item.**

### Pattern

```text
Greedy + Sorting
```

### Formula

```text
Contribution = max(0, value - day)
```

### Complexity

```text
Time  → O(N log N)
Space → O(1) auxiliary
```
