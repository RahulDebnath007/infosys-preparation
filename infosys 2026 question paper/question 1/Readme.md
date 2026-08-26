# 🔦 Mirror Beacon Placement

## 📌 Problem Statement

You are given:

* A string `s` of length `N`.
* An integer `B`, representing the number of beacons that must be installed.

A beacon can be placed in two ways:

### 1. Odd Beacon

A beacon can be centered on a character.

The selected substring must be an **odd-length palindrome**.

Example:

```text
ababa
  ↑
center
```

Possible palindromes centered at the middle:

```text
a       → length 1
aba     → length 3
ababa   → length 5
```

---

### 2. Even Beacon

A beacon can be centered between two adjacent characters.

The selected substring must be an **even-length palindrome**.

Example:

```text
abba
  ↑
center between b and b
```

Possible palindromes:

```text
bb      → length 2
abba    → length 4
```

---

## 🎯 Objective

We must install **exactly `B` beacons**.

Their palindrome spans:

* must not overlap,
* are allowed to touch,
* and each beacon's strength is equal to the length of its selected palindrome.

We need to find:

> **The maximum possible total signal strength.**

---

# 🧠 Main Idea

This problem looks complicated because it talks about:

* beacon centers,
* odd palindromes,
* even palindromes,
* maximum reach,
* operating strength,
* non-overlapping spans.

But we can simplify it into two problems.

```text
                Original Problem
                      │
                      ▼
          ┌───────────────────────┐
          │  Find all palindromes │
          └───────────┬───────────┘
                      │
                      ▼
          Convert them into intervals
                      │
                      ▼
          ┌────────────────────────┐
          │ Choose exactly B       │
          │ non-overlapping        │
          │ intervals              │
          └────────────┬───────────┘
                       │
                       ▼
                Maximum total length
```

So the solution uses **two algorithmic patterns**:

### Pattern 1 — Expand Around Center

Used to find all odd and even palindromes.

### Pattern 2 — Dynamic Programming

Used to choose exactly `B` non-overlapping palindromes with maximum total length.

---

# 🔍 How to Recognize This Pattern

When you see a problem containing:

```text
Choose exactly K items
+
Items occupy intervals/ranges
+
Intervals cannot overlap
+
Each item has a value/weight
+
Maximize total value
```

you should think:

```text
Interval Selection + DP
```

A natural DP state is:

```text
dp[i][k]
```

meaning:

> Maximum value using exactly `k` selected intervals in the first `i` positions.

This problem has one additional condition:

```text
The intervals must be palindromes.
```

Therefore, we first generate the valid palindrome intervals.

---

# 🔑 Important Observation

We don't actually need to keep thinking about the **center** during the DP.

The center is only useful when finding palindromes.

After finding a palindrome, we can represent it simply as:

```text
[start, end, length]
```

For example:

```text
aba
```

is:

```text
start = 0
end   = 2
length = 3
```

Now it is simply a weighted interval.

So the problem becomes:

> Select exactly `B` non-overlapping weighted palindrome intervals.

---

# 🟢 Step 1 — Find Odd Palindromes

For every character, treat it as the center.

Example:

```text
a b a b a
    ↑
  center
```

Start with:

```text
left = center
right = center
```

Then expand outward while:

```python
s[left] == s[right]
```

For:

```text
ababa
```

with center at index `2`:

```text
radius 1 → a
radius 2 → aba
radius 3 → ababa
```

The possible lengths are:

```text
1, 3, 5
```

---

# 🟡 Step 2 — Find Even Palindromes

For even palindromes, the center is between two characters.

Example:

```text
a b | b a
    ↑
   gap
```

Start with:

```text
left = i
right = i + 1
```

and expand.

For:

```text
abba
```

we get:

```text
bb
abba
```

with lengths:

```text
2, 4
```

---

# 📦 Step 3 — Store Palindromes in `ends_at`

The code creates:

```python
ends_at = [[] for _ in range(N)]
```

The meaning is:

```text
ends_at[r]
```

contains the lengths of all valid palindromes that end at index `r`.

For example:

```text
s = ababa
```

The palindrome:

```text
aba
```

from index `0` to index `2` has:

```text
end = 2
length = 3
```

Therefore:

```python
ends_at[2].append(3)
```

---

# 🤔 Why Store Only the Length?

Suppose:

```text
r = 6
L = 3
```

