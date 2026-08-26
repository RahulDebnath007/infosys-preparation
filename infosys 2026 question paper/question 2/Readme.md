#  📈 Stock Trader's Alternating Streak – Maximum Valid Subsequence

## 📌 Problem Statement

You are given `N` stock price values:

```text
P[0], P[1], ..., P[N-1]
```

You need to find the **maximum length of a valid subsequence**.

A subsequence is formed by selecting some elements while maintaining their original order.

For example:

```text
P = [10, 15, 20, 10, 30]
```

We can select:

```text
10 → 20 → 10 → 30
```

We are allowed to skip elements.

---

# 📜 Rules for a Valid Subsequence

A valid subsequence must satisfy three rules.

## 1. Noise Threshold

For every two consecutive selected prices:

```text
|next - current| >= M
```

For example, if:

```text
M = 10
```

then:

```text
10 → 20
```

is valid because:

```text
|20 - 10| = 10
```

But:

```text
10 → 15
```

is invalid because:

```text
|15 - 10| = 5
```

---

## 2. Directions Must Alternate

There are two possible directions.

### UP

When:

```text
next > current
```

### DOWN

When:

```text
next < current
```

Normally, the directions must alternate:

```text
UP → DOWN → UP → DOWN
```

or:

```text
DOWN → UP → DOWN → UP
```

For example:

```text
10 → 20 → 10 → 30
```

has:

```text
UP → DOWN → UP
```

So it is valid.

But:

```text
10 → 20 → 30
```

has:

```text
UP → UP
```

which violates the normal alternating rule.

---

## 3. One Mulligan Is Allowed

The problem allows **at most one violation** of the alternating-direction rule.

For example:

```text
10 → 20 → 30 → 20
```

has:

```text
UP → UP → DOWN
```

The first:

```text
UP → UP
```

is normally invalid, but we can use the one available mulligan.

Therefore, the sequence can be valid.

However:

```text
10 → 20 → 30 → 40
```

has:

```text
UP → UP → UP
```

There are two consecutive-direction violations.

Only one mulligan is available, so the complete sequence cannot be used.

---

# 🧠 How to Recognize the Pattern

The important keywords are:

```text
maximum length
subsequence
alternating direction
one exception
```

These strongly suggest **Dynamic Programming**.

The key question is:

> What information about the previous elements affects the next decision?

Here, two things are important:

1. What was the previous direction?
2. Has the mulligan already been used?

Therefore:

```text
Previous Direction × Mulligan Status
```

gives the DP states.

There are:

```text
2 directions × 2 mulligan states = 4 states
```

---

# 🔑 The Four DP States

The code uses four main variables:

```python
up0
down0
up1
down1
```

Their meanings are:

| State   | Meaning                                        |
| ------- | ---------------------------------------------- |
| `up0`   | Last direction was UP, mulligan unused         |
| `down0` | Last direction was DOWN, mulligan unused       |
| `up1`   | Last direction was UP, mulligan already used   |
| `down1` | Last direction was DOWN, mulligan already used |

The suffix means:

```text
0 = mulligan unused
1 = mulligan used
```

So the state table is:

```text
                  Mulligan
               unused     used

UP              up0       up1

DOWN            down0     down1
```

This four-state representation is the central idea of the solution.

---

# 📍 Why We Need `last_*`

The code also maintains:

```python
last_up0
last_down0
last_up1
last_down1
```

These store the ending price associated with each state.

For example:

```python
up0 = 4
last_up0 = 30
```

roughly means:

> We have a subsequence of length `4`, its last direction is UP, the mulligan has not been used, and its tracked ending price is `30`.

The ending price matters because every new transition must satisfy:

```text
|current - previous| >= M
```

---

# 🚀 Initial State

The code starts with:

```python
up0, down0 = 1, 1
up1, down1 = 1, 1
```

and:

```python
last_up0 = P[0]
last_down0 = P[0]
last_up1 = P[0]
last_down1 = P[0]
```

