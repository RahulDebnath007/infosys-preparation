# 🤖 LeetCode 62 — Unique Paths

[![LeetCode](https://img.shields.io/badge/LeetCode-62-orange)](https://leetcode.com/problems/unique-paths/)

## 📌 Problem Overview

A robot is placed on an `m × n` grid.

The robot starts at the **top-left corner**:

```text
(0, 0)
```

and wants to reach the **bottom-right corner**:

```text
(m - 1, n - 1)
```

At every step, the robot can move in only two directions:

```text
→ Right
↓ Down
```

The task is to calculate the **total number of unique paths** the robot can take to reach the destination.

---

# 🧩 Problem Statement

Given two integers:

```text
m
n
```

representing the number of rows and columns in the grid, return the number of unique paths from:

```text
(0, 0)
```

to:

```text
(m - 1, n - 1)
```

The robot can only move:

```text
Right
Down
```

---

## 📥 Input

Two integers:

```text
m
n
```

### Constraints

```text
1 ≤ m, n ≤ 100
```

The test cases are generated so that the answer is at most:

```text
2 × 10⁹
```

---

## 📤 Output

Return the number of possible unique paths from the top-left corner to the bottom-right corner.

---

# 🧪 Example 1

```text
Input:
m = 3
n = 7

Output:
28
```

There are `28` different ways for the robot to reach the destination.

---

# 🧪 Example 2

```text
Input:
m = 3
n = 2

Output:
3
```

The three possible paths are:

```text
Right → Down → Down

Down → Down → Right

Down → Right → Down
```

Therefore:

```text
Answer = 3
```

---

# 🧠 Understanding the Problem

The robot has only two possible moves:

```text
→ Right
↓ Down
```

Suppose the robot is currently at cell:

```text
(i, j)
```

To eventually reach the bottom-right corner, it can move to:

```text
(i + 1, j)
```

or:

```text
(i, j + 1)
```

Therefore, the number of paths from `(i,j)` is:

```text
dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
```

This overlapping-subproblem structure makes the problem a natural **Dynamic Programming** problem.

---

# 💡 Why Dynamic Programming?

Consider a small grid.

```text
┌───┬───┬───┐
│   │   │   │
├───┼───┼───┤
│   │   │   │
├───┼───┼───┤
│   │   │   │
└───┴───┴───┘
```

From any cell, the robot can branch into two possible directions.

A naive recursive solution would repeatedly calculate the same subproblems.

For example:

```text
paths(0,0)
├── paths(1,0)
│   ├── paths(2,0)
│   └── paths(1,1)
└── paths(0,1)
    ├── paths(1,1)
    └── paths(0,2)
```

Notice that:

```text
paths(1,1)
```

is calculated multiple times.

For larger grids, this repeated work becomes expensive.

Dynamic Programming solves this by storing previously calculated results.

---

# 🧩 DP State

Define:

```text
dp[i][j]
```

as:

> The number of unique paths from cell `(i,j)` to the bottom-right corner.

The recurrence is:

```text
dp[i][j] = dp[i+1][j] + dp[i][j+1]
```

because every path from `(i,j)` must first move either:

```text
Down
```

or:

```text
Right
```

---

# 🏁 Base Cases

The destination cell:

```text
(m - 1, n - 1)
```

has exactly:

```text
1
```

path to itself.

More generally:

## Last Row

If:

```text
i == m - 1
```

the robot can only move right.

Therefore:

```text
dp[i][j] = 1
```

for every cell in the last row.

---

## Last Column

If:

```text
j == n - 1
```

the robot can only move down.

Therefore:

```text
dp[i][j] = 1
```

for every cell in the last column.

---

# 🔄 Bottom-Up Dynamic Programming

Instead of starting at `(0,0)` and recursively moving toward the destination, we can work **backwards**.

We start by filling:

```text
Last row
Last column
```

with `1`.

Then calculate every other cell using:

```text
dp[i][j] = dp[i+1][j] + dp[i][j+1]
```

We process the grid from:

```text
Bottom-right → Top-left
```

---

# 📊 Example DP Table

Consider:

```text
m = 3
n = 3
```

Initially, the last row and last column contain `1`:

```text
┌───┬───┬───┐
│ ? │ ? │ 1 │
├───┼───┼───┤
│ ? │ ? │ 1 │
├───┼───┼───┤
│ 1 │ 1 │ 1 │
└───┴───┴───┘
```

Now calculate from bottom-right toward top-left.

### Cell `(1,1)`

```text
dp[1][1] = dp[2][1] + dp[1][2]
         = 1 + 1
         = 2
```

### Cell `(1,0)`

```text
dp[1][0] = dp[2][0] + dp[1][1]
         = 1 + 2
         = 3
```

### Cell `(0,1)`

```text
dp[0][1] = dp[1][1] + dp[0][2]
         = 2 + 1
         = 3
```

### Cell `(0,0)`

```text
dp[0][0] = dp[1][0] + dp[0][1]
         = 3 + 3
         = 6
```

Final DP table:

```text
┌───┬───┬───┐
│ 6 │ 3 │ 1 │
├───┼───┼───┤
│ 3 │ 2 │ 1 │
├───┼───┼───┤
│ 1 │ 1 │ 1 │
└───┴───┴───┘
```

Therefore:

```text
dp[0][0] = 6
```

There are `6` unique paths.

---

# 🔍 Step-by-Step Algorithm

### Step 1 — Create the DP Table

Create an `m × n` table:

```python
dp = [[0] * n for _ in range(m)]
```

---

### Step 2 — Initialize the Last Row

Every cell in the last row has exactly one path to the destination.

```python
for j in range(n):
    dp[m - 1][j] = 1
```

---

### Step 3 — Initialize the Last Column

Every cell in the last column also has exactly one path to the destination.

```python
for i in range(m):
    dp[i][n - 1] = 1
```

---

### Step 4 — Fill the Remaining Cells

Traverse from bottom-right toward top-left:

```python
for i in range(m - 2, -1, -1):
    for j in range(n - 2, -1, -1):
        dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
```

---

### Step 5 — Return the Answer

The top-left cell contains the number of unique paths:

```python
return dp[0][0]
```

---

# 💻 Python 3 Solution

```python
class Solution:
    def uniquePaths(self, m, n):

        # Create DP table
        dp = [[0] * n for _ in range(m)]

        # Last row
        for j in range(n):
            dp[m - 1][j] = 1

        # Last column
        for i in range(m):
            dp[i][n - 1] = 1

        # Fill the table from bottom-right to top-left
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]
```

---

# 🧠 Dry Run

Consider:

```text
m = 3
n = 2
```

Create:

```text
┌───┬───┐
│ 0 │ 0 │
├───┼───┤
│ 0 │ 0 │
├───┼───┤
│ 0 │ 0 │
└───┴───┘
```

Initialize the last row and last column:

```text
┌───┬───┐
│ 0 │ 1 │
├───┼───┤
│ 0 │ 1 │
├───┼───┤
│ 1 │ 1 │
└───┴───┘
```

Now calculate `(1,0)`:

```text
dp[1][0] = dp[2][0] + dp[1][1]
         = 1 + 1
         = 2
```

Table:

```text
┌───┬───┐
│ 0 │ 1 │
├───┼───┤
│ 2 │ 1 │
├───┼───┤
│ 1 │ 1 │
└───┴───┘
```

Now calculate `(0,0)`:

```text
dp[0][0] = dp[1][0] + dp[0][1]
         = 2 + 1
         = 3
```

Final table:

```text
┌───┬───┐
│ 3 │ 1 │
├───┼───┤
│ 2 │ 1 │
├───┼───┤
│ 1 │ 1 │
└───┴───┘
```

Therefore:

```text
Answer = 3
```

---

# 🔁 Alternative: Initialize the Entire DP Table With `1`

There is a slightly shorter implementation.

Because the last row and last column are always `1`, we can initialize the entire table with `1`:

```python
class Solution:
    def uniquePaths(self, m, n):

        dp = [[1] * n for _ in range(m)]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]
```

This is equivalent to explicitly initializing the last row and last column.

It is also the cleaner version.

---

# 🧠 Why Does `dp[i][j]` Add Two Values?

Suppose we are at:

```text
(i, j)
```

There are only two possible first moves:

```text
        (i,j)
        /   \
       ↓     →
 (i+1,j)   (i,j+1)
```

Every path from `(i,j)` belongs to exactly one of these two groups.

Therefore:

```text
Paths from current cell
=
Paths going down
+
Paths going right
```

Hence:

```text
dp[i][j] = dp[i+1][j] + dp[i][j+1]
```

This is the fundamental recurrence of the problem.

---

# 🚫 Why Naive Recursion Can TLE

A recursive solution might look like:

```python
def paths(i, j):

    if i == m - 1 or j == n - 1:
        return 1

    return paths(i + 1, j) + paths(i, j + 1)
```

The problem is repeated computation.

For example:

```text
paths(0,0)
├── paths(1,0)
│   ├── paths(2,0)
│   └── paths(1,1)
│       ├── ...
│       └── ...
└── paths(0,1)
    ├── paths(1,1)
    └── paths(0,2)
```

`paths(1,1)` can be reached through multiple branches.

Without memoization, the same state is calculated repeatedly.

The recursive solution therefore grows exponentially.

Dynamic Programming stores each state once.

---

# 💾 Memoization vs Bottom-Up DP

There are two common DP approaches.

## Top-Down — Memoization

Start from:

```text
(0,0)
```

and recursively calculate the answer while storing results.

```text
Recursive solution
        ↓
Repeated states
        ↓
Store results
        ↓
Memoization
```

---

## Bottom-Up — Tabulation

Start from the known base cases and build toward the answer.

```text
Base cases
    ↓
Last row / last column
    ↓
Fill remaining cells
    ↓
dp[0][0]
```

This problem uses **bottom-up DP**.

---

# ⚙️ Complexity Analysis

There are:

```text
m × n
```

cells in the DP table.

Each cell is calculated exactly once.

Therefore:

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

---

# 🚀 Space Optimization

We don't actually need the entire 2D table.

Each state only depends on:

```text
dp[i + 1][j]
dp[i][j + 1]
```

So we can reduce the DP to a **1D array**.

```python
class Solution:
    def uniquePaths(self, m, n):

        dp = [1] * n

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[j] = dp[j] + dp[j + 1]

        return dp[0]
```

Here:

```text
dp[j]
```

represents the number of paths from the current row's cell `(i,j)`.

The previous row's value is already stored in `dp[j]`, while:

```text
dp[j + 1]
```

represents the cell to the right.

Therefore:

```text
dp[j] = dp[j] + dp[j + 1]
```

---

# 📊 Space-Optimized Example

For:

```text
m = 3
n = 3
```

initially:

```text
dp = [1, 1, 1]
```

Process the second row:

```text
j = 1

dp[1] = dp[1] + dp[2]
      = 1 + 1
      = 2

dp = [1, 2, 1]
```

Then:

```text
j = 0

dp[0] = dp[0] + dp[1]
      = 1 + 2
      = 3

dp = [3, 2, 1]
```

Process the first row:

```text
j = 1

dp[1] = 2 + 1
      = 3

dp = [3, 3, 1]
```

Then:

```text
j = 0

dp[0] = 3 + 3
      = 6
```

Final:

```text
dp = [6, 3, 1]
```

Therefore:

```text
Answer = dp[0] = 6
```

---

# 🏆 Recommended Solution

For understanding DP, the 2D table is easier to visualize:

```python
class Solution:
    def uniquePaths(self, m, n):

        dp = [[1] * n for _ in range(m)]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]
```

Once the recurrence is understood, use the 1D version when you want to optimize space:

```python
class Solution:
    def uniquePaths(self, m, n):

        dp = [1] * n

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[j] += dp[j + 1]

        return dp[0]
```

The optimized version has:

```text
Time:  O(m × n)
Space: O(n)
```

---

# 🔑 How to Recognize This DP Pattern

When a grid problem says:

* Start from one cell.
* Reach another cell.
* There are a limited number of moves.
* You need to count the number of ways.
* Multiple paths reach the same cells.

Think:

```text
Grid DP
```

Ask:

> "From this cell, what previous or next states can lead to the answer?"

Here:

```text
Current Cell
    ↓
┌─────────────┐
│             │
│  ↓       →  │
│             │
└─────────────┘
```

So:

```text
dp[i][j]
=
dp[i+1][j]
+
dp[i][j+1]
```

---

# 🎯 Key Takeaway

The central idea of **Unique Paths** is:

> **The number of paths from a cell is the sum of the paths from the two cells you can move to.**

Therefore:

```text
dp[i][j] = dp[i+1][j] + dp[i][j+1]
```

The boundary cells have only one possible direction:

```text
Last row    → 1 path
Last column → 1 path
```

The complete DP process is:

```text
             Grid
               ↓
       Define DP state
               ↓
   dp[i][j] = paths from
       (i,j) to destination
               ↓
          Base Cases
      Last row = 1
      Last col = 1
               ↓
       Fill bottom → top
               ↓
   dp[i][j] = dp[i+1][j]
            + dp[i][j+1]
               ↓
           dp[0][0]
               ↓
             Answer
```

### Complexity

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

This is a fundamental **2D Dynamic Programming** problem and a good pattern to recognize before moving on to more complicated grid-DP problems such as **Unique Paths II**, **Minimum Path Sum**, and obstacle-based grid problems.
