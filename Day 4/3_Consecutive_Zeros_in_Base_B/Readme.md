# 🔢 Consecutive Zeros in Base B

## 📌 Problem Overview

Given a positive decimal integer `N` and a base `B`, convert `N` from decimal (base 10) to base `B`.

After conversion, find the **maximum number of consecutive `0`s** in the resulting representation.

If the base-`B` representation contains **no zero**, print:

```text
-1
```

---

## 🧩 Problem Statement

You are given:

* A positive decimal integer `N`
* A base `B`

First, convert `N` into its representation in base `B`.

Then determine the length of the **longest consecutive sequence of zeros**.

### Example

For:

```text
N = 68
B = 2
```

The binary representation is:

```text
68 = 1000100₂
```

The zero sequences are:

```text
1 000 1 00
  ↑↑↑
```

The longest sequence contains:

```text
3 zeros
```

Therefore, the answer is:

```text
3
```

---

## 📥 Input Format

The first line contains a positive integer `N`.

The second line contains an integer `B`.

```text
N
B
```

### Constraints

```text
1 ≤ N ≤ 10⁹
2 ≤ B ≤ 36
```

---

## 📤 Output Format

Print a single integer representing the maximum number of consecutive zeros in the base-`B` representation of `N`.

If there are no zeros, print:

```text
-1
```

---

# 🧪 Sample Input

```text
68
2
```

## 🧪 Sample Output

```text
3
```

### Explanation

Convert `68` from decimal to binary:

```text
68 = 1000100₂
```

There are two groups of zeros:

```text
1000100
 ───
```

The first group contains `3` consecutive zeros.

The second group contains `2` consecutive zeros.

Therefore:

```text
Maximum consecutive zeros = 3
```

---

# 💡 Approach

The problem has two main parts:

1. Convert `N` into base `B`.
2. Find the longest sequence of consecutive zeros.

---

# 🔄 Step 1 — Convert to Base B

To convert a decimal number into another base, repeatedly divide the number by `B`.

For every division:

```text
remainder = N % B
```

The remainder gives the next digit of the representation.

Then update:

```text
N = N // B
```

Continue until `N` becomes `0`.

### Example

Convert:

```text
68 → base 2
```

| Number |     Division | Remainder |
| -----: | -----------: | --------: |
|     68 | 68 // 2 = 34 |         0 |
|     34 | 34 // 2 = 17 |         0 |
|     17 |  17 // 2 = 8 |         1 |
|      8 |   8 // 2 = 4 |         0 |
|      4 |   4 // 2 = 2 |         0 |
|      2 |   2 // 2 = 1 |         0 |
|      1 |   1 // 2 = 0 |         1 |

The remainders are generated from **right to left**:

```text
0 0 1 0 0 0 1
```

Reversing them gives:

```text
1000100
```

Therefore:

```text
68 = 1000100₂
```

---

# 🔢 Supporting Bases up to 36

The maximum base is `36`.

Therefore, digits can range from:

```text
0 - 9
A - Z
```

The mapping used is:

```python
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
```

So:

```text
Remainder 0  → 0
Remainder 1  → 1
...
Remainder 9  → 9
Remainder 10 → A
Remainder 11 → B
...
Remainder 35 → Z
```

For example:

```text
10 → A
11 → B
15 → F
35 → Z
```

This allows the same conversion function to work for every base from `2` through `36`.

---

# 🔍 Step 2 — Find Consecutive Zeros

After conversion, we have a string such as:

```text
1000100
```

We scan the string from left to right.

Maintain two variables:

```python
count
max_zero
```

### `count`

Stores the number of consecutive zeros in the **current** sequence.

### `max_zero`

Stores the largest zero sequence found so far.

When the current character is `0`:

```python
count += 1
```

When a non-zero character is found:

```python
count = 0
```

At every zero:

```python
max_zero = max(max_zero, count)
```

---

# 🧠 Dry Run

Consider:

```text
N = 68
B = 2
```

After conversion:

```text
1000100
```

Process each character:

