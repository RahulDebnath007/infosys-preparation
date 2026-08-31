# 🤖 LeetCode 63 — Unique Paths II

[![LeetCode](https://img.shields.io/badge/LeetCode-63-orange)](https://leetcode.com/problems/unique-paths-ii/)

## 📌 Problem Overview

You are given an `m × n` grid containing:

```text
0 → Empty cell
1 → Obstacle
```

A robot starts at the **top-left corner**:

```text
(0, 0)
```

and wants to reach the **bottom-right corner**:

```text
(m - 1, n - 1)
```

The robot can move only:

```text
→ Right
↓ Down
```

The robot **cannot enter an obstacle cell**.

The goal is to calculate the **number of unique paths** from the starting cell to the destination while avoiding all obstacles.

---

# 🧩 Problem Statement

Given:

```python
obstacleGrid
```

where:

```text
0 = open cell
1 = obstacle
```

return the number of unique paths from:

```text
grid[0][0]
```

to:

```text
grid[m-1][n-1]
```

without passing through any obstacle.

---

## 📥 Input

An `m × n` integer matrix:

```text
obstacleGrid
```

### Constraints

```text
m == obstacleGrid.length
n == obstacleGrid[i].length

1 ≤ m, n ≤ 100

obstacleGrid[i][j] ∈ {0, 1}
```

The answer is guaranteed to be at most:

```text
2 × 10⁹
```

---

## 📤 Output

Return the number of unique paths from the top-left corner to the bottom-right corner while avoiding obstacles.

If there is no possible path, return:

```text
0
```

---

# 🧪 Example 1

```text
Input:
obstacleGrid =
[
    [0,0,0],
    [0,1,0],
    [0,0,0]
]

Output:
2
```

The grid looks like:

```text
┌───┬───┬───┐
│ 0 │ 0 │ 0 │
├───┼───┼───┤
│ 0 │ X │ 0 │
├───┼───┼───┤
│ 0 │ 0 │ 0 │
└───┴───┴───┘

0 = Open
X = Obstacle
```

There are two possible paths:

```text
Right → Right → Down → Down

Down → Down → Right → Right
```

Therefore:

```text
Answer = 2
```

---

# 🧪 Example 2

```text
Input:
obstacleGrid =
[
    [0,1],
    [0,0]
]

Output:
1
```

The only possible path is:

```text
Down → Right
```

Therefore:

```text
Answer = 1
```

---

# 🧠 Problem Understanding

This problem is an extension of **LeetCode 62 — Unique Paths**.

In the original problem, every cell is accessible.

Here, some cells are blocked:

```text
0 → Can enter
1 → Cannot enter
```

The key question is:

> How many ways can we reach the current cell?

If the current cell is not an obstacle, we can arrive from:

```text
↑ Above
← Left
```

Therefore:

```text
ways(i,j)
=
ways(i-1,j)
+
ways(i,j-1)
```

However, if the current cell is an obstacle:

```text
obstacleGrid[i][j] == 1
```

then:

```text
ways(i,j) = 0
```

because the robot cannot enter that cell.

---

# 💡 Dynamic Programming

Define:

```text
dp[i][j]
```

as:

> The number of ways to reach cell `(i,j)` from the starting cell `(0,0)`.

For a normal cell:

```text
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

For an obstacle:

```text
dp[i][j] = 0
```

So the complete transition is:

```text
dp[i][j] =
    0                              if obstacleGrid[i][j] == 1
    dp[i-1][j] + dp[i][j-1]       otherwise
```

---

# 🔄 Why Does the Transition Work?

Consider this cell:

```text
      Above
        ↓
      ┌───┐
Left →│ X │
      └───┘
```

The robot can reach the current cell only from:

```text
Above
```

or:

```text
Left
```

Therefore, the number of ways to reach it is:

```text
Ways from Above + Ways from Left
```

If the cell itself is an obstacle:

```text
      ┌───┐
      │ 1 │
      └───┘
```

then it cannot be entered:

```text
dp[i][j] = 0
```

---

# 🧠 2D DP Approach

The most straightforward implementation uses a 2D table.

For example:

```text
obstacleGrid =
0 0 0
0 1 0
0 0 0
```

The DP table becomes:

```text
1 1 1
1 0 1
1 1 2
```

The `1` in the center represents the obstacle, so its number of paths is `0`.

The bottom-right cell contains:

```text
2
```

which is the answer.

---

# 🚀 Space Optimization

Notice that:

```text
dp[i][j]
```

only depends on:

```text
dp[i-1][j]
```

from the previous row and:

```text
dp[i][j-1]
```

from the current row.

Therefore, we do not need to store the entire `m × n` table.

We can use a single 1D array:

```text
dp[j]
```

This reduces space from:

```text
O(m × n)
```

to:

```text
O(n)
```

This technique is called **rolling-array optimization**.

---

# 📊 1D DP Representation

For:

```text
0 0 0
0 1 0
0 0 0
```

start with:

```text
dp = [1, 0, 0]
```

### Process Row 0

```text
0 0 0
```

We get:

```text
dp = [1, 1, 1]
```

---

### Process Row 1

```text
0 1 0
```

First cell:

```text
dp[0] = 1
```

Obstacle at column `1`:

```text
dp[1] = 0
```

Last cell:

```text
dp[2] = dp[2] + dp[1]
      = 1 + 0
      = 1
```

Now:

```text
dp = [1, 0, 1]
```

---

### Process Row 2

```text
0 0 0
```

First cell:

```text
dp[0] = 1
```

Second cell:

```text
dp[1] = dp[1] + dp[0]
      = 0 + 1
      = 1
```

Third cell:

```text
dp[2] = dp[2] + dp[1]
      = 1 + 1
      = 2
```

Final:

```text
dp = [1, 1, 2]
```

Therefore:

```text
Answer = dp[2] = 2
```

---

# 🔑 Important Initialization

The starting cell must be initialized as:

```python
dp[0] = 1
```

Why?

Because there is exactly **one way to reach the starting cell**:

```text
Start there.
```

So initially:

```text
dp = [1, 0, 0, ...]
```

As we process the grid, the values are updated according to the DP transition.

---

# ⚠️ Starting Cell Is an Obstacle

If:

```python
obstacleGrid[0][0] == 1
```

then the robot cannot even start.

Therefore:

```text
Answer = 0
```

Similarly, if the destination is an obstacle:

```python
obstacleGrid[m-1][n-1] == 1
```

then:

```text
Answer = 0
```

because the robot cannot reach the destination.

The implementation naturally handles the destination obstacle by setting its DP value to `0`.

---

# 🔄 Algorithm

1. Check whether the grid is empty.
2. If the starting cell is an obstacle, return `0`.
3. Create a 1D DP array of size `n`.
4. Initialize:

```python
dp[0] = 1
```

5. Process every row.
6. For each cell:

   * If it is an obstacle, set its path count to `0`.
   * Otherwise, add the paths from above and left.
7. After processing the entire grid, return:

```python
dp[n - 1]
```

---

# 💻 Python 3 Solution

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If starting cell is blocked
        if obstacleGrid[0][0] == 1:
            return 0

        # 1D DP array
        dp = [0] * n
        dp[0] = 1

        for i in range(m):
            for j in range(n):

                # Obstacle means no path through this cell
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0

                else:
                    # Add paths from the left
                    if j > 0:
                        dp[j] += dp[j - 1]

        return dp[n - 1]
```

---

# 🔍 Understanding the 1D Transition

This line is the most important:

```python
dp[j] += dp[j - 1]
```

Before updating:

```text
dp[j]
```

contains the number of ways from **above**.

And:

```text
dp[j - 1]
```

contains the number of ways from the **left**.

Therefore:

```text
new dp[j]
=
paths from above
+
paths from left
```

which is exactly:

```text
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

We are simply reusing the same array instead of maintaining a 2D table.

---

# 🧠 Why Does Setting an Obstacle to `0` Work?

Suppose we encounter:

```text
1
```

in the grid.

We do:

```python
dp[j] = 0
```

This means:

> There are zero ways to reach this cell.

More importantly, future cells that depend on this cell will automatically receive fewer paths.

For example:

```text
0 0 1 0
```

The obstacle blocks all paths from passing through that position.

Setting:

```text
dp[j] = 0
```

correctly propagates the obstacle's effect.

---

# 🧪 Dry Run

Consider:

```text
obstacleGrid =
[
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
```

Initialize:

```text
dp = [1, 0, 0]
```

### Row 0

```text
[0,0,0]
```

After processing:

```text
dp = [1,1,1]
```

---

### Row 1

```text
[0,1,0]
```

First cell:

```text
dp[0] = 1
```

Obstacle:

```text
dp[1] = 0
```

Third cell:

```text
dp[2] = dp[2] + dp[1]
      = 1 + 0
      = 1
```

Result:

```text
dp = [1,0,1]
```

---

### Row 2

```text
[0,0,0]
```

First cell:

```text
dp[0] = 1
```

Second:

```text
dp[1] = 0 + 1
      = 1
```

Third:

```text
dp[2] = 1 + 1
      = 2
```

Final:

```text
dp = [1,1,2]
```

Therefore:

```text
Answer = 2
```

---

# 🆚 2D DP vs 1D DP

| Approach |       Time |      Space |
| -------- | ---------: | ---------: |
| 2D DP    | `O(m × n)` | `O(m × n)` |
| 1D DP    | `O(m × n)` |     `O(n)` |

The time complexity does not change because every cell still needs to be processed.

The improvement is in memory usage.

---

# 🚫 Why Not Use DFS?

A natural approach might be:

```text
Start
 ↓
DFS
 ↙ ↘
...
```

But many different paths can reach the same cell.

Without memoization, the same subproblems are solved repeatedly.

For example:

```text
          Start
         /     \
        A       B
       / \     / \
      C   D   D   E
```

Cell `D` can be reached from multiple paths.

Dynamic Programming avoids this repeated computation by storing the number of ways to reach each cell.

---

# 🧠 DP Pattern

This problem follows the classic **Grid DP** pattern:

```text
Current Cell
     ↓
 ┌───┴───┐
 ↑       ←
Above   Left
```

For an open cell:

```text
dp[i][j]
=
dp[i-1][j]
+
dp[i][j-1]
```

For an obstacle:

```text
dp[i][j] = 0
```

The general pattern is:

```text
                    Grid
                     ↓
               Define State
                     ↓
          dp[i][j] = ways to reach
                     cell (i,j)
                     ↓
              Check obstacle
                ↙       ↘
             Yes         No
              ↓           ↓
          dp = 0      Above + Left
                          ↓
                     Next Cell
                          ↓
                     Final Cell
```

---

# 🔑 How to Recognize This Pattern

When you see a problem involving:

* A grid
* Starting from one cell
* Reaching another cell
* Restricted movement directions
* Counting the number of ways
* Obstacles or blocked cells

you should immediately consider:

```text
Dynamic Programming
```

Ask:

> "From which cells can I arrive at the current cell?"

Here the answer is:

```text
Above
+
Left
```

So:

```text
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

with the additional obstacle condition:

```text
if obstacle:
    dp[i][j] = 0
```

---

# ⚙️ Complexity Analysis

Let:

```text
m = number of rows
n = number of columns
```

We visit every cell exactly once.

Therefore:

### Time Complexity

```text
O(m × n)
```

### Space Complexity

The optimized solution stores only one row:

```text
O(n)
```

Therefore:

```text
Time:  O(m × n)
Space: O(n)
```

This is optimal for this DP formulation because every grid cell must be inspected at least once.

---

# 📌 Edge Cases

## 1. Starting Cell Is Blocked

```text
[[1,0],
 [0,0]]
```

The robot cannot start.

Output:

```text
0
```

---

## 2. Destination Is Blocked

```text
[[0,0],
 [0,1]]
```

The robot cannot reach the destination.

Output:

```text
0
```

---

## 3. Single Cell Without Obstacle

```text
[[0]]
```

The robot is already at the destination.

There is exactly one path:

```text
1
```

---

## 4. Single Cell With Obstacle

```text
[[1]]
```

The starting cell is blocked.

Output:

```text
0
```

---

## 5. Entire Row Blocked

```text
[
    [0,1,0],
    [0,1,0],
    [0,1,0]
]
```

The obstacle column completely separates the grid.

Therefore:

```text
0
```

paths exist.

---

# 🔬 Comparison With LeetCode 62

**LeetCode 62 — Unique Paths** has no obstacles.

Its transition is simply:

```text
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

**LeetCode 63 — Unique Paths II** adds obstacles.

The transition becomes:

```text
if obstacleGrid[i][j] == 1:
    dp[i][j] = 0
else:
    dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

So the key difference is:

```text
Unique Paths
     ↓
Every cell is available

Unique Paths II
     ↓
Some cells are blocked
     ↓
Blocked cell → 0 ways
```

---

# 🎯 Key Takeaway

The central idea of **Unique Paths II** is:

> **For every open cell, the number of ways to reach it equals the number of ways to reach the cell above plus the number of ways to reach the cell to the left.**

Therefore:

```text
dp[i][j] =
    0                           if obstacle
    dp[i-1][j] + dp[i][j-1]    otherwise
```

The important optimization is recognizing that we only need the current row and the previous row, allowing us to reduce:

```text
O(m × n)
```

space to:

```text
O(n)
```

using a **1D rolling DP array**.

The final pattern is:

```text
             Grid With Obstacles
                      ↓
                 1D DP Array
                      ↓
             Start dp[0] = 1
                      ↓
                Process Cell
                 ↙        ↘
            Obstacle      Open
               ↓            ↓
           dp[j] = 0   dp[j] += dp[j-1]
                 \        /
                  \      /
                   ↓    ↓
                 Next Cell
                      ↓
              dp[n - 1]
                      ↓
                   Answer
```

### Final Complexity

```text
Time:  O(m × n)
Space: O(n)
```

This is the standard optimized Dynamic Programming solution for **LeetCode 63 — Unique Paths II**.