Then the palindrome starts at:

```text
start = r - L + 1
      = 6 - 3 + 1
      = 4
```

So:

```text
[4, 6]
```

Therefore, if we already know:

```text
end
length
```

we don't need to separately store the starting position.

---

# 🧮 Step 4 — Dynamic Programming

Now define:

```python
dp[i][k]
```

as:

> The maximum total signal obtainable using exactly `k` beacons in the first `i` characters.

For example:

```text
dp[5][2]
```

means:

> Maximum signal using exactly 2 beacons in the first 5 characters.

---

# 🟢 Base Case

Initially:

```python
dp[0][0] = 0
```

Meaning:

> Using zero characters and zero beacons gives signal `0`.

All other states are initially:

```text
-1
```

which means:

> This state is impossible.

---

# 🔵 DP Has Two Choices

At every position, we have two possibilities.

## Choice 1 — Skip the Current Position

We don't end a beacon here.

Therefore:

```python
dp[i][k] = dp[i-1][k]
```

The code:

```python
if dp[i - 1][k] != -1:
    dp[i][k] = max(dp[i][k], dp[i - 1][k])
```

---

## Choice 2 — Place a Beacon

Suppose a palindrome of length `L` ends at index `r`.

Since:

```python
i = r + 1
```

the palindrome occupies:

```text
[i-L ... i-1]
```

Therefore, everything before it is:

```text
first i-L characters
```

So we can take:

```python
dp[i-L][k-1]
```

and add the current palindrome's length:

```python
dp[i-L][k-1] + L
```

Therefore:

```python
dp[i][k] = max(
    dp[i][k],
    dp[i-L][k-1] + L
)
```

---

# 🚫 Why Can't the Beacons Overlap?

This is one of the most important parts.

Suppose the current palindrome is:

```text
[4.....6]
```

Its length is:

```text
3
```

Then:

```text
i = 7
L = 3
```

We use:

```python
dp[i-L]
```

which is:

```python
dp[4]
```

So previous beacons can only occupy:

```text
[0.....3]
```

The current beacon starts at:

```text
4
```

Therefore:

```text
Previous beacon(s): [0.....3]
Current beacon:     [4.....6]
```

They don't overlap.

They are allowed to touch, so this is perfectly valid.

---

# 🧠 The DP Formula

The complete idea can be written as:

```text
dp[i][k] =
    maximum of:

    1. dp[i-1][k]

    2. dp[i-L][k-1] + L
       for every palindrome of length L
       ending at position i-1
```

Or mathematically:

```text
dp[i][k] =
max(
    dp[i-1][k],
    dp[i-L][k-1] + L
)
```

for every valid palindrome length `L`.

---

# 🧪 Dry Run

Consider the first sample:

```text
N = 5
B = 2
s = ababa
```

String with indices:

```text
index:  0 1 2 3 4
        a b a b a
```

We need exactly:

```text
2 beacons
```

---

# Step 1 — Find Odd Palindromes

For `ababa`, the useful palindromes are:

```text
a       → length 1
b       → length 1
a       → length 1
b       → length 1
a       → length 1

aba     → length 3
bab     → length 3
aba     → length 3

ababa   → length 5
```

There are no useful even palindromes because there are no equal adjacent characters.

---

# Step 2 — Build `ends_at`

The resulting structure is:

```text
ends_at[0] = [1]

ends_at[1] = [1]

ends_at[2] = [3, 1]

ends_at[3] = [3, 1]

ends_at[4] = [5, 3, 1]
```

Interpretation:

### Position 0

```text
"a"
```

length:

```text
1
```

So:

```text
ends_at[0] = [1]
```

---

### Position 2

Two palindromes end here:

```text
"a"    → length 1
"aba"  → length 3
```

Therefore:

```text
ends_at[2] = [3, 1]
```

---

### Position 4

Three palindromes end here:

```text
"a"      → 1
"aba"    → 3
"ababa"  → 5
```

Therefore:

```text
ends_at[4] = [5, 3, 1]
```

---

# Step 3 — Initialize DP

We create:

```text
dp[i][k]
```

for:

```text
i = 0 ... 5
k = 0 ... 2
```

Initially:

```text
dp[0][0] = 0
```

Everything else:

```text
-1
```

---

# Step 4 — Process First Character

Position:

```text
r = 0
```

Palindrome:

```text
"a"
```

length:

```text
L = 1
```

For one beacon:

```text
dp[1][1]
=
dp[0][0] + 1
=
1
```

So:

```text
dp[1][1] = 1
```

---

# Step 5 — Process `"ab"`

Now we can use two single-character palindromes:

```text
"a" + "b"
```

Therefore:

```text
dp[2][2] = 2
```

Meaning:

```text
2 beacons
total signal = 2
```

---

# Step 6 — Process `"aba"`

Now we find:

```text
aba
```

length:

```text
3
```

It ends at index:

```text
2
```

For one beacon:

```text
dp[3][1]
=
dp[0][0] + 3
=
3
```

Therefore:

```text
dp[3][1] = 3
```

This means:

```text
Beacon 1 = "aba"
Signal = 3
```

---

# Step 7 — Add Another Beacon

Now consider index `3`:

```text
a b a b
0 1 2 3
```

We can choose:

```text
"aba" + "b"
```

The first beacon occupies:

```text
[0,2]
```

The second beacon occupies:

```text
[3,3]
```

They touch but don't overlap.

The DP transition is:

```text
dp[4][2]
=
dp[3][1] + 1
```

Therefore:

```text
dp[4][2]
=
3 + 1
=
4
```

So:

```text
dp[4][2] = 4
```

---

# Step 8 — Process Final Character

At index `4`, we have:

```text
a
aba
ababa
```

with lengths:

```text
1, 3, 5
```

For exactly two beacons, we could use:

```text
"aba" + "b"
```

giving:

```text
3 + 1 = 4
```

No valid combination of two non-overlapping palindromes gives more than `4`.

Therefore:

```text
dp[5][2] = 4
```

Final answer:

```text
4
```

---

# 📊 Complete DP Table for the Example

For:

```text
s = ababa
B = 2
```

the DP table becomes:

```text
             k = 0   k = 1   k = 2
           -------------------------
i = 0  |       0      -1      -1
i = 1  |       0       1      -1
i = 2  |       0       1       2
i = 3  |       0       3       2
i = 4  |       0       3       4
i = 5  |       0       5       4
```

The answer is:

```text
dp[5][2] = 4
```

---

# ⭐ Why Isn't the Answer 5?

Because the palindrome:

```text
ababa
```

has length `5`.

But we need:

```text
B = 2
```

beacons.

If we select:

```text
ababa
```

we have used only **one beacon**.

We need exactly two.

Therefore we have to split the string into two non-overlapping palindrome spans.

The best choice is:

```text
aba + b
```

or:

```text
a + bab
```

giving:

```text
3 + 1 = 4
```

So the answer is:

```text
4
```

---

# 💻 Complete Python Code

```python
import sys

input = sys.stdin.readline


def solve(N: int, B: int, s: str) -> int:
    ends_at = [[] for _ in range(N)]

    # --------------------------------------------------
    # 1. Precompute Odd Beacons
    # --------------------------------------------------
    #
    # Every character can be the center of an
    # odd-length palindrome.
    #
    # Example:
    #       a b a
    #         ^
    #       center
    #
    # Possible lengths are 1, 3, 5, ...
    #
    for i in range(N):
        max_reach = 0

        while (
            i - max_reach >= 0
            and i + max_reach < N
            and s[i - max_reach] == s[i + max_reach]
        ):
            max_reach += 1

        # Generate every valid odd palindrome
        for rad in range(1, max_reach + 1):
            L = 2 * rad - 1
            r = i + rad - 1

            ends_at[r].append(L)

    # --------------------------------------------------
    # 2. Precompute Even Beacons
    # --------------------------------------------------
    #
    # The center is between i and i+1.
    #
    # Example:
    #
    #     a b | b a
    #         ^
    #        center
    #
    # Possible lengths are 2, 4, 6, ...
    #
    for i in range(N - 1):
        max_reach = 0

        while (
            i - max_reach >= 0
            and i + 1 + max_reach < N
            and s[i - max_reach] == s[i + 1 + max_reach]
        ):
            max_reach += 1

        # Generate every valid even palindrome
        for rad in range(1, max_reach + 1):
            L = 2 * rad
            r = i + rad

            ends_at[r].append(L)

    # --------------------------------------------------
    # 3. Dynamic Programming
    # --------------------------------------------------
    #
    # dp[i][k] =
    # maximum signal using exactly k beacons
    # in the first i characters.
    #
    dp = [[-1] * (B + 1) for _ in range(N + 1)]

    # Base case:
    # zero characters + zero beacons = signal 0
    dp[0][0] = 0

    # Process the string from left to right
    for i in range(1, N + 1):
        r = i - 1

        for k in range(B + 1):

            # --------------------------------------------------
            # Option 1: Don't place a beacon ending at r
            # --------------------------------------------------
            if dp[i - 1][k] != -1:
                dp[i][k] = max(
                    dp[i][k],
                    dp[i - 1][k]
                )

            # --------------------------------------------------
            # Option 2: Place a palindrome ending at r
            # --------------------------------------------------
            if k > 0:

                for L in ends_at[r]:

                    # Previous k-1 beacons must fit
                    # completely before this palindrome.
                    if (
                        i - L >= 0
                        and dp[i - L][k - 1] != -1
                    ):
                        dp[i][k] = max(
                            dp[i][k],
                            dp[i - L][k - 1] + L
                        )

    return max(0, dp[N][B])


if __name__ == "__main__":
    try:
        N = int(input())
        B = int(input())
        s = input().strip()

        result = solve(N, B, s)

        print(result)

    except (EOFError, ValueError):
        pass
```

