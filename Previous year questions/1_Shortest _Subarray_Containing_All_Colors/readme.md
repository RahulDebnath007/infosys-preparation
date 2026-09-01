# 🎨 Question 1 — Shortest Subarray Containing All Colors

## 📌 Problem Overview

Given an array `A` of `N` integers and an integer `C`, find the **minimum length of a contiguous subarray** that contains every color from:

```text
1, 2, 3, ..., C
```

at least once.

If it is impossible to find such a subarray, return:

```text
-1
```

---

# 🧩 Problem Statement

You are given:

```text
N = number of elements
C = number of required colors
A = array
```

The task is to find the shortest **contiguous** portion of `A` that contains all colors from `1` to `C`.

For example:

```text
A = [1, 2, 3, 2, 1]
C = 3
```

The subarray:

```text
[1, 2, 3]
```

contains:

```text
1
2
3
```

Therefore:

```text
Answer = 3
```

---

# 📥 Input Format

The input contains:

### First line

```text
N
```

Number of elements in the array.

### Second line

```text
C
```

Number of required colors.

### Third line

```text
A[0] A[1] A[2] ... A[N-1]
```

The elements of the array.

---

# 📤 Output Format

Print the length of the shortest contiguous subarray containing all colors from `1` through `C`.

If no such subarray exists:

```text
-1
```

---

# 📋 Example

### Input

```text
5
3
1 2 3 2 1
```

### Output

```text
3
```

### Explanation

The shortest valid subarray is:

```text
[1, 2, 3]
```

Its length is:

```text
3
```

It contains every required color:

```text
1 ✓
2 ✓
3 ✓
```

---

# 🧠 Intuition

This is a classic **Sliding Window** problem.

The important word is:

> **Contiguous**

We need a continuous section of the array, so we can use two pointers:

```text
left
right
```

Think of them as defining a window:

```text
[left ........ right]
```

We expand the window using `right` until it contains every required color.

Once the window becomes valid:

```text
distinct == C
```

we try to shrink it from the left.

This gives us the smallest possible window ending at the current `right`.

---

# 🔥 Why Sliding Window?

A brute-force solution could examine every possible subarray.

There are approximately:

```text
N × N
```

possible subarrays.

That leads to:

```text
O(N²)
```

which is too slow for large `N`.

Instead, the sliding window allows us to move each pointer only forward.

```text
left  → → → →
right → → → →
```

Neither pointer moves backward.

Therefore, the entire array is processed in:

```text
O(N)
```

time.

---

# 🧩 Pattern Used

## Sliding Window + Frequency Array

The main components are:

```text
Sliding Window
      +
Frequency Array
      +
Two Pointers
```

We maintain:

```text
left
right
freq
distinct
ans
```

---

# 📦 Data Structures

## 1. Frequency Array

```python
freq = [0] * (c + 1)
```

`freq[x]` stores how many times color `x` occurs inside the current window.

For example:

```text
Window = [1, 2, 2, 3]
```

Then:

```text
freq[1] = 1
freq[2] = 2
freq[3] = 1
```

---

## 2. Distinct Counter

We maintain:

```python
distinct
```

which represents the number of different required colors currently present in the window.

For example:

```text
Window = [1, 2, 2, 3]
```

contains:

```text
1
2
3
```

So:

```text
distinct = 3
```

Duplicates do not increase `distinct`.

---

# 🪟 Sliding Window

Initially:

```text
left = 0
right = 0
```

The window starts empty.

We move `right` through the array.

Suppose:

```text
A = [1, 2, 3, 2, 1]
```

The window grows:

```text
[1]
```

then:

```text
[1, 2]
```

then:

```text
[1, 2, 3]
```

At this point all three colors are present.

Therefore:

```text
distinct == C
```

The window is valid.

---

# 🔽 Shrinking the Window

Once the window contains all colors, we try to remove elements from the left.

For:

```text
[1, 2, 3]
```

remove `1`:

```text
[2, 3]
```

Now color `1` is missing.

Therefore the window is no longer valid.

So we stop shrinking.

The smallest valid window found is:

```text
[1, 2, 3]
```

with length:

```text
3
```

---

# 🔄 Core Algorithm

The algorithm is:

```text
1. Create a frequency array.
2. Set left = 0.
3. Set distinct = 0.
4. Move right from 0 to N-1.
5. Add A[right] to the window.
6. If its frequency was 0, increase distinct.
7. When distinct == C:
      a. Update the minimum answer.
      b. Remove A[left].
      c. If its frequency becomes 0,
         decrease distinct.
      d. Move left forward.
8. Print the answer.
```

---

# 💻 Python 3 Solution

```python
def solve():
    n = int(input())
    c = int(input())
    arr = list(map(int, input().split()))

    # Frequency of each color inside the window
    freq = [0] * (c + 1)

    left = 0
    distinct = 0
    ans = float('inf')

    for right in range(n):

        x = arr[right]

        # First occurrence of this color
        # inside the current window
        if freq[x] == 0:
            distinct += 1

        freq[x] += 1

        # Window contains all required colors
        while distinct == c:

            # Update minimum window length
            ans = min(ans, right - left + 1)

            # Remove leftmost element
            freq[arr[left]] -= 1

            # This color is no longer present
            if freq[arr[left]] == 0:
                distinct -= 1

            left += 1

    print(-1 if ans == float('inf') else ans)


solve()
```

