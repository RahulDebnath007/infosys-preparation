# 🤖 Robot Grid Game

## 📌 Problem Overview

A robot is placed on an `n × m` rectangular grid.

It starts at:

```text
(1, 1)
```

and must reach:

```text
(n, m)
```

There is one **broken cell** at:

```text
(x, y)
```

which the robot cannot pass through.

The robot can move in four directions:

```text
UP
DOWN
LEFT
RIGHT
```

The task is to find the **number of shortest paths** from `(1, 1)` to `(n, m)` that avoid the broken cell.

---

# 🧩 Problem Statement

Given:

* Grid dimensions `n × m`
* Starting position `(1, 1)`
* Destination `(n, m)`
* Broken cell `(x, y)`

calculate the number of shortest paths that do not pass through `(x, y)`.

The starting and destination cells are guaranteed not to be broken.

---

# 📥 Input Format

The input contains four lines:

```text
n
m
x
y
```

where:

* `n` = number of rows
* `m` = number of columns
* `x` = row of the broken cell
* `y` = column of the broken cell

### Constraints

```text
1 ≤ n ≤ 30
1 ≤ m ≤ 30
1 ≤ x ≤ n
1 ≤ y ≤ m
```

The broken cell is guaranteed to be different from:

```text
(1, 1)
(n, m)
```

---

# 📤 Output Format

Print a single integer representing the number of shortest paths from `(1, 1)` to `(n, m)` while avoiding the broken cell.

---

# 🧪 Sample Input

```text
3
4
2
3
```

## 🧪 Sample Output

```text
4
```

---

# 🔍 Sample Explanation

The grid has:

```text
n = 3
m = 4
```

So the robot moves from:

```text
(1, 1)
```

to:

```text
(3, 4)
```

The broken cell is:

```text
(2, 3)
```

For a shortest path, the robot must move:

```text
2 steps DOWN
3 steps RIGHT
```

Therefore, every shortest path contains exactly:

```text
5 steps
```

Without the broken cell, there are:

```text
C(5, 2) = 10
```

shortest paths.

Some of these paths pass through `(2, 3)`.

The number of shortest paths from `(1,1)` to `(2,3)` is:

```text
C(3, 1) = 3
```

The number of shortest paths from `(2,3)` to `(3,4)` is:

```text
C(2, 1) = 2
```

Therefore, paths passing through the broken cell:

```text
3 × 2 = 6
```

Finally:

```text
10 - 6 = 4
```

So the answer is:

```text
4
```

---

# 💡 Key Observation

Although the robot is technically allowed to move in **four directions**, a shortest path from `(1,1)` to `(n,m)` can only move:

```text
RIGHT
DOWN
```

Any `UP` or `LEFT` movement would increase the total number of steps and therefore cannot be part of a shortest path.

So the problem becomes a **combinatorics** problem.

---

# 📐 Number of Shortest Paths

To reach `(n,m)` from `(1,1)`:

* Number of DOWN moves = `n - 1`
* Number of RIGHT moves = `m - 1`

Therefore, the total number of moves is:

```text
(n - 1) + (m - 1)
= n + m - 2
```

We need to choose where the `n - 1` DOWN moves occur among the total moves.

Therefore:

```text
Total Paths = C(n + m - 2, n - 1)
```

where:

```text
C(a, b) = a! / (b! × (a-b)!)
```

---

# 🚧 Handling the Broken Cell

Instead of trying to generate every path and checking whether it contains the broken cell, we count the paths that **must pass through the broken cell** and subtract them.

This is much more efficient.

A path passing through `(x,y)` consists of two parts:

```text
Start → Broken Cell → Destination
```

Therefore:

```text
Blocked Paths
=
Paths(Start → Broken)
×
Paths(Broken → Destination)
```

---

# 1️⃣ Paths From Start to Broken Cell

From:

```text
(1,1)
```

to:

```text
(x,y)
```

we need:

```text
x - 1 DOWN moves
y - 1 RIGHT moves
```

Total moves:

```text
x + y - 2
```

Therefore:

```text
Paths to Broken Cell
=
C(x + y - 2, x - 1)
```

---

# 2️⃣ Paths From Broken Cell to Destination

From:

```text
(x,y)
```

to:

```text
(n,m)
```

we need:

```text
n - x DOWN moves
m - y RIGHT moves
```

Total moves:

```text
(n - x) + (m - y)
```

Therefore:

```text
Paths from Broken Cell
=
C((n-x) + (m-y), n-x)
```

---

# 3️⃣ Calculate Blocked Paths

Every path that passes through the broken cell can be uniquely divided into:

```text
Start → Broken
```

and:

```text
Broken → Destination
```

Therefore, by the multiplication principle:

```text
Blocked Paths
=
C(x+y-2, x-1)
×
C((n-x)+(m-y), n-x)
```

---

# 4️⃣ Calculate the Final Answer

Start with all shortest paths:

```text
Total Paths = C(n+m-2, n-1)
```

Subtract paths passing through the broken cell:

```text
Answer = Total Paths - Blocked Paths
```

So the final formula is:

```text
Answer =
C(n+m-2, n-1)
-
C(x+y-2, x-1)
×
C((n-x)+(m-y), n-x)
```

---

# 🔄 Algorithm

