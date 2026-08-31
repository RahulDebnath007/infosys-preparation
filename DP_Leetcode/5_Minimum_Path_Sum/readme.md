# 🛣️ LeetCode 64 — Minimum Path Sum

[![LeetCode](https://img.shields.io/badge/LeetCode-64-orange)](https://leetcode.com/problems/minimum-path-sum/)

## 📌 Problem Overview

You are given an `m × n` grid containing **non-negative integers**.

The robot starts at the **top-left corner**:

```text
(0, 0)
```

and needs to reach the **bottom-right corner**:

```text
(m - 1, n - 1)
```

The robot can only move:

```text
→ Right
↓ Down
```

Each cell contains a number, which contributes to the total path sum.

The goal is to find the path with the **minimum possible sum**.

---

# 🧩 Problem Statement

Given an `m × n` grid filled with non-negative integers, find a path from the top-left corner to the bottom-right corner such that the sum of all values along the path is minimized.

You can only move:

```text
Right
Down
```

Return the minimum possible path sum.

---

## 📥 Input

An integer matrix:

```text
grid
```

### Constraints

```text
1 ≤ m, n ≤ 200
0 ≤ grid[i][j] ≤ 200
```

where:

```text
m = number of rows
n = number of columns
```

---

## 📤 Output

Return a single integer representing the **minimum path sum** from the top-left cell to the bottom-right cell.

---

# 🧪 Example 1

```text
Input:
grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]

Output:
7
```

The minimum-sum path is:

```text
1 → 3 → 1 → 1 → 1
```

Its sum is:

```text
1 + 3 + 1 + 1 + 1 = 7
```

Therefore:

```text
Answer = 7
```

---

# 🧪 Example 2

```text
Input:
grid = [
    [1,2,3],
    [4,5,6]
]

Output:
12
```

The minimum path is:

```text
1 → 2 → 3 → 6
```

Therefore:

```text
1 + 2 + 3 + 6 = 12
```

---

# 🧠 Intuition

This is a classic **Dynamic Programming** problem.

Why?

At every cell, the robot can only arrive from two possible directions:

```text
        Top
         ↓
       ┌───┐
Left → │ X │
       └───┘
```

So to reach cell `(i,j)`, we only need to know the minimum path sum to:

```text
(i - 1, j)   → from above
(i, j - 1)   → from left
```

We choose the smaller of these two values and add the current cell's value.

Therefore:

```text
dp[i][j] =
    min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
```

This is the core recurrence.

---

# 💡 Dynamic Programming State

Define:

```text
dp[i][j]
```

as:

> The minimum path sum required to reach cell `(i,j)` from the top-left corner.

For every cell except the first row and first column:

```text
dp[i][j] =
min(
    dp[i-1][j],
    dp[i][j-1]
) + grid[i][j]
```

The logic is:

```text
             Current Cell
                  ↑
        ┌─────────┴─────────┐
        ↓                   ↓
     From Top            From Left
        ↓                   ↓
    dp[i-1][j]          dp[i][j-1]
        \                   /
         \                 /
          └──────┬────────┘
                 ↓
               min()
                 ↓
          + grid[i][j]
                 ↓
              dp[i][j]
```

---

# 🏁 Base Case

The starting cell is:

```text
dp[0][0]
```

There is only one way to reach it:

```text
dp[0][0] = grid[0][0]
```

For example:

```text
grid[0][0] = 1
```

then:

```text
dp[0][0] = 1
```

---

# ➡️ First Row

For cells in the first row, the robot can only move:

```text
→ Right
```

It cannot come from above.

Therefore:

```text
dp[0][j] = dp[0][j-1] + grid[0][j]
```

For example:

```text
grid:

1  3  1
```

The DP values become:

```text
1  4  5
```

because:

```text
dp[0][0] = 1

dp[0][1] = 1 + 3 = 4

dp[0][2] = 4 + 1 = 5
```

---

# ⬇️ First Column

For cells in the first column, the robot can only move:

```text
↓ Down
```

It cannot come from the left.

Therefore:

```text
dp[i][0] = dp[i-1][0] + grid[i][0]
```

For example:

```text
grid:

1
1
4
```

The DP values become:

```text
1
2
6
```

because:

```text
dp[0][0] = 1

dp[1][0] = 1 + 1 = 2

dp[2][0] = 2 + 4 = 6
```

---

# 🔄 DP Transition

For every inner cell:

```text
i > 0
j > 0
```

we can come from:

```text
Top
Left
```

Therefore:

```text
dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
```

This is the most important line in the solution.

---

# 📊 Example DP Table

Consider:

```text
grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]
```

### Original Grid

```text
┌───┬───┬───┐
│ 1 │ 3 │ 1 │
├───┼───┼───┤
│ 1 │ 5 │ 1 │
├───┼───┼───┤
│ 4 │ 2 │ 1 │
└───┴───┴───┘
```

### Build DP Table

Start:

```text
dp[0][0] = 1
```

First row:

```text
1  4  5
```

First column:

```text
1
2
6
```

Now calculate the remaining cells.

### Cell `(1,1)`

```text
dp[1][1]
= min(dp[0][1], dp[1][0]) + grid[1][1]

= min(4, 2) + 5

= 7
```

### Cell `(1,2)`

```text
dp[1][2]
= min(5, 7) + 1

= 6
```

### Cell `(2,1)`

```text
dp[2][1]
= min(7, 6) + 2

= 8
```

### Cell `(2,2)`

```text
dp[2][2]
= min(6, 8) + 1

= 7
```

Final DP table:

```text
┌───┬───┬───┐
│ 1 │ 4 │ 5 │
├───┼───┼───┤
│ 2 │ 7 │ 6 │
├───┼───┼───┤
│ 6 │ 8 │ 7 │
└───┴───┴───┘
```

Therefore:

```text
dp[2][2] = 7
```

Final answer:

```text
7
```

---

# 🔍 Step-by-Step Algorithm

### Step 1 — Get Grid Dimensions

```python
m, n = len(grid), len(grid[0])
```

---

### Step 2 — Create DP Table

Create an `m × n` table:

```python
dp = [[0] * n for _ in range(m)]
```

---

### Step 3 — Initialize Starting Cell

```python
dp[0][0] = grid[0][0]
```

---

### Step 4 — Fill the First Column

The robot can only move downward:

```python
for i in range(1, m):
    dp[i][0] = dp[i - 1][0] + grid[i][0]
```

---

### Step 5 — Fill the First Row

The robot can only move right:

```python
for j in range(1, n):
    dp[0][j] = dp[0][j - 1] + grid[0][j]
```

---

### Step 6 — Fill the Remaining Cells

For every inner cell:

```python
for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = min(
            dp[i - 1][j],
            dp[i][j - 1]
        ) + grid[i][j]
```

---

### Step 7 — Return the Destination

The bottom-right cell contains the minimum path sum:

```python
return dp[m - 1][n - 1]
```

---

# 💻 Python 3 Solution

```python
class Solution:
    def minPathSum(self, grid):

        m, n = len(grid), len(grid[0])

        # Create DP table
        dp = [[0] * n for _ in range(m)]

        # Starting cell
        dp[0][0] = grid[0][0]

        # First column
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # First row
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # Remaining cells
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = (
                    min(dp[i - 1][j], dp[i][j - 1])
                    + grid[i][j]
                )

        return dp[m - 1][n - 1]
```

---

# 🧠 Dry Run

Consider:

```text
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
```

### Initialization

```text
dp[0][0] = 1
```

DP:

```text
1  0  0
0  0  0
0  0  0
```

### First Row

```text
dp[0][1] = 1 + 3 = 4
dp[0][2] = 4 + 1 = 5
```

```text
1  4  5
0  0  0
0  0  0
```

### First Column

```text
dp[1][0] = 1 + 1 = 2
dp[2][0] = 2 + 4 = 6
```

```text
1  4  5
2  0  0
6  0  0
```

### Inner Cells

For `(1,1)`:

```text
min(4, 2) + 5 = 7
```

For `(1,2)`:

```text
min(5, 7) + 1 = 6
```

For `(2,1)`:

```text
min(7, 6) + 2 = 8
```

For `(2,2)`:

```text
min(6, 8) + 1 = 7
```

Final:

```text
1  4  5
2  7  6
6  8  7
```

Answer:

```text
7
```

---

# 🚫 Why Not Greedy?

A tempting approach is:

> "At every cell, just move to whichever neighboring cell has the smaller value."

That is **not guaranteed to work**.

For example:

```text
1  2  100
10 1  1
10 10 1
```

Choosing the locally smaller value can lead to a bad overall path.

The problem is that a locally optimal decision does not necessarily produce a globally optimal path.

Dynamic Programming considers the best accumulated cost from previous cells, rather than only looking at the current cell.

The correct logic is:

```text
Minimum cost to current cell
=
minimum of previous paths
+
current cost
```

---

# 🧠 Why DP Works

Every path reaching `(i,j)` must come from exactly one of:

```text
(i-1, j)
```

or:

```text
(i, j-1)
```

Suppose the optimal path to `(i,j)` came from the top.

Then the part of the path from `(0,0)` to `(i-1,j)` must also be optimal.

Otherwise, we could replace it with a cheaper path and obtain a cheaper path to `(i,j)`.

This is the **optimal substructure** property of Dynamic Programming.

The problem also has overlapping subproblems because many different paths depend on the same intermediate cells.

Therefore, DP is a natural fit.

---

# 🔄 DP Pattern

This problem follows the standard **Grid Minimum DP** pattern:

```text
                 Current Cell
                      ↑
            ┌─────────┴─────────┐
            ↓                   ↓
         From Top            From Left
            ↓                   ↓
      previous cost        previous cost
            \                   /
             \                 /
              └──────┬────────┘
                     ↓
                   min()
                     ↓
             + current value
                     ↓
                  dp[i][j]
```

The recurrence is:

```text
dp[i][j] =
min(
    dp[i-1][j],
    dp[i][j-1]
) + grid[i][j]
```

---

# 🆚 Unique Paths vs Minimum Path Sum

This problem is closely related to **LeetCode 62 — Unique Paths**.

### Unique Paths

We are counting paths:

```text
dp[i][j] =
dp[i-1][j] + dp[i][j-1]
```

### Minimum Path Sum

We are minimizing a cost:

```text
dp[i][j] =
min(dp[i-1][j], dp[i][j-1])
+ grid[i][j]
```

The structure is almost identical.

The key difference is the operation used to combine the previous states:

```text
Unique Paths:
        ADD

Minimum Path Sum:
        MIN + COST
```

This is an important DP pattern to recognize.

---

# 🚀 Space Optimization

The 2D DP table is easy to understand, but we can optimize the space.

Each cell only depends on:

```text
Top
Left
```

Therefore, a 1D DP array is sufficient.

```python
class Solution:
    def minPathSum(self, grid):

        m, n = len(grid), len(grid[0])

        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(m):
            for j in range(n):

                if j > 0:
                    dp[j] = min(dp[j], dp[j - 1])

                dp[j] += grid[i][j]

        return dp[n - 1]
```

Here:

```text
dp[j]
```

represents the minimum cost to reach the current cell.

Before updating:

```text
dp[j]
```

contains the cost from above.

And:

```text
dp[j-1]
```

contains the cost from the left.

Therefore:

```text
dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
```

---

# 📊 Complexity Comparison

| Approach |       Time |      Space |
| -------- | ---------: | ---------: |
| 2D DP    | `O(m × n)` | `O(m × n)` |
| 1D DP    | `O(m × n)` |     `O(n)` |

Both approaches visit every cell exactly once.

The 1D version simply reduces memory usage.

---

# ⚙️ Complexity Analysis

For the 2D DP solution:

There are `m × n` cells, and each cell is processed once.

### Time Complexity

```text
O(m × n)
```

### Space Complexity

The DP table contains `m × n` values:

```text
O(m × n)
```

Therefore:

```text
Time:  O(m × n)
Space: O(m × n)
```

For the space-optimized version:

```text
Time:  O(m × n)
Space: O(n)
```

---

# 🔑 How to Recognize This DP Pattern

When you see:

* A grid
* Start at top-left
* Reach bottom-right
* Only move right/down
* Every cell has a cost
* Need minimum/maximum total cost

think:

```text
Grid DP
```

Ask:

> "What are the possible previous states?"

Here:

```text
Top
Left
```

Then ask:

> "What operation combines them?"

For minimum path:

```text
min()
```

Therefore:

```text
dp[i][j] =
min(dp[i-1][j], dp[i][j-1])
+ grid[i][j]
```

---

# 🎯 Key Takeaway

The core idea of **Minimum Path Sum** is:

> **The minimum cost to reach a cell is the smaller of the minimum costs to reach its top and left neighbors, plus the current cell's value.**

The recurrence is:

```text
dp[i][j] =
min(dp[i-1][j], dp[i][j-1])
+ grid[i][j]
```

The DP process is:

```text
                  Grid
                   ↓
              Define State
                   ↓
       dp[i][j] = minimum cost
             to reach (i,j)
                   ↓
              Base Cases
             ↙          ↘
        First Row     First Column
             \          /
              \        /
               ↓      ↓
              Inner Cells
                   ↓
             min(Top, Left)
                   ↓
            + Current Value
                   ↓
             dp[m-1][n-1]
                   ↓
                Answer
```

### Final Complexity

**2D DP:**

```text
Time:  O(m × n)
Space: O(m × n)
```

**1D optimized DP:**

```text
Time:  O(m × n)
Space: O(n)
```

The most important DP pattern to remember is:

```text
Previous States
      ↓
Choose Best
      ↓
Add Current Cost
      ↓
Current State
```

For this problem:

```text
Top + Left
    ↓
   min()
    ↓
+ grid[i][j]
    ↓
 dp[i][j]
```