Conceptually, selecting only the first element gives a subsequence of length:

```text
1
```

There is no actual direction yet, but the first element can act as the starting point for a future UP or DOWN transition.

---

# 🔄 Processing the Prices

The prices are processed from left to right:

```python
for i in range(1, N):
    x = P[i]
```

This is necessary because a subsequence must preserve the original order.

For every new price `x`, the algorithm considers four types of transitions:

```text
1. Normal UP
2. Normal DOWN
3. Mulligan UP
4. Mulligan DOWN
```

---

# ⬆️ Normal UP Transition

Suppose the previous direction was DOWN.

Moving UP is normal alternation:

```text
DOWN0 → UP0
```

The condition is:

```python
if x - last_down0 >= M:
```

This means:

```text
current - previous >= M
```

Therefore the price increased by at least `M`.

The length becomes:

```python
new_up0 = down0 + 1
```

So:

```text
DOWN0
   ↓
 UP0
```

---

# ⬆️ Normal UP After Mulligan

If the mulligan has already been used, normal alternation is still required.

Therefore:

```text
DOWN1 → UP1
```

The code checks:

```python
if x - last_down1 >= M:
    new_up1 = down1 + 1
```

Notice:

```text
1 → 1
```

The mulligan remains used.

---

# ⬇️ Normal DOWN Transition

Suppose the previous direction was UP.

Moving DOWN is normal alternation:

```text
UP0 → DOWN0
```

The condition is:

```python
if last_up0 - x >= M:
```

This means:

```text
previous - current >= M
```

So the price decreased by at least `M`.

The length becomes:

```python
new_down0 = up0 + 1
```

---

# ⬇️ Normal DOWN After Mulligan

When the mulligan has already been used:

```text
UP1 → DOWN1
```

The code checks:

```python
if last_up1 - x >= M:
    new_down1 = up1 + 1
```

Again:

```text
1 → 1
```

The mulligan cannot be reused.

---

# 🃏 Mulligan UP Transition

Normally:

```text
UP → UP
```

is invalid.

But the one available mulligan can be used.

Therefore:

```text
UP0 → UP1
```

The code checks:

```python
if x - last_up0 >= M:
    new_up1 = up0 + 1
```

The important change is:

```text
up0 → up1
```

which means:

```text
mulligan unused → mulligan used
```

---

# 🃏 Mulligan DOWN Transition

Similarly:

```text
DOWN → DOWN
```

is normally invalid.

Using the mulligan gives:

```text
DOWN0 → DOWN1
```

The code:

```python
if last_down0 - x >= M:
    new_down1 = down0 + 1
```

Again:

```text
0 → 1
```

means that the mulligan has been consumed.

---

# 🔀 Complete State Transition Diagram

Normal transitions:

```text
DOWN0 ─────────→ UP0
  ↑                │
  │                │
  └───────────────┘
       NORMAL
```

More clearly:

```text
DOWN0 → UP0
UP0   → DOWN0

DOWN1 → UP1
UP1   → DOWN1
```

Mulligan transitions:

```text
UP0   ──mulligan──→ UP1
DOWN0 ──mulligan──→ DOWN1
```

So the complete state structure is:

```text
             NORMAL UP
      DOWN0 ─────────────→ UP0
        │                    │
        │                    │
        │                    │
        ↓                    ↓
      DOWN1 ←───────────── UP1
             NORMAL DOWN
```

with:

```text
UP0   → UP1
DOWN0 → DOWN1
```

for the one-time violation.

---

# 🎯 Why `min()` Is Used for UP

For an UP transition we need:

```text
current - previous >= M
```

A smaller previous value is better.

For example:

```text
M = 10
current = 30
```

Previous value `20` gives:

```text
30 - 20 = 10
```

which is valid.

Previous value `30` gives:

```text
30 - 30 = 0
```

which is invalid.

