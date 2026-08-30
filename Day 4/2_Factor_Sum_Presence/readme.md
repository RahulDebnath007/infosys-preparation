# 🔢 Factor Sum Presence

## 📌 Problem Overview

A number is considered **special** if the **sum of its proper divisors** is also present in the given list `L`.

For every number in the list:

1. Calculate the sum of its proper divisors.
2. Check whether that sum exists anywhere in the original list.
3. If it exists, include the number in the output.

If no number satisfies the condition, print:

```text
-1
```

### What Are Proper Divisors?

The **proper divisors** of a number are all positive divisors excluding the number itself.

For example:

```text
6 → 1, 2, 3
```

Therefore:

```text
sum = 1 + 2 + 3 = 6
```

Since `6` itself is present in the list, `6` is considered special.

> **Special rule:** The sum of proper divisors of `0` and `1` is defined as `0`.

---

# 🧩 Problem Statement

Given a list `L` of integers, find all numbers `x` such that:

```text
sum of proper divisors of x ∈ L
```

The numbers should be printed in their **original order**.

If no such number exists, print:

```text
-1
```

---

## 📥 Input Format

A single line containing comma-separated integers.

```text
a₁,a₂,a₃,...,aₙ
```

### Constraints

```text
0 ≤ L[i] ≤ 10⁹
1 ≤ |L| ≤ 10³
```

---

## 📤 Output Format

Print all numbers satisfying the condition, separated by spaces.

If no number satisfies the condition, print:

```text
-1
```

---

# 🧪 Sample Input

```text
0,1,6
```

## 🧪 Sample Output

```text
0 1 6
```

---

# 🔍 Sample Explanation

The input list is:

```text
L = [0, 1, 6]
```

### Number `0`

According to the problem statement:

```text
sum of proper divisors of 0 = 0
```

Since `0` is present in the list:

```text
0 ∈ L
```

`0` is special.

---

### Number `1`

According to the special rule:

```text
sum of proper divisors of 1 = 0
```

Since `0` exists in the list:

```text
0 ∈ L
```

`1` is special.

---

### Number `6`

The proper divisors of `6` are:

```text
1, 2, 3
```

Their sum is:

```text
1 + 2 + 3 = 6
```

Since `6` exists in the list:

```text
6 ∈ L
```

`6` is special.

Therefore, all three numbers satisfy the condition:

```text
0 1 6
```

---

# 💡 Approach

A straightforward solution would calculate the proper divisors of every number and then search for the resulting sum in the list.

However, because:

```text
L[i] ≤ 10⁹
```

we should **not** check every number from `1` to `n - 1` as a potential divisor.

Instead, we use the fact that divisors occur in pairs.

For example, for:

```text
n = 36
```

the divisor pairs are:

```text
1 × 36
2 × 18
3 × 12
4 × 9
6 × 6
```

So we only need to check possible divisors up to:

```text
√n
```

---

# 🔎 Efficient Divisor Calculation

For a number `n > 1`, `1` is always a proper divisor.

Therefore:

```python
s = 1
```

Then we iterate:

```python
for i in range(2, math.isqrt(n) + 1):
```

If:

```python
n % i == 0
```

then `i` is a divisor.

Its paired divisor is:

```python
n // i
```

So we add both:

```python
s += i

if i != n // i:
    s += n // i
```

The second condition is necessary for perfect squares.

For example:

```text
36
```

has the pair:

```text
6 × 6
```

We must add `6` only once.

---

# 🔄 Algorithm

1. Read the comma-separated input.
2. Convert it into a list of integers.
3. Convert the list into a `set`.
4. For every number:

   * Calculate its proper divisor sum.
   * Check whether that sum exists in the set.
5. If it exists, add the original number to the result.
6. Print the result in the original order.
7. If the result is empty, print `-1`.

---

# 💻 Python 3 Solution

```python
import math

nums = list(map(int, input().split(",")))
num_set = set(nums)


def divisor_sum(n):
    # Special cases
    if n == 0 or n == 1:
        return 0

    # 1 is always a proper divisor for n > 1
    total = 1

    # Check divisors only up to sqrt(n)
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            total += i

            # Add the paired divisor
            # only if it is different from i
            if i != n // i:
                total += n // i

    return total


result = [
    num
    for num in nums
    if divisor_sum(num) in num_set
]

print(" ".join(map(str, result)) if result else -1)
```

