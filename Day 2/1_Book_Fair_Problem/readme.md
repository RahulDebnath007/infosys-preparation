# 📚 Book Fair Problem

## 🧩 Problem Overview

A school has `N` books and `N` shelves.
Each book has a thickness, and each shelf has a capacity.
The librarian follows a fixed placement strategy:

1. Process books from left to right.
2. For each book, check shelves from left to right.
3. Place the book on the **first unused shelf** whose capacity is greater than or equal to the book's thickness.
4. Once a shelf is used, it cannot be used again.
5. If no suitable shelf is available, the book remains unplaced.

The task is to find the total number of **unplaced books**.

---

## 📥 Input Format

The input consists of:

- The first line containing an integer `N`.
- The next `N` lines containing the `Books` array.
- The following `N` lines containing the `Shelves` array.

### Example

```
3
2
5
7
6
3
8
```

This represents:

```
N = 3

Books   = [2, 5, 7]
Shelves = [6, 3, 8]
```

---

## 📤 Output Format

Print a single integer representing the number of books that could not be placed.

---

## 🔢 Constraints

```
1 ≤ N ≤ 10³
1 ≤ Books[i], Shelves[i] ≤ 10⁵
```

---

## 🧠 Approach

This is a **Greedy + Simulation** problem.
For every book, scan the shelves from left to right and select the **first available shelf** that can accommodate it.
To track used shelves, maintain a boolean array:

```
used = [False] * n
```

Initially, every shelf is available.
When a shelf is used, change its value to `True`.

---

## 🔍 Algorithm

For every book:

1. Set `placed = False`.
2. Scan all shelves from left to right.
3. Check whether:
   ```
   not used[j] and shelves[j] >= book
   ```
4. If the condition is satisfied:
   - Mark the shelf as used.
   - Mark the book as placed.
   - Stop searching using `break`.
5. If no suitable shelf is found, increment `unplaced`.

---

## 🧪 Dry Run

### Input

```
3
2
5
7
6
3
8
```

Initial state:

```
Books   = [2, 5, 7]
Shelves = [6, 3, 8]

Used     = [False, False, False]
Unplaced = 0
```

### Book 1 → `2`

Check shelves from left to right:

```
Shelf 1 → 6 >= 2 ✅
```

Place the book on Shelf 1.

```
Used = [True, False, False]
```

### Book 2 → `5`

Check:

```
Shelf 1 → Used ❌
Shelf 2 → 3 >= 5 ❌
Shelf 3 → 8 >= 5 ✅
```

Place the book on Shelf 3.

```
Used = [True, False, True]
```

### Book 3 → `7`

Check:

```
Shelf 1 → Used ❌
Shelf 2 → 3 >= 7 ❌
Shelf 3 → Used ❌
```

No suitable shelf exists.
Therefore:

```
Unplaced = 1
```

### Output

```
1
```

---

## 💻 Python 3 Solution

```python
def arrange_books(n, books, shelves):
    used = [False] * n
    unplaced = 0

    for book in books:
        placed = False

        for j in range(n):
            if not used[j] and shelves[j] >= book:
                used[j] = True
                placed = True
                break

        if not placed:
            unplaced += 1

    return unplaced


if __name__ == "__main__":
    n = int(input().strip())

    books = [int(input().strip()) for _ in range(n)]
    shelves = [int(input().strip()) for _ in range(n)]

    print(arrange_books(n, books, shelves))
```

---

## 🎯 Why `break` Is Important

The problem requires the **first suitable shelf**.
Suppose:

```
Book = 5
Shelves = [6, 8, 10]
```

All three shelves can hold the book, but Shelf 1 must be selected because it is the first suitable shelf.
Therefore:

```
used[j] = True
placed = True
break
```

The `break` stops the search immediately.

---

## 🚨 Important: Do Not Sort

Do **not** sort the books or shelves:

```python
books.sort()      # ❌
shelves.sort()    # ❌
```

The original order is part of the problem.

```
Books   → original order
Shelves → original order
```

Changing the order can change the result.

---

## 🧩 Why This Is Greedy

The librarian makes the first valid choice immediately:

```
Current book
    ↓
First available suitable shelf
    ↓
Place book
    ↓
Mark shelf as used
    ↓
Move to next book
```

There is no reconsideration of previous placements.
The key clue is:

> **"First unused shelf that can hold the book."**

This is a classic greedy placement strategy combined with simulation.

---

## 🧠 Exam Recognition

| Problem Clue                      | Think                |
| ---------------------------------- | --------------------- |
| Process elements in given order    | 🔄 Simulation         |
| Search left to right               | ➡️ Sequential scan     |
| First valid position               | 🟢 Greedy             |
| Shelf can be used once             | 🔒 Boolean `used[]`   |
| Capacity must be enough            | `shelf >= book`       |
| Stop after finding one             | `break`               |
| Count failed placements            | Counter               |

---

## ⚠️ Common Mistakes

### ❌ 1. Forgetting to mark the shelf

Wrong:

```python
if shelves[j] >= book:
    placed = True
```

This allows the same shelf to be reused.

Correct:

```python
used[j] = True
```

### ❌ 2. Forgetting `break`

Without `break`, the search continues after finding a suitable shelf.

Correct:

```python
used[j] = True
placed = True
break
```

### ❌ 3. Sorting the arrays

```python
books.sort()      # ❌
shelves.sort()    # ❌
```

The problem requires the original order.

### ❌ 4. Using `>` instead of `>=`

A shelf with capacity exactly equal to the book thickness can hold it.

Correct:

```python
shelves[j] >= book
```

---

## ⏱️ Complexity Analysis

There are `N` books. For each book, we may scan all `N` shelves.

### Time Complexity

```
O(N²)
```

Since `N ≤ 1000`, the worst case is approximately:

```
1000 × 1000 = 1,000,000
```

shelf checks, which is easily manageable.

### Space Complexity

The `used` array requires:

```
O(N)
```

---

## 🗺️ Mental Model

```
📚 Take next book
       ↓
🗄️ Scan shelves left → right
       ↓
🔍 Unused AND capacity >= book?
       ↓
   ┌───────────────┐
   │               │
  YES              NO
   │               │
   ↓               ↓
✅ Place        Next shelf
   │
   ↓
🔒 Mark used
   │
   ↓
📚 Next book
```

If every shelf fails:

```
unplaced += 1
```

---

## ⭐ Key Takeaway

Remember this pattern:

```
BOOK ORDER FIXED
       ↓
SHELVES LEFT → RIGHT
       ↓
FIRST VALID SHELF
       ↓
MARK AS USED
       ↓
REPEAT
```

### 🔑 One-Line Memory Trick

> **Take each book in order and give it the first available shelf that fits.**

This is a classic **Greedy + Simulation + Boolean Tracking** problem.