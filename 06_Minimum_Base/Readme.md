#  7. 🔢 Minimum Base with Identical Digits

## 📌 Problem Statement

You are given a natural number `M` in decimal representation:

> `1 ≤ M ≤ 10¹²`

Find the **minimum base `B ≥ 2`** such that the representation of `M` in base `B` consists entirely of **identical digits**.

### Example

For `M = 63`:

* Base `10` → `63` ❌
* Base `8` → `77` ✅
* Base `4` → `333` ✅

Therefore, the minimum valid base is:

```text
4
```

---

## 💡 Key Idea

A brute-force approach would check every base:

```text
B = 2, 3, 4, ..., M - 1
```

For `M = 10¹²`, this could require checking up to `10¹²` bases, which is far too slow.

The key is to divide the possible bases into two cases based on the number of digits in the representation.

---

## 🧠 Mathematical Observation

Suppose the representation of `M` in base `B` has `L` identical digits, each having value `d`.

Then:

```text
M = d × (B^(L-1) + B^(L-2) + ... + B + 1)
```

### Case 1: `L ≥ 3`

Since `d ≥ 1`:

```text
M ≥ B² + B + 1
```

Therefore:

```text
M > B²
```

which implies:

```text
B < √M
```

So every representation having at least 3 digits must use a base smaller than `√M`.

For:

```text
M = 10¹²
```

we only need to test bases up to:

```text
√M = 10⁶
```

This is manageable.

---

### Case 2: `L = 2`

A two-digit representation with identical digits looks like:

```text
dd
```

Its value is:

```text
M = d × B + d
```

Therefore:

```text
M = d(B + 1)
```

Rearranging:

```text
B = M / d - 1
```

Thus, `d` must be a divisor of `M`.

To find the smallest possible `B`, we can search for divisors `d ≤ √M`.

---

## 🚀 Algorithm

The solution works in two phases.

### Phase 1 — Small Bases

1. Calculate:

   ```python
   limit = floor(√M)
   ```

2. Test every base:

   ```text
   B = 2 ... √M
   ```

3. Convert `M` into base `B` using repeated division.

4. Check whether every digit is identical.

5. Since bases are tested in increasing order, the first valid base is the answer.

---

### Phase 2 — Large Bases

If no base up to `√M` works:

1. Start with:

   ```python
   best_B = M - 1
   ```

2. For every possible digit `d` from `1` to `√M`:

   * Check whether `d` divides `M`.

   * Calculate:

     ```text
     B = M / d - 1
     ```

   * Verify that:

     ```text
     d < B
     ```

   * Keep the smallest valid base.

3. Return `best_B`.

---

## 🔍 Base Representation

| Digit Length | Equation        | Base Range | Approach        |
| ------------ | --------------- | ---------- | --------------- |
| `L ≥ 3`      | `M = d × Σ(Bⁱ)` | `B < √M`   | Test every base |
| `L = 2`      | `M = d(B + 1)`  | Large `B`  | Search divisors |

---

## 🧩 Python Implementation

```python
from math import isqrt


def check_all_digits_same(M, B):
    """
    Check whether all digits of M in base B are identical.
    """

    first_digit = M % B
    M //= B

    while M > 0:
        if M % B != first_digit:
            return False

        M //= B

    return True


def min_base_identical_digits(M):
    """
    Find the minimum base B >= 2 such that
    the representation of M in base B
    contains identical digits.
    """

    # Handle small values
    if M <= 2:
        return M + 1

    # Integer square root
    limit = isqrt(M)

    # -------------------------------------------------
    # Phase 1: Check bases up to sqrt(M)
    # -------------------------------------------------
    for B in range(2, limit + 1):
        if check_all_digits_same(M, B):
            return B

    # -------------------------------------------------
    # Phase 2: Check two-digit representations
    # -------------------------------------------------

    # Base M - 1 always represents M as "11"
    best_B = M - 1

    for d in range(1, limit + 1):

        # d must divide M
        if M % d == 0:

            # M = d(B + 1)
            B = (M // d) - 1

            # Digit must be smaller than the base
            if d < B:
                best_B = min(best_B, B)

    return best_B


# Example
M = 63
print(min_base_identical_digits(M))
```

### Output

```text
4
```

---

## 📝 Code Explanation

### 1. Checking whether all digits are identical

```python
first_digit = M % B
```

`M % B` gives the rightmost digit when `M` is represented in base `B`.

This digit is stored as the reference digit.

---

### 2. Remove the rightmost digit

```python
M //= B
```

Integer division by `B` removes the rightmost base-`B` digit.

For example, if:

```text
M = 63
B = 4
```

then:

```text
63₁₀ = 333₄
```

