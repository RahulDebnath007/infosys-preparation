# 🎯 Minimize Unique Elements

A classic **Frequency Counting + Greedy** problem: given a list of integers and a limited deletion budget, minimize the number of distinct values remaining.

---

## 🧩 Problem Overview

You are given a list of integers `L`.

You are allowed to delete **at most `X`** elements from the list.

Your goal is to delete elements so that the number of **distinct integers** remaining is as small as possible.

**Key idea:** To eliminate one distinct value, you must delete *all* occurrences of that value. So, to eliminate as many distinct values as possible, remove the values with the **smallest frequencies first**.

---

## 📥 Input Format

```
X
L (space-separated integers)
```

- Line 1: integer `X` — the maximum number of elements that can be deleted
- Line 2: space-separated integers representing the list `L`

**Example:**
```
4
1 1 1 2 2 3 3 4 5 6
```
This represents `X = 4` and `L = [1, 1, 1, 2, 2, 3, 3, 4, 5, 6]`.

## 📤 Output Format

A single integer: the minimum possible number of unique elements remaining after performing at most `X` deletions.

## 🔢 Constraints

- `1 ≤ |L| ≤ 10⁵`
- `0 ≤ X`

---

## 🧠 Key Insight

The goal is **not** to minimize the number of *elements* — it's to minimize the number of *distinct values*.

For `L = [1, 1, 1, 2, 2, 3, 3, 4, 5, 6]`, the frequencies are:

| Value | Frequency |
|-------|-----------|
| 1     | 3         |
| 2     | 2         |
| 3     | 2         |
| 4     | 1         |
| 5     | 1         |
| 6     | 1         |

Removing a value entirely reduces the distinct count by exactly 1, and costs exactly its frequency in deletions. To eliminate the **maximum number** of distinct values, always eliminate the **cheapest** ones first — i.e., sort frequencies ascending.

---

## 🧪 Sample Walkthrough

**Input**
```
4
1 1 1 2 2 3 3 4 5 6
```

1. **Count frequencies** → `{1:3, 2:2, 3:2, 4:1, 5:1, 6:1}` → 6 unique values initially
2. **Sort frequencies ascending** → `[1, 1, 1, 2, 2, 3]`
3. **Spend the budget** (`X = 4`):
   - Remove value `4` (cost 1) → `X = 3`, unique = 5
   - Remove value `5` (cost 1) → `X = 2`, unique = 4
   - Remove value `6` (cost 1) → `X = 1`, unique = 3
   - Next frequency is `2`, but only `1` deletion remains → **stop**

**Final Answer: `3`**

---

## 🔍 Algorithm

1. Count how many times each integer occurs (`Counter`).
2. Extract all frequencies.
3. Sort frequencies ascending.
4. Start with `unique = len(freq)`.
5. For each frequency `f`, in order:
   - If `X >= f`: subtract `f` from `X`, decrement `unique` (value fully removed).
   - Else: stop — no later (larger) frequency can be afforded either.
6. Print the remaining `unique` count.

---

## 💻 Python 3 Solution

```python
from collections import Counter

X = int(input().strip())
L = list(map(int, input().split()))

freq = sorted(Counter(L).values())
unique = len(freq)

for f in freq:
    if X >= f:
        X -= f
        unique -= 1
    else:
        break

print(unique)
```

---

## 🧩 Code Breakdown

1. **Count frequencies** — `Counter(L)` maps each value to its occurrence count.
2. **Get frequencies** — `Counter(L).values()` yields `3, 2, 2, 1, 1, 1` for the example.
3. **Sort ascending** — `sorted(...)` → `[1, 1, 1, 2, 2, 3]` (cheapest removals first).
4. **Initial unique count** — `unique = len(freq)` (one entry per distinct value).
5. **Greedy elimination** — for each frequency, ask "can I afford to delete *all* occurrences?" If yes, remove the value completely; if no, stop.

### Why the greedy strategy works

With `X = 3` and frequencies `[1, 2, 5]`:
- Trying to remove frequency `5` first is impossible (`5 > 3`).
- Removing `1` then `2` costs `1 + 2 = 3`, eliminating **2** distinct values.

Processing smallest-to-largest always lets you eliminate the greatest number of distinct groups for a given budget.

---

## 🧪 Another Example

**Input**
```
5
1 1 2 2 3 3 3 4
```

Frequencies: `{1:2, 2:2, 3:3, 4:1}` → sorted: `[1, 2, 2, 3]`, initial unique = 4

- Remove freq `1` → `X = 4`, unique = 3
- Remove freq `2` → `X = 2`, unique = 2
- Remove freq `2` → `X = 0`, unique = 1
- Can't afford freq `3` → stop

**Answer: `1`**

---

## 🧩 Pattern Recognition

| Problem Clue | 💡 Think |
|---|---|
| Count occurrences | `Counter` / HashMap |
| Minimize distinct values | Remove complete groups |
| Limited deletion budget | Greedy |
| Cost to remove a value | Its frequency |
| Cheapest group first | Sort ascending |
| Cannot afford next group | `break` |

---

## ⚠️ Common Mistakes

- **Sorting the original list.** You don't need `L.sort()` — only frequency counts matter.
- **Removing elements randomly.** Deleting one occurrence from `[1, 1, 1]` still leaves `1` as distinct. The *entire* frequency must be spent to eliminate a value.
- **Processing frequencies in descending order.** Always go smallest → largest, not `[3, 2, 2, 1, 1, 1]`.
- **Forgetting to `break`.** Since frequencies are sorted ascending, once one can't be afforded, none of the later (larger) ones can either — stop immediately.

---

## ⏱️ Complexity Analysis

Let `N = len(L)` and `K` = number of distinct values (`K ≤ N`):

- **Time:** `O(N + K log K)` → worst case `O(N log N)`
- **Space:** `O(N)` (frequency map can hold up to `N` distinct values)

---

## ⭐ Key Takeaway

> How many complete frequency groups can I eliminate with `X` deletions?

**Count frequencies → Sort ascending → Remove cheapest groups first → Count remaining unique values**

### 🚀 One-line memory trick

```
Frequency → Sort → Cheapest First → Reduce Unique
```

```python
freq = sorted(Counter(L).values())
for f in freq:
    if X >= f:
        X -= f
        unique -= 1
    else:
        break
```