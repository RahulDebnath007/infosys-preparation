# 2 🔢 Count Arrays – Dynamic Programming on Sequences

## 📌 Problem Statement

You are given two integers:

- **N** → Maximum value allowed in the array.
- **K** → Length of the array.

Your task is to count the number of arrays of length **K** such that:

1. Every element is between **1** and **N**.
2. Every adjacent pair satisfies:

```text
a[i+1] % a[i] == 0
```

In other words, every next element must be divisible by the previous element.

Return the answer **modulo 10000**.

---

# 💡 Approach

A brute-force solution would generate every possible array of length **K**.

The total number of possible arrays is:

```text
N^K
```

This quickly becomes infeasible for larger values of **N** and **K**.

### Key Observation

If the current number is:

```text
2
```

the next number can only be:

```text
2, 4, 6, 8, ...
```

Similarly,

```text
3 → 3, 6, 9, ...

4 → 4, 8, 12, ...
```

Each number can transition **only to its multiples**.

Instead of generating every possible array, we store previously computed answers using **Dynamic Programming**.

### DP State

```text
dp[length][last]
```

Meaning:

> Number of valid arrays of length **length** ending with **last**.

### Transition

For every valid ending number, extend the array to all of its multiples.

```python
for multiple in range(num, n + 1, num):
    dp[length + 1][multiple] += dp[length][num]
```

---

# 💻 Python Code

```python
MOD = 10000

def countArrays(n, k):

    # dp[length][number]
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    # Base case
    for num in range(1, n + 1):
        dp[1][num] = 1

    # Build DP
    for length in range(1, k):
        for num in range(1, n + 1):

            # Visit every multiple of num
            for multiple in range(num, n + 1, num):
                dp[length + 1][multiple] = (
                    dp[length + 1][multiple] + dp[length][num]
                ) % MOD

    # Sum all arrays of length k
    return sum(dp[k]) % MOD


# Driver Code
n = int(input())
k = int(input())

print(countArrays(n, k))
```

---

# 📝 Code Explanation (Step-by-Step)

## Step 1

```python
MOD = 10000
```

The answer can become very large.

Store every value modulo **10000**.

---

## Step 2

```python
def countArrays(n, k):
```

Create the function.

Parameters:

- `n` → Maximum number allowed.
- `k` → Required array length.

---

## Step 3

```python
dp = [[0] * (n + 1) for _ in range(k + 1)]
```

Create the DP table.

State:

```text
dp[length][last]
```

It stores the number of valid arrays of a given length ending with a particular number.

---

## Step 4

```python
for num in range(1, n + 1):
    dp[1][num] = 1
```

Initialize the base case.

Every number forms one valid array of length **1**.

Example:

```text
[1]
[2]
[3]
...
```

---

## Step 5

```python
for length in range(1, k):
```

Build arrays from smaller lengths to larger lengths.

---

## Step 6

```python
for num in range(1, n + 1):
```

Visit every possible ending number.

---

## Step 7

```python
for multiple in range(num, n + 1, num):
```

Visit every multiple of the current number.

Example:

If

```text
num = 2
```

The multiples are

```text
2
4
6
8
...
```

These are the only valid next elements.

---

## Step 8

```python
dp[length + 1][multiple]
```

Represents:

Number of arrays of length **length + 1** ending at **multiple**.

---

## Step 9

```python
dp[length][num]
```

Represents:

Number of arrays already built of length **length** ending at **num**.

---

## Step 10

```python
dp[length + 1][multiple] += dp[length][num]
```

Extend every existing valid array ending with **num** to **multiple**.

---

## Step 11

```python
% MOD
```

Take modulo **10000** after every update.

---

## Step 12

```python
return sum(dp[k]) % MOD
```

After building all arrays of length **k**, add every possible ending value.

---

## Step 13

```python
n = int(input())
k = int(input())
```

Read the input values.

---

## Step 14

```python
print(countArrays(n, k))
```

Call the function and print the final answer.

---