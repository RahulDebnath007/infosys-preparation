# 🔢 Four-Seven Sum

## 📌 Problem Overview

You are given a sequence of single-digit integers `nums`.

The sequence is guaranteed to contain at least one `4` and one `7`, and the **first occurrence of `4` appears before the first occurrence of `7`**.

The task is to perform three calculations:

1. Find the sum of all numbers **before the first `4`**.
2. Find the sum of all numbers **after the first `7`**.
3. Concatenate all numbers from the first `4` to the first `7`, **including both `4` and `7`**, to form a single integer.

Finally, add all three results together.

---

## 🧩 Problem Statement

Given:

```text
nums = [a₁, a₂, ..., aₙ]
```

Let:

* `i4` = index of the first occurrence of `4`
* `i7` = index of the first occurrence of `7`

Calculate:

```text
Sum before 4
+
Sum after 7
+
Concatenated number from 4 to 7
```

The final value is the required answer.

---

## 📥 Input Format

A single line containing space-separated integers.

```text
a₁ a₂ a₃ ... aₙ
```

### Constraints

```text
2 ≤ |nums| ≤ 16
0 ≤ nums[i] ≤ 9
```

Additional guarantees:

* At least one `4` exists.
* At least one `7` exists.
* The first `4` appears before the first `7`.

---

## 📤 Output Format

Print a single integer representing the final calculated result.

---

# 🧪 Sample Input

```text
3 1 6 4 2 3 7 2
```

## 🧪 Sample Output

```text
4249
```

---

# 🔍 Sample Explanation

Given:

```text
3 1 6 4 2 3 7 2
```

### Step 1 — Sum Before the First `4`

The numbers before `4` are:

```text
3 1 6
```

Their sum is:

```text
3 + 1 + 6 = 10
```

### Step 2 — Sum After the First `7`

The number after `7` is:

```text
2
```

So:

```text
sum_after = 2
```

Therefore:

```text
sum_before + sum_after
= 10 + 2
= 12
```

### Step 3 — Concatenate From `4` to `7`

The numbers from the first `4` through the first `7` are:

```text
4 2 3 7
```

Concatenating them produces:

```text
4237
```

### Step 4 — Final Result

```text
12 + 4237 = 4249
```

Therefore:

```text
Answer = 4249
```

---

# 💡 Approach

The solution can be broken into four simple steps.

## 1. Read the Input

The input is provided as space-separated integers.

```python
line = input().strip()
nums = list(map(int, line.split()))
```

For example:

```text
3 1 6 4 2 3 7 2
```

becomes:

```python
[3, 1, 6, 4, 2, 3, 7, 2]
```

---

## 2. Find the First `4` and First `7`

Python's `.index()` method returns the position of the **first occurrence** of a value.

```python
i4 = nums.index(4)
i7 = nums.index(7)
```

For:

```text
3 1 6 4 2 3 7 2
```

the indices are:

```text
Index:  0 1 2 3 4 5 6 7
Value:  3 1 6 4 2 3 7 2
                  ↑     ↑
                  4     7
```

Therefore:

```text
i4 = 3
i7 = 6
```

---

## 3. Calculate the Required Values

### Sum Before `4`

Use:

```python
sum(nums[:i4])
```

This selects:

```text
3 1 6
```

and gives:

```text
10
```

### Sum After `7`

Use:

```python
sum(nums[i7 + 1:])
```

This selects:

```text
2
```

and gives:

```text
2
```

### Concatenate `4` Through `7`

Use:

```python
"".join(str(x) for x in nums[i4:i7 + 1])
```

The slice:

```python
nums[i4:i7 + 1]
```

produces:

```text
[4, 2, 3, 7]
```

Converting each number to a string and joining them gives:

```text
"4237"
```

Finally:

```python
int("4237")
```

converts it into the integer:

```text
4237
```

---

# 🔄 Algorithm

1. Read the input and convert it into a list of integers.
2. Find the index of the first `4`.
3. Find the index of the first `7`.
4. Calculate the sum of elements before `4`.
5. Calculate the sum of elements after `7`.
6. Extract the elements from `4` to `7` inclusive.
7. Convert those elements to strings and concatenate them.
8. Convert the concatenated string into an integer.
9. Add all three values.
10. Print the result.

---

# 💻 Python 3 Solution

```python
line = input().strip()
nums = list(map(int, line.split()))

# Find the first occurrence of 4 and 7
i4 = nums.index(4)
i7 = nums.index(7)

# Sum of numbers before 4
sum_before = sum(nums[:i4])

# Sum of numbers after 7
sum_after = sum(nums[i7 + 1:])

# Concatenate numbers from 4 to 7 inclusive
concat_num = int(
    "".join(str(x) for x in nums[i4:i7 + 1])
)

# Final result
result = sum_before + sum_after + concat_num

print(result)
```

---

# 🧠 Dry Run

Consider:

```text
2 5 4 1 8 7 3
```

### Find Positions

```text
Index:  0 1 2 3 4 5 6
Value:  2 5 4 1 8 7 3
            ↑       ↑
            4       7
```

So:

```text
i4 = 2
i7 = 5
```

### Before `4`

```text
2 5
```

Sum:

```text
2 + 5 = 7
```

### After `7`

```text
3
```

Sum:

```text
3
```

### From `4` to `7`

```text
4 1 8 7
```

Concatenate:

```text
4187
```

### Final Calculation

```text
7 + 3 + 4187
= 4197
```

Output:

```text
4197
```

---

# ⚙️ Complexity Analysis

Let:

```text
N = number of elements in nums
```

### Time Complexity

Finding the first `4` and first `7` requires traversing the list:

```text
O(N)
```

The slicing, summing, and concatenation operations together also take at most:

```text
O(N)
```

Therefore:

```text
Time Complexity: O(N)
```

### Space Complexity

The solution uses slices and a temporary string for concatenation.

Therefore:

```text
Space Complexity: O(N)
```

Given the constraint:

```text
N ≤ 16
```

this approach is easily fast enough.

---

# 📌 Edge Cases

## 1. `4` Appears Immediately

Input:

```text
4 2 3 7 5
```

There are no elements before `4`.

So:

```text
sum_before = 0
```

---

## 2. `7` Is the Last Element

Input:

```text
1 2 4 5 7
```

There are no elements after `7`.

So:

```text
sum_after = 0
```

---

## 3. `4` and `7` Are Adjacent

Input:

```text
1 2 4 7 8
```

The concatenated number is:

```text
47
```

The elements between `4` and `7` do not have to exist.

---

## 4. Multiple `4`s or `7`s

Only the **first occurrence** of each matters.

For example:

```text
1 4 2 4 3 7 7 5
```

The first `4` is used, and the first `7` is used.

---

# 🔑 Key Concepts

This problem demonstrates:

* List indexing
* `list.index()`
* List slicing
* `sum()`
* String conversion
* String concatenation
* `join()`
* Converting strings to integers
* Combining multiple operations into a final calculation

---

# 🎯 Key Takeaway

The important part of this problem is correctly separating the input into three regions:

```text
Before 4 | From 4 to 7 | After 7
─────────┼─────────────┼────────
  SUM    | CONCATENATE  |  SUM
```

For:

```text
3 1 6 | 4 2 3 7 | 2
```

we get:

```text
10 + 4237 + 2
```

which gives:

```text
4249
```

The core Python operations are:

```python
nums.index(4)
nums.index(7)
nums[:i4]
nums[i7 + 1:]
nums[i4:i7 + 1]
```

Together, they provide a simple `O(N)` solution.
