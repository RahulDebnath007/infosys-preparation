# 🏠 LeetCode 213 — House Robber II

[![LeetCode](https://img.shields.io/badge/LeetCode-213-orange)](https://leetcode.com/problems/house-robber-ii/)

## 📌 Problem Overview

You are a professional robber planning to rob houses arranged in a **circle**.

Each house contains some amount of money.

However, adjacent houses have connected security systems. If two adjacent houses are robbed on the same night, the police are alerted.

The goal is to determine the **maximum amount of money** that can be robbed without robbing two adjacent houses.

---

# 🧩 Problem Statement

Given an integer array:

```text
nums[i]
```

where `nums[i]` represents the money stored in the `i-th` house, return the maximum amount of money that can be robbed without alerting the police.

The houses are arranged in a circle, meaning:

```text
House 0
   ↕
House n - 1
```

are also adjacent.

This creates an additional restriction compared with the original **House Robber** problem.

---

## 📥 Input

An integer array:

```text id="0x5g4n"
nums
```

### Constraints

```text id="nkjx4v"
1 ≤ nums.length ≤ 100
0 ≤ nums[i] ≤ 1000
```

---

## 📤 Output

Return the maximum amount of money that can be robbed without robbing two adjacent houses.

---

# 🧪 Example 1

```text id="9u8i1c"
Input:
nums = [2,3,2]

Output:
3
```

### Explanation

The houses are arranged in a circle:

```text id="h1qj8m"
     2
   /   \
  3     2
   \   /
```

House `0` and house `2` are adjacent.

Therefore, we cannot rob:

```text id="x7x6qf"
2 + 2
```

The best choice is to rob the middle house:

```text id="6w8h92"
3
```

So the answer is:

```text id="e8bqz3"
3
```

---

# 🧪 Example 2

```text id="g5z6sj"
Input:
nums = [1,2,3,1]

Output:
4
```

The optimal choice is:

```text id="kn3x5h"
1 + 3 = 4
```

So:

```text id="1p3k9f"
Answer = 4
```

---

# 🧪 Example 3

```text id="3k7p2r"
Input:
nums = [1,2,3]

Output:
3
```

The best option is to rob:

```text id="g3u2d9"
house 2 → 3
```

Therefore:

```text id="9j6m1s"
Answer = 3
```

---

# 🧠 The Main Challenge: Circular Houses

The original **House Robber** problem is a linear problem.

For example:

```text id="bq7w3p"
a0 → a1 → a2 → a3 → a4
```

But House Robber II is circular:

```text id="3p6j8d"
        a0
      /    \
    a1      a4
    |        |
    a2      a3
      \    /
        ...
```

This means:

```text id="9x7tq3"
a0 and a(n-1)
```

are adjacent.

So if we rob `a0`, we cannot rob `a(n-1)`.

---

# 💡 Key Insight

There are only **two possible cases**.

## Case 1 — Rob the First House

If we decide to rob:

```text id="gk8l32"
nums[0]
```

then we cannot rob the last house:

```text id="r9w0n4"
nums[n-1]
```

So the remaining houses we can consider are:

```text id="l5j7b1"
nums[2 ... n-2]
```

The total becomes:

```text id="9ym0q5"
nums[0] + best(nums[2:n-1])
```

---

## Case 2 — Do Not Rob the First House

If we don't rob:

```text id="2c4b8x"
nums[0]
```

then the circular restriction disappears.

We can consider:

```text id="1q8z5n"
nums[1 ... n-1]
```

The total becomes:

```text id="k1m4w9"
best(nums[1:])
```

---

# 🏆 Final Decision

We calculate both possibilities:

```text id="e8v7q1"
Case 1 = nums[0] + best(nums[2:n-1])

Case 2 = best(nums[1:])
```

Then choose the larger result:

```text id="b8m2x4"
max(Case 1, Case 2)
```

This converts the circular problem into **two ordinary House Robber problems**.

---

# 🔄 Visualizing the Two Cases

Suppose we have:

```text id="z2p6x8"
[a0, a1, a2, a3, a4, a5]
```

### Case 1 — Rob `a0`

Because `a0` is robbed:

```text id="a0"
[a0, a1, a2, a3, a4, a5]
 ↑                       ↑
rob                     cannot rob
```

So we solve:

```text id="w4n8c2"
a2 → a3 → a4
```

Total:

```text id="7s1m9x"
a0 + best(a2...a4)
```

---

### Case 2 — Don't Rob `a0`

Now we solve:

```text id="q5x8m1"
a1 → a2 → a3 → a4 → a5
```

Total:

```text id="t7c3v5"
best(a1...a5)
```

Finally:

```text id="6n2z8q"
max(Case 1, Case 2)
```

---

# 🧩 Solving the Linear House Robber Problem

After breaking the circle into two cases, we still need to solve the normal House Robber problem.

For a linear sequence, maintain two variables:

```python id="7f3v2x"
dp1
dp2
```

They represent the best results from the previous states.

For every house containing `num`:

```python id="w8q1k4"
dp1, dp2 = dp2, max(dp1 + num, dp2)
```

The two choices are:

### Rob Current House

Then we cannot rob the previous house:

```text id="7x3p9m"
dp1 + num
```

### Skip Current House

Keep the previous maximum:

```text id="2n8v5q"
dp2
```

Therefore:

```text id="4r6m1s"
new_dp2 = max(dp1 + num, dp2)
```

---

# 💻 Python Solution

```python id="9x4m2k"
class Solution:
    def rob(self, nums):

        def rob_helper(nums):
            dp1, dp2 = 0, 0

            for num in nums:
                dp1, dp2 = dp2, max(dp1 + num, dp2)

            return dp2

        # Case 1:
        # Rob first house, so exclude last house.
        case1 = nums[0] + rob_helper(nums[2:-1])

        # Case 2:
        # Don't rob first house, so consider houses 1 through n-1.
        case2 = rob_helper(nums[1:])

        return max(case1, case2)
```

---

# 🔍 Code Breakdown

## `rob_helper()`

```python id="j8w3p1"
def rob_helper(nums):
    dp1, dp2 = 0, 0

    for num in nums:
        dp1, dp2 = dp2, max(dp1 + num, dp2)

    return dp2
```

This solves the standard **linear House Robber** problem.

At every house, we have two choices:

```text id="p4n8x2"
Rob it    → dp1 + num
Skip it   → dp2
```

Choose the maximum:

```text id="7m2q9z"
max(dp1 + num, dp2)
```

---

# 🧠 Dry Run

Consider:

```text id="r8m2x5"
nums = [2, 3, 2]
```

There are two cases.

### Case 1 — Rob First House

Rob:

```text id="5m8k2n"
2
```

The last house cannot be robbed.

The middle range:

```text id="6x1q7v"
nums[2:-1]
```

is empty.

Therefore:

```text id="j3n9p4"
case1 = 2
```

---

### Case 2 — Don't Rob First House

Consider:

```text id="7x4m1q"
[3, 2]
```

Linear House Robber gives:

```text id="0k9p3v"
3
```

Therefore:

```text id="m2x7q8"
case2 = 3
```

Finally:

```text id="p6n4z1"
max(2, 3) = 3
```

Answer:

```text id="q8m1v6"
3
```

---

# 🧪 Another Dry Run

Consider:

```text id="j7x3m9"
nums = [1, 2, 3, 1]
```

### Case 1

Rob first house:

```text id="5q8n2m"
1
```

Exclude the last house.

Remaining:

```text id="r4x7p1"
[3]
```

Best:

```text id="w2m8q5"
1 + 3 = 4
```

So:

```text id="n9x3v7"
case1 = 4
```

### Case 2

Don't rob first house.

Consider:

```text id="q6m1x8"
[2, 3, 1]
```

The best choice is:

```text id="h7p4n2"
3
```

So:

```text id="z8m2q6"
case2 = 3
```

Final:

```text id="4v9x1m"
max(4, 3) = 4
```

Answer:

```text id="p3n7q8"
4
```

---

# ⚠️ Important Edge Case: One House

The provided solution using:

```python id="5z7q2m"
nums[0] + rob_helper(nums[2:-1])
```

and:

```python id="7m3x9p"
rob_helper(nums[1:])
```

needs a special case when `len(nums) == 1`.

If there is only one house, simply return its value.

A fully robust solution is:

```python id="k8p4m2"
class Solution:
    def rob(self, nums):

        if len(nums) == 1:
            return nums[0]

        def rob_helper(nums):
            dp1, dp2 = 0, 0

            for num in nums:
                dp1, dp2 = dp2, max(dp1 + num, dp2)

            return dp2

        return max(
            rob_helper(nums[2:]),
            rob_helper(nums[1:])
        )
```

This version is also cleaner because:

* Case 1: exclude the first house → `nums[1:]`
* Case 2: exclude the last house → `nums[:-1]`

A standard formulation is:

```python id="j4x8p6"
max(
    rob_helper(nums[:-1]),
    rob_helper(nums[1:])
)
```

This is generally the clearest implementation.

### Recommended Version

```python id="c8m3q7"
class Solution:
    def rob(self, nums):

        if len(nums) == 1:
            return nums[0]

        def rob_helper(houses):
            prev2 = 0
            prev1 = 0

            for money in houses:
                current = max(
                    prev1,
                    prev2 + money
                )

                prev2 = prev1
                prev1 = current

            return prev1

        return max(
            rob_helper(nums[:-1]),
            rob_helper(nums[1:])
        )
```

---

# 🔬 Why `nums[:-1]` and `nums[1:]`?

The circular problem can be reduced to:

```text id="m6x2q9"
Exclude first house
        OR
Exclude last house
```

### Exclude Last

```python id="f3n7x1"
nums[:-1]
```

Example:

```text id="j8q2m5"
[2,3,2,4,5]
```

becomes:

```text id="y4p9n1"
[2,3,2,4]
```

### Exclude First

```python id="w2m6q8"
nums[1:]
```

becomes:

```text id="r7x3k1"
[3,2,4,5]
```

One of these two cases must contain the optimal solution.

---

# 🎯 Why Does This Guarantee the Optimal Answer?

Every valid solution falls into exactly one of these categories:

```text id="k4x8m2"
1. First house is robbed
2. First house is not robbed
```

If the first house is robbed, the last house cannot be robbed.

So the solution belongs to:

```text id="a9m3q7"
nums[:-1]
```

If the first house is not robbed, we can consider:

```text id="c2x7n4"
nums[1:]
```

Therefore, checking both cases covers every possible optimal solution.

---

# 📊 Complexity Analysis

Let:

```text id="q7m2x8"
n = len(nums)
```

The linear House Robber helper runs in:

```text id="1x9p4m"
O(n)
```

We run it twice:

```text id="7m3q8v"
O(n) + O(n)
```

which is still:

```text id="k5x1q9"
O(n)
```

### Time Complexity

```text id="m8q2x4"
O(n)
```

### Space Complexity

The DP itself uses only two variables:

```text id="p4x7m1"
O(1)
```

Therefore:

```text id="z9q3n6"
Time:  O(n)
Space: O(1)
```

> **Note:** Python slicing such as `nums[:-1]` and `nums[1:]` creates new lists, so the literal implementation shown above uses `O(n)` temporary space for the slices. If strict `O(1)` auxiliary space is required, pass index ranges to the helper instead of creating slices.

---

# 🔑 Key Concepts

This problem demonstrates:

* Dynamic Programming
* 1D DP
* Circular arrays
* Breaking a circular problem into linear cases
* State transitions
* Space optimization
* Subproblem decomposition
* `max()` optimization
* Avoiding adjacent selections

---

# 🧠 DP Pattern

The standard House Robber recurrence is:

```text id="s8m3x1"
dp[i] = max(
    dp[i-1],
    dp[i-2] + nums[i]
)
```

Meaning:

```text id="w5q9m2"
Skip current house → dp[i-1]

Rob current house  → dp[i-2] + nums[i]
```

For House Robber II, the circular constraint adds one extra layer:

```text id="p3x7n8"
Circular Array
      ↓
Two Cases
   ↙       ↘
Exclude   Exclude
Last      First
   ↓         ↓
Linear     Linear
Robber     Robber
   ↘       ↙
     max()
       ↓
    Answer
```

---

# 🎯 Key Takeaway

The biggest insight in **House Robber II** is not a complicated DP formula.

It is recognizing that:

> **A circular problem can be split into two linear problems.**

Because the first and last houses are adjacent:

```text id="v8m2x5"
Either:

Rob first → cannot rob last

OR:

Don't rob first → last can be considered
```

Therefore:

```text id="k3q7m1"
answer =
max(
    HouseRobber(nums[:-1]),
    HouseRobber(nums[1:])
)
```

And the linear House Robber problem itself uses:

```text id="n5x8q2"
current = max(
    previous,
    two_before + current_house
)
```

So the overall strategy is:

```text id="m7q2x9"
             House Robber II
                    ↓
             Houses in Circle
                    ↓
          ┌─────────┴─────────┐
          ↓                   ↓
   Exclude Last          Exclude First
          ↓                   ↓
    nums[:-1]              nums[1:]
          ↓                   ↓
    Linear DP              Linear DP
          ↓                   ↓
          └─────────┬─────────┘
                    ↓
                  max()
                    ↓
              Maximum Money
```

**Final complexity:**

```text id="q4m8x1"
Time  → O(n)
Space → O(1) DP space
```

This is the standard and efficient way to solve **LeetCode 213 — House Robber II**.
