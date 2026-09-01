# 🔗 Make Equal Elements Adjacent

## 📌 Problem Overview

You are given an array `A` of even length `N`.

The following conditions are guaranteed:

* `N` is even.
* Every distinct value appears **exactly twice**.
* In one operation, you can swap two **adjacent elements**.
* Your goal is to make every pair of equal elements adjacent.
* Find the **minimum number of adjacent swaps** required.

---

# 🧩 Problem Statement

Given:

```text
N = number of elements
A = array
```

Every value in `A` occurs exactly twice.

We need to transform the array so that equal values appear next to each other.

For example:

```text
A = [1, 2, 1, 2]
```

The two `1`s are separated by one element:

```text
[1, 2, 1, 2]
    ↑
```

Swap the middle elements:

```text
[1, 2, 1, 2]
       ↓
[1, 1, 2, 2]
```

Only one adjacent swap was required.

Therefore:

```text
Answer = 1
```

---

# 📥 Input Format

### First line

```text
N
```

The number of elements.

### Second line

```text
A[0] A[1] A[2] ... A[N-1]
```

The array elements.

---

# 📤 Output Format

Print one integer:

```text
minimum number of adjacent swaps
```

required to make every pair of equal elements adjacent.

---

# 🧪 Example

### Input

```text
4
1 2 1 2
```

### Output

```text
1
```

---

# 🧠 Main Idea

Suppose we have:

```text
[1, 2, 3, 1, 2, 3]
```

Take the first unprocessed element:

```text
1
```

Its matching `1` occurs later:

```text
[1, 2, 3, 1, 2, 3]
 ↑        ↑
 i        j
```

There are two currently active elements between them:

```text
2, 3
```

To bring the two `1`s together, one of the `1`s must cross those elements.

Therefore:

```text
cost = 2
```

After pairing the `1`s, we can conceptually remove both of them.

Now the remaining sequence is:

```text
[2, 3, 2, 3]
```

We repeat the same process.

---

# 🎯 Pattern Used

## Greedy + Fenwick Tree

This problem combines:

```text
Greedy Processing
       +
Fenwick Tree
(Binary Indexed Tree)
```

### Why Greedy?

Process pairs according to the first occurrence of each value.

For the current first unprocessed element, there is no benefit in delaying its pairing. Its matching copy must eventually cross every currently active element lying between the pair.

### Why Fenwick Tree?

After a pair is completed, we conceptually remove both elements.

We repeatedly need to answer:

> How many elements are still alive between positions `i` and `j`?

A Fenwick Tree can answer this in:

```text
O(log N)
```

and can also remove an element in:

```text
O(log N)
```

---

# 🧠 Key Observation

Suppose equal elements occur at:

```text
i < j
```

For example:

```text
[5, 8, 3, 7, 5]
 ↑           ↑
 i           j
```

The elements between them are:

```text
8, 3, 7
```

If all of them are still active, then:

```text
cost = 3
```

because the second `5` needs three adjacent swaps to reach the first `5`:

```text
[5, 8, 3, 7, 5]
             ↑

[5, 8, 3, 5, 7]   cost = 1
[5, 8, 5, 3, 7]   cost = 2
[5, 5, 8, 3, 7]   cost = 3
```

Therefore:

```text
Number of swaps
=
Number of currently alive elements
between the equal pair
```

This is the core of the solution.

---

# ❓ Why Can't We Just Use `j - i - 1`?

Initially, we could calculate:

```text
j - i - 1
```

But this becomes incorrect after previous pairs are processed.

Consider:

```text
[1, 2, 3, 1, 2, 3]
```

For pair `1`:

```text
[1, 2, 3, 1, 2, 3]
 ↑        ↑
```

Cost:

```text
2
```

Conceptually remove both `1`s:

```text
[2, 3, 2, 3]
```

Now consider pair `2`.

Their **original indexes** are:

```text
1 and 4
```

So:

```text
4 - 1 - 1 = 2
```

But in the current active sequence:

```text
[2, 3, 2, 3]
 ↑     ↑
```

there is only:

```text
1
```

element between them.

So the real cost is:

```text
1
```

not `2`.

We therefore need a data structure that knows which positions are still active.