Therefore, for equal-length UP states, a **smaller ending price is better**.

So the code tries to preserve the smaller ending value:

```python
new_last_up0 = min(new_last_up0, x)
```

---

# 🎯 Why `max()` Is Used for DOWN

For a DOWN transition we need:

```text
previous - current >= M
```

A larger previous value is better.

For example:

```text
M = 10
current = 20
```

Previous `30`:

```text
30 - 20 = 10
```

Valid.

Previous `25`:

```text
25 - 20 = 5
```

Invalid.

Therefore:

```text
UP states
→ prefer smaller ending prices

DOWN states
→ prefer larger ending prices
```

This is an important optimization idea in the DP.

---

# 🧪 Dry Run

Consider:

```text
N = 4
M = 10

P = [10, 20, 10, 20]
```

We want to determine the maximum valid subsequence.

Consider:

```text
10 → 20 → 10 → 20
```

Its directions are:

```text
UP → DOWN → UP
```

Everything alternates correctly.

---

## Step 1 — Start With `10`

Initially:

```text
up0 = 1
down0 = 1
up1 = 1
down1 = 1
```

and:

```text
last_up0 = 10
last_down0 = 10
last_up1 = 10
last_down1 = 10
```

Current maximum length:

```text
1
```

---

## Step 2 — Process `20`

Current:

```text
x = 20
```

Check:

```text
20 - 10 >= 10
```

Yes.

Therefore:

```text
DOWN0 → UP0
```

Length:

```text
up0 = down0 + 1
     = 1 + 1
     = 2
```

Subsequence:

```text
10 → 20
```

---

## Step 3 — Process `10`

Current:

```text
x = 10
```

We can make a DOWN transition:

```text
20 - 10 >= 10
```

Yes.

Therefore:

```text
UP0 → DOWN0
```

Length:

```text
down0 = up0 + 1
       = 2 + 1
       = 3
```

Subsequence:

```text
10 → 20 → 10
```

Directions:

```text
UP → DOWN
```

---

## Step 4 — Process `20`

Current:

```text
x = 20
```

Check:

```text
20 - 10 >= 10
```

Yes.

Therefore:

```text
DOWN0 → UP0
```

Length:

```text
up0 = down0 + 1
     = 3 + 1
     = 4
```

Final subsequence:

```text
10 → 20 → 10 → 20
```

Directions:

```text
UP → DOWN → UP
```

Therefore:

```text
Answer = 4
```

---

# 📊 Dry Run Table

| Current Price | Transition    | State       | Length | Subsequence         |
| ------------: | ------------- | ----------- | -----: | ------------------- |
|          `10` | Start         | `UP0/DOWN0` |    `1` | `10`                |
|          `20` | `DOWN0 → UP0` | `UP0`       |    `2` | `10 → 20`           |
|          `10` | `UP0 → DOWN0` | `DOWN0`     |    `3` | `10 → 20 → 10`      |
|          `20` | `DOWN0 → UP0` | `UP0`       |    `4` | `10 → 20 → 10 → 20` |

Final answer:

```text
4
```

---

# 🃏 Dry Run With a Mulligan

Consider:

```text
N = 4
M = 10

P = [10, 20, 30, 20]
```

Take:

```text
10 → 20 → 30 → 20
```

Directions:

```text
UP → UP → DOWN
```

The first:

```text
UP → UP
```

violates the alternating rule.

But we have one mulligan.

---

## `10 → 20`

Normal UP:

```text
DOWN0 → UP0
```

So:

```text
up0 = 2
```

---

## `20 → 30`

This is:

```text
UP → UP
```

Normally invalid.

Use the mulligan:

```text
UP0 → UP1
```

Therefore:

```text
up1 = 3
```

---

## `30 → 20`

This is DOWN.

The mulligan has already been used:

```text
UP1 → DOWN1
```

Therefore:

```text
down1 = 4
```

Final sequence:

