# 🪙 LeetCode 518 — Coin Change II

[![LeetCode](https://img.shields.io/badge/LeetCode-518-orange)](https://leetcode.com/problems/coin-change-ii/)

## 📌 Problem Overview

You are given:

* An integer array `coins`, where each value represents a different coin denomination.
* An integer `amount`, representing the target amount.

Your task is to find the **number of different combinations** of coins that can make exactly `amount`.

You have an **infinite supply** of every coin denomination.

If the amount cannot be formed, return:

```text
0
```

The order of coins **does not matter**.

For example:

```text
2 + 1 + 2
```

and:

```text
1 + 2 + 2
```

represent the **same combination**.

---

# 🧩 Problem Statement

Given:

```text
coins = [1,2,5]
amount = 5
```

the possible combinations are:

```text
5
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1
```

Therefore:

```text
Answer = 4
```

---

## 📥 Input

Two values:

```text
amount
coins
```

### Constraints

```text
1 ≤ coins.length ≤ 300
1 ≤ coins[i] ≤ 5000
0 ≤ amount ≤ 5000
```

All coin values are unique.

The final answer fits inside a signed 32-bit integer.

---

## 📤 Output

Return the number of **different combinations** that can produce `amount`.

If no combination exists:

```text
0
```

---

# 🧪 Example 1

```text
Input:
amount = 5
coins = [1,2,5]

Output:
4
```

The four combinations are:

```text
5

2 + 2 + 1

2 + 1 + 1 + 1

1 + 1 + 1 + 1 + 1
```

---

# 🧪 Example 2

```text
Input:
amount = 3
coins = [2]

Output:
0
```

There is no combination of `2`s that can produce `3`.

---

# 🧪 Example 3

```text
Input:
amount = 10
coins = [10]

Output:
1
```

The only possible combination is:

```text
10
```

Therefore:

```text
Answer = 1
```

---

# 🧠 Intuition

This is a classic **Unbounded Knapsack** problem.

The key difference from **LeetCode 322 — Coin Change** is that we are not asking:

> What is the minimum number of coins?

Instead, we are asking:

> **How many different combinations of coins can produce the target amount?**

For every coin, we can use it:

```text
0 times
1 time
2 times
3 times
...
```

because we have an unlimited supply.

Therefore, this is an **Unbounded Knapsack counting problem**.

---

# 🔥 The Most Important Difference

Compare the two Coin Change problems:

### Coin Change — LeetCode 322

Question:

```text
What is the minimum number of coins?
```

DP stores:

```text
dp[amount] = minimum number of coins
```

Transition:

```text
dp[a] = min(dp[a], 1 + dp[a - coin])
```

---

### Coin Change II — LeetCode 518

Question:

```text
How many combinations exist?
```

DP stores:

```text
dp[amount] = number of combinations
```

Transition:

```text
dp[a] += dp[a - coin]
```

This difference is extremely important.

---

# 💡 DP State

We use a one-dimensional array:

```python
C = [0] * (amount + 1)
```

Define:

```text
C[a]
```

as:

> The number of combinations that can make amount `a` using the coins processed so far.

For example:

```text
C[5] = 4
```

means:

> There are 4 combinations that can make amount 5.

---

# 🏁 Base Case

The most important initialization is:

```python
C[0] = 1
```

Why `1`?

There is exactly **one way** to make amount `0`:

```text
Choose nothing
```

This may initially seem strange, but it is essential for the recurrence to work.

For example, if:

```text
coin = 5
```

then:

```text
C[5] += C[5 - 5]
```

which becomes:

```text
C[5] += C[0]
```

Since:

```text
C[0] = 1
```

we correctly count:

```text
5
```

as one valid combination.

---

# 🔄 DP Transition

For every coin:

```text
coin
```

we iterate through amounts from:

```text
coin → amount
```

For every amount `a`:

```python
C[a] += C[a - coin]
```

Why?

Suppose:

```text
a = 5
coin = 2
```

Then:

```text
5 - 2 = 3
```

Every combination that makes `3` can be extended by adding one `2`.

Therefore:

```text
ways to make 5
=
ways already known
+
ways to make 3 and add 2
```

So:

```text
C[5] += C[3]
```

---

# 🧠 Visualizing the Transition

Suppose:

```text
coin = 2
amount = 5
```

To make `5` using a `2`:

```text
        5
        ↓
   Remove one 2
        ↓
        3
        ↓
  Make amount 3
        ↓
    Add coin 2
        ↓
        5
```

Therefore:

```text
C[5] += C[3]
```

The DP state represents all combinations that can be extended with the current coin.

---

# 🔥 Why Is the Coin Loop Outside?

The implementation is:

```python
for coin in coins:
    for a in range(coin, amount + 1):
        C[a] += C[a - coin]
```

The order of these loops is **critical**.

The coin loop comes first:

```text
Coin 1
 ↓
Coin 2
 ↓
Coin 5
```

and then we process all amounts for that coin.

This ensures that each combination is counted **only once**, regardless of the order in which its coins appear.

---

# 🚨 Why Loop Order Matters

Suppose:

```text
coins = [1,2]
amount = 3
```

The valid combinations are:

```text
1 + 1 + 1
1 + 2
```

Answer:

```text
2
```

We do **not** want to separately count:

```text
2 + 1
```

because:

```text
1 + 2
```

and:

```text
2 + 1
```

are the same combination.

---

# ❌ What Happens If Amount Is the Outer Loop?

If we wrote:

```python
for a in range(1, amount + 1):
    for coin in coins:
        ...
```

we could count different **orders** of the same coins as separate solutions.

That changes the problem from:

```text
Combinations
```

to:

```text
Permutations / ordered sequences
```

which is incorrect.

---

# ✅ Correct Loop Structure

Use:

```python
for coin in coins:
    for a in range(coin, amount + 1):
        C[a] += C[a - coin]
```

This means:

```text
Process coin 1 completely
        ↓
Process coin 2 completely
        ↓
Process coin 5 completely
```

Each combination gets constructed in a consistent coin order.

Therefore:

```text
1 + 2
```

is counted once, and:

```text
2 + 1
```

is not counted separately.

---

# 🧠 Combinations vs Permutations

This is one of the most important concepts in this problem.

### Combination

Order doesn't matter.

```text
1 + 2 + 2
```

is the same as:

```text
2 + 1 + 2
```

and:

```text
2 + 2 + 1
```

All represent:

```text
{1,2,2}
```

So they count as **one combination**.

---

### Permutation

Order matters.

```text
1 + 2
```

and:

```text
2 + 1
```

would be considered different.

Coin Change II asks for:

```text
Combinations
```

not permutations.

---

# 📊 Example Walkthrough

Consider:

```text
coins = [1,2,5]
amount = 5
```

Initialize:

```text
C = [1,0,0,0,0,0]
```

The first value is `1` because:

```text
C[0] = 1
```

---

## 🪙 Process Coin = 1

We can use coin `1` any number of times.

After processing:

```text
C = [1,1,1,1,1,1]
```

There is exactly one combination for every amount:

```text
0
1
1+1
1+1+1
...
```

---

## 🪙 Process Coin = 2

Now we add combinations that use coin `2`.

For amount `2`:

```text
C[2] += C[0]
```

So:

```text
C[2] = 2
```

The combinations are:

```text
1 + 1
2
```

---

For amount `3`:

```text
C[3] += C[1]
```

So:

```text
C[3] = 2
```

The combinations are:

```text
1 + 1 + 1
1 + 2
```

---

For amount `4`:

```text
C[4] += C[2]
```

Since:

```text
C[2] = 2
```

we get:

```text
C[4] = 3
```

The combinations are:

```text
1 + 1 + 1 + 1
1 + 1 + 2
2 + 2
```

---

For amount `5`:

```text
C[5] += C[3]
```

Since:

```text
C[3] = 2
```

we get:

```text
C[5] = 3
```

The combinations currently are:

```text
1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 2
1 + 2 + 2
```

---

## 🪙 Process Coin = 5

For amount `5`:

```text
C[5] += C[0]
```

Since:

```text
C[0] = 1
```

we get:

```text
C[5] = 4
```

The new combination is:

```text
5
```

Therefore the final answer is:

```text
4
```

---

# 📋 DP Evolution

For:

```text
coins = [1,2,5]
amount = 5
```

| Stage          | DP Array        |
| -------------- | --------------- |
| Initial        | `[1,0,0,0,0,0]` |
| After coin `1` | `[1,1,1,1,1,1]` |
| After coin `2` | `[1,1,2,2,3,3]` |
| After coin `5` | `[1,1,2,2,3,4]` |

Therefore:

```text
C[5] = 4
```

---

# 🧠 Why `C[0] = 1`?

This deserves special attention.

Suppose:

```text
coins = [5]
amount = 5
```

Initially:

```text
C[0] = 1
```

When processing coin `5`:

```python
C[5] += C[5 - 5]
```

which becomes:

```text
C[5] += C[0]
```

Therefore:

```text
C[5] += 1
```

This represents the combination:

```text
5
```

If we incorrectly initialized:

```text
C[0] = 0
```

then:

```text
C[5] += C[0]
```

would add nothing, and we would fail to count the basic combination.

So:

```text
C[0] = 1
```

is not arbitrary.

It represents the **empty combination**, which acts as the foundation for constructing every other combination.

---

# 🔁 Why Can Coins Be Reused?

The problem gives us an unlimited supply of every coin.

When processing:

```text
coin = 2
```

we iterate forward:

```text
2 → 3 → 4 → 5 → ...
```

So a newly updated state can be used again.

For example:

```text
C[2]
```

can help calculate:

```text
C[4]
```

which can help calculate:

```text
C[6]
```

This naturally allows:

```text
2
2 + 2
2 + 2 + 2
...
```

Therefore, this is an **unbounded** problem.

---

# 🆚 Coin Change vs Coin Change II

These two problems look almost identical but have completely different DP objectives.

| Problem      | Goal                   | DP Meaning               |
| ------------ | ---------------------- | ------------------------ |
| LeetCode 322 | Minimum coins          | `dp[a] = minimum coins`  |
| LeetCode 518 | Number of combinations | `dp[a] = number of ways` |

### Coin Change

```python
dp[a] = min(dp[a], 1 + dp[a - coin])
```

### Coin Change II

```python
C[a] += C[a - coin]
```

This is a major DP pattern:

> **The recurrence depends on what the problem is asking you to optimize or count.**

---

# 🆚 Coin Change II vs Partition Equal Subset Sum

Both use knapsack-style DP, but their state types differ.

### Partition Equal Subset Sum

```text
Question:
Can this sum be formed?
```

DP:

```text
True / False
```

Transition:

```text
dp[s] |= dp[s-num]
```

Each element is used once.

---

### Coin Change II

```text
Question:
How many ways can this sum be formed?
```

DP:

```text
Number of combinations
```

Transition:

```text
dp[a] += dp[a-coin]
```

Coins can be used unlimited times.

---

# 🧩 Algorithm

1. Create a DP array of size `amount + 1`.
2. Set:

```text
C[0] = 1
```

3. Process every coin one by one.
4. For each coin, iterate from `coin` through `amount`.
5. Update:

```text
C[a] += C[a - coin]
```

6. Return:

```text
C[amount]
```

---

# 💻 Python 3 Solution

```python
class Solution:
    def change(self, amount, coins):

        # C[a] = number of combinations
        # that make amount a
        C = [0] * (amount + 1)

        # One way to make amount 0:
        # choose no coins.
        C[0] = 1

        # Process each coin
        for coin in coins:

            # Forward iteration allows
            # unlimited reuse of the coin.
            for a in range(coin, amount + 1):

                C[a] += C[a - coin]

        return C[amount]
```

---

# 🔍 Code Breakdown

## Step 1 — Initialize DP

```python
C = [0] * (amount + 1)
```

We create one state for every amount from:

```text
0 → amount
```

---

## Step 2 — Base Case

```python
C[0] = 1
```

There is one way to create amount `0`:

```text
Choose nothing
```

---

## Step 3 — Process Coins

```python
for coin in coins:
```

We process each denomination separately.

This is what ensures combinations are counted without considering different orderings as separate answers.

---

## Step 4 — Iterate Forward

```python
for a in range(coin, amount + 1):
```

Forward iteration allows the current coin to be reused.

---

## Step 5 — Count New Combinations

```python
C[a] += C[a - coin]
```

Every way of making:

```text
a - coin
```

can become a way of making:

```text
a
```

by adding the current coin.

---

# 🔬 Correctness Intuition

Consider a fixed coin `coin`.

For every amount `a`, every combination that makes:

```text
a - coin
```

can be extended by adding one `coin`.

Therefore:

```text
C[a - coin]
```

new combinations can make `a`.

So:

```text
C[a] += C[a - coin]
```

is correct.

Because coins are processed one denomination at a time, each unordered combination has exactly one construction order in the DP.

Therefore, no duplicate permutations are counted.

---

# 🚨 The Critical Pattern

For **Coin Change II**, remember:

```text
for coin in coins:
    for amount in range(coin, target + 1):
```

Not:

```text
for amount in range(1, target + 1):
    for coin in coins:
```

The first version counts:

```text
COMBINATIONS
```

while the second structure can count:

```text
ORDERED SEQUENCES
```

which is a different problem.

---

# ⚙️ Complexity Analysis

Let:

```text
n = len(coins)
A = amount
```

We process every coin against every amount.

### Time Complexity

```text
O(n × A)
```

or:

```text
O(len(coins) × amount)
```

### Space Complexity

We use a single DP array of size:

```text
A + 1
```

Therefore:

```text
O(A)
```

Final:

```text
Time:  O(len(coins) × amount)
Space: O(amount)
```

Given:

```text
len(coins) ≤ 300
amount ≤ 5000
```

the DP approach is efficient enough.

---

# 📌 Edge Cases

## 1. Amount = 0

```text
coins = [1,2,5]
amount = 0
```

There is exactly one combination:

```text
Choose nothing
```

Therefore:

```text
Answer = 1
```

---

## 2. Impossible Amount

```text
coins = [2]
amount = 3
```

No combination exists.

Therefore:

```text
Answer = 0
```

---

## 3. Exact Coin

```text
coins = [10]
amount = 10
```

Only:

```text
10
```

is possible.

Therefore:

```text
Answer = 1
```

---

## 4. Multiple Coin Orders

For:

```text
coins = [1,2]
amount = 3
```

we have:

```text
1 + 1 + 1
1 + 2
```

We do **not** count:

```text
2 + 1
```

separately.

Therefore:

```text
Answer = 2
```

---

# 🧠 How to Recognize This DP Pattern

When you see:

* A target amount
* A collection of denominations/items
* Unlimited use of each item
* Need to count the number of ways
* Order does not matter

think:

```text
Unbounded Knapsack
        +
Counting DP
```

The typical structure is:

```python
dp[0] = 1

for item in items:
    for target in range(item, amount + 1):
        dp[target] += dp[target - item]
```

---

# 🎯 Pattern Recognition

```text
                    Target Sum
                        ↓
              Unlimited Items?
                    ↙     ↘
                  Yes      No
                   ↓        ↓
             Unbounded    0/1
              Knapsack   Knapsack
                   ↓
             What is asked?
              ↙         ↘
          Minimum       Count
             ↓            ↓
       Coin Change    Coin Change II
```

---

# 🔑 Key Takeaways

### 1. DP State

```text
C[a] = number of combinations to make a
```

---

### 2. Base Case

```python
C[0] = 1
```

---

### 3. Core Transition

```python
C[a] += C[a - coin]
```

---

### 4. Unlimited Coins

The same coin can be used repeatedly.

Therefore, we iterate amounts **forward**.

---

### 5. Coin Loop Comes First

```python
for coin in coins:
```

This ensures that different orders of the same coins are not counted separately.

---

### 6. Combinations ≠ Permutations

```text
1 + 2
```

and:

```text
2 + 1
```

are the same combination.

The loop ordering prevents duplicate counting.

---

# 🏆 Final Solution

```python
class Solution:
    def change(self, amount, coins):

        C = [0] * (amount + 1)

        C[0] = 1

        for coin in coins:
            for a in range(coin, amount + 1):
                C[a] += C[a - coin]

        return C[amount]
```

### Complexity

```text
Time:  O(amount × len(coins))
Space: O(amount)
```

---

# 🚀 Final Mental Model

When solving **Coin Change II**, think:

```text
                  Target Amount
                       ↓
             How many ways exist?
                       ↓
                Choose a coin
                       ↓
             Remaining amount
              = amount - coin
                       ↓
          Count ways for remaining
                       ↓
             dp[amount - coin]
                       ↓
          Add those combinations
                       ↓
             dp[amount] +=
             dp[amount - coin]
```

The two formulas to keep separate are:

### Minimum Coins — LeetCode 322

```text
dp[a] = min(dp[a], 1 + dp[a - coin])
```

### Number of Combinations — LeetCode 518

```text
dp[a] += dp[a - coin]
```

And for Coin Change II, the critical loop pattern is:

```text
for coin in coins:
    for amount in increasing_order:
```

That combination of **counting DP + unbounded reuse + coin-first iteration** is the core pattern behind the solution.
