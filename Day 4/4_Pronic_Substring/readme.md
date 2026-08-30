# 🔢 Pronic Substrings

## 📌 Problem Overview

Given a string `S` consisting only of digits, find all **unique numeric substrings** that represent **pronic numbers**.

A number is called a **pronic number** if it can be expressed as the product of two consecutive non-negative integers:

```text
k × (k + 1)
```

### Example

```text
30 = 5 × 6
```

Since `5` and `6` are consecutive integers, `30` is a pronic number.

The valid pronic numbers found in the string must be:

1. Unique
2. Sorted in ascending order
3. Printed in list format

If no pronic number is found, print:

```text
[]
```

---

# 🧩 Problem Statement

Given a digit string `S`, consider **every possible substring** of `S`.

Convert each substring into its numeric value and determine whether that value is pronic.

If it is pronic, store it.

Finally:

```text
Remove duplicates
      ↓
Sort ascending
      ↓
Print the result
```

---

## 📥 Input Format

The input contains a single line consisting only of digits.

```text
S
```

### Constraints

```text
1 ≤ |S| ≤ 18
0 ≤ S[i] ≤ 9
```

---

## 📤 Output Format

Print a list containing all unique pronic numbers found in the string, sorted in ascending order.

The output must use the following format:

```text
[2, 6, 12]
```

If no pronic number is found:

```text
[]
```

---

# 🧪 Sample Input

```text
2612
```

## 🧪 Sample Output

```text
[2, 6, 12]
```

---

# 🔍 Sample Explanation

Given:

```text
S = "2612"
```

All unique numeric substrings are:

```text
2
6
1
2
26
61
12
261
612
2612
```

Now check which of these are pronic.

### `2`

```text
2 = 1 × 2
```

So `2` is pronic.

### `6`

```text
6 = 2 × 3
```

So `6` is pronic.

### `12`

```text
12 = 3 × 4
```

So `12` is pronic.

The remaining values are not pronic.

Therefore:

```text
[2, 6, 12]
```

---

# 💡 Approach

The solution consists of three main steps:

1. Generate every substring.
2. Check whether the substring's numeric value is pronic.
3. Store unique values and sort them.

---

# 1️⃣ Generate All Substrings

For a string of length `N`, we can generate every substring using two nested loops.

The outer loop chooses the starting position:

```python
for i in range(n):
```

The inner loop extends the substring:

```python
for j in range(i, n):
```

Instead of repeatedly converting substrings such as:

```python
int(s[i:j+1])
```

we build the number incrementally.

For example:

```text
S = "2612"
```

Starting at index `0`:

```text
2
26
261
2612
```

The numeric value can be updated using:

```python
num = num * 10 + int(s[j])
```

For example:

```text
2
2 × 10 + 6 = 26
26 × 10 + 1 = 261
261 × 10 + 2 = 2612
```

This avoids repeatedly converting strings to integers.

---

# 2️⃣ Check Whether a Number Is Pronic

A number `x` is pronic if:

```text
x = k × (k + 1)
```

for some integer `k`.

For example:

```text
12 = 3 × 4
```

Therefore, `12` is pronic.

---

## 🔍 Efficient Pronic Check

We can use the square root of `x` to find the possible value of `k`.

If:

```text
k × (k + 1) = x
```

then `k` is close to:

```text
√x
```

So we calculate:

```python
k = math.isqrt(x)
```

and check:

```python
k * (k + 1) == x
```

Using `math.isqrt()` is preferable to floating-point `math.sqrt()` because it directly gives the exact integer square root.

The implementation can simply be:

```python
def is_pronic(num):
    if num < 0:
        return False

    k = math.isqrt(num)
    return k * (k + 1) == num
```

---

# 3️⃣ Remove Duplicates

Different substrings can produce the same numeric value.

For example:

```text
S = "22"
```

The substring `"2"` occurs twice.

We only want the number `2` once.

Therefore, use a Python `set`:

```python
pronic_set = set()
```

When a pronic number is found:

```python
pronic_set.add(num)
```

The set automatically removes duplicates.

---

# 4️⃣ Sort the Result

After processing all substrings:

```python
result = sorted(pronic_set)
```

This produces the values in ascending order.

Finally:

```python
print(result)
```

prints them in the required format.

---

# 🔄 Algorithm

1. Read the digit string `S`.
2. Initialize an empty set `pronic_set`.
3. For every starting index `i`:

   * Set `num = 0`.
4. For every ending index `j` from `i` to `N - 1`:

   * Update:

```python
num = num * 10 + int(s[j])
```

* Check whether `num` is pronic.
* If it is, add it to `pronic_set`.

5. Sort the set.
6. Print the sorted list.

---

# 💻 Python 3 Solution

```python
import math


def is_pronic(num):
    if num < 0:
        return False

    k = math.isqrt(num)

    return k * (k + 1) == num


def main():
    s = input().strip()
    n = len(s)

    pronic_set = set()

    # Generate every possible substring
    for i in range(n):
        num = 0

        for j in range(i, n):
            # Build the numeric value incrementally
            num = num * 10 + int(s[j])

            # Check if the number is pronic
            if is_pronic(num):
                pronic_set.add(num)

    # Sort unique pronic numbers
    result = sorted(pronic_set)

    print(result)


if __name__ == "__main__":
    main()
```

---

# 🧠 Dry Run

Consider:

```text
S = "2612"
```

### Starting at index `0`

