# 6 Problem Name: Maximum XOR-Sum Under Range Constraint

---

## 📄 Problem Statement

Resli defined a new function called **Xor-sum** for an array $A$ of length $N$ and an integer $x$:

$$\text{Xor-sum}(x) = (x \oplus A[1]) + (x \oplus A[2]) + \dots + (x \oplus A[N])$$

Given an array $A$ of length $N$ and an integer $K$, find an integer $x$ in the range $[0, K]$ that maximizes $\text{Xor-sum}(x)$. 

Print **only the maximum $\text{Xor-sum}(x)$ value**.

### Examples
* **Example 1:**
  * $N = 3, K = 7$, $A = [1, 6, 3]$
  * Output: `14`
  * *Explanation:* $x = 4 \in [0, 7]$ gives $(4 \oplus 1) + (4 \oplus 6) + (4 \oplus 3) = 5 + 2 + 7 = 14$.

* **Example 2:**
  * $N = 4, K = 9$, $A = [7, 4, 0, 3]$
  * Output: `46`
  * *Explanation:* $x = 8 \in [0, 9]$ gives $(8 \oplus 7) + (8 \oplus 4) + (8 \oplus 0) + (8 \oplus 3) = 15 + 12 + 8 + 11 = 46$.

### Constraints
* $1 \le N \le 10^5$
* $0 \le K \le 10^9$
* $0 \le A[i] \le 10^9$

---

## 🎯 Used Pattern & Algorithmic Concepts

1. **Bit Independence:**
   Each bit position operates independently. The contribution of bit $b$ to the total sum depends only on whether the $b$-th bit of $x$ is $0$ or $1$.
2. **Digit DP / Bitwise Construction:**
   We construct candidate values for $x$ from Most Significant Bit (MSB) to Least Significant Bit (LSB). At any bit where $x$ becomes strictly smaller than $K$, all lower bits can be chosen greedily.

---

## 💡 Approach to Solve

1. **Precompute Bit Contributions:**
   * Count how many numbers in $A$ have the $b$-th bit set to $1$.
   * `cost0[b]`: Contribution if $b$-th bit of $x$ is $0$.
   * `cost1[b]`: Contribution if $b$-th bit of $x$ is $1$.

2. **Precompute Suffix Maxima:**
   `suffix_max[b]` stores the maximum sum achievable for bits $0 \dots b-1$ when we have complete freedom to choose bit values.