| Character | Current Count | Maximum |
| --------- | ------------: | ------: |
| `1`       |             0 |       0 |
| `0`       |             1 |       1 |
| `0`       |             2 |       2 |
| `0`       |             3 |       3 |
| `1`       |             0 |       3 |
| `0`       |             1 |       3 |
| `0`       |             2 |       3 |

Final result:

```text
max_zero = 3
```

So the output is:

```text
3
```

---

# 💻 Python 3 Solution

```python
def to_base(N, B):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""

    while N > 0:
        res = digits[N % B] + res
        N //= B

    return res


def find_max_consecutive_zeros(s):
    count = 0
    max_zero = 0
    has_zero = False

    for c in s:
        if c == '0':
            count += 1
            has_zero = True
            max_zero = max(max_zero, count)
        else:
            count = 0

    return max_zero if has_zero else -1


N = int(input())
B = int(input())

base_representation = to_base(N, B)

print(find_max_consecutive_zeros(base_representation))
```

---

# 📌 Why Return `-1`?

The problem specifically requires `-1` when the base-`B` representation contains no zero.

For example:

```text
N = 7
B = 2
```

The representation is:

```text
111
```

There are no zeros.

Therefore:

```text
Output:
-1
```

The `has_zero` flag is used to distinguish between:

```text
No zero exists → -1
```

and:

```text
A zero exists → return max_zero
```

---

# 🧪 Additional Examples

## Example 1 — No Zeros

Input:

```text
7
2
```

Binary representation:

```text
111
```

No zeros exist.

Output:

```text
-1
```

---

## Example 2 — One Zero

Input:

```text
10
2
```

Binary representation:

```text
1010
```

The longest zero sequence has length `1`.

Output:

```text
1
```

---

## Example 3 — Multiple Zero Groups

Input:

```text
68
2
```

Representation:

```text
1000100
```

Zero groups:

```text
000
00
```

Longest:

```text
3
```

Output:

```text
3
```

---

## Example 4 — Base 10

Input:

```text
10020003
10
```

The representation remains:

```text
10020003
```

The zero groups are:

```text
00
```

and:

```text
000
```

Therefore:

```text
Output:
3
```

---

## Example 5 — Base Greater Than 10

For bases greater than `10`, digits after `9` are represented using uppercase letters.

For example, in base `16`:

```text
15 = F
```

and:

```text
16 = 10
```

The same conversion technique works because the remainder is mapped through:

```python
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
```

---

# ⚙️ Complexity Analysis

Let:

```text
L = number of digits in N when represented in base B
```

The number of base-`B` digits is:

```text
L = O(log_B N)
```

### Base Conversion

Each iteration divides `N` by `B`, so conversion takes:

```text
O(log_B N)
```

time.

### Finding Consecutive Zeros

We scan the resulting representation once:

```text
O(log_B N)
```

time.

Therefore, the overall time complexity is:

```text
O(log_B N)
```

### Space Complexity

The converted representation is stored as a string:

```text
O(log_B N)
```

space.

Therefore:

```text
Time Complexity:  O(log_B N)
Space Complexity: O(log_B N)
```

---

# 🔑 Key Concepts

This problem demonstrates:

* Number-system conversion
* Decimal to arbitrary-base conversion
* Repeated division
* Modulo (`%`)
* Integer division (`//`)
* Character mapping
* String processing
* Consecutive sequence counting
* Tracking maximum values
* Handling edge cases

---

# 🎯 Key Takeaway

The core idea is:

```text
Decimal Number N
       ↓
Repeatedly divide by B
       ↓
Collect remainders
       ↓
Reverse remainders
       ↓
Base-B Representation
       ↓
Scan for consecutive '0's
       ↓
Track longest sequence
       ↓
No zero? → -1
       ↓
Otherwise → maximum count
```

For the sample:

```text
68
B = 2
```

we get:

```text
68
 ↓
1000100₂
 ↓
1000100
 ↓
Longest zero sequence = 3
```

Therefore:

```text
Answer = 3
```

The important pattern to remember is:

> **Convert first, then process the resulting representation as a string.**

This separates the number-system logic from the consecutive-character counting logic and keeps the solution simple and efficient.