That is exactly what the **Fenwick Tree** provides.

---

# 🌳 Fenwick Tree Representation

Initially every element is active.

For:

```text
A = [1, 2, 1, 2]
```

the Fenwick Tree logically represents:

```text
Index:   0  1  2  3
Array:   1  2  1  2
Alive:   1  1  1  1
```

Here:

```text
1 = active
0 = removed
```

After processing pair `1` at positions `0` and `2`:

```text
Index:   0  1  2  3
Array:   1  2  1  2
Alive:   0  1  0  1
```

The remaining active elements are effectively:

```text
[2, 2]
```

---

# 🔍 Fenwick Tree Operations

We need two operations.

## 1. Update

```python
fenwick.add(i, value)
```

This changes the active state of index `i`.

Initially:

```python
fenwick.add(i, 1)
```

means:

```text
element is active
```

Later:

```python
fenwick.add(i, -1)
```

means:

```text
remove this element
```

---

## 2. Prefix Sum

```python
fenwick.sum(i)
```

returns the number of active elements from:

```text
0 ... i
```

For example:

```text
Alive = [0, 1, 0, 1]
```

then:

```text
sum(0) = 0
sum(1) = 1
sum(2) = 1
sum(3) = 2
```

---

# 🧮 Counting Elements Between `i` and `j`

We want active elements strictly between:

```text
i and j
```

The range is:

```text
i + 1 ... j - 1
```

Using prefix sums:

```python
cost = fenwick.sum(j - 1) - fenwick.sum(i)
```

This gives exactly the number of currently active elements between the pair.

---

# 🔄 Algorithm

The complete algorithm is:

```text
1. Store the two positions of every value.

2. Create a Fenwick Tree.

3. Mark every array position as active.

4. Traverse the array from left to right.

5. For each value not already processed:

      i = first occurrence
      j = second occurrence

6. Count active elements between i and j.

7. Add this count to the answer.

8. Remove positions i and j from the Fenwick Tree.

9. Mark the value as processed.

10. Continue until every pair is processed.
```

---

# 💻 Python 3 Solution

```python
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, value):
        i += 1

        while i <= self.n:
            self.bit[i] += value
            i += i & -i

    def sum(self, i):
        result = 0
        i += 1

        while i > 0:
            result += self.bit[i]
            i -= i & -i

        return result


def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    # Store the two positions of every value
    positions = {}

    for i, x in enumerate(arr):
        positions.setdefault(x, []).append(i)

    # Fenwick Tree:
    # 1 = element is currently active
    fenwick = Fenwick(n)

    for i in range(n):
        fenwick.add(i, 1)

    answer = 0
    used = set()

    for i in range(n):
        x = arr[i]

        # Pair already processed
        if x in used:
            continue

        # Second occurrence of x
        j = positions[x][1]

        # Number of active elements strictly
        # between positions i and j
        cost = fenwick.sum(j - 1) - fenwick.sum(i)

        answer += cost

        # Conceptually remove the pair
        fenwick.add(i, -1)
        fenwick.add(j, -1)

        used.add(x)

    print(answer)


solve()
```

---

# 🔍 Code Explanation

## Step 1 — Store Positions

```python
positions = {}

for i, x in enumerate(arr):
    positions.setdefault(x, []).append(i)
```

For:

```text
A = [1, 2, 1, 2]
```

we get:

```text
positions = {
    1: [0, 2],
    2: [1, 3]
}
```

Because every value occurs exactly twice, each list contains exactly two indexes.

---

# Step 2 — Initialize Fenwick Tree

```python
fenwick = Fenwick(n)
```

Then:

```python
for i in range(n):
    fenwick.add(i, 1)
```

marks every position as active.

Initially:

```text
[1, 1, 1, 1]
```

---

# Step 3 — Traverse the Array

```python
for i in range(n):
```

We process elements from left to right.

Suppose:

```text
A = [1, 2, 1, 2]
```

At:

```text
i = 0
```

we have:

```text
x = 1
```

---

# Step 4 — Skip Already Processed Pairs

```python
if x in used:
    continue
```

Once both copies of a value have been processed, we do not process that value again.

---

# Step 5 — Find Matching Position

```python
j = positions[x][1]
```

For:

```text
x = 1
```

we have:

```text
positions[1] = [0, 2]
```

Therefore:

```text
i = 0
j = 2
```

---

# Step 6 — Calculate Cost

```python
cost = fenwick.sum(j - 1) - fenwick.sum(i)
```

For:

```text
[1, 2, 1, 2]
 ↑     ↑
 0     2
```

the only active element between the two `1`s is:

```text
2
```

Therefore:

```text
cost = 1
```

---

# Step 7 — Add Cost

```python
answer += cost
```

Now:

```text
answer = 1
```

---

# Step 8 — Remove the Pair

```python
fenwick.add(i, -1)
fenwick.add(j, -1)
```

The active-state representation changes from:

```text
[1, 1, 1, 1]
```

to:

```text
[0, 1, 0, 1]
```

Conceptually:

```text
[1, 2, 1, 2]
 ↓     ↓
remove remove
```

Remaining:

```text
[2, 2]
```

---

# Step 9 — Mark as Used

```python
used.add(x)
```

Now:

```text
used = {1}
```

So the `1` pair will never be processed again.

---

# 🔬 Complete Dry Run

Consider:

```text
A = [1, 2, 1, 2]
```

Initial active positions:

```text
[1, 1, 1, 1]
```

Answer:

```text
0
```

---

## Pair `1`

Positions:

```text
0, 2
```

Visualization:

```text
[1, 2, 1, 2]
 ↑     ↑
```

Active elements between:

```text
[2]
```

Therefore:

```text
cost = 1
```

Answer:

```text
answer = 1
```

Remove both `1`s:

```text
Alive:
[0, 1, 0, 1]
```

Conceptually remaining:

```text
[2, 2]
```

---

## Pair `2`

Originally at:

```text
1, 3
```

But the `1`s have already been removed.

Current active sequence:

```text
[2, 2]
```

There are no active elements between the `2`s.

Therefore:

```text
cost = 0
```

Answer:

```text
answer = 1 + 0
       = 1
```

---

# ✅ Final Answer

```text
1
```

---

# 🧪 Larger Example

Consider:

```text
A = [1, 2, 3, 1, 2, 3]
```

### Pair `1`

```text
[1, 2, 3, 1, 2, 3]
 ↑        ↑
```

Active elements between:

```text
2, 3
```

Cost:

```text
2
```

Conceptually remove `1`s:

```text
[2, 3, 2, 3]
```

---

### Pair `2`

```text
[2, 3, 2, 3]
 ↑     ↑
```

Active elements between:

```text
3
```

Cost:

```text
1
```

Remove `2`s:

```text
[3, 3]
```

---

### Pair `3`

Already adjacent:

```text
[3, 3]
```

Cost:

```text
0
```

Total:

```text
2 + 1 + 0 = 3
```

Therefore:

```text
Answer = 3
```

---

# 📊 Dry Run Table

For:

```text
A = [1, 2, 3, 1, 2, 3]
```

| Pair | Original Positions | Active Elements Between | Cost | Total |
| ---- | ------------------ | ----------------------: | ---: | ----: |
| `1`  | `(0,3)`            |                       2 |    2 |     2 |
| `2`  | `(1,4)`            |                       1 |    1 |     3 |
| `3`  | `(2,5)`            |                       0 |    0 |     3 |

Final:

```text
3
```

---

# ⚙️ Complexity Analysis

Let:

```text
N = number of elements
```

## Building Positions

```python
for i, x in enumerate(arr):
```

takes:

```text
O(N)
```

---

## Initializing Fenwick Tree

We perform `N` updates.

Each Fenwick update takes:

```text
O(log N)
```

Therefore:

```text
O(N log N)
```

---

## Processing Pairs

There are:

```text
N / 2
```

pairs.

For each pair we perform:

* Prefix-sum queries
* Two Fenwick updates

Each operation takes:

```text
O(log N)
```

Therefore:

```text
O(N log N)
```

---

## Final Complexity

```text
Time Complexity:  O(N log N)
Space Complexity: O(N)
```

---

# 🧠 Fenwick Tree Functions to Remember

## Update

```python
def add(self, i, value):
    i += 1

    while i <= self.n:
        self.bit[i] += value
        i += i & -i
```

