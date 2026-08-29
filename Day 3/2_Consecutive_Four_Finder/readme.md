# 🔢 Consecutive Four Finder

## 📌 Problem Overview

Given an `M × N` matrix of positive integers, find whether there exists a sequence of **at least four identical numbers** that are adjacent to each other.

The sequence can appear in any of these directions:

* ➡️ Horizontal
* ⬇️ Vertical
* ↘️ Diagonal down-right
* ↗️ Diagonal up-right

If multiple numbers form a valid sequence, return the **smallest number**.

If no number forms a sequence of four or more consecutive identical values, print:

```text
-1
```

---

## 🧩 Problem Statement

You are given an `M × N` matrix.

A number forms a valid sequence if the same number occurs **four or more times consecutively** in:

```text
Horizontal     →  (0, 1)
Vertical       ↓  (1, 0)
Diagonal       ↘  (1, 1)
Diagonal       ↗  (-1, 1)
```

If multiple numbers satisfy this condition, output the **minimum value** among them.

---

## 📥 Input Format

The first line contains two space-separated integers:

```text
m n
```

where:

* `m` = number of rows
* `n` = number of columns

The next `m` lines contain `n` space-separated integers representing the matrix.

### Example

```text
6 7
1 2 3 4 5 6 7
8 9 1 5 3 4 5
6 7 8 5 8 8 9
1 2 3 5 5 6 7
8 9 1 5 3 4 5
1 1 1 2 2 2 2
```

---

## 📤 Output Format

Print the smallest number that forms a sequence of at least four consecutive identical values.

If no such sequence exists, print:

```text
-1
```

---

# 🧪 Sample Input 1

```text
6 7
1 2 3 4 5 6 7
8 9 1 5 3 4 5
6 7 8 5 8 8 9
1 2 3 5 5 6 7
8 9 1 5 3 4 5
1 1 1 2 2 2 2
```

## 🧪 Sample Output 1

```text
2
```

### Explanation

There are two valid sequences.

### Vertical sequence of `5`

The `5`s in column `4` form:

```text
5
5
5
5
```

So:

```text
5 → valid
```

### Horizontal sequence of `2`

The last row contains:

```text
1 1 1 2 2 2 2
      └──────┘
```

There are four consecutive `2`s.

So:

```text
2 → valid
```

The valid numbers are:

```text
{2, 5}
```

The smallest value is:

```text
2
```

Therefore, the answer is:

```text
2
```

---

# 💡 Approach

The simplest way to solve the problem is to examine every cell as a possible starting point of a sequence.

Instead of checking all **8 directions**, we only need to check **4 directions**:

```python
directions = [
    (0, 1),    # Right
    (1, 0),    # Down
    (1, 1),    # Down-right diagonal
    (-1, 1)    # Up-right diagonal
]
```

Why only four?

Because every line has two opposite directions.

For example:

```text
→
←
```

Checking `→` from every cell is enough to detect the same sequence that could be found by checking `←`.

Similarly:

```text
↓ and ↑
↘ and ↖
↗ and ↙
```

Therefore, four directions cover every possible straight sequence.

---

# 🔍 Algorithm

For every cell `(i, j)`:

1. Store its value as `num`.
2. Try each of the four possible directions.
3. Start from the neighboring cell in that direction.
4. Continue while:

   * The position remains inside the matrix.
   * The value is equal to `num`.
5. Count consecutive matching values.
6. If the count reaches `4`, add `num` to a set.
7. After checking the entire matrix:

   * Return the minimum value in the set.
   * If the set is empty, return `-1`.

---

# 🧠 Why Use a Set?

Suppose the number `5` forms several different sequences.

We do not need to store `5` multiple times.

A Python `set` automatically stores each value only once:

```python
sequences = set()
```

When a valid sequence is found:

```python
sequences.add(num)
```

At the end:

```python
min(sequences)
```

gives the smallest number that forms a valid sequence.

---

# 🔍 Direction Representation

Each direction is represented as:

```text
(dx, dy)
```

where:

* `dx` = change in row
* `dy` = change in column

### 1. Right

```text
(0, 1)
```

Example:

```text
→ → →
```

The row stays the same while the column increases.

---

### 2. Down

```text
(1, 0)
```

Example:

```text
↓
↓
↓
```

The row increases while the column stays the same.

---

### 3. Down-Right

```text
(1, 1)
```

Example:

```text
↘
  ↘
    ↘
```

Both row and column increase.

---

### 4. Up-Right

```text
(-1, 1)
```

Example:

