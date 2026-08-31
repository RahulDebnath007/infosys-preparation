# 🪜 LeetCode 70 — Climbing Stairs

[![LeetCode](https://img.shields.io/badge/LeetCode-70-orange)](https://leetcode.com/problems/climbing-stairs/)

## 📌 Problem Overview

You are climbing a staircase with `n` steps.

At each move, you can climb either:

* `1` step
* `2` steps

The task is to determine the **number of distinct ways** to reach the top.

---

## 🧩 Problem Statement

Given an integer `n`, return the number of distinct ways to climb to the top of a staircase containing `n` steps.

### Example 1

```text
Input:
n = 2

Output:
2
```

There are two possible ways:

```text
1 + 1
2
```

---

### Example 2

```text
Input:
n = 3

Output:
3
```

The three possible ways are:

```text
1 + 1 + 1
1 + 2
2 + 1
```

---

## 📥 Input

An integer:

```text
1 ≤ n ≤ 45
```

---

## 📤 Output

Return the number of distinct ways to reach the top.

---

# 💡 Key Observation

The most important observation is that the number of ways to reach step `n` depends on the number of ways to reach the previous two steps.

To reach step `n`, the last move must be either:

```text
1 step
```

or:

```text
2 steps
```

Therefore:

```text
ways(n) = ways(n - 1) + ways(n - 2)
```

This is exactly the recurrence used by the **Fibonacci sequence**.

---

# 🧠 Dynamic Programming Approach

Instead of repeatedly calculating the same subproblems, we store their results in a DP table.

Define:

```text
dp[i] = number of distinct ways to reach step i
```

The base cases are:

```text
dp[1] = 1
dp[2] = 2
```

Because:

```text
dp[1] = 1
```

There is only:

```text
1
```

way to reach the first step.

And:

```text
dp[2] = 2
```

because:

```text
1 + 1
2
```

are the two possible ways.

---

# 🔄 Recurrence Relation

For every `i ≥ 3`:

```text
dp[i] = dp[i - 1] + dp[i - 2]
```

The DP table looks like:

```text
Step:  0  1  2  3  4  5  6  ...
       ↓  ↓  ↓  ↓  ↓  ↓  ↓
dp:    0  1  2  3  5  8  13 ...
```

Therefore:

```text
dp[n] = dp[n - 1] + dp[n - 2]
```

---

# 🔍 Why Does the Recurrence Work?

Consider reaching step `5`.

The final move can only be:

### Case 1 — Take 1 Step

The robot was previously at step `4`.

Number of ways:

```text
dp[4]
```

### Case 2 — Take 2 Steps

The robot was previously at step `3`.

Number of ways:

```text
dp[3]
```

Therefore:

```text
dp[5] = dp[4] + dp[3]
```

The same logic works for every step:

```text
dp[n] = dp[n-1] + dp[n-2]
```

---

# 🧪 Dry Run

Consider:

```text
n = 5
```

Initialize:

```text
dp[1] = 1
dp[2] = 2
```

Now calculate:

```text
dp[3] = dp[2] + dp[1]
      = 2 + 1
      = 3
```

```text
dp[4] = dp[3] + dp[2]
      = 3 + 2
      = 5
```

```text
dp[5] = dp[4] + dp[3]
      = 5 + 3
      = 8
```

Therefore:

```text
Answer = 8
```

The complete DP table is:

| Step | Number of Ways |
| ---: | -------------: |
|    0 |              0 |
|    1 |              1 |
|    2 |              2 |
|    3 |              3 |
|    4 |              5 |
|    5 |              8 |

---

# 💻 Python Solution

```python
def climb(n):
    # Edge cases
    if n == 0:
        return 0

    if n == 1:
        return 1

    if n == 2:
        return 2

    # DP table
    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 2

    # Build the DP table
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```

---

# 🧪 Example

```python
n = 3

print(climb(n))
```

Output:

```text
3
```

---

# 📊 DP Table Visualization

For:

```text
n = 6
```

the calculation is:

```text
dp[1] = 1
dp[2] = 2

dp[3] = dp[2] + dp[1]
      = 2 + 1
      = 3

dp[4] = dp[3] + dp[2]
      = 3 + 2
      = 5

dp[5] = dp[4] + dp[3]
      = 5 + 3
      = 8

dp[6] = dp[5] + dp[4]
      = 8 + 5
      = 13
```

So:

```text
dp = [0, 1, 2, 3, 5, 8, 13]
```

and:

```text
dp[6] = 13
```

---

# 🚫 Why Not Use Recursion?

A recursive solution might look like:

```python
def climb(n):
    if n <= 2:
        return n

    return climb(n - 1) + climb(n - 2)
```

The problem is that it repeatedly calculates the same values.

For example:

```text
climb(5)
├── climb(4)
│   ├── climb(3)
│   │   ├── climb(2)
│   │   └── climb(1)
│   └── climb(2)
└── climb(3)
    ├── climb(2)
    └── climb(1)
```

Notice that:

```text
climb(3)
climb(2)
```

are calculated multiple times.

This creates an exponential number of recursive calls.

The naive recursive solution has approximately:

```text
O(2^n)
```

time complexity.

Dynamic programming eliminates this repeated work.

---

# 🧠 DP Pattern

This problem follows a very common Dynamic Programming pattern:

```text
Current State
     ↓
Depends on Previous States
     ↓
Store Previous Results
     ↓
Build Current Result
```

For Climbing Stairs:

```text
dp[i]
  ↓
dp[i-1] + dp[i-2]
```

This is one of the simplest examples of **1D Dynamic Programming**.

---

# 🔑 How to Recognize This DP Problem

When you see a problem where:

* You need to count the number of ways.
* The current state can be reached from a small number of previous states.
* The same smaller problems appear repeatedly.

Think:

```text
Dynamic Programming
```

For this problem, ask:

> "How can I reach step `i`?"

There are only two possibilities:

```text
From i - 1 → take 1 step
From i - 2 → take 2 steps
```

Therefore:

```text
dp[i] = dp[i-1] + dp[i-2]
```

---

# ⚙️ Complexity Analysis

Let `n` be the number of stairs.

### Time Complexity

The loop runs from `3` to `n`:

```text
O(n)
```

### Space Complexity

The DP array contains `n + 1` elements:

```text
O(n)
```

Therefore:

```text
Time:  O(n)
Space: O(n)
```

---

# 🚀 Space-Optimized Solution

The complete DP table is not actually necessary.

To calculate:

```text
dp[i]
```

we only need:

```text
dp[i-1]
dp[i-2]
```

So we can store only two variables.

```python
def climb(n):
    if n == 1:
        return 1

    prev2 = 1  # dp[1]
    prev1 = 2  # dp[2]

    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1
```

This reduces the space complexity to:

```text
O(1)
```

while keeping the time complexity:

```text
O(n)
```

---

# 🔄 Space-Optimized Logic

Instead of:

```text
dp = [0, 1, 2, 3, 5, 8, ...]
```

we only maintain:

```text
prev2 → dp[i-2]
prev1 → dp[i-1]
```

Then:

```text
current = prev1 + prev2
```

and shift:

```text
prev2 = prev1
prev1 = current
```

The process looks like:

```text
prev2  prev1
  ↓      ↓
 dp[i-2] dp[i-1]
     \    /
      \  /
       ↓
    current
       ↓
    dp[i]
```

---

# 🧪 Edge Cases

### `n = 1`

There is only one way:

```text
1
```

Output:

```text
1
```

---

### `n = 2`

There are two ways:

```text
1 + 1
2
```

Output:

```text
2
```

---

### `n = 3`

There are three ways:

```text
1 + 1 + 1
1 + 2
2 + 1
```

Output:

```text
3
```

---

# 📈 Connection to Fibonacci

The sequence of answers is:

```text
1, 2, 3, 5, 8, 13, 21, ...
```

Compare this with Fibonacci:

```text
1, 1, 2, 3, 5, 8, 13, 21, ...
```

The Climbing Stairs sequence is essentially Fibonacci shifted by one position:

```text
climb(n) = Fibonacci(n + 1)
```

This is a useful observation, but using the DP recurrence is generally the clearest approach for this problem.

---

# 🔑 Key Concepts

This problem demonstrates:

* Dynamic Programming
* 1D DP
* State definition
* Base cases
* Recurrence relations
* Counting distinct ways
* Avoiding overlapping subproblems
* Fibonacci-style recurrence
* Space optimization

---

# 🎯 Key Takeaway

The central idea is:

> **To reach step `n`, the final move must come from either `n-1` or `n-2`.**

Therefore:

```text
dp[n] = dp[n-1] + dp[n-2]
```

The complete thought process is:

```text
                 Step n
                /      \
        1-step /        \ 2-step
              /          \
           n-1            n-2
            ↓              ↓
          dp[n-1]        dp[n-2]
              \            /
               \          /
                ──────────
                     ↓
              dp[n-1] + dp[n-2]
                     ↓
                   dp[n]
```

The DP table approach gives:

```text
Time:  O(n)
Space: O(n)
```

and the optimized two-variable approach improves it to:

```text
Time:  O(n)
Space: O(1)
```

For LeetCode's constraint:

```text
1 ≤ n ≤ 45
```

both approaches are easily fast enough.