The repeated division process extracts:

```text
3 → 3 → 3
```

---

### 3. Compare every digit

```python
while M > 0:
    if M % B != first_digit:
        return False

    M //= B
```

Each remaining digit is compared with the first digit.

If any digit differs, the representation does not satisfy the condition.

---

### 4. Handle small values

```python
if M <= 2:
    return M + 1
```

This handles:

```text
M = 1 → 11₂
M = 2 → 11₃
```

Therefore:

```text
M = 1 → B = 2
M = 2 → B = 3
```

---

### 5. Calculate the search boundary

```python
limit = isqrt(M)
```

`isqrt()` calculates the exact integer value of:

```text
floor(√M)
```

Using `isqrt()` avoids floating-point precision issues.

---

### 6. Search small bases

```python
for B in range(2, limit + 1):
    if check_all_digits_same(M, B):
        return B
```

Every base from `2` to `√M` is checked.

Because the loop is in ascending order, the first valid base is automatically the minimum.

---

### 7. Initialize the large-base answer

```python
best_B = M - 1
```

Base `M - 1` always represents `M` as:

```text
11
```

because:

```text
1 × (M - 1) + 1 = M
```

So a valid solution always exists for `M > 2`.

---

### 8. Search possible digits

```python
for d in range(1, limit + 1):
```

For a two-digit representation:

```text
M = d(B + 1)
```

The smaller factor `d` is sufficient to search up to `√M`.

---

### 9. Check whether `d` is a divisor

```python
if M % d == 0:
```

If `d` divides `M`, then:

```text
B = M / d - 1
```

is an integer.

---

### 10. Calculate the candidate base

```python
B = (M // d) - 1
```

This comes directly from:

```text
M = d(B + 1)
```

Therefore:

```text
B = M/d - 1
```

---

### 11. Validate the digit

```python
if d < B:
```

Every digit in base `B` must satisfy:

```text
0 ≤ digit < B
```

Therefore, `d` must be strictly smaller than `B`.

---

## 🧪 Dry Run

### Input

```text
M = 41
```

Calculate:

```text
√41 ≈ 6.4
```

Therefore:

```text
limit = 6
```

### Phase 1

Check bases:

```text
B = 2 → 101001₂ ❌
B = 3 → 1112₃  ❌
B = 4 → 221₄   ❌
B = 5 → 131₅   ❌
B = 6 → 105₆   ❌
```

No valid small base exists.

### Phase 2

Initialize:

```text
best_B = 41 - 1
        = 40
```

Check divisors up to `6`:

```text
1 → divisor
2 → not a divisor
3 → not a divisor
4 → not a divisor
5 → not a divisor
6 → not a divisor
```

For:

```text
d = 1
```

we get:

```text
B = 41 / 1 - 1
  = 40
```

And:

```text
1 < 40
```

So:

```text
41₁₀ = 11₄₀
```

### Output

```text
40
```

---

## 📊 Complexity Analysis

### Time Complexity

**Phase 1:**

At most `√M` bases are checked.

Each base conversion takes:

```text
O(log_B M)
```

time.

**Phase 2:**

At most `√M` possible digit values are checked.

Therefore, the overall complexity is:

```text
O(√M)
```

For:

```text
M ≤ 10¹²
```

we have:

```text
√M ≤ 10⁶
```

which is practical.

### Space Complexity

```text
O(1)
```

Only a constant number of variables are used.

---

## 🧠 Concepts Used

* **Number Systems**
* **Base Conversion**
* **Number Theory**
* **Divisors and Factors**
* **Square Root Decomposition**
* **Search Space Reduction**
* **Mathematical Optimization**

---

## 🎯 Key Learning

The main lesson is that mathematical reasoning can dramatically reduce a brute-force search.

Instead of checking:

```text
O(M)
```

possible bases, we reduce the search to approximately:

```text
O(√M)
```

by observing:

1. Representations with **3 or more digits** must have:

   ```text
   B < √M
   ```

2. Two-digit representations satisfy:

   ```text
   M = d(B + 1)
   ```

3. Therefore, large-base candidates can be generated directly from the **divisors of `M`**.

This transforms an impractical brute-force solution into an efficient number-theoretic solution.

---

## 📁 Suggested Repository Structure

```text
minimum-base-identical-digits/
│
├── README.md
├── solution.py
└── LICENSE
```

---

## ▶️ Running the Program

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate to the project:

```bash
cd minimum-base-identical-digits
```

Run the Python program:

```bash
python solution.py
```

---

## ⭐ Example

```text
Input:
63

Output:
4
```

Because:

```text
63₁₀ = 333₄
```

and no smaller base represents `63` using identical digits.