```text
    ↗
  ↗
↗
```

The row decreases while the column increases.

---

# 💻 Python 3 Solution

```python
def find_sequence(matrix, m, n):
    sequences = set()

    # Right, Down, Down-Right, Up-Right
    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (-1, 1)
    ]

    for i in range(m):
        for j in range(n):
            num = matrix[i][j]

            for dx, dy in directions:
                count = 1
                x = i + dx
                y = j + dy

                while (
                    0 <= x < m
                    and 0 <= y < n
                    and matrix[x][y] == num
                ):
                    count += 1

                    if count >= 4:
                        sequences.add(num)
                        break

                    x += dx
                    y += dy

    return min(sequences) if sequences else -1


# Read input
m, n = map(int, input().split())

matrix = [
    list(map(int, input().split()))
    for _ in range(m)
]

# Print result
print(find_sequence(matrix, m, n))
```

---

# 🧪 Example Walkthrough

Consider:

```text
1 2 3 4
5 5 5 5
6 7 8 9
2 3 4 5
```

Starting from the first `5`:

```text
5 5 5 5
```

Moving right:

```text
(0, 1)
```

we get:

```text
5 → 5 → 5 → 5
```

The count becomes:

```text
1 → 2 → 3 → 4
```

Once:

```text
count >= 4
```

the number `5` is added to the set.

Therefore:

```text
sequences = {5}
```

and the answer is:

```text
5
```

---

# ⚙️ Complexity Analysis

Let:

```text
M = number of rows
N = number of columns
```

There are:

```text
M × N
```

cells.

For every cell, we check four directions.

In the worst case, a direction can traverse many cells, especially when the matrix contains large regions of the same value.

Therefore, the worst-case complexity of the provided implementation is:

```text
Time Complexity: O(M × N × max(M, N))
```

The matrix itself requires:

```text
O(M × N)
```

space.

The `sequences` set requires at most:

```text
O(K)
```

where `K` is the number of distinct values forming valid sequences.

So the overall auxiliary space is:

```text
O(M × N)
```

for storing the matrix.

---

# 🚨 Important Optimization Note

The given solution is easy to understand, but for the maximum constraint:

```text
M, N ≤ 1000
```

the worst-case repeated traversal can become expensive.

A more optimized solution can process each direction using **dynamic programming / run-length counting**, checking each cell once per direction.

That approach can reduce the sequence detection to:

```text
O(M × N)
```

time.

For learning purposes, however, the direction-based traversal above is a straightforward and intuitive solution.

---

# 📌 Edge Cases

### No Sequence

```text
1 2 3 4
5 6 7 8
9 1 2 3
4 5 6 7
```

No number occurs four times consecutively.

Output:

```text
-1
```

---

### Horizontal Sequence

```text
1 2 3 4
7 7 7 7
5 6 8 9
2 3 4 5
```

Output:

```text
7
```

---

### Vertical Sequence

```text
1 5 2 3
4 5 6 7
8 5 9 1
2 5 3 4
```

Output:

```text
5
```

---

### Diagonal Sequence

```text
5 1 2 3
4 5 6 7
8 9 5 1
2 3 4 5
```

The `5`s form a diagonal:

```text
5
  5
    5
      5
```

Output:

```text
5
```

---

### Multiple Valid Numbers

If:

```text
2
```

and:

```text
7
```

both form valid sequences, the answer is:

```text
2
```

because the problem asks for the **smallest valid number**.

---

# 🔑 Key Concepts

This problem demonstrates:

* 2D matrix traversal
* Direction vectors
* Horizontal/vertical traversal
* Diagonal traversal
* Boundary checking
* Consecutive element counting
* Python `set`
* Minimum value selection
* Grid-based problem solving

---

# 🎯 Key Takeaway

For matrix problems involving consecutive elements, think in terms of **direction vectors**.

Instead of writing separate logic for every possible line, represent movement as:

```text
(dx, dy)
```

For this problem:

```text
Right        → (0, 1)
Down         → (1, 0)
Down-Right   → (1, 1)
Up-Right     → (-1, 1)
```

Then systematically check every cell in those directions.

The overall idea is:

```text
        Matrix
           ↓
    Check every cell
           ↓
   Check 4 directions
           ↓
 Count consecutive values
           ↓
      Count >= 4?
       ↙        ↘
     No          Yes
     ↓            ↓
 Continue      Store value
                  ↓
             Find minimum
                  ↓
                Answer
```

This provides a clean way to solve the **Consecutive Four Finder** problem.