3. **Digit DP Loop (Bit 29 down to 0):**
   * Maintain `tight_sum` (sum accumulated by matching $K$'s bits so far).
   * If the $b$-th bit of $K$ is $1$:
     * **Branch A ($x_b = 0$):** $x$ becomes strictly less than $K$. Contribution is `tight_sum + cost0[b] + suffix_max[b]`. Update global max answer.
     * **Branch B ($x_b = 1$):** $x$ stays tight with $K$. Add `cost1[b]` to `tight_sum`.
   * If the $b$-th bit of $K$ is $0$:
     * $x_b$ must be $0$. Add `cost0[b]` to `tight_sum`.

4. **Final Answer:**
   Return the maximum value collected across all tight and non-tight branches.

---

## 🔍 Line-by-Line Code Explanation

# Maximum XOR Sum — Bitwise Optimization

## Problem Overview

Given an array `A` containing non-negative integers and an integer `K`, the goal is to find a value `x` such that:

```text
0 <= x <= K
```

and maximize:

```text
sum(x XOR A[i])
```

for all elements `A[i]`.

The solution uses **bit manipulation** and **digit DP / binary DP** to efficiently find the optimal `x`.

---

## Key Idea

Instead of checking every possible value of `x` from `0` to `K`, we process the numbers **bit by bit**.

Since:

```text
10^9 < 2^30
```

we need at most **30 bits** to represent the numbers.

```python
BITS = 30
```

For every bit position, we calculate how much contribution that bit would make to the total XOR sum depending on whether the corresponding bit of `x` is `0` or `1`.

---

## 1. Number of Bits

```python
BITS = 30
```

`BITS = 30` because:

```text
10^9 < 2^30
```

Therefore, bit positions:

```text
0, 1, 2, ..., 29
```

are sufficient to represent every number up to `10^9`.

---

## 2. Counting Set Bits

```python
count1 = [0] * BITS
```

`count1[b]` stores the number of elements in `A` whose `b`-th bit is `1`.

For example, if:

```text
A = [5, 6]
```

Binary representation:

```text
5 = 101
6 = 110
```

Then:

```text
bit 0 → one number has 1
bit 1 → one number has 1
bit 2 → two numbers have 1
```

So `count1` allows us to calculate XOR contributions without checking every element for every possible `x`.

---

## 3. Calculating `cost0` and `cost1`

For every bit `b`, we calculate two possible contributions.

### `cost0[b]`

```text
cost0[b] = contribution from bit b
            when bit b of x is 0
```

If `x_b = 0`, then:

```text
0 XOR A[i]_b = A[i]_b
```

Therefore, the contribution comes from the numbers in `A` that have a `1` at bit `b`.

```text
cost0[b] = count1[b] × 2^b
```

---

### `cost1[b]`

```text
cost1[b] = contribution from bit b
            when bit b of x is 1
```

If `x_b = 1`, then:

```text
1 XOR A[i]_b
```

is `1` when `A[i]_b = 0`.

The number of zeros at bit `b` is:

```text
N - count1[b]
```

Therefore:

```text
cost1[b] = (N - count1[b]) × 2^b
```

---

## 4. Why We Cannot Simply Choose the Larger Cost

At first glance, we might think that for every bit we should simply choose:

```text
max(cost0[b], cost1[b])
```

But there is an important restriction:

```text
x <= K
```

Choosing a `1` at a particular bit can make `x` greater than `K`.

Therefore, we need to maintain whether the currently constructed `x` is still **equal to the corresponding prefix of `K`**.

This is called the **tight condition**.

---

# Binary Digit DP

We process bits from the **Most Significant Bit (MSB)** to the **Least Significant Bit (LSB)**.

```python
for b in range(BITS - 1, -1, -1):
```

This iterates:

```text
29 → 28 → 27 → ... → 1 → 0
```

Processing from the MSB is important because the comparison:

```text
x <= K
```

is determined by the first bit where `x` and `K` differ.

---

## 5. Extracting the Current Bit of K

```python
k_bit = (k >> b) & 1
```

This extracts the `b`-th bit of `K`.

For example:

```text
K = 13
Binary = 1101
```

To obtain a particular bit, we shift `K` right by `b` positions and use:

```python
& 1
```

So:

```python
k_bit = (K >> b) & 1
```

returns either:

```text
0
```

or:

```text
1
```

---

# Case 1: `k_bit == 1`

```python
if k_bit == 1:
```

Suppose the current bit of `K` is:

```text
K_b = 1
```

There are two possibilities for `x_b`.

### Option A: Choose `x_b = 0`

```text
0 < 1
```

Therefore, `x` becomes **strictly smaller than K**.

Once this happens, all remaining lower bits can be chosen freely.

So we add the best possible contribution from all remaining bits:

```text
suffix_max[b]
```

Conceptually:

```python
candidate = tight_sum + cost0[b] + suffix_max[b]
```

---

### Option B: Choose `x_b = 1`

```text
1 = 1
```

The prefix of `x` remains equal to the prefix of `K`.

Therefore, we must continue processing the lower bits while remaining **tight**.

The contribution of choosing `1` is:

```python
tight_sum += cost1[b]
```

---

# Case 2: `k_bit == 0`

```python
else:
```

If:

```text
K_b = 0
```

then we cannot choose:

```text
x_b = 1
```

because:

```text
1 > 0
```

would immediately make:

```text
x > K
```

Therefore, we are forced to choose:

```text
x_b = 0
```

and add:

```python
tight_sum += cost0[b]
```

The prefix remains tight.

---

# 6. `suffix_max`

```text
suffix_max[b]
```

stores the maximum possible contribution from bits:

```text
0 ... b-1
```

when the prefix has already become smaller than `K`.

Once:

```text
x < K
```

there is no longer any restriction from `K`.

Therefore, for every remaining bit we can independently choose whichever option gives the larger contribution.

Conceptually:

```text
suffix_max[b]
=
max contribution achievable using bits 0 to b-1
```

This avoids repeatedly calculating the best possible lower-bit configuration.

---

# 7. `tight_sum`

```text
tight_sum
```

stores the total contribution obtained so far while the constructed value of `x` is still equal to the corresponding prefix of `K`.

In other words:

```text
x_prefix == K_prefix
```

As long as we remain tight, the next bit of `x` is restricted by the corresponding bit of `K`.

---

# 8. Updating the Answer

Whenever:

```text
K_b = 1
```

we can choose:

```text
x_b = 0
```

This makes:

```text
x < K
```

After that, all lower bits become unrestricted.

Therefore, we calculate:

```text
candidate = tight_sum + cost0[b] + suffix_max[b]
```

and update:

```python
max_ans = max(max_ans, candidate)
```

This considers every possible position where `x` becomes smaller than `K`.

---

# 9. Final Tight Case

It is also possible that:

```text
x = K
```

through all bits.

Therefore, after processing every bit, the value stored in:

```text
tight_sum
```

must also be considered.

The final answer is essentially:

```python
max_ans = max(max_ans, tight_sum)
```

---

# Algorithm Summary

The complete approach can be summarized as follows:

```text
1. Determine the number of bits required.
        ↓
2. Count how many A[i] values contain 1 at every bit.
        ↓
3. Calculate cost0[b] and cost1[b].
        ↓
4. Precompute suffix_max[b].
        ↓
5. Process K from MSB to LSB.
        ↓
6. If K's bit is 1:
       ├── Choose x's bit = 0 → x becomes smaller than K
       │                       → use suffix_max
       │
       └── Choose x's bit = 1 → remain tight
        ↓
7. If K's bit is 0:
       └── x's bit must be 0
        ↓
8. Take the maximum possible XOR sum.
```

---

# Complexity Analysis

Let:

```text
N = length of A
B = number of bits
```

### Preprocessing

Counting the set bits requires:

```text
O(N × B)
```

time.

Calculating the costs requires:

```text
O(B)
```

time.

The DP over the bits requires:

```text
O(B)
```

time.

Therefore, the overall time complexity is:

```text
O(N × B)
```

Since `B = 30` for values up to `10^9`, this is effectively:

```text
O(N)
```

for practical purposes.

### Space Complexity

We store arrays of size `B`:

```text
count1
cost0
cost1
suffix_max
```

Therefore:

```text
O(B)
```

space is used.

With `B = 30`, the extra space is effectively constant.

---

# Important Concepts

| Concept         | Meaning                                               |
| --------------- | ----------------------------------------------------- |
| `BITS`          | Number of bits required                               |
| `count1[b]`     | Number of values having bit `b` set                   |
| `cost0[b]`      | XOR contribution when `x_b = 0`                       |
| `cost1[b]`      | XOR contribution when `x_b = 1`                       |
| `suffix_max[b]` | Best contribution from unrestricted lower bits        |
| `tight_sum`     | Contribution while `x` is still equal to `K`'s prefix |
| `k_bit`         | Current bit of `K`                                    |
| `max_ans`       | Maximum XOR sum found                                 |

---

# Core Insight

The key observation is that we **do not need to try every value of `x` from `0` to `K`**.

Instead, we exploit two properties:

1. XOR contribution can be calculated **independently for each bit**.
2. The constraint `x <= K` can be handled using **binary digit DP**.

When a bit of `x` becomes smaller than the corresponding bit of `K`, all remaining lower bits become unrestricted. This is exactly why `suffix_max` makes the solution efficient.

The final complexity is therefore:

```text
O(N × B)
```

instead of:

```text
O(N × K)
```

which would be infeasible when `K` is large.
