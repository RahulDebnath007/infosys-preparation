# 3🧩 Longest Increasing Subsequence with Bitwise Condition (Dynamic Programming)

## 📌 Problem Statement

You are given an array `A` of `N` integers.

Your task is to find the **Longest Increasing Subsequence (LIS)** such that for every adjacent pair of elements in the chosen subsequence, the following condition is satisfied:

```text
(A[i] & A[j]) * 2 < (A[i] | A[j])
```

where:

- `&` = Bitwise AND
- `|` = Bitwise OR

A valid pair must satisfy:

1. `A[i] < A[j]` (Increasing Order)
2. `(A[i] & A[j]) * 2 < (A[i] | A[j])`

Return the length of the longest such subsequence.

---

## 📝 Example

### Input

```text
5
15
6
5
12
1
```

### Output

```text
2
```

### Explanation

One possible valid subsequence is:

```text
5 12
```

Since:

- `5 < 12`
- `(5 & 12) = 4`
- `(5 | 12) = 13`
- `4 × 2 = 8`
- `8 < 13` ✅

Therefore, the answer is **2**.

---

# 💡 Approach

This problem is a **variation of the Longest Increasing Subsequence (LIS)**.

For every element, we try to extend a valid subsequence ending at a previous element.

### Step 1

Create a DP array.

```text
dp[i]
```

represents:

> Length of the longest valid subsequence ending at index `i`.

Initially,

```text
dp[i] = 1
```

because every element alone forms a subsequence of length `1`.

---

### Step 2

For every element `i`, check every previous element `j`.

If both conditions are satisfied:

```text
A[j] < A[i]
```

and

```text
(A[j] & A[i]) * 2 < (A[j] | A[i])
```

then update

```text
dp[i] = max(dp[i], dp[j] + 1)
```

---

### Step 3

The answer is

```text
max(dp)
```

because the longest subsequence can end at any index.

---

## ✅ Time Complexity

```text
O(N²)
```

Every pair of elements is checked once.

## ✅ Space Complexity

```text
O(N)
```

Only one DP array is used.

---

# 💻 Python Code

```python
def longest_valid_subsequence(n, arr):
    # dp[i] = Length of longest valid subsequence ending at index i
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            # Check increasing condition and bitwise condition
            if arr[j] < arr[i] and ((arr[j] & arr[i]) * 2 < (arr[j] | arr[i])):
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# Input
n = int(input())
arr = [int(input()) for _ in range(n)]

# Output
print(longest_valid_subsequence(n, arr))
```

---

# 🔍 Step-by-Step Code Explanation

## Step 1: Function Definition

```python
def longest_valid_subsequence(n, arr):
```

Creates a function that takes:

- `n` → Number of elements
- `arr` → Input array

---

## Step 2: Initialize DP

```python
dp = [1] * n
```

Initially every element itself forms a subsequence.

Example:

```text
Array: 15 6 5 12 1

DP:    1 1 1 1 1
```

---

## Step 3: Traverse Every Element

```python
for i in range(n):
```

Treat `arr[i]` as the last element of the subsequence.

---

## Step 4: Check All Previous Elements

```python
for j in range(i):
```

Try extending the subsequence ending at every previous index.

---

## Step 5: Verify the Conditions

```python
if arr[j] < arr[i] and ((arr[j] & arr[i]) * 2 < (arr[j] | arr[i])):
```

Two conditions are checked:

1. Increasing order
2. Bitwise condition

Only if both are true can `arr[i]` follow `arr[j]`.

---

## Step 6: Update DP

```python
dp[i] = max(dp[i], dp[j] + 1)
```

Extend the previous subsequence and keep the maximum length.

---

## Step 7: Return the Answer

```python
return max(dp)
```

The longest valid subsequence may end at any position, so return the maximum value in the DP array.

---

# 🧪 Dry Run

For the input:

```text
15
6
5
12
1
```

Initially:

```text
DP = [1, 1, 1, 1, 1]
```

Processing `12`:

- `15 → 12` ❌ (Not increasing)
- `6 → 12` ✅
- `5 → 12` ✅

Updated DP:

```text
DP = [1, 1, 1, 2, 1]
```

Maximum value:

```text
2
```

Hence the answer is:

```text
2
```

---

# 🎯 Pattern Recognition

Whenever a problem asks for:

- Longest subsequence
- Elements remain in original order
- Maximum length
- An additional condition between consecutive selected elements

it is often an **LIS Dynamic Programming variation**.

General template:

```python
dp = [1] * n

for i in range(n):
    for j in range(i):
        if can_extend(arr[j], arr[i]):
            dp[i] = max(dp[i], dp[j] + 1)

answer = max(dp)
```

Only the `can_extend()` condition changes from one problem to another.