Mental model:

```text
add(index, +1) → activate
add(index, -1) → remove
```

---

## Prefix Sum

```python
def sum(self, i):
    result = 0
    i += 1

    while i > 0:
        result += self.bit[i]
        i -= i & -i

    return result
```

Mental model:

```text
sum(i)
=
number of active elements
from index 0 through i
```

---

# 🔑 Most Important Formula

For two equal elements at:

```text
i < j
```

the number of currently active elements strictly between them is:

```python
fenwick.sum(j - 1) - fenwick.sum(i)
```

Therefore:

```text
Pair Cost
=
Alive elements between i and j
```

---

# 🎯 Why the Greedy Strategy Works

For the first active element, suppose its matching element occurs later.

Example:

```text
[x, a, b, c, x]
```

To make the two `x`s adjacent, one of them must cross:

```text
a, b, c
```

There is no way around those crossings.

Each crossing requires one adjacent swap.

Therefore the unavoidable cost is:

```text
3
```

Once the pair has been made adjacent, we can treat it as completed and remove it from future consideration.

That gives the greedy strategy:

```text
Take first active element
        ↓
Find matching copy
        ↓
Count active elements between them
        ↓
Add that unavoidable cost
        ↓
Remove the pair
        ↓
Repeat
```

---

# 🧠 Pattern Recognition

When you see a problem involving:

```text
Adjacent swaps
      +
Pairs
      +
Elements becoming irrelevant/removed
      +
Need to count remaining elements between positions
```

consider:

```text
Fenwick Tree
```

The key clue is:

> We repeatedly need dynamic range counts while elements are being removed.

Fenwick Trees are excellent for:

```text
Point Update
+
Prefix Sum
+
Range Sum
```

in:

```text
O(log N)
```

per operation.

---

# 🆚 Brute Force vs Fenwick Tree

A simpler approach could physically move the matching element through the array using adjacent swaps.

For example:

```text
[1, 4, 7, 9, 1]
```

Move the second `1` left:

```text
[1, 4, 7, 1, 9]
[1, 4, 1, 7, 9]
[1, 1, 4, 7, 9]
```

This works, but repeatedly modifying the array can lead to:

```text
O(N²)
```

in the worst case.

The Fenwick Tree avoids physically moving elements.

Instead, it asks:

```text
How many active elements are between
the two matching positions?
```

That gives the required swap count directly.

---

# 🏆 Final Solution

```python
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, value):
        i += 1

        while i <= self.n:
            self.bit[i] += value
            i += i & -i

    def sum(self, i):
        result = 0
        i += 1

        while i > 0:
            result += self.bit[i]
            i -= i & -i

        return result


def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    positions = {}

    for i, x in enumerate(arr):
        positions.setdefault(x, []).append(i)

    fenwick = Fenwick(n)

    # Initially every position is active
    for i in range(n):
        fenwick.add(i, 1)

    answer = 0
    used = set()

    for i in range(n):
        x = arr[i]

        if x in used:
            continue

        j = positions[x][1]

        # Active elements strictly between i and j
        cost = fenwick.sum(j - 1) - fenwick.sum(i)

        answer += cost

        # Remove completed pair
        fenwick.add(i, -1)
        fenwick.add(j, -1)

        used.add(x)

    print(answer)


solve()
```

---

# 🚀 Final Mental Model

Remember the problem like this:

```text
[ x | . . . . | x ]
  ↑             ↑
first         match

        ↓

Count ACTIVE elements
between the pair

        ↓

Each active element
requires one crossing

        ↓

cost = active elements between

        ↓

Remove both x's

        ↓

Repeat
```

So the entire solution can be remembered as:

```text
First Unprocessed Element
          ↓
Find its Matching Position
          ↓
Fenwick Range Count
          ↓
Add Cost
          ↓
Remove Both Positions
          ↓
Repeat
```

## 🔥 One-Line Exam Recall

> **Process each pair greedily from left to right; its swap cost equals the number of still-active elements between its two occurrences, which a Fenwick Tree can query and update in `O(log N)`.**

### Pattern

```text
Greedy + Fenwick Tree / BIT
```

### Complexity

```text
Time  → O(N log N)
Space → O(N)
```
