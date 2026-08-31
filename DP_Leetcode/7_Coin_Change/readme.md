# 🪙 LeetCode 322 — Coin Change

[![LeetCode](https://img.shields.io/badge/LeetCode-322-orange)](https://leetcode.com/problems/coin-change/)

## 📌 Problem Overview

You are given:

* An integer array `coins`, where each value represents a coin denomination.
* An integer `amount`, representing the total amount of money you need to make.

Your task is to find the **minimum number of coins** required to make exactly `amount`.

You have an **unlimited supply** of every coin denomination.

If the amount cannot be formed using the given coins, return:

```text
-1
```

---

# 🧩 Problem Statement

Given:

```text
coins
amount
```

find the smallest number of coins whose values add up exactly to:

```text
amount
```

A coin can be used **any number of times**.

For example:

```text
coins = [1, 2, 5]
amount = 11
```

The optimal solution is:

```text
5 + 5 + 1 = 11
```

which uses:

```text
3 coins
```

Therefore:

```text
Answer = 3
```

---

## 📥 Input

An integer array:

```text
coins
```

and an integer:

```text
amount
```

### Constraints

```text
1 ≤ coins.length ≤ 12
1 ≤ coins[i] ≤ 2³¹ - 1
0 ≤ amount ≤ 10⁴
```

---

## 📤 Output

Return the **minimum number of coins** needed to make `amount`.

If it is impossible:

```text
return -1
```

---

# 🧪 Example 1

```text
Input:
coins = [1,2,5]
amount = 11

Output:
3
```

Explanation:

```text
11 = 5 + 5 + 1
```

Number of coins:

```text
3
```

---

# 🧪 Example 2

```text
Input:
coins = [2]
amount = 3

Output:
-1
```

It is impossible to make `3` using only coins of value `2`.

---

# 🧪 Example 3

```text
Input:
coins = [1]
amount = 0

Output:
0
```

No coins are needed to make amount `0`.

---

# 🧠 Intuition

This is a classic **Dynamic Programming** problem.

The main question is:

> What is the minimum number of coins needed to make every amount from `0` to `amount`?

Instead of trying every possible combination recursively, we build the answer from smaller amounts.

For example, if we already know the minimum number of coins needed to make:

```text
amount = 6
```

then we can use a coin `5` to form:

```text
6 = 5 + 1
```

So if:

```text
dp[1] = 1
```

then:

```text
dp[6] = 1 + dp[1]
      = 2
```

This leads directly to our DP recurrence.

---

# 💡 Dynamic Programming State

Define:

```text
dp[i]
```

as:

> The minimum number of coins required to make exactly amount `i`.

For example:

```text
dp[0] = 0
```

means:

```text
0 coins are required to make amount 0.
```

If we have:

```text
coins = [1,2,5]
```

then eventually:

```text
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 1
...
```

---

# 🏁 Base Case

The most important base case is:

```python
dp[0] = 0
```

Why?

Because making an amount of `0` requires no coins.

---

# ♾️ Initialization

Initially, we don't know how many coins are required for each amount.

So we initialize every value to infinity:

```python
dp = [float('inf')] * (amount + 1)
```

For example, if:

```text
amount = 5
```

we get:

```text
[∞, ∞, ∞, ∞, ∞, ∞]
```

Then:

```python
dp[0] = 0
```

becomes:

```text
[0, ∞, ∞, ∞, ∞, ∞]
```

`∞` represents:

> We currently don't know a way to make this amount.

---

# 🔄 DP Transition

Suppose the current amount is:

```text
i
```

and the current coin is:

```text
coin
```

If:

```text
coin <= i
```

we can use that coin.

After using it, the remaining amount is:

```text
i - coin
```

We already know the best solution for that smaller amount:

```text
dp[i - coin]
```

Adding the current coin requires one additional coin:

```text
1 + dp[i - coin]
```

Therefore:

```text
dp[i] = min(dp[i], 1 + dp[i - coin])
```

This is the core recurrence.

---

# 🧠 Visualizing the Transition

Suppose:

```text
i = 11
coin = 5
```

Then:

```text
11
↓
Use coin 5
↓
Remaining amount = 6
```

If:

```text
dp[6] = 2
```

then:

```text
dp[11] = 1 + dp[6]
       = 3
```

Visually:

```text
        Amount 11
            ↓
       Choose coin 5
            ↓
       Remaining 6
            ↓
         dp[6] = 2
            ↓
       + current coin
            ↓
         1 + 2
            ↓
         dp[11] = 3
```

---

# 🔁 Why Bottom-Up DP?

We calculate amounts in increasing order:

```text
0 → 1 → 2 → 3 → ... → amount
```

When calculating:

```text
dp[i]
```

the smaller value:

```text
dp[i - coin]
```

has already been calculated.

Therefore, we can build the solution progressively.

This is called:

```text
Bottom-Up Dynamic Programming
```

or:

```text
Tabulation
```

---

# 📊 Example Walkthrough

Consider:

```text
coins = [1,2,5]
amount = 5
```

We create:

```text
dp = [∞,∞,∞,∞,∞,∞]
```

Set:

```text
dp[0] = 0
```

So:

```text
dp = [0,∞,∞,∞,∞,∞]
```

---

## Amount = 1

Using coin `1`:

```text
dp[1] = min(∞, 1 + dp[0])
      = 1
```

Now:

```text
[0,1,∞,∞,∞,∞]
```

---

## Amount = 2

Using coin `1`:

```text
dp[2] = 1 + dp[1]
      = 2
```

Using coin `2`:

```text
dp[2] = 1 + dp[0]
      = 1
```

Take the minimum:

```text
dp[2] = 1
```

Now:

```text
[0,1,1,∞,∞,∞]
```

---

## Amount = 3

Using coin `1`:

```text
1 + dp[2] = 2
```

Using coin `2`:

```text
1 + dp[1] = 2
```

Therefore:

```text
dp[3] = 2
```

Now:

```text
[0,1,1,2,∞,∞]
```

---

## Amount = 4

Using coin `1`:

```text
1 + dp[3] = 3
```

Using coin `2`:

```text
1 + dp[2] = 2
```

Therefore:

```text
dp[4] = 2
```

Now:

```text
[0,1,1,2,2,∞]
```

---

## Amount = 5

Using coin `1`:

```text
1 + dp[4] = 3
```

Using coin `2`:

```text
1 + dp[3] = 3
```

Using coin `5`:

```text
1 + dp[0] = 1
```

Therefore:

```text
dp[5] = 1
```

Final:

```text
[0,1,1,2,2,1]
```

So:

```text
Answer = dp[5] = 1
```

The optimal solution is simply:

```text
5
```

---

# 📋 DP Table

For:

```text
coins = [1,2,5]
amount = 5
```

| Amount | Best Combination | Minimum Coins |
| -----: | ---------------- | ------------: |
|    `0` | Nothing          |           `0` |
|    `1` | `1`              |           `1` |
|    `2` | `2`              |           `1` |
|    `3` | `1 + 2`          |           `2` |
|    `4` | `2 + 2`          |           `2` |
|    `5` | `5`              |           `1` |

Final:

```text
dp[5] = 1
```

---

# 🚫 Why Greedy Does Not Always Work

A common mistake is to always choose the largest possible coin.

For example:

```text
coins = [1,3,4]
amount = 6
```

A greedy strategy chooses:

```text
4 + 1 + 1
```

which uses:

```text
3 coins
```

But the optimal solution is:

```text
3 + 3
```

which uses only:

```text
2 coins
```

Therefore:

> Choosing the largest coin at every step does not guarantee the minimum number of coins.

Dynamic Programming considers all possible coin choices and keeps the minimum.

---

# 🧠 Why This Is an Unbounded Knapsack Problem

Coin Change has an important property:

> **Each coin can be used unlimited times.**

For example, if:

```text
coins = [2]
```

we can use:

```text
2
2 + 2
2 + 2 + 2
...
```

There is no restriction on how many times a coin can be selected.

This makes Coin Change related to the:

```text
Unbounded Knapsack
```

pattern.

Compare:

### 0/1 Knapsack

Each item can be used at most once:

```text
Item → Take OR Skip
```

### Unbounded Knapsack

Each item can be used multiple times:

```text
Item → Use again if useful
```

Coin Change belongs to the second category.

---

# 🔄 0/1 vs Unbounded Knapsack

This distinction is important when deciding loop direction.

### 0/1 Knapsack

Usually iterate sums **backward**:

```text
target → item
```

because each item can be used once.

### Unbounded Knapsack

We can allow repeated use.

A forward sum iteration can therefore be used in appropriate formulations:

```text
item → target
```

However, this particular solution uses:

```text
for amount:
    for coin:
```

so loop direction is not the main issue. The increasing `amount` loop ensures that:

```text
dp[i - coin]
```

has already been computed and can itself represent solutions using the same coin multiple times.

---

# 🧠 Why Does the Amount Loop Allow Unlimited Coins?

Consider:

```text
coins = [2]
amount = 6
```

When calculating:

```text
dp[2]
```

we get:

```text
dp[2] = 1
```

Then when calculating:

```text
dp[4]
```

we use:

```text
dp[4 - 2]
=
dp[2]
```

Therefore:

```text
dp[4] = 1 + dp[2]
      = 2
```

Then:

```text
dp[6] = 1 + dp[4]
      = 3
```

So:

```text
6 = 2 + 2 + 2
```

The previously computed states naturally allow the same denomination to be reused.

---

# 🚫 Impossible Amounts

Consider:

```text
coins = [2]
amount = 3
```

There is no combination of `2`s that equals `3`.

During DP:

```text
dp[0] = 0
dp[1] = ∞
dp[2] = 1
dp[3] = ∞
```

Therefore:

```text
dp[3] = ∞
```

This means the amount cannot be formed.

So we return:

```text
-1
```

---

# 🔍 Handling the Impossible Case

The implementation checks:

```python
return dp[amount] if dp[amount] != float('inf') else -1
```

If:

```text
dp[amount] == ∞
```

then no combination of the available coins can produce the required amount.

Therefore:

```text
∞ → -1
```

---

# 🧩 Algorithm

1. Create a DP array of size `amount + 1`.
2. Initialize every state to infinity.
3. Set:

```text
dp[0] = 0
```

4. For every amount from `1` to `amount`:

   * Try every coin.
   * If the coin can be used:

```text
i - coin >= 0
```

* Update:

```text
dp[i] = min(dp[i], 1 + dp[i - coin])
```

5. After processing all amounts:

   * If `dp[amount]` is finite, return it.
   * Otherwise return `-1`.

---

# 💻 Python 3 Solution

```python
class Solution:
    def coinChange(self, coins, amount):

        # dp[i] = minimum coins needed
        # to make amount i
        dp = [float('inf')] * (amount + 1)

        # Base case
        dp[0] = 0

        # Build answers from 1 to amount
        for i in range(1, amount + 1):

            for coin in coins:

                if i - coin >= 0:

                    dp[i] = min(
                        dp[i],
                        1 + dp[i - coin]
                    )

        # If amount is still unreachable
        if dp[amount] == float('inf'):
            return -1

        return dp[amount]
```

---

# 🔍 Code Breakdown

### Create DP Array

```python
dp = [float('inf')] * (amount + 1)
```

This gives us one state for every amount:

```text
0 → amount
```

---

### Base Case

```python
dp[0] = 0
```

Zero coins are required to make amount `0`.

---

### Iterate Through Amounts

```python
for i in range(1, amount + 1):
```

We solve smaller amounts before larger amounts.

---

### Try Every Coin

```python
for coin in coins:
```

Each coin provides a possible way to reach the current amount.

---

### Check Whether the Coin Fits

```python
if i - coin >= 0:
```

We can only use the coin if its value is not greater than the current amount.

---

### Update the Minimum

```python
dp[i] = min(
    dp[i],
    1 + dp[i - coin]
)
```

This asks:

```text
Current best
       OR
Use this coin + best solution for remaining amount
```

---

# 🧠 The Core DP Formula

The entire problem can be reduced to:

```text
dp[i] = min(
    dp[i],
    dp[i - coin] + 1
)
```

Interpretation:

```text
Minimum coins for amount i
=
minimum of all possible
"one coin + solution for remaining amount"
```

---

# 🔄 State Transition Diagram

```text
                 Amount i
                    ↓
             Choose a coin
                    ↓
              coin = x
                    ↓
             Remaining:
                i - x
                    ↓
          dp[i - x] coins
                    ↓
             + 1 current coin
                    ↓
          dp[i - x] + 1
                    ↓
              Compare with
              current dp[i]
                    ↓
                  min()
                    ↓
                 dp[i]
```

---

# 🧠 Why Dynamic Programming Works

The problem has **optimal substructure**.

If the optimal solution for amount `i` uses coin `x`, then the remaining amount:

```text
i - x
```

must also be solved optimally.

Otherwise, if there were a better solution for `i - x`, we could replace the existing solution and get a better solution for `i`.

The problem also has **overlapping subproblems** because the same smaller amounts are needed repeatedly.

For example:

```text
dp[11]
   ↓
dp[6]
   ↓
dp[1]
```

and other paths may also need:

```text
dp[6]
```

Instead of calculating it repeatedly, DP stores it.

---

# 📈 Bottom-Up DP Pattern

The general pattern is:

```text
              Target Amount
                    ↑
              Build backwards
                    ↑
              Smaller Amounts
                    ↑
                  dp[0]
```

More specifically:

```text
dp[0]
 ↓
dp[1]
 ↓
dp[2]
 ↓
dp[3]
 ↓
...
 ↓
dp[amount]
```

Every state depends on a previously computed smaller state.

---

# ⚙️ Complexity Analysis

Let:

```text
n = number of coin denominations
S = amount
```

We have:

```text
S
```

amount states.

For every amount, we try all:

```text
n
```

coins.

Therefore:

### Time Complexity

```text
O(S × n)
```

or:

```text
O(amount × len(coins))
```

### Space Complexity

The DP array contains:

```text
amount + 1
```

elements.

Therefore:

```text
O(S)
```

or:

```text
O(amount)
```

Final:

```text
Time:  O(amount × len(coins))
Space: O(amount)
```

---

# 📌 Edge Cases

## 1. Amount is Zero

```text
coins = [1,2,5]
amount = 0
```

No coins are needed:

```text
Answer = 0
```

---

## 2. Impossible Amount

```text
coins = [2]
amount = 3
```

Output:

```text
-1
```

---

## 3. Exact Coin Exists

```text
coins = [1,2,5]
amount = 5
```

Since coin `5` exists:

```text
Answer = 1
```

---

## 4. Coin Larger Than Amount

```text
coins = [5,10]
amount = 3
```

No coin can be used.

Therefore:

```text
Answer = -1
```

---

# 🆚 Coin Change vs Partition Equal Subset Sum

Both problems use a knapsack-style DP, but their goals are different.

### Partition Equal Subset Sum

Question:

```text
Can I reach target?
```

DP state:

```text
dp[s] = True / False
```

Transition:

```text
dp[s] |= dp[s - num]
```

Each number is generally used once.

---

### Coin Change

Question:

```text
What is the minimum number of coins
needed to reach target?
```

DP state:

```text
dp[s] = minimum number of coins
```

Transition:

```text
dp[s] = min(dp[s], 1 + dp[s-coin])
```

Coins can be used unlimited times.

---

# 🧠 Important Pattern Comparison

| Problem                    | DP State | Goal                   | Item Usage |
| -------------------------- | -------- | ---------------------- | ---------- |
| Partition Equal Subset Sum | Boolean  | Can target be reached? | Once       |
| Coin Change                | Integer  | Minimum items          | Unlimited  |
| 0/1 Knapsack               | Integer  | Maximum value          | Once       |
| Unbounded Knapsack         | Integer  | Maximum value          | Unlimited  |

Recognizing **what the DP state represents** is more important than memorizing code.

---

# 🎯 How to Recognize This DP Pattern

When you see:

* A target amount
* A list of denominations/items
* Unlimited reuse of items
* Need minimum number of items
* Need to reach an exact target

think:

```text
Unbounded Knapsack / Coin Change DP
```

Ask:

> "If I use one coin, what smaller amount remains?"

Answer:

```text
amount - coin
```

Then:

```text
dp[amount]
=
1 + dp[amount - coin]
```

Since multiple coins are possible:

```text
dp[amount]
=
min(
    1 + dp[amount - coin]
)
```

over all available coins.

---

# 🔑 Key Takeaways

### 1. Define the DP State

```text
dp[i] = minimum coins needed to make i
```

---

### 2. Base Case

```text
dp[0] = 0
```

---

### 3. Unknown States Start at Infinity

```python
dp = [float('inf')] * (amount + 1)
```

---

### 4. Try Every Coin

```python
for coin in coins:
```

---

### 5. Core Transition

```python
dp[i] = min(
    dp[i],
    1 + dp[i - coin]
)
```

---

### 6. Unlimited Coins

The same coin can be used repeatedly because each state can depend on a previously computed state that may itself use that coin.

---

### 7. Impossible State

If:

```text
dp[amount] == infinity
```

then return:

```text
-1
```

---

# 🏆 Final Solution

```python
class Solution:
    def coinChange(self, coins, amount):

        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:

                if i - coin >= 0:
                    dp[i] = min(
                        dp[i],
                        1 + dp[i - coin]
                    )

        return dp[amount] if dp[amount] != float('inf') else -1
```

### Complexity

```text
Time:  O(amount × len(coins))
Space: O(amount)
```

---

# 🚀 Final Mental Model

When solving **Coin Change**, think:

```text
                Target Amount
                      ↓
             What coin can I use?
                      ↓
                Choose coin
                      ↓
            Remaining = amount - coin
                      ↓
        What is the minimum for remaining?
                      ↓
                 dp[remaining]
                      ↓
               + 1 coin used
                      ↓
             Candidate Solution
                      ↓
              Try every coin
                      ↓
                  min(...)
                      ↓
                dp[amount]
                      ↓
                 Answer
```

The single most important formula to remember is:

```text
dp[i] = min(dp[i], 1 + dp[i - coin])
```

And the key pattern is:

```text
Target
  ↓
Smaller Target
  ↓
Previously Solved State
  ↓
Add One Item
  ↓
Take Minimum
```

This is the fundamental **Unbounded Knapsack / Minimum Coin DP** pattern behind **LeetCode 322 — Coin Change**.