```text
10 → 20 → 30 → 20
```

Length:

```text
4
```

State progression:

```text
UP0
 ↓
UP1
 ↓
DOWN1
```

---

# ❌ Example With Too Many Violations

Consider:

```text
P = [10, 20, 30, 40]
M = 10
```

The complete sequence is:

```text
10 → 20 → 30 → 40
```

Directions:

```text
UP → UP → UP
```

There are two violations:

```text
UP → UP
UP → UP
```

But only one mulligan is available.

Therefore, all four elements cannot be selected.

We can select:

```text
10 → 20 → 30
```

using one mulligan.

So the maximum length is:

```text
3
```

---

# 💻 Python Implementation

The core implementation follows the four-state DP described above:

```python
def solve(N: int, M: int, P: list) -> int:
    if N == 0:
        return 0

    if N == 1:
        return 1

    up0, down0 = 1, 1
    up1, down1 = 1, 1

    last_up0 = P[0]
    last_down0 = P[0]
    last_up1 = P[0]
    last_down1 = P[0]

    for i in range(1, N):
        x = P[i]

        new_up0 = up0
        new_down0 = down0
        new_up1 = up1
        new_down1 = down1

        new_last_up0 = last_up0
        new_last_down0 = last_down0
        new_last_up1 = last_up1
        new_last_down1 = last_down1

        # Normal UP: DOWN0 -> UP0
        if x - last_down0 >= M:
            if down0 + 1 > new_up0:
                new_up0 = down0 + 1
                new_last_up0 = x
            elif down0 + 1 == new_up0:
                new_last_up0 = min(new_last_up0, x)

        # Normal DOWN: UP0 -> DOWN0
        if last_up0 - x >= M:
            if up0 + 1 > new_down0:
                new_down0 = up0 + 1
                new_last_down0 = x
            elif up0 + 1 == new_down0:
                new_last_down0 = max(new_last_down0, x)

        # Normal UP after mulligan: DOWN1 -> UP1
        if x - last_down1 >= M:
            if down1 + 1 > new_up1:
                new_up1 = down1 + 1
                new_last_up1 = x
            elif down1 + 1 == new_up1:
                new_last_up1 = min(new_last_up1, x)

        # Normal DOWN after mulligan: UP1 -> DOWN1
        if last_up1 - x >= M:
            if up1 + 1 > new_down1:
                new_down1 = up1 + 1
                new_last_down1 = x
            elif up1 + 1 == new_down1:
                new_last_down1 = max(new_last_down1, x)

        # Mulligan UP: UP0 -> UP1
        if x - last_up0 >= M:
            if up0 + 1 > new_up1:
                new_up1 = up0 + 1
                new_last_up1 = x
            elif up0 + 1 == new_up1:
                new_last_up1 = min(new_last_up1, x)

        # Mulligan DOWN: DOWN0 -> DOWN1
        if last_down0 - x >= M:
            if down0 + 1 > new_down1:
                new_down1 = down0 + 1
                new_last_down1 = x
            elif down0 + 1 == new_down1:
                new_last_down1 = max(new_last_down1, x)

        up0 = new_up0
        down0 = new_down0
        up1 = new_up1
        down1 = new_down1

        last_up0 = new_last_up0
        last_down0 = new_last_down0
        last_up1 = new_last_up1
        last_down1 = new_last_down1

    return max(up0, down0, up1, down1)
```

---

# ⏱️ Complexity of the Above State Compression

The loop processes every price once:

```python
for i in range(1, N):
```

Each iteration performs a constant number of transitions.

Therefore the intended complexity is:

```text
Time:  O(N)
Space: O(1)
```

This is attractive when:

```text
N <= 10^5
```

because an `O(N²)` dynamic-programming solution would be too slow.

---

# ⚠️ Important Correctness Caveat

There is an important limitation in this particular implementation.

It stores only **one ending price per DP state**:

```python
last_up0
last_down0
last_up1
last_down1
```

