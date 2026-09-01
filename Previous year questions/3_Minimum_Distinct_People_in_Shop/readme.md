# 👥 Minimum Distinct People in Shop

## 📌 Problem Overview

You are given a binary string `S` representing people entering and leaving a shop.

Each character represents an event:

```text
1 → A person enters the shop
0 → A person leaves the shop
```

A person can enter and leave the shop multiple times.

The goal is to determine the **minimum number of distinct people** that could have produced the given sequence of entry and exit events.

---

# 🧩 Problem Statement

Given a binary string:

```text id="j8f4qv"
S
```

where:

```text id="tq4f4w"
1 = person enters
0 = person leaves
```

find the minimum number of distinct people that must exist for the sequence to be possible.

### Examples

```text id="7f3bq2"
000 → 3
110011 → 2
10101 → 1
```

---

# 💡 Key Observation

The important thing is to track the number of people currently inside the shop.

We call this:

```text id="p7h4w9"
balance
```

For every:

```text id="4c5v1a"
1 → balance += 1
0 → balance -= 1
```

However, the balance can become negative.

For example:

```text id="u6g8te"
000
```

Starting with:

```text id="k9m0s2"
balance = 0
```

First `0`:

```text id="2f0q9r"
balance = -1
```

This means one person must have existed outside before the sequence started.

Second `0`:

```text id="h7a3pc"
balance = -2
```

Now two distinct people are required.

Third `0`:

```text id="x2r5yd"
balance = -3
```

Therefore, at least three distinct people are required.

So:

```text id="7m4z2a"
Answer = 3
```

---

# 🧠 Main Idea

We track both:

```text id="0svv5r"
maximum positive balance
```

and:

```text id="a5yd8n"
maximum negative imbalance
```

The required number of distinct people is:

```text id="4zhqf0"
max(maximum_balance, -minimum_balance)
```

In other words:

> **The answer is the maximum absolute prefix imbalance.**

---

# 🎯 Pattern Used

## Prefix Sum + Simulation

This problem is essentially a **prefix sum / running balance** problem.

We process the string from left to right:

```text id="v4cmj1"
Input
 ↓
Read one event
 ↓
Update balance
 ↓
Track minimum and maximum
 ↓
Calculate answer
```

No array or complex data structure is required.

---

# 🔍 Why Prefix Sum Works

Consider:

```text id="8k4x9r"
110011
```

Calculate the running balance:

| Event | Balance |
| ----- | ------: |
| `1`   |     `1` |
| `1`   |     `2` |
| `0`   |     `1` |
| `0`   |     `0` |
| `1`   |     `1` |
| `1`   |     `2` |

The balances are:

```text id="x5r2m8"
1 → 2 → 1 → 0 → 1 → 2
```

The largest number of people simultaneously inside is:

```text id="q8v3nf"
2
```

Therefore at least two distinct people are required.

```text id="2y5m7k"
Answer = 2
```

---

# 🚨 Why Do We Track the Minimum?

Consider:

```text id="g5s1cd"
000
```

The balances are:

```text id="0k2q7w"
-1
-2
-3
```

The minimum balance is:

```text id="h4p8yz"
-3
```

A negative balance means the sequence contains more departures than previous arrivals.

That means some people must have already been outside before the observed sequence began.

The number of such people required is:

```text id="k9x3vd"
-(-3) = 3
```

Therefore:

```text id="5m8q1f"
answer = 3
```

---

# 🔄 Algorithm

1. Initialize:

   ```python
   balance = 0
   minimum = 0
   maximum = 0
   ```

2. Traverse every character in the string.

3. If the character is `1`:

   ```python
   balance += 1
   ```

4. If the character is `0`:

   ```python
   balance -= 1
   ```

5. Update:

   ```python
   minimum = min(minimum, balance)
   maximum = max(maximum, balance)
   ```

6. At the end, calculate:

   ```python
   max(maximum, -minimum)
   ```

7. Print the result.

---

# 💻 Python 3 Solution

```python
def solve():
    s = input().strip()

    balance = 0
    minimum = 0
    maximum = 0

    for ch in s:
        if ch == '1':
            balance += 1
        else:
            balance -= 1

        minimum = min(minimum, balance)
        maximum = max(maximum, balance)

    print(max(maximum, -minimum))


solve()
```

---

# 🔍 Code Explanation

## Step 1 — Initialize Variables

```python
balance = 0
minimum = 0
maximum = 0
```

### `balance`

Represents the current difference between entries and exits.

```text
1 → person enters
0 → person leaves
```

### `minimum`

Stores the lowest balance reached.

This is important when there are more exits than entries.

### `maximum`

Stores the highest balance reached.

This tells us the maximum number of people simultaneously needed inside.

---

# Step 2 — Process Each Character

```python
for ch in s:
```

We scan the string once.

---

## If Person Enters

```python
if ch == '1':
    balance += 1
```

Example:

```text
balance = 2
```

After an entry:

```text
balance = 3
```

---

## If Person Leaves

```python
else:
    balance -= 1
```

Example:

```text
balance = 2
```

After a departure:

```text
balance = 1
```

---

# Step 3 — Track Minimum and Maximum

After every event:

```python
minimum = min(minimum, balance)
maximum = max(maximum, balance)
```

This records the complete range of the prefix balance.

For example:

```text
Balances:
-1 → -2 → -3 → -2 → 0
```

Then:

```text
minimum = -3
maximum = 0
```

---

# Step 4 — Calculate the Answer

```python
max(maximum, -minimum)
```

There are two possible requirements.

### Positive side

If the balance reaches:

```text
+5
```

we need at least five distinct people inside at some point.

### Negative side

If the balance reaches:

```text
-4
```

we need four distinct people who could have been outside before the sequence.

Therefore:

```text
answer = max(5, 4)
```

---

# 🔬 Dry Run — Example 1

Input:

```text
000
```

Initial:

```text
balance = 0
minimum = 0
maximum = 0
```

### First `0`

```text
balance = -1
minimum = -1
maximum = 0
```

### Second `0`

```text
balance = -2
minimum = -2
maximum = 0
```

### Third `0`

```text
balance = -3
minimum = -3
maximum = 0
```

Final:

```text
max(0, -(-3))
= max(0, 3)
= 3
```

Output:

```text
3
```

---

# 🔬 Dry Run — Example 2

Input:

```text
110011
```

| Character | Balance | Minimum | Maximum |
| --------- | ------: | ------: | ------: |
| `1`       |       1 |       0 |       1 |
| `1`       |       2 |       0 |       2 |
| `0`       |       1 |       0 |       2 |
| `0`       |       0 |       0 |       2 |
| `1`       |       1 |       0 |       2 |
| `1`       |       2 |       0 |       2 |

Final:

```text
maximum = 2
minimum = 0
```

Therefore:

```text
max(2, 0)
= 2
```

Output:

```text
2
```

---

# 🔬 Dry Run — Example 3

Input:

```text
10101
```

Balances:

```text
1
0
1
0
1
```

So:

```text
minimum = 0
maximum = 1
```

Answer:

```text
max(1, 0)
= 1
```

Output:

```text
1
```

Only one distinct person is needed because the same person can repeatedly enter and leave.

---

# 📊 Dry Run Table

For:

```text
S = 10101
```

| Step | Character | Balance | Minimum | Maximum |
| ---: | :-------: | ------: | ------: | ------: |
|    0 |     -     |       0 |       0 |       0 |
|    1 |    `1`    |       1 |       0 |       1 |
|    2 |    `0`    |       0 |       0 |       1 |
|    3 |    `1`    |       1 |       0 |       1 |
|    4 |    `0`    |       0 |       0 |       1 |
|    5 |    `1`    |       1 |       0 |       1 |

Final:

```text
max(1, 0) = 1
```

---

# 🧠 Important Insight

The balance itself is **not necessarily the answer**.

You must consider both directions.

For example:

```text
S = 000111
```

Balances:

```text
-1
-2
-3
-2
-1
 0
```

The final balance is:

```text
0
```

But the answer is:

```text
3
```

because three people had to exist before the sequence began.

This is why we track the **minimum prefix balance**, not just the final balance.

---

# ⚠️ Common Mistake

A common incorrect solution is:

```python
balance = 0

for ch in s:
    if ch == '1':
        balance += 1
    else:
        balance -= 1

print(balance)
```

This is wrong.

For:

```text
000
```

it gives:

```text
-3
```

But the answer should be:

```text
3
```

Another incorrect approach is to return only the maximum balance.

That fails for:

```text
000
```

because the maximum balance is:

```text
0
```

while the correct answer is:

```text
3
```

Therefore, both extremes must be considered:

```text
maximum positive balance
minimum negative balance
```

---

# ⚙️ Complexity Analysis

Let:

```text
N = length of S
```

We scan the string exactly once.

### Time Complexity

```text
O(N)
```

Every character is processed once.

### Space Complexity

```text
O(1)
```

Only a few integer variables are maintained:

```text
balance
minimum
maximum
```

Final:

```text
Time:  O(N)
Space: O(1)
```

---

# 🧩 Pattern Recognition

This problem is a good example of **Prefix Sum / Running Balance**.

Look for this pattern when a problem involves:

* `1` and `0`
* Enter / leave
* Open / close
* Gain / loss
* Increase / decrease
* Current balance
* Maximum or minimum prefix difference

The basic template is:

```python
balance = 0

for x in arr:

    # Update balance

    balance += ...

    # Track prefix information
```

---

# 🔑 Key Takeaways

### 1. `1` increases the balance

```python
balance += 1
```

### 2. `0` decreases the balance

```python
balance -= 1
```

### 3. Track the maximum balance

It represents the largest number of people that must be inside simultaneously.

### 4. Track the minimum balance

A negative balance represents people who must have already been outside.

### 5. The answer is:

```python
max(maximum, -minimum)
```

### 6. No data structure is required

Only:

```text
O(1)
```

extra space is needed.

---

# 🎯 Final Mental Model

Think of the binary string as a running balance:

```text
1 → +1
0 → -1
```

Then:

```text
             Prefix Balance
                   ↓
        ┌──────────┴──────────┐
        ↓                     ↓
   Maximum                  Minimum
        ↓                     ↓
 People needed          People needed
   inside                 outside
        └──────────┬──────────┘
                   ↓
              Take maximum
```

For example:

```text
000
```

becomes:

```text
0 → -1 → -2 → -3
```

The deepest negative point is:

```text
-3
```

so:

```text
answer = 3
```

For:

```text
110011
```

we get:

```text
0 → 1 → 2 → 1 → 0 → 1 → 2
```

The highest positive point is:

```text
2
```

so:

```text
answer = 2
```

## 🚀 One-Line Exam Recall

> **Treat `1` as `+1` and `0` as `-1`; track the maximum and minimum prefix balance, and the minimum number of distinct people is `max(max_balance, -min_balance)`.**

### Pattern

```text
Prefix Sum / Running Balance
```

### Complexity

```text
Time  → O(N)
Space → O(1)
```