---

# 🔍 Code Explanation

## Step 1 — Read Input

```python
n = int(input())
c = int(input())
arr = list(map(int, input().split()))
```

We read:

```text
N
C
Array
```

---

# Step 2 — Create Frequency Array

```python
freq = [0] * (c + 1)
```

We use indexes corresponding to colors.

For example, if:

```text
C = 3
```

then:

```text
freq = [0, 0, 0, 0]
```

Index `0` is unused.

Indexes:

```text
freq[1]
freq[2]
freq[3]
```

represent colors `1`, `2`, and `3`.

---

# Step 3 — Initialize Variables

```python
left = 0
distinct = 0
ans = float('inf')
```

### `left`

Left boundary of the current window.

### `distinct`

Number of required colors currently inside the window.

### `ans`

Smallest valid window length found so far.

Initially:

```text
ans = infinity
```

because we haven't found a valid window yet.

---

# Step 4 — Expand the Window

```python
for right in range(n):
```

The `right` pointer moves through every array element.

For example:

```text
right = 0
right = 1
right = 2
...
```

---

# Step 5 — Add the New Color

```python
x = arr[right]
```

Suppose:

```text
x = 2
```

We check:

```python
if freq[x] == 0:
    distinct += 1
```

If this is the first `2` inside the current window, we increase the number of distinct colors.

Then:

```python
freq[x] += 1
```

records its frequency.

---

# Step 6 — Check Whether Window Is Valid

```python
while distinct == c:
```

If:

```text
distinct == C
```

then every required color:

```text
1, 2, ..., C
```

exists inside the current window.

Therefore, we have a valid candidate.

---

# Step 7 — Update Answer

```python
ans = min(ans, right - left + 1)
```

The current window length is:

```text
right - left + 1
```

We compare it with the best answer found so far.

---

# Step 8 — Shrink the Window

After finding a valid window, we want to make it smaller.

So we remove:

```python
arr[left]
```

from the window:

```python
freq[arr[left]] -= 1
```

If its frequency becomes zero:

```python
if freq[arr[left]] == 0:
    distinct -= 1
```

that means the color has completely disappeared from the window.

Then:

```python
left += 1
```

moves the window forward.

---

# 🔬 Complete Dry Run

Consider:

```text
A = [1, 2, 3, 2, 1]
C = 3
```

Initially:

```text
left = 0
distinct = 0
```

---

## `right = 0`

Element:

```text
1
```

Window:

```text
[1]
```

Distinct colors:

```text
1
```

Not enough.

---

## `right = 1`

Element:

```text
2
```

Window:

```text
[1, 2]
```

Distinct:

```text
2
```

Still missing color `3`.

---

## `right = 2`

Element:

```text
3
```

Window:

```text
[1, 2, 3]
```

Distinct:

```text
3
```

Since:

```text
distinct == C
```

the window is valid.

Length:

```text
2 - 0 + 1 = 3
```

So:

```text
ans = 3
```

---

## Try to Shrink

Remove:

```text
A[left] = 1
```

Window becomes:

```text
[2, 3]
```

Color `1` is gone.

Therefore:

```text
distinct = 2
```

Stop shrinking.

---

## `right = 3`

Add:

```text
2
```

Window:

```text
[2, 3, 2]
```

Distinct colors:

```text
2
3
```

Only two distinct colors.

Not valid.

---

## `right = 4`

Add:

```text
1
```

Window:

```text
[2, 3, 2, 1]
```

Now:

```text
distinct = 3
```

Valid.

Length:

```text
4 - 1 + 1 = 4
```

But:

```text
ans = min(3, 4)
```

Therefore:

```text
ans = 3
```

Final answer:

```text
3
```

---

# 📊 Dry Run Table

For:

```text
A = [1,2,3,2,1]
C = 3
```

| Right | Window      | Distinct | Valid? | Best |
| ----: | ----------- | -------: | ------ | ---: |
|     0 | `[1]`       |        1 | ❌      |    ∞ |
|     1 | `[1,2]`     |        2 | ❌      |    ∞ |
|     2 | `[1,2,3]`   |        3 | ✅      |    3 |
|     2 | `[2,3]`     |        2 | ❌      |    3 |
|     3 | `[2,3,2]`   |        2 | ❌      |    3 |
|     4 | `[2,3,2,1]` |        3 | ✅      |    3 |
|     4 | `[3,2,1]`   |        3 | ✅      |    3 |

The shortest valid window is:

```text
[1,2,3]
```

or:

```text
[3,2,1]
```

Both have length:

```text
3
```

---

# 🚨 Why Do We Need `freq`?

We cannot simply remove a color whenever its element leaves the window.

Consider:

```text
Window = [1, 2, 2, 3]
```

For color `2`:

```text
freq[2] = 2
```

If we remove one `2`:

```text
Window = [1, 2, 3]
```

color `2` is still present.

Therefore:

```text
distinct
```