---

# 🔍 Code Structure at a Glance

The code has only **three major stages**.

```text
solve()
  │
  ├── 1. Find odd palindromes
  │
  ├── 2. Find even palindromes
  │
  └── 3. DP
        │
        ├── Skip current position
        │
        └── Take a palindrome
```

---

# ⏱️ Complexity

There can be `O(N²)` palindromic substrings.

The palindrome generation takes approximately:

```text
O(N²)
```

The DP considers every stored palindrome for every beacon count.

Therefore, the worst-case time complexity of this implementation is:

```text
O(B × N²)
```

Since:

```text
B <= N
```

the theoretical worst case can reach:

```text
O(N³)
```

The DP table requires:

```text
O(N × B)
```

space.

`ends_at` can store `O(N²)` palindrome lengths in the worst case.

So total auxiliary space is approximately:

```text
O(NB + N²)
```

For the given constraint:

```text
N <= 1000
```

this approach is reasonable depending on the platform's time limit, but the worst-case complexity is worth remembering.

---

# 🧩 The Pattern to Remember

Don't memorize this exact code.

Memorize the reasoning:

```text
             Is there a special structure?
                        │
                        ▼
                 PALINDROME
                        │
                        ▼
              Expand Around Center
                        │
                        ▼
             Generate valid intervals
                        │
                        ▼
          Do intervals overlap?
                        │
                        ▼
                       YES
                        │
                        ▼
              Interval-selection DP
                        │
                        ▼
            Need exactly B intervals?
                        │
                        ▼
               Add count dimension
                        │
                        ▼
                 dp[i][k]
```

The most important formula is:

```text
dp[i][k] =
max(
    dp[i-1][k],

    dp[i-L][k-1] + L
)
```

where `L` is a valid palindrome ending at the current position.

---

# 🧠 How to Recognize This in Future Problems

When reading a new problem, ask:

### Question 1

**What am I selecting?**

Here:

```text
Beacons
```

### Question 2

**Does each selection occupy a range?**

Here:

```text
Palindrome substring
```

### Question 3

**Can those ranges overlap?**

Here:

```text
No
```

### Question 4

**Do I need exactly K selections?**

Here:

```text
Exactly B
```

### Question 5

**Does each selection have a value?**

Here:

```text
Palindrome length
```

### Question 6

**Am I maximizing the total value?**

Here:

```text
Maximum total signal
```

Then you should start thinking:

```text
Weighted non-overlapping interval selection
+
exactly K selections
+
DP
```

And because the intervals are palindromes:

```text
Palindrome detection
+
Interval DP
```

---

# 🚀 Final Mental Model

The problem initially looks like:

```text
"Place B special beacons on a string."
```

Don't think about the story.

Translate it into algorithmic language:

```text
Find all valid palindrome intervals.
```

Then:

```text
Each palindrome = interval + weight(length)
```

Then:

```text
Choose exactly B intervals.
```

Then:

```text
Intervals cannot overlap.
```

Then:

```text
Maximize total weight.
```

Therefore:

```text
             PALINDROME
                 +
          INTERVAL DP
                 +
          EXACTLY B
```

That is the complete approach used by the given code.
