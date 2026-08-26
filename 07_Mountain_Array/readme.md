# 10 🏔️ Mountain Array – Minimum Elements to Change

[![Repository](https://img.shields.io/badge/Repository-infosys--preparation-blue?logo=github)](https://github.com/RahulDebnath007/infosys-preparation)

**Pattern:** Mathematical Transformation + Frequency Counting

---

## 📌 Problem Statement

You are given an array of size `N`.

You need to change the array into a **mountain**.

A valid mountain has the following structure:

* The two ends of the array must contain equal values.
* Moving from either end toward the middle, every next element must be exactly `1` greater than the previous element.
* The array increases toward the middle and then decreases symmetrically.

### Valid Mountain Examples

```text
[1, 2, 3, 2, 1]
```

```text
[6, 7, 8, 8, 7, 6]
```

### Invalid Mountain Examples

```text
[1, 2, 4, 2, 1]
```

This is invalid because the difference between `2` and `4` is `2`, not `1`.

```text
[1, 2, 3, 1]
```

This is invalid because the array is not symmetric.

The task is to find the **minimum number of elements that must be changed** to transform the array into a valid mountain.

Elements can be changed to any integer, including negative values and zero.

---

# 💡 Approach

A brute-force solution would try different possible mountain values and compare the entire array with every possible mountain.

This is inefficient for:

```text
N <= 10^5
```

### Key Observation

Once the starting/base value of the mountain is known, the entire mountain is completely determined.

For example, for:

```text
N = 5
```

if the base value is `x`, the mountain must be:

```text
[x, x+1, x+2, x+1, x]
```

For:

```text
N = 6
```

the mountain is:

```text
[x, x+1, x+2, x+2, x+1, x]
```

Therefore, there is only **one important parameter**:

```text
x = Base Value
```

Instead of generating every possible mountain, we calculate which base value each original element requires.

This leads to:

```text
Mathematical Transformation
+
Frequency Counting
```

---

# 🧠 Mountain Formula

For position `i`, the height of a valid mountain is:

```text
mountain[i] = base + min(i, N - 1 - i)
```

where:

* `base` → value at either end of the mountain
* `i` → current index
* `N - 1 - i` → distance from the right end

Therefore:

```text
mountain[i] = base + min(i, N - 1 - i)
```

### Example

Suppose:

```text
N = 5
base = 1
```

Then:

```text
i = 0 → 1 + 0 = 1
i = 1 → 1 + 1 = 2
i = 2 → 1 + 2 = 3
i = 3 → 1 + 1 = 2
i = 4 → 1 + 0 = 1
```

So the mountain is:

```text
[1, 2, 3, 2, 1]
```

---

# 🔑 Key Observation

Suppose the original value at position `i` is:

```text
array[i]
```

For this value to remain unchanged, it must satisfy:

```text
array[i] = base + min(i, N - 1 - i)
```

Rearranging:

```text
base = array[i] - min(i, N - 1 - i)
```

Therefore, for every element, calculate:

```text
base[i] = array[i] - min(i, N - 1 - i)
```

If several elements produce the same base value, those elements can all remain unchanged in the same final mountain.

Therefore:

> Find the most frequent `base` value.

If `max_frequency` elements can remain unchanged, then:

```text
minimum_changes = N - max_frequency
```

---

# 🔍 Understanding the Transformation

Suppose:

```text
N = 5
Array = [1, 2, 3, 4, 5]
```

Calculate:

```text
min(i, N - 1 - i)
```

for every position:

```text
i:          0  1  2  3  4
distance:   0  1  2  1  0
```

Now calculate:

```text
base = array[i] - distance
```

Therefore:

```text
i = 0 → 1 - 0 = 1
i = 1 → 2 - 1 = 1
i = 2 → 3 - 2 = 1
i = 3 → 4 - 1 = 3
i = 4 → 5 - 0 = 5
```

The transformed values are:

```text
[1, 1, 1, 3, 5]
```

The value `1` occurs three times.

Therefore, we can preserve three elements by choosing:

```text
base = 1
```

The resulting mountain is:

```text
[1, 2, 3, 2, 1]
```

We need to change the remaining two elements.

Therefore:

```text
Answer = 5 - 3 = 2
```

---

# 📝 Algorithm

1. Read `N` and the array.
2. Create a frequency dictionary.
3. For every index `i`:

   * Calculate the distance from the nearest end:

     ```text
     min(i, N - 1 - i)
     ```
   * Calculate the base value:

     ```text
     array[i] - min(i, N - 1 - i)
     ```
   * Store its frequency.
4. Find the maximum frequency.
5. The elements corresponding to this frequency can remain unchanged.
6. Change every other element.
7. Return:

   ```text
   N - maximum_frequency
   ```

---

# 📝 Code Explanation

## Step 1 — Read `N`

```python
N = int(input())
```

Read the number of elements in the array.

For example:

```text
N = 5
```

---

## Step 2 — Read the Array

```python
arr = []

for _ in range(N):
    arr.append(int(input()))
```

Read all `N` array elements.

For example:

```text
1
2
3
4
5
```

becomes:

```text
[1, 2, 3, 4, 5]
```

---

## Step 3 — Create the Frequency Dictionary

```python
frequency = {}
```

Create a dictionary to count how many times each possible base value occurs.

For example, if:

```text
base = 1
```

appears three times:

```text
{
    1: 3
}
```

---

## Step 4 — Process Every Position

```python
for i in range(N):
```

Process every element of the array.

The index goes from:

```text
0 → N - 1
```

---

## Step 5 — Calculate the Mountain Level

```python
level = min(i, N - 1 - i)
```

Calculate the distance of the current position from the nearest end.

For:

```text
N = 5
```

the values are:

```text
i:          0 1 2 3 4
level:      0 1 2 1 0
```

This represents how high the mountain should be at each position relative to its base.

---

## Step 6 — Calculate the Required Base

```python
base = arr[i] - level
```

From:

```text
arr[i] = base + level
```

we get:

```text
base = arr[i] - level
```

Example:

```text
arr[i] = 3
level = 2
```

Therefore:

```text
base = 3 - 2
     = 1
```

---

## Step 7 — Count the Base Frequency

```python
frequency[base] = frequency.get(base, 0) + 1
```

Increase the frequency of this base value.

If the dictionary does not contain `base`:

```python
frequency.get(base, 0)
```

returns `0`.

Then we add `1`.

Example:

```text
base = 1
```

First occurrence:

```text
frequency[1] = 1
```

Second occurrence:

```text
frequency[1] = 2
```

Third occurrence:

```text
frequency[1] = 3
```

---

## Step 8 — Find the Maximum Frequency

```python
max_kept = max(frequency.values())
```

Find the largest frequency.

This tells us the maximum number of elements that can remain unchanged for one particular mountain base.

For:

```text
frequency = {
    1: 3,
    3: 1,
    5: 1
}
```

we get:

```text
max_kept = 3
```

---

## Step 9 — Calculate the Minimum Changes

```python
answer = N - max_kept
```

If `N` elements exist and `max_kept` can remain unchanged, then the remaining elements must be modified.

Therefore:

```text
changes = N - max_kept
```

For:

```text
N = 5
max_kept = 3
```

we get:

```text
answer = 5 - 3
       = 2
```

---

## Step 10 — Print the Answer

```python
print(answer)
```

Print the minimum number of elements that need to be changed.

---

# 💻 Complete Code

```python
N = int(input())

arr = []

for _ in range(N):
    arr.append(int(input()))

frequency = {}

for i in range(N):

    # Distance from the nearest end
    level = min(i, N - 1 - i)

    # Base value required for arr[i]
    base = arr[i] - level

    frequency[base] = frequency.get(base, 0) + 1

# Maximum number of elements that can remain unchanged
max_kept = max(frequency.values())

# Remaining elements need to be changed
answer = N - max_kept

print(answer)
```

---

# 🧪 Dry Run

## Sample Input 1

```text
5
1
2
3
4
5
```

So:

```text
N = 5

Array = [1, 2, 3, 4, 5]
```

Calculate the distance from the nearest end:

```text
Index:       0  1  2  3  4
Distance:    0  1  2  1  0
```

Calculate the base:

```text
1 - 0 = 1
2 - 1 = 1
3 - 2 = 1
4 - 1 = 3
5 - 0 = 5
```

Therefore:

```text
Base Values = [1, 1, 1, 3, 5]
```

Frequency:

```text
1 → 3
3 → 1
5 → 1
```

Maximum frequency:

```text
3
```

Therefore:

```text
Answer = 5 - 3
       = 2
```

Final mountain:

```text
[1, 2, 3, 2, 1]
```

---

# 🧪 Dry Run — Sample 2

Input:

```text
9
1
1
1
2
3
2
1
1
1
```

Therefore:

```text
Array = [1, 1, 1, 2, 3, 2, 1, 1, 1]
```

Distances:

```text
Index:       0 1 2 3 4 5 6 7 8
Distance:    0 1 2 3 4 3 2 1 0
```

Calculate the base values:

```text
1 - 0 = 1
1 - 1 = 0
1 - 2 = -1
2 - 3 = -1
3 - 4 = -1
2 - 3 = -1
1 - 2 = -1
1 - 1 = 0
1 - 0 = 1
```

Therefore:

```text
Base Values:

[1, 0, -1, -1, -1, -1, -1, 0, 1]
```

Frequency:

```text
1  → 2
0  → 2
-1 → 5
```

The maximum frequency is:

```text
5
```

Therefore:

```text
Answer = 9 - 5
       = 4
```

The corresponding mountain is:

```text
[-1, 0, 1, 2, 3, 2, 1, 0, -1]
```

Five elements remain unchanged, so four elements need to be changed.

---

# 🔍 Why the Frequency Approach Works

Every valid mountain can be written as:

```text
mountain[i] = base + min(i, N - 1 - i)
```

For an original element to remain unchanged:

```text
array[i] = base + min(i, N - 1 - i)
```

Therefore:

```text
base = array[i] - min(i, N - 1 - i)
```

Every element effectively **votes** for the base value that would allow it to remain unchanged.

If multiple elements vote for the same base, all of those elements can remain unchanged simultaneously.

Therefore:

```text
Maximum frequency
        ↓
Maximum elements kept
        ↓
N - maximum frequency
        ↓
Minimum elements changed
```

This avoids trying every possible mountain.

---

# 📊 Complexity Analysis

## Time Complexity

We process every array element exactly once.

For each element, we perform constant-time operations:

```text
min()
dictionary lookup
dictionary update
```

Therefore:

```text
O(N)
```

---

## Space Complexity

The frequency dictionary can contain up to `N` different base values.

Therefore:

```text
O(N)
```

---

# 🧩 Pattern Used

* Mathematical Transformation
* Frequency Counting
* Hash Map / Dictionary
* Pattern Recognition

---

# 🎯 Pattern Recognition

This problem has the structure:

```text
Change minimum elements
        +
Make array follow a mathematical pattern
```

Instead of trying to construct every possible target array, ask:

> **What parameter completely defines the target pattern?**

For this problem, the entire mountain is determined by:

```text
Base Value
```

Then transform every element into the base value it requires:

```text
base = array[i] - min(i, N - 1 - i)
```

Finally, count frequencies.

The general pattern is:

```text
Original Element
       ↓
Convert to Required Pattern Parameter
       ↓
Count Frequencies
       ↓
Keep Maximum Matching Elements
       ↓
Change the Rest
```

---

# 🚀 Key Learning

> When a target array follows a fixed mathematical pattern controlled by one or a small number of parameters, transform each original element into the parameter value it requires and use **frequency counting** to maximize the number of unchanged elements.

For this problem:

```text
Mountain Structure
       ↓
base + min(i, N - 1 - i)
       ↓
base = array[i] - min(i, N - 1 - i)
       ↓
Frequency Counting
       ↓
Maximum Elements Kept
       ↓
Minimum Changes
```

The core formula is:

```text
base = array[i] - min(i, N - 1 - i)
```

and the final answer is:

```text
N - maximum_frequency
```

---

# 📚 Suitable For

* Infosys Coding Assessment
* Array Problems
* Hash Map / Dictionary Practice
* Frequency Counting
* Mathematical Observation Problems
* Pattern Recognition Practice
* Competitive Programming
* Coding Interviews