should **not** decrease.

Only when:

```text
freq[2] == 0
```

should we decrease `distinct`.

This is exactly why the frequency array is necessary.

---

# 🚨 Why Not Just Use a Set?

A set can tell us whether a color exists:

```python
set(window)
```

but when we move `left`, we need to know whether there are **other copies** of the same color still inside the window.

For example:

```text
[1, 2, 2, 3]
```

Removing one `2` should not remove `2` from the set.

A frequency map/array handles this correctly:

```text
freq[2] = 2
```

then:

```text
freq[2] = 1
```

The color is still present.

---

# ⚡ Why Is the Algorithm O(N)?

At first glance, there is a nested loop:

```python
for right in range(n):
    while distinct == c:
```

This may look like:

```text
O(N²)
```

but it isn't.

The important observation is:

> `left` only moves forward.

For example:

```text
left:
0 → 1 → 2 → 3 → ...
```

It never moves backward.

Similarly:

```text
right:
0 → 1 → 2 → 3 → ...
```

Therefore, across the entire algorithm:

```text
right moves at most N times
left moves at most N times
```

So the total number of operations is proportional to:

```text
2N
```

which simplifies to:

```text
O(N)
```

---

# ⚙️ Complexity Analysis

Let:

```text
N = number of elements
C = number of colors
```

### Time Complexity

```text
O(N)
```

Every element is:

* Added to the window at most once.
* Removed from the window at most once.

Therefore:

```text
Time = O(N)
```

### Space Complexity

The frequency array contains:

```text
C + 1
```

elements.

Therefore:

```text
Space = O(C)
```

Final:

```text
Time Complexity:  O(N)
Space Complexity: O(C)
```

---

# ❌ Brute Force Approach

A naive approach would be:

```text
Start from every index
    ↓
Expand to every possible ending index
    ↓
Check whether all colors exist
```

There are:

```text
O(N²)
```

possible subarrays.

If checking the colors also takes time, the solution can become even slower.

For large `N`, this is unnecessary.

The sliding window avoids repeatedly processing the same elements.

---

# 🧠 Pattern Recognition

Whenever you see:

* "Shortest subarray"
* "Longest subarray"
* "Minimum window"
* "Maximum window"
* "Contains all required elements"
* "Contains at least K distinct elements"
* "Find a contiguous segment satisfying a condition"

you should immediately consider:

```text
Sliding Window
```

If duplicates matter, combine it with:

```text
HashMap / Frequency Array
```

---

# 🎯 General Sliding Window Template

A useful template to remember is:

```python
left = 0

for right in range(n):

    # Add arr[right]
    # Update frequency/state

    while window_is_valid:

        # Update answer

        # Remove arr[left]
        # Update frequency/state

        left += 1
```

For this problem:

```python
while distinct == c:
```

is the condition that tells us the window is valid.

---

# 🔑 Key Takeaways

### 1. Contiguous → Think Sliding Window

The answer must be a continuous portion of the array.

---

### 2. Two Pointers

Use:

```text
left
right
```

to represent the current window.

---

### 3. Frequency Tracking

Use:

```python
freq[x]
```

to count how many times each color appears inside the window.

---

### 4. Track Distinct Colors

```python
distinct
```

tells us how many required colors are currently present.

---

### 5. Expand Until Valid

Move `right` until:

```text
distinct == C
```

---

### 6. Shrink While Valid

Once all colors are present, move `left` forward to minimize the window.

---

### 7. Update Before Shrinking

Always record:

```python
ans = min(ans, right - left + 1)
```

before removing the leftmost element.

---

### 8. Each Pointer Moves Forward

This is why the algorithm is:

```text
O(N)
```

rather than:

```text
O(N²)
```

---

# 🏆 Final Solution

```python
def solve():
    n = int(input())
    c = int(input())
    arr = list(map(int, input().split()))

    freq = [0] * (c + 1)

    left = 0
    distinct = 0
    ans = float('inf')

    for right in range(n):

        x = arr[right]

        if freq[x] == 0:
            distinct += 1

        freq[x] += 1

        while distinct == c:

            ans = min(ans, right - left + 1)

            freq[arr[left]] -= 1

            if freq[arr[left]] == 0:
                distinct -= 1

            left += 1

    print(-1 if ans == float('inf') else ans)


solve()
```

---

# 🚀 Final Mental Model

Remember the problem like this:

```text
              ARRAY
                ↓
        Create a Window
        [left ... right]
                ↓
       Count each color
                ↓
       Have all C colors?
          ↙           ↘
        NO             YES
        ↓               ↓
   Move RIGHT      Save answer
                        ↓
                   Move LEFT
                        ↓
              Still all colors?
                  ↙       ↘
                YES        NO
                 ↓          ↓
             Shrink       Expand
```

The core pattern is:

```text
Shortest Contiguous Subarray
            ↓
      Sliding Window
            +
    Frequency Tracking
            ↓
      Expand → Valid
            ↓
       Shrink → Minimize
```

**Remember this one sentence for the exam:**

> **Expand the right pointer until all required colors are present, then shrink the left pointer while the window remains valid to find the minimum-length window.**
