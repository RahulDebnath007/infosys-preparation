# 8 🏝️ Andy's Vacation – Maximum Consecutive Vacation Days (Sliding Window)

[![Repository](https://img.shields.io/badge/Repository-infosys--preparation-blue?logo=github)](https://github.com/RahulDebnath007/infosys-preparation)

## 📌 Problem Statement

Andy wants to go on a vacation to de-stress himself.

There are **N consecutive days**, numbered from `1` to `N`.

Andy already has **M obligations**, where the `i-th` obligation is scheduled on day `D[i]`.

Andy can cancel at most **K obligations** in order to create one continuous vacation period.

The objective is to determine the **maximum number of consecutive days** Andy can take as vacation.

### Important Observation

Suppose Andy chooses a vacation interval:

```text
[L ... R]
```

The length of the vacation is:

```text
R - L + 1
```

For this interval to be possible, the number of obligations inside the interval must be at most `K`.

Therefore, the problem becomes:

```text
Find the longest consecutive range
whose number of obligations is <= K.
```

This is a classic **Sliding Window / Two Pointer** problem.

---

# 💡 Approach

A brute-force solution could check every possible vacation interval.

There are approximately:

```text
N × N
```

possible intervals.

This would result in:

```text
O(N²)
```

time complexity, which is inefficient for large constraints such as:

```text
N <= 10⁶
M <= 2 × 10⁶
```

### Key Observation

For every possible vacation interval:

```text
[L ... R]
```

we only care about:

```text
Number of obligations inside the window
```

The window is valid when:

```text
obligations_in_window <= K
```

Therefore, we can maintain a **sliding window** using two pointers:

```text
left
right
```

The `right` pointer expands the window.

If the window becomes invalid:

```text
obligations_in_window > K
```

we move the `left` pointer forward until the window becomes valid again.

---

# 🧠 Algorithm

1. Create an array `obligations` of size `N + 1`.
2. Store the number of obligations for each day.
3. Initialize:

   * `left = 1`
   * `current_obligations = 0`
   * `max_vacation = 0`
4. Move the `right` pointer from day `1` to day `N`.
5. Add the obligations of day `right` to `current_obligations`.
6. If:

   ```text
   current_obligations > K
   ```

   shrink the window from the left.
7. Once the window becomes valid, calculate:

   ```text
   vacation_length = right - left + 1
   ```
8. Update the maximum vacation length.
9. Continue until `right` reaches `N`.
10. Return `max_vacation`.

---

# 🔍 Understanding the Obligation Array

Suppose:

```text
N = 10
```

and obligations are:

```text
2
3
6
7
9
```

We create:

```text
Day:          1 2 3 4 5 6 7 8 9 10
Obligations:  0 1 1 0 0 1 1 0 1 0
```

Each index represents a day.

The value represents the number of obligations scheduled on that day.

For example:

```text
obligations[2] = 1
```

means there is one obligation on day `2`.

---

## Handling Duplicate Obligations

There can be multiple obligations on the same day.

For example:

```text
D = [2, 2, 3, 3, 7]
```

The array becomes:

```text
Day:          1 2 3 4 5 6 7
Obligations:  0 2 2 0 0 0 1
```

This is why we use:

```python
obligations[day] += 1
```

instead of:

```python
obligations[day] = 1
```

Each obligation counts separately because Andy can cancel obligations individually.

---

# 📝 Code Explanation (Step-by-Step)

## Step 1 — Read Input

```python
N = int(input())
M = int(input())
K = int(input())
```

We read the three main inputs:

* `N` → Total number of days
* `M` → Total number of obligations
* `K` → Maximum number of obligations Andy can cancel

Example:

```text
N = 10
M = 5
K = 2
```

---

## Step 2 — Create the Obligation Array

```python
obligations = [0] * (N + 1)
```

Create an array to store the number of obligations on each day.

`N + 1` is used because days are numbered from:

```text
1 to N
```

Index `0` is unused.

For:

```text
N = 5
```

the array initially looks like:

```text
[0, 0, 0, 0, 0, 0]
```

---

## Step 3 — Store Obligations

```python
for _ in range(M):
    day = int(input())
    obligations[day] += 1
```

Read all `M` obligations.

For example:

```text
6
9
3
2
7
```

After processing them:

```text
Day:          1 2 3 4 5 6 7 8 9 10
Obligations:  0 1 1 0 0 1 1 0 1 0
```

---

## Step 4 — Initialize the Left Pointer

```python
left = 1
```

`left` represents the beginning of the current vacation window.

Initially:

```text
left = 1
```

The window starts from day `1`.

---

## Step 5 — Track Current Obligations

```python
current_obligations = 0
```

This stores the number of obligations currently inside the sliding window.

Initially:

```text
current_obligations = 0
```

The window is empty.

---

## Step 6 — Track Maximum Vacation

```python
max_vacation = 0
```

This stores the longest valid vacation found so far.

Initially:

```text
max_vacation = 0
```

---

## Step 7 — Expand the Window

```python
for right in range(1, N + 1):
```

The `right` pointer moves from:

```text
1 → 2 → 3 → ... → N
```

It expands the current vacation window.

For example:

```text
[1]
```

then:

```text
[1 2]
```

then:

```text
[1 2 3]
```

and so on.

---

## Step 8 — Add Obligations

```python
current_obligations += obligations[right]
```

When the `right` pointer enters a new day, add the number of obligations on that day.

For example, if:

```text
right = 3
```

and:

```text
obligations[3] = 1
```

then:

```text
current_obligations += 1
```

---

## Step 9 — Check Whether the Window Is Invalid

```python
while current_obligations > K:
```

The window is valid only when:

```text
current_obligations <= K
```

If:

```text
current_obligations > K
```

Andy cannot cancel all the obligations inside the window.

Therefore, the window must be reduced.

---

## Step 10 — Remove Obligations From the Left

```python
current_obligations -= obligations[left]
```

Remove the obligations belonging to the day at the left boundary.

For example:

```text
left = 2
obligations[2] = 1
```

Then:

```text
current_obligations -= 1
```

This effectively removes day `2` from the window.

---

## Step 11 — Move the Left Pointer

```python
left += 1
```

Move the left pointer forward.

For example:

```text
Before:

[1 2 3 4 5 6]
 ↑
left
```

After removing day `1`:

```text
[2 3 4 5 6]
 ↑
left
```

The `while` loop continues until:

```text
current_obligations <= K
```

---

## Step 12 — Calculate Vacation Length

```python
vacation_length = right - left + 1
```

Once the window becomes valid, calculate its length.

The window is:

```text
[left ... right]
```

Therefore:

```text
length = right - left + 1
```

For example:

```text
left = 3
right = 6
```

Then:

```text
6 - 3 + 1 = 4
```

The vacation consists of:

```text
3, 4, 5, 6
```

which is `4` days.

---

## Step 13 — Update the Maximum

```python
max_vacation = max(max_vacation, vacation_length)
```

Keep the maximum vacation length found so far.

Example:

```text
Current maximum = 5
Current window = 4
```

Then:

```text
max(5, 4) = 5
```

If the current window has length `7`:

```text
max(5, 7) = 7
```

So the answer becomes `7`.

---

## Step 14 — Print the Answer

After processing all `N` days:

```python
print(max_vacation)
```

Print the maximum number of consecutive vacation days.

---

# 🔍 Complete Code

```python
N = int(input())
M = int(input())
K = int(input())

# obligations[day] = number of obligations on that day
obligations = [0] * (N + 1)

for _ in range(M):
    day = int(input())
    obligations[day] += 1

left = 1
current_obligations = 0
max_vacation = 0

for right in range(1, N + 1):

    # Add obligations of the current day
    current_obligations += obligations[right]

    # Shrink the window if more than K
    # obligations are present
    while current_obligations > K:
        current_obligations -= obligations[left]
        left += 1

    # Calculate current valid window length
    vacation_length = right - left + 1

    # Update maximum vacation
    max_vacation = max(max_vacation, vacation_length)

print(max_vacation)
```

---

# 🧪 Dry Run

## Sample Input

```text
10
5
2
6
9
3
2
7
```

Therefore:

```text
N = 10
M = 5
K = 2
```

Obligations:

```text
6, 9, 3, 2, 7
```

After storing them:

```text
Day:          1 2 3 4 5 6 7 8 9 10
Obligations:  0 1 1 0 0 1 1 0 1 0
```

---

## Window 1

```text
left = 1
right = 1
```

Window:

```text
[1]
```

Obligations:

```text
0
```

Valid.

Vacation length:

```text
1
```

Maximum:

```text
1
```

---

## Window 2

```text
left = 1
right = 2
```

Window:

```text
[1 2]
```

Obligations:

```text
1
```

Valid because:

```text
1 <= 2
```

Length:

```text
2
```

Maximum:

```text
2
```

---

## Window 3

```text
left = 1
right = 3
```

Window:

```text
[1 2 3]
```

Obligations:

```text
2
```

Valid because:

```text
2 <= 2
```

Length:

```text
3
```

Maximum:

```text
3
```

---

## Window 4

```text
left = 1
right = 4
```

Window:

```text
[1 2 3 4]
```

Obligations:

```text
2
```

Length:

```text
4
```

Maximum:

```text
4
```

---

## Window 5

```text
left = 1
right = 5
```

Window:

```text
[1 2 3 4 5]
```

Obligations:

```text
2
```

Length:

```text
5
```

Maximum:

```text
5
```

---

## Window 6

Day `6` contains an obligation.

Now:

```text
current_obligations = 3
```

But:

```text
K = 2
```

Therefore:

```text
3 > 2
```

The window is invalid.

We move `left` forward until the window becomes valid.

The final valid window becomes:

```text
[3 4 5 6]
```

It contains:

```text
Day 3 → 1 obligation
Day 6 → 1 obligation
```

Total:

```text
2 obligations
```

Length:

```text
4
```

The maximum remains:

```text
5
```

---

## Final Answer

```text
5
```

Andy can cancel the obligations on days `2` and `3` and take:

```text
1 2 3 4 5
```

as his vacation.

Therefore:

```text
Maximum Vacation = 5 days
```

---

# 📊 Complexity Analysis

## Time Complexity

Reading the `M` obligations takes:

```text
O(M)
```

The sliding window scans all `N` days.

Although there is a `while` loop inside the `for` loop, both pointers only move forward. Therefore, each day is added to and removed from the window at most once.

The sliding window takes:

```text
O(N)
```

Overall:

```text
O(N + M)
```

This is efficient for large constraints such as:

```text
N <= 10⁶
M <= 2 × 10⁶
```

---

## Space Complexity

The obligation frequency array requires:

```text
O(N)
```

space.

Therefore:

```text
O(N)
```

---

# 🧩 Pattern Used

* Sliding Window
* Two Pointers
* Variable Size Window
* Frequency Array
* Greedy Window Expansion/Shrinking

### General Pattern

```text
Expand Right
      ↓
Add current element
      ↓
Is the window invalid?
      ↓
   YES → Move Left
      ↓
Until window becomes valid
      ↓
Calculate window size
      ↓
Update maximum
```

---

# 🎯 Pattern Recognition

This problem is a **Sliding Window** problem because it asks for:

```text
Longest
+
Consecutive
+
Range
+
With a constraint
```

Specifically:

```text
Longest consecutive range
whose number of obligations <= K
```

Whenever you see a problem involving:

* Longest subarray
* Shortest subarray
* Longest substring
* Consecutive elements
* At most `K` occurrences
* At most `K` bad elements
* At most `K` changes
* A condition that becomes invalid as the window grows

you should consider:

```text
Sliding Window / Two Pointers
```

---

# 🚀 Key Learning

> If you need to find the **longest consecutive range** satisfying a condition, and you can efficiently maintain that condition while expanding and shrinking the range, a **Sliding Window** approach is often the right solution.

For this problem:

```text
Window = Vacation Period

Window Value = Number of Obligations

Valid Window = Obligations <= K

Goal = Maximum Window Length
```

Therefore:

```text
Sliding Window
+
Two Pointers
=
Maximum Vacation Days
```

---

# 📚 Suitable For

* Infosys Coding Assessment
* Sliding Window Practice
* Two Pointer Problems
* Array Problems
* Competitive Programming
* Coding Interviews
* Pattern Recognition Practice