This is an aggressive compression.

Two different subsequences can have:

```text
same length
same direction
same mulligan status
```

but different ending prices.

For example:

```text
Subsequence A:
length = 5
state = UP0
ending price = 20

Subsequence B:
length = 5
state = UP0
ending price = 50
```

For a future UP transition, `20` is better because:

```text
current - 20
```

is easier to make at least `M`.

For a future DOWN transition, `50` could be more useful because:

```text
50 - current
```

is easier to make at least `M`.

A single `last_up0` value cannot preserve every potentially useful possibility.

Therefore, this `O(N)` implementation should be understood as a **state-design demonstration**, not as a guaranteed-correct solution for every possible input.

A fully robust solution requires maintaining DP information across multiple ending prices, typically using:

```text
Coordinate Compression
        +
Fenwick Tree / Segment Tree
        +
4 DP States
```

which can achieve:

```text
O(N log N)
```

---

# 🧠 The Real DP Insight

Do not memorize:

```text
up0
down0
up1
down1
```

Instead, ask:

> What information from the past affects my next decision?

For this problem:

```text
Previous direction
        +
Mulligan used or not
        +
Ending price
```

The first two pieces create the four logical states:

```text
UP0
DOWN0
UP1
DOWN1
```

The ending price is necessary because every transition depends on:

```text
|current - previous| >= M
```

Therefore, the conceptual DP state is:

```text
DP =
(last direction,
 mulligans used,
 ending price)
```

---

# 🔄 Pattern Recognition

The complete thought process is:

```text
Maximum subsequence
        ↓
Dynamic Programming
        ↓
Direction matters
        ↓
Remember UP / DOWN
        ↓
One exception is allowed
        ↓
Remember mulligan used / unused
        ↓
4 logical states
        ↓
Ending price affects future transitions
        ↓
Track ending prices efficiently
```

This pattern is useful for problems involving:

* Maximum/minimum subsequences
* Alternating behavior
* Limited exceptions
* Previous-value-dependent transitions
* Threshold-based transitions

---

# 📚 Quick Revision

## Four States

```text
up0
↓
Last direction UP, mulligan unused

down0
↓
Last direction DOWN, mulligan unused

up1
↓
Last direction UP, mulligan used

down1
↓
Last direction DOWN, mulligan used
```

## Normal Transitions

```text
down0 → up0
up0   → down0

down1 → up1
up1   → down1
```

## Mulligan Transitions

```text
up0   → up1
down0 → down1
```

## Noise Condition

For UP:

```text
current - previous >= M
```

For DOWN:

```text
previous - current >= M
```

## Ending-Value Preference

For UP:

```text
smaller ending price is better
```

For DOWN:

```text
larger ending price is better
```

## Complexity of the Demonstrated Implementation

```text
Time Complexity:  O(N)
Space Complexity: O(1)
```

## Robust-Solution Caveat

```text
Single ending-price compression
        ↓
Not guaranteed correct for every input

Fully robust approach:
Coordinate Compression
+
Fenwick Tree / Segment Tree
+
4 DP states

Complexity:
O(N log N)
```

---

# 🎯 Final Takeaway

The main lesson from this problem is **DP state design**.

The problem initially looks complicated because several conditions interact.

Break them down:

```text
Longest subsequence
        ↓
DP

Alternating direction
        ↓
Remember previous direction

One allowed violation
        ↓
Remember whether mulligan was used

Noise threshold
        ↓
Ending price matters
```

This produces the conceptual state:

```text
DP =
(last direction,
 mulligan status,
 ending price)
```

The four basic logical states are:

```text
UP0
DOWN0
UP1
DOWN1
```

The most important pattern to recognize is:

```text
Maximum subsequence
+
Alternating behavior
+
Limited exceptions
+
Previous-value constraint
        ↓
Dynamic Programming
```

That state-design technique is much more important than memorizing the implementation.