```text
2
26
261
2612
```

Pronic check:

```text
2    → 1 × 2    → ✓
26   → not pronic
261  → not pronic
2612 → not pronic
```

Set:

```text
{2}
```

---

### Starting at index `1`

```text
6
61
612
```

Pronic check:

```text
6   → 2 × 3 → ✓
61  → not pronic
612 → not pronic
```

Set:

```text
{2, 6}
```

---

### Starting at index `2`

```text
1
12
```

Pronic check:

```text
1  → 0 × 1 → ✓
12 → 3 × 4 → ✓
```

Therefore, strictly under the stated definition that allows **non-negative consecutive integers**, `1` is also pronic.

⚠️ **Important:** The provided sample output is `[2, 6, 12]`, which excludes `1`. This indicates that the intended problem definition likely considers pronic numbers as products of **positive consecutive integers**, meaning:

```text
1 × 2 = 2
2 × 3 = 6
3 × 4 = 12
...
```

Under that interpretation, `1` is **not** considered pronic.

The implementation below follows the **sample's intended definition** and therefore excludes `1`.

---

# ✅ Correct Pronic Definition for This Problem

A number is pronic if:

```text
k × (k + 1)
```

where:

```text
k ≥ 1
```

Therefore:

```text
2  = 1 × 2   ✓
6  = 2 × 3   ✓
12 = 3 × 4   ✓
20 = 4 × 5   ✓
30 = 5 × 6   ✓
```

But:

```text
0 = 0 × 1
1 = 0 × 1
```

should not be accepted under the sample's intended definition.

A robust implementation is therefore:

```python
def is_pronic(num):
    if num < 2:
        return False

    k = math.isqrt(num)

    return k >= 1 and k * (k + 1) == num
```

### Recommended Final Code

```python
import math


def is_pronic(num):
    if num < 2:
        return False

    k = math.isqrt(num)

    return k * (k + 1) == num


def main():
    s = input().strip()
    n = len(s)

    pronic_set = set()

    for i in range(n):
        num = 0

        for j in range(i, n):
            num = num * 10 + int(s[j])

            if is_pronic(num):
                pronic_set.add(num)

    result = sorted(pronic_set)

    print(result)


if __name__ == "__main__":
    main()
```

---

# ⚠️ Leading Zeros

Since the input is a string, a substring can contain leading zeros.

For example:

```text
S = "012"
```

The substring:

```text
"02"
```

has the numeric value:

```text
2
```

Since the problem asks for **numeric substrings**, the value `2` should be treated as the number represented by that substring.

The incremental construction:

```python
num = num * 10 + int(s[j])
```

naturally handles leading zeros.

For example:

```text
"02"

0
↓
0 × 10 + 2
↓
2
```

---

# 📊 Number of Substrings

A string of length `N` contains:

```text
N × (N + 1) / 2
```

substrings.

For:

```text
N = 18
```

the maximum number of substrings is:

```text
18 × 19 / 2 = 171
```

So even though the problem uses nested loops, the maximum input size is small enough for this approach.

---

# ⚙️ Complexity Analysis

Let:

```text
N = length of S
```

There are:

```text
N(N + 1) / 2
```

possible substrings.

Therefore, we generate:

```text
O(N²)
```

substrings.

Each substring is checked for being pronic using `math.isqrt()`.

For a numeric value up to approximately `10¹⁸`, the integer square-root operation is extremely small in practice.

Thus, the overall approach is approximately:

```text
Time Complexity: O(N²)
Space Complexity: O(K)
```

where `K` is the number of distinct pronic values found.

Since:

```text
N ≤ 18
```

this approach is easily fast enough.

---

# 📌 Edge Cases

## 1. No Pronic Numbers

Input:

```text
13579
```

If no substring represents a pronic number:

```text
[]
```

is printed.

---

## 2. Repeated Pronic Numbers

Input:

```text
222
```

The number `2` appears as multiple substrings:

```text
2
2
2
```

but the result should contain it only once:

```text
[2]
```

---

## 3. Leading Zeros

Input:

```text
02
```

The substring `"02"` represents the number `2`.

Therefore:

```text
[2]
```

---

## 4. Multiple Pronic Numbers

Input:

```text
2612
```

The pronic numbers are:

```text
2
6
12
```

After sorting:

```text
[2, 6, 12]
```

---

# 🔑 Key Concepts

This problem demonstrates:

* String substring generation
* Nested loops
* Incremental number construction
* Pronic numbers
* Integer square root
* `math.isqrt()`
* Python `set`
* Removing duplicates
* Sorting
* Handling leading zeros
* Edge-case analysis

---

# 🎯 Key Takeaway

The main pattern is:

```text
Digit String
     ↓
Generate every substring
     ↓
Build numeric value
     ↓
Is it pronic?
     ↓
   Yes
     ↓
Store in Set
     ↓
Remove duplicates
     ↓
Sort
     ↓
Print
```

For:

```text
2612
```

we examine every possible substring and identify:

```text
2  → 1 × 2  ✓
6  → 2 × 3  ✓
12 → 3 × 4  ✓
```

Therefore:

```text
[2, 6, 12]
```

The key optimization is building each substring's numeric value incrementally:

```python
num = num * 10 + int(s[j])
```

rather than repeatedly converting complete substrings with `int()`.

With `|S| ≤ 18`, the `O(N²)` substring-generation approach is simple, efficient, and well within the constraints.