---

# 🧠 Dry Run

Consider:

```text
L = [6, 8, 10, 28]
```

We calculate the proper divisor sum of every number.

### For `6`

```text
Proper divisors = 1, 2, 3
Sum = 6
```

Since `6` exists in the list:

```text
6 → special
```

### For `8`

```text
Proper divisors = 1, 2, 4
Sum = 7
```

`7` is not in the list:

```text
8 → not special
```

### For `10`

```text
Proper divisors = 1, 2, 5
Sum = 8
```

`8` exists in the list:

```text
10 → special
```

### For `28`

```text
Proper divisors = 1, 2, 4, 7, 14
Sum = 28
```

`28` exists in the list:

```text
28 → special
```

Therefore:

```text
Output:
6 10 28
```

---

# 🔬 Understanding `math.isqrt()`

The code uses:

```python
math.isqrt(n)
```

instead of:

```python
int(math.sqrt(n))
```

`math.isqrt(n)` directly calculates the **integer square root** without floating-point precision issues.

For example:

```text
isqrt(36) = 6
isqrt(37) = 6
isqrt(100) = 10
```

This makes it suitable for divisor calculations with values as large as `10⁹`.

---

# ⚙️ Complexity Analysis

Let:

```text
N = number of elements in the list
V = maximum value in the list
```

For each number, the divisor calculation checks up to:

```text
√V
```

Therefore, the worst-case time complexity is approximately:

```text
O(N√V)
```

With:

```text
N ≤ 10³
V ≤ 10⁹
```

this is much more efficient than checking every possible divisor up to `V`.

### Space Complexity

The set containing all input values requires:

```text
O(N)
```

space.

The result list also requires up to:

```text
O(N)
```

space.

Therefore:

```text
Space Complexity: O(N)
```

---

# 📌 Edge Cases

## 1. Input Contains Only `0`

```text
Input:
0
```

By definition:

```text
sum(0) = 0
```

Since `0` is present:

```text
Output:
0
```

---

## 2. Input Contains Only `1`

```text
Input:
1
```

The proper divisor sum of `1` is defined as:

```text
0
```

But `0` is not present.

Therefore:

```text
Output:
-1
```

---

## 3. `0` and `1`

```text
Input:
0,1
```

For both:

```text
divisor_sum(0) = 0
divisor_sum(1) = 0
```

Since `0` exists:

```text
Output:
0 1
```

---

## 4. No Special Numbers

If none of the numbers have a divisor sum present in the list:

```text
Output:
-1
```

---

# 🔑 Key Concepts

This problem demonstrates:

* Proper divisors
* Divisor pairs
* Square-root optimization
* `math.isqrt()`
* Python `set`
* Membership testing
* List comprehensions
* Input parsing
* Handling special cases
* Time complexity optimization

---

# 🎯 Key Takeaway

The most important optimization is recognizing that divisors come in **pairs**.

Instead of checking:

```text
1 → 2 → 3 → ... → n-1
```

we only check:

```text
1 → 2 → 3 → ... → √n
```

Whenever `i` divides `n`, we automatically get another divisor:

```text
n // i
```

So:

```text
n = i × (n // i)
```

This reduces the divisor-sum calculation from roughly:

```text
O(N)
```

per number to:

```text
O(√N)
```

per number.

The complete strategy is:

```text
Input List
    ↓
Convert to Set
    ↓
For every number
    ↓
Calculate proper divisor sum
    ↓
Is the sum present in the set?
    ↓
   Yes ─────→ Keep number
    ↓
   No
    ↓
 Ignore
    ↓
Print special numbers
    ↓
No results → -1
```

For the sample:

```text
0,1,6
```

we get:

```text
0 → divisor sum = 0 → present ✓
1 → divisor sum = 0 → present ✓
6 → divisor sum = 6 → present ✓
```

Final result:

```text
0 1 6
```