1. Read `n`, `m`, `x`, and `y`.
2. Calculate the total number of shortest paths:

```python
comb(n + m - 2, n - 1)
```

3. Calculate the number of paths from the start to the broken cell:

```python
comb(x + y - 2, x - 1)
```

4. Calculate the number of paths from the broken cell to the destination:

```python
comb((n - x) + (m - y), n - x)
```

5. Multiply the two values to get the number of blocked paths.
6. Subtract blocked paths from total paths.
7. Print the result.

---

# 💻 Python 3 Solution

```python
from math import comb


def robot_grid(n, m, x, y):
    # Total shortest paths from (1, 1) to (n, m)
    total = comb(n + m - 2, n - 1)

    # Paths from (1, 1) to the broken cell (x, y)
    paths_to_block = comb(x + y - 2, x - 1)

    # Paths from the broken cell to (n, m)
    paths_from_block = comb(
        (n - x) + (m - y),
        n - x
    )

    # All paths passing through the broken cell
    blocked = paths_to_block * paths_from_block

    # Valid shortest paths
    return total - blocked


# Read input
n = int(input().strip())
m = int(input().strip())
x = int(input().strip())
y = int(input().strip())

# Print answer
print(robot_grid(n, m, x, y))
```

---

# 🧠 Dry Run

Consider:

```text
n = 3
m = 4
x = 2
y = 3
```

### Step 1 — Total Paths

```text
C(n + m - 2, n - 1)
```

Substitute:

```text
C(3 + 4 - 2, 3 - 1)
= C(5, 2)
= 10
```

So:

```text
Total = 10
```

---

### Step 2 — Paths to Broken Cell

```text
C(x + y - 2, x - 1)
```

Substitute:

```text
C(2 + 3 - 2, 2 - 1)
= C(3, 1)
= 3
```

So:

```text
To Broken = 3
```

---

### Step 3 — Paths From Broken Cell

```text
C((n-x)+(m-y), n-x)
```

Substitute:

```text
C((3-2)+(4-3), 3-2)
= C(2, 1)
= 2
```

So:

```text
From Broken = 2
```

---

### Step 4 — Blocked Paths

```text
3 × 2 = 6
```

Therefore:

```text
Blocked = 6
```

---

### Step 5 — Final Answer

```text
Total - Blocked
= 10 - 6
= 4
```

Output:

```text
4
```

---

# 📊 Visual Representation

For the sample grid:

```text
       Column
       1   2   3   4
     ┌───┬───┬───┬───┐
Row 1│ S │   │   │   │
     ├───┼───┼───┼───┤
Row 2│   │   │ X │   │
     ├───┼───┼───┼───┤
Row 3│   │   │   │ D │
     └───┴───┴───┴───┘

S = Start
X = Broken Cell
D = Destination
```

Every shortest path has exactly:

```text
2 DOWN + 3 RIGHT
```

moves.

We count all such paths and remove the paths that go through `X`.

---

# 📌 Why We Don't Use BFS or DFS

A common first thought is:

> "This is a grid path problem, so I should use BFS or DFS."

That would work for finding a shortest distance, but it is unnecessary here.

The grid has no varying movement cost, and the problem asks specifically for **the number of shortest paths**.

Because every shortest path consists only of:

```text
DOWN + RIGHT
```

we can solve the problem directly using combinations.

This is both simpler and more efficient than explicitly traversing the grid.

---

# ⚙️ Complexity Analysis

The solution uses Python's `math.comb()` to calculate binomial coefficients.

There are only a constant number of combination calculations.

Therefore, in terms of the grid dimensions, the algorithm performs:

```text
O(1)
```

combination operations.

The values involved are at most:

```text
n + m - 2 ≤ 58
```

because:

```text
n, m ≤ 30
```

Therefore, the computation is extremely small.

### Space Complexity

Only a few integer variables are used:

```text
O(1)
```

So:

```text
Time Complexity:  O(1)
Space Complexity: O(1)
```

with respect to the input grid dimensions.

---

# 🔑 Key Concepts

This problem demonstrates:

* Grid path counting
* Shortest paths
* Combinatorics
* Binomial coefficients
* `math.comb()`
* Multiplication principle
* Inclusion/exclusion-style subtraction
* Mathematical optimization
* Avoiding unnecessary BFS/DFS

---

# 🎯 Key Takeaway

The most important insight is:

> **A shortest path from the top-left to the bottom-right can only move DOWN and RIGHT.**

Therefore, instead of exploring the grid, count the paths mathematically.

The complete idea is:

```text
             All Shortest Paths
                    ↓
          C(n+m-2, n-1)
                    ↓
          ┌─────────┴─────────┐
          │                   │
          ↓                   ↓
     Valid Paths        Paths Through
                         Broken Cell
                              ↓
              Paths to Broken ×
              Paths from Broken
                              ↓
                    Subtract from Total
                              ↓
                         Final Answer
```

The formula to remember is:

```text
Valid Paths
=
Total Paths
-
Paths Through Broken Cell
```

or:

```text
C(n+m-2, n-1)
-
C(x+y-2, x-1)
×
C((n-x)+(m-y), n-x)
```

For the sample:

```text
10 - (3 × 2)
= 10 - 6
= 4
```

Therefore, the robot has:

```text
4
```

valid shortest paths.
