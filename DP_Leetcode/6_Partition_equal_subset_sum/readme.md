# ⚖️ LeetCode 416 — Partition Equal Subset Sum

[![LeetCode](https://img.shields.io/badge/LeetCode-416-orange)](https://leetcode.com/problems/partition-equal-subset-sum/)

## 📌 Problem Overview

You are given an integer array `nums`.

The goal is to determine whether the array can be divided into **two subsets** such that the sum of the elements in both subsets is equal.

Return:

```text
true
```

if such a partition is possible, otherwise return:

```text
false
```

---

# 🧩 Problem Statement

Given:

```text
nums
```

we need to split its elements into two groups:

```text
Subset A
Subset B
```

such that:

```text
sum(Subset A) = sum(Subset B)
```

Every element must belong to one of the two subsets.

---

## 📥 Input

An integer array:

```text
nums
```

### Constraints

```text
1 ≤ nums.length ≤ 200
1 ≤ nums[i] ≤ 100
```

---

## 📤 Output

Return:

```text
true
```

if the array can be partitioned into two equal-sum subsets.

Otherwise:

```text
false
```

---

# 🧪 Example 1

```text
Input:
nums = [1,5,11,5]

Output:
true
```

The array can be divided into:

```text
[1,5,5] → 11

[11] → 11
```

Both subsets have the same sum.

Therefore:

```text
true
```

---

# 🧪 Example 2

```text
Input:
nums = [1,2,3,5]

Output:
false
```

Total sum:

```text
1 + 2 + 3 + 5 = 11
```

Since `11` is odd, it cannot be divided equally into two integer sums.

Therefore:

```text
false
```

---

# 🧠 Key Insight

At first, the problem looks like we need to explicitly construct two subsets.

We don't.

Instead, we can transform the problem into a **Subset Sum** problem.

Suppose the total sum is:

```text
totalSum
```

If two subsets have equal sums, then each subset must have:

```text
totalSum / 2
```

Therefore, the original problem becomes:

> **Can we select some elements from `nums` whose sum is exactly `totalSum / 2`?**

This is a classic **0/1 Knapsack / Subset Sum DP** problem.

---

# 1️⃣ Step 1 — Calculate Total Sum

First calculate:

```python
totalSum = sum(nums)
```

For:

```text
nums = [1,5,11,5]
```

we get:

```text
totalSum = 22
```

---

# 2️⃣ Step 2 — Check Whether the Sum Is Odd

If:

```text
totalSum % 2 != 0
```

then partitioning is impossible.

Why?

Because two equal integer sums must add up to an even number.

For example:

```text
9 / 2 = 4.5
```

There is no way to divide `9` into two equal integer subset sums.

Therefore:

```python
if totalSum % 2 != 0:
    return False
```

This is an important early exit.

---

# 3️⃣ Step 3 — Find the Target Sum

If the total sum is even:

```text
targetSum = totalSum / 2
```

In Python:

```python
targetSum = totalSum // 2
```

For:

```text
[1,5,11,5]
```

we have:

```text
totalSum = 22
targetSum = 11
```

Now the problem becomes:

> Can we find a subset whose sum is `11`?

If yes, the remaining elements automatically sum to `11`.

Therefore, the partition is possible.

---

# 💡 Why Finding One Subset Is Enough

Suppose:

```text
totalSum = 22
```

and we find a subset with:

```text
sum = 11
```

The remaining elements must have:

```text
22 - 11 = 11
```

Therefore:

```text
Subset A = 11
Subset B = 11
```

So we only need to find **one subset with the target sum**.

---

# 🧠 Dynamic Programming State

Create a boolean DP array:

```python
dp = [False] * (targetSum + 1)
```

Define:

```text
dp[s]
```

as:

> `True` if it is possible to form sum `s` using the numbers processed so far.

Otherwise:

```text
False
```

---

# 🏁 Base Case

The most important base case is:

```python
dp[0] = True
```

Why?

Because a sum of `0` is always possible by choosing **no elements**.

So initially:

```text
dp = [T,F,F,F,F,F,...]
```

where:

```text
T = True
F = False
```

---

# 🔄 DP Transition

Suppose the current number is:

```text
num
```

and we want to determine whether we can make:

```text
currSum
```

There are two choices.

### Option 1 — Don't Pick `num`

If `currSum` was already possible:

```text
dp[currSum] = True
```

we can keep it.

### Option 2 — Pick `num`

If we can already make:

```text
currSum - num
```

then adding `num` gives:

```text
(currSum - num) + num = currSum
```

Therefore:

```text
dp[currSum] = dp[currSum] OR dp[currSum - num]
```

In Python:

```python
dp[currSum] = dp[currSum] or dp[currSum - num]
```

---

# 🔥 Why Iterate Backwards?

This is one of the most important parts of the solution.

We iterate:

```python
for currSum in range(targetSum, num - 1, -1):
```

which means:

```text
targetSum → num
```

rather than:

```text
num → targetSum
```

### Why?

Because every number can be used **only once**.

This is a **0/1 Knapsack** problem.

Suppose:

```text
num = 5
```

If we iterate forward:

```text
5 → 6 → 7 → 8 → ...
```

we might accidentally use the same `5` multiple times during the same iteration.

For example:

```text
dp[5] = True
```

could immediately cause:

```text
dp[10] = True
```

using the same `5` again.

That would incorrectly treat one element as if it could be selected multiple times.

---

# 🔄 Reverse Iteration Prevents Reuse

By iterating backward:

```text
target → num
```

we ensure that the current number only uses states that existed **before processing the current number**.

Therefore:

```text
Each element → used at most once
```

This is exactly what we need for a 0/1 Knapsack problem.

---

# 📊 Example Walkthrough

Consider:

```text
nums = [1,5,11,5]
```

### Step 1 — Total Sum

```text
1 + 5 + 11 + 5 = 22
```

Since:

```text
22 % 2 = 0
```

partitioning is possible in principle.

---

### Step 2 — Target

```text
targetSum = 22 / 2 = 11
```

We need to determine whether a subset can make `11`.

---

### Step 3 — Initialize DP

Create:

```text
dp = [F,F,F,F,F,F,F,F,F,F,F,F]
```

Then:

```text
dp[0] = T
```

So:

```text
[T,F,F,F,F,F,F,F,F,F,F,F]
```

---

## Process `num = 1`

We iterate from:

```text
11 → 1
```

Since:

```text
dp[0] = True
```

we can form:

```text
1
```

Therefore:

```text
dp[1] = True
```

DP becomes:

```text
[T,T,F,F,F,F,F,F,F,F,F,F]
```

---

## Process `num = 5`

We can now form:

```text
5
```

and:

```text
1 + 5 = 6
```

Therefore:

```text
[T,T,F,F,F,T,T,F,F,F,F,F]
```

---

## Process `num = 11`

Since:

```text
dp[0] = True
```

we can form:

```text
11
```

So:

```text
dp[11] = True
```

At this point, we already know the answer is:

```text
true
```

because the subset:

```text
[11]
```

has sum `11`.

The remaining elements:

```text
[1,5,5]
```

also have sum `11`.

---

# 📋 DP State Table

For:

```text
nums = [1,5,11,5]
target = 11
```

we can visualize the important states as:

| Processed Number | Possible Important Sums         |
| ---------------- | ------------------------------- |
| Initial          | `0`                             |
| `1`              | `0, 1`                          |
| `5`              | `0, 1, 5, 6`                    |
| `11`             | `0, 1, 5, 6, 11`                |
| `5`              | Additional sums become possible |

The moment:

```text
dp[11] = True
```

we have found a valid partition.

---

# 🔍 Algorithm

1. Calculate the total sum.
2. If the total sum is odd, return `False`.
3. Set:

```text
targetSum = totalSum / 2
```

4. Create a boolean DP array of size `targetSum + 1`.
5. Set:

```text
dp[0] = True
```

6. For every number `num`:

   * Iterate `currSum` backward from `targetSum` to `num`.
   * Update:

```text
dp[currSum] =
    dp[currSum] OR dp[currSum - num]
```

7. Return:

```text
dp[targetSum]
```

---

# 💻 Python 3 Solution

```python
class Solution:
    def canPartition(self, nums):

        totalSum = sum(nums)

        # Equal partition is impossible
        # if total sum is odd.
        if totalSum % 2 != 0:
            return False

        targetSum = totalSum // 2

        # dp[s] = True if sum s is possible
        dp = [False] * (targetSum + 1)

        # Sum 0 is always possible
        dp[0] = True

        for num in nums:

            # Iterate backwards so each number
            # is used at most once.
            for currSum in range(targetSum, num - 1, -1):

                dp[currSum] = (
                    dp[currSum]
                    or dp[currSum - num]
                )

        return dp[targetSum]
```

---

# 🧩 Code Breakdown

## Calculate Total

```python
totalSum = sum(nums)
```

This tells us whether an equal partition is even possible.

---

## Odd Sum Check

```python
if totalSum % 2 != 0:
    return False
```

An odd number cannot be split into two equal integers.

---

## Target

```python
targetSum = totalSum // 2
```

We only need to find one subset with this sum.

---

## DP Array

```python
dp = [False] * (targetSum + 1)
```

For example, if:

```text
targetSum = 11
```

then:

```text
dp = [
    False, False, False, ..., False
]
```

There are `12` positions:

```text
0 → 11
```

---

## Base Case

```python
dp[0] = True
```

Sum `0` is achievable without selecting any elements.

---

## Process Every Number

```python
for num in nums:
```

Each number is considered exactly once.

---

## Reverse Traversal

```python
for currSum in range(targetSum, num - 1, -1):
```

This is what makes the algorithm a **0/1 Knapsack** solution.

Each number can be:

```text
Used once
```

or:

```text
Not used
```

but never used multiple times.

---

## Update DP

```python
dp[currSum] = dp[currSum] or dp[currSum - num]
```

This means:

```text
Can I already make currSum?
          OR
Can I make currSum - num and then add num?
```

If either is true:

```text
dp[currSum] = True
```

---

# 🧠 Visual DP Transition

For a number `num`:

```text
                    currSum
                       ↑
                       |
                 Can we make it?
                    /       \
                  NO        YES
                  /           \
                 /             \
currSum - num possible?       Already possible
        |
        ↓
      Add num
        |
        ↓
   currSum possible
```

Mathematically:

```text
dp[s] = dp[s] OR dp[s-num]
```

---

# 🚫 Why Forward Iteration Is Wrong

Suppose:

```text
nums = [5]
target = 10
```

Initially:

```text
dp[0] = True
```

If we iterate **forward**:

```text
5 → 10
```

At `5`:

```text
dp[5] = dp[5] or dp[0]
      = True
```

Then when we reach `10`:

```text
dp[10] = dp[10] or dp[5]
       = True
```

We have incorrectly concluded:

```text
5 + 5 = 10
```

But there is only **one `5`** in the array.

The same element was effectively used twice.

---

# ✅ Why Backward Iteration Is Correct

Instead:

```text
10 → 5
```

When calculating `dp[10]`, the value `dp[5]` has not yet been updated using the current `5`.

So the current number cannot reuse itself.

This guarantees:

```text
One element → At most one use
```

Therefore, for subset-sum / 0/1 knapsack problems, remember:

```text
➡️ 0/1 Knapsack → iterate backwards
```

---

# 🆚 0/1 Knapsack vs Unbounded Knapsack

This distinction is important.

### 0/1 Knapsack

Each item can be used once:

```text
Item → take or skip
```

Therefore:

```text
Iterate backwards
```

### Unbounded Knapsack

An item can be used multiple times.

Therefore:

```text
Iterate forwards
```

For this problem:

```text
Partition Equal Subset Sum
        ↓
0/1 Knapsack
        ↓
Backward iteration
```

---

# 🧠 Why This Is a Knapsack Problem

Traditional 0/1 Knapsack asks:

> Which items should I select without exceeding a capacity?

Here the question is slightly different:

> Can I select some numbers whose sum is exactly the target?

The structure is still the same:

```text
Items → nums
Capacity → targetSum
Choice → take / don't take
Goal → reach exact target
```

So this is essentially a **Subset Sum version of 0/1 Knapsack**.

---

# 🔬 Correctness Intuition

If the total sum is even:

```text
totalSum = 2 × targetSum
```

If we can find a subset whose sum is:

```text
targetSum
```

then the remaining elements have sum:

```text
totalSum - targetSum
=
2 × targetSum - targetSum
=
targetSum
```

Therefore both subsets have equal sums.

Conversely, if the array can be partitioned into two equal-sum subsets, each subset must have sum:

```text
targetSum
```

So finding a subset with sum `targetSum` is both **necessary and sufficient**.

---

# 📌 Example: Impossible Case

Consider:

```text
nums = [1,2,3,5]
```

Total:

```text
1 + 2 + 3 + 5 = 11
```

Since:

```text
11 % 2 != 0
```

we immediately return:

```text
False
```

No DP is necessary.

This is an example of using a mathematical observation to eliminate unnecessary computation.

---

# 📌 Example: Possible Case

Consider:

```text
nums = [1,5,11,5]
```

Total:

```text
22
```

Target:

```text
11
```

Possible subset:

```text
[11]
```

Remaining:

```text
[1,5,5]
```

Both sum to:

```text
11
```

Therefore:

```text
True
```

---

# ⚙️ Complexity Analysis

Let:

```text
n = len(nums)
```

and:

```text
T = targetSum
```

For every number, we iterate through the possible sums from `T` down to `num`.

Therefore:

### Time Complexity

```text
O(n × targetSum)
```

### Space Complexity

We use a single DP array of size:

```text
targetSum + 1
```

Therefore:

```text
O(targetSum)
```

Final:

```text
Time:  O(n × targetSum)
Space: O(targetSum)
```

Given:

```text
n ≤ 200
nums[i] ≤ 100
```

the maximum total sum is:

```text
200 × 100 = 20,000
```

so:

```text
targetSum ≤ 10,000
```

which makes the DP approach practical.

---

# 🧠 How to Recognize This DP Pattern

When you see a problem involving:

* Selecting elements from an array
* Each element can be selected or skipped
* A target sum
* Asking whether an exact sum is possible
* Every element can be used at most once

think:

```text
0/1 Knapsack
```

Then define:

```text
dp[s]
```

as:

> Can I form sum `s`?

Initialize:

```text
dp[0] = True
```

Transition:

```text
dp[s] = dp[s] OR dp[s-num]
```

And most importantly:

```text
for s in range(target, num - 1, -1)
```

**Iterate backward.**

---

# 🔑 DP Pattern Summary

```text
             Partition Problem
                    ↓
             Total Sum = S
                    ↓
          Is S odd or even?
              ↙         ↘
           Odd          Even
            ↓             ↓
         False        Target = S/2
                          ↓
                    Subset Sum
                          ↓
                   0/1 Knapsack
                          ↓
                 dp[0] = True
                          ↓
                 Process each num
                          ↓
                Iterate backwards
                          ↓
            dp[s] |= dp[s - num]
                          ↓
                  dp[target]?
                   ↙       ↘
                True       False
                  ↓           ↓
                True        False
```

---

# 🎯 Key Takeaways

### 1. Convert Partition Into Subset Sum

Instead of explicitly finding two subsets:

```text
Equal Partition
       ↓
Find one subset with sum = total / 2
```

---

### 2. Odd Total Means Impossible

```python
if totalSum % 2 != 0:
    return False
```

This is the fastest possible check.

---

### 3. `dp[0] = True`

An empty subset can always produce sum `0`.

---

### 4. Reverse Iteration Matters

```python
for currSum in range(targetSum, num - 1, -1):
```

This prevents using the same element more than once.

---

### 5. The Core Transition

```python
dp[currSum] = dp[currSum] or dp[currSum - num]
```

Meaning:

```text
Don't take num
       OR
Take num
```

---

### 6. Final State

```python
dp[targetSum]
```

answers the question:

> Can we form a subset whose sum is exactly half of the total?

If yes:

```text
Partition possible → True
```

Otherwise:

```text
Partition impossible → False
```

---

# 🏆 Final Solution

```python
class Solution:
    def canPartition(self, nums):

        totalSum = sum(nums)

        if totalSum % 2 != 0:
            return False

        targetSum = totalSum // 2

        dp = [False] * (targetSum + 1)
        dp[0] = True

        for num in nums:
            for currSum in range(targetSum, num - 1, -1):
                dp[currSum] = dp[currSum] or dp[currSum - num]

        return dp[targetSum]
```

### Complexity

```text
Time:  O(n × targetSum)
Space: O(targetSum)
```

The core pattern to remember is:

```text
Equal Partition
      ↓
Half of Total
      ↓
Subset Sum
      ↓
0/1 Knapsack
      ↓
1D Boolean DP
      ↓
Backward Iteration
```
