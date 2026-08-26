# 11 ✂️ Equal String Pieces – Maximum Number of Identical Parts

[![Repository](https://img.shields.io/badge/Repository-infosys--preparation-blue?logo=github)](https://github.com/RahulDebnath007/infosys-preparation)

**Pattern:** Frequency Counting + GCD

---

## 📌 Problem Statement

You are given an interesting string `S` of length `N`.

The string is interesting because its characters can be **rearranged in any order**.

You want to cut the rearranged string into contiguous pieces such that:

* All pieces are exactly equal.
* The number of pieces is as large as possible.
* Characters inside the pieces cannot be rearranged after cutting.
* The pieces cannot be joined together after cutting.

The answer is always at least `1` because the entire string itself can be considered one piece.

The task is to find the **maximum number of equal pieces** that can be obtained.

---

# 💡 Approach

A brute-force approach might try different numbers of pieces and check whether the string can be divided into equal parts.

However, the important observation is:

> The string can be rearranged before cutting.

Therefore, the original positions of the characters do not matter.

Only the **frequency of each character** matters.

Suppose:

```text id="7y2l9x"
S = "ababcc"
```

The frequencies are:

```text id="x9k2v3"
a → 2
b → 2
c → 2
```

We can rearrange the string as:

```text id="4d6n8r"
abcabc
```

and split it into:

```text id="q4v7sm"
abc | abc
```

Therefore, the answer is:

```text id="z1k8qp"
2
```

This leads to:

```text id="a8m3nc"
Frequency Counting
+
GCD
```

---

# 🔑 Key Observation

Suppose we want to create `K` identical pieces.

Every character must be distributed equally among all `K` pieces.

Therefore, the frequency of every character must be divisible by `K`.

For example:

```text id="4q8t1b"
a → 6
b → 9
c → 3
```

If we want `3` pieces:

```text id="2s7f9m"
a → 6 / 3 = 2 per piece
b → 9 / 3 = 3 per piece
c → 3 / 3 = 1 per piece
```

So `3` pieces are possible.

But `4` pieces are impossible because:

```text id="n2x7qp"
6 % 4 != 0
9 % 4 != 0
3 % 4 != 0
```

Therefore, the maximum possible number of pieces is:

```text id="c7m4vs"
GCD(all character frequencies)
```

---

# 🧠 Why GCD?

Suppose the character frequencies are:

```text id="9x4k2m"
a → 12
b → 8
c → 4
```

We need a number that divides every frequency.

Possible numbers include:

```text id="q7v1ds"
1
2
4
```

The largest one is:

```text id="t5n8pl"
GCD(12, 8, 4) = 4
```

Therefore:

```text id="h3m6qx"
Maximum pieces = 4
```

Each piece will contain:

```text id="w9c2kr"
a → 12 / 4 = 3
b → 8 / 4 = 2
c → 4 / 4 = 1
```

So every piece contains exactly the same characters.

---

# 🔍 Why Rearrangement Matters

Without rearrangement, this would be a much harder problem because the original character order would matter.

For example:

```text id="p3q8vz"
ababcc
```

can be rearranged into:

```text id="j6k1sx"
abcabc
```

Then:

```text id="0r5m9n"
abc | abc
```

Both pieces are identical.

The original string:

```text id="5c2x8k"
a b a b c c
```

does not itself contain two identical contiguous pieces.

But because rearrangement is allowed, we only need to care about:

```text id="m8q4ws"
a → 2
b → 2
c → 2
```

This is why the problem becomes a frequency/divisibility problem.

---

# 📝 Algorithm

1. Read the string `S`.
2. Count the frequency of every character.
3. Initialize the answer as `0`.
4. Calculate the GCD of all non-zero character frequencies.
5. Return the final GCD.

The result is the maximum number of identical pieces.

---

# 📝 Code Explanation

## Step 1 — Import GCD

```python id="r3k7vy"
from math import gcd
```

Python provides the `gcd()` function through the `math` module.

For example:

```python id="s6m2qx"
gcd(12, 8)
```

returns:

```text id="v4n9pc"
4
```

---

## Step 2 — Read the String

```python id="k8p3wd"
S = input().strip()
```

Read the input string.

For example:

```text id="a2f7lm"
ababcc
```

becomes:

```text id="y5q1sr"
S = "ababcc"
```

---

## Step 3 — Create the Frequency Dictionary

```python id="m9v4kx"
frequency = {}
```

This dictionary stores the number of occurrences of every character.

For example:

```text id="p2s8hc"
{
    'a': 2,
    'b': 2,
    'c': 2
}
```

---

## Step 4 — Count Character Frequencies

```python id="q7w3nf"
for ch in S:
    frequency[ch] = frequency.get(ch, 0) + 1
```

Process every character.

If the character does not exist in the dictionary:

```python id="r8k2xm"
frequency.get(ch, 0)
```

returns `0`.

Then `1` is added.

For:

```text id="c4n7sv"
ababcc
```

the dictionary becomes:

```text id="d5m1qx"
a → 2
b → 2
c → 2
```

---

## Step 5 — Initialize the Answer

```python id="h6v9rp"
answer = 0
```

We start the GCD calculation from `0`.

This works because:

```text id="x3k8qm"
GCD(0, x) = x
```

Therefore, the first frequency automatically becomes the initial GCD.

---

## Step 6 — Calculate the GCD

```python id="n4s7wc"
for count in frequency.values():
    answer = gcd(answer, count)
```

Process every character frequency.

For:

```text id="m2q9vx"
a → 2
b → 2
c → 2
```

the calculation becomes:

```text id="k8w4pn"
GCD(0, 2) = 2
GCD(2, 2) = 2
GCD(2, 2) = 2
```

Therefore:

```text id="s5m1qr"
answer = 2
```

---

## Step 7 — Print the Answer

```python id="y3k7vd"
print(answer)
```

The GCD represents the maximum number of identical pieces.

---

# 💻 Complete Code

```python id="e8m3qs"
from math import gcd

S = input().strip()

frequency = {}

# Count frequency of each character
for ch in S:
    frequency[ch] = frequency.get(ch, 0) + 1

# Calculate GCD of all character frequencies
answer = 0

for count in frequency.values():
    answer = gcd(answer, count)

print(answer)
```

---

# 🧪 Dry Run

## Sample Input 1

```text id="x4p8vn"
zzzzz
```

Frequency:

```text id="k7m2qc"
z → 5
```

Calculate:

```text id="v9s1wb"
GCD(5) = 5
```

Therefore:

```text id="q3n6xm"
Answer = 5
```

The string can be split as:

```text id="w8k4rp"
z | z | z | z | z
```

---

# 🧪 Dry Run — Sample 2

Input:

```text id="c5m8vq"
ababcc
```

Frequency:

```text id="r7x2kn"
a → 2
b → 2
c → 2
```

Calculate:

```text id="p4w9ms"
GCD(2, 2, 2)
```

Therefore:

```text id="n6q1xc"
2
```

The string can be rearranged as:

```text id="v3m8kr"
abcabc
```

and divided into:

```text id="q5x2pn"
abc | abc
```

Therefore:

```text id="z8w4ms"
Answer = 2
```

---

# 🧪 Dry Run — Sample 3

Input:

```text id="p7m2vx"
abccdcabacda
```

Character frequencies:

```text id="k4x8qn"
a → 4
b → 2
c → 4
d → 2
```

Calculate:

```text id="s9m3wr"
GCD(4, 2, 4, 2)
```

Step by step:

```text id="v6q1kp"
GCD(4, 2) = 2
GCD(2, 4) = 2
GCD(2, 2) = 2
```

Therefore:

```text id="j5x8mc"
Answer = 2
```

The string can be rearranged into two identical pieces.

For example:

```text id="r2k7vn"
aaccbd | aaccbd
```

Each piece contains:

```text id="w4m9qx"
a → 2
b → 1
c → 2
d → 1
```

---

# 🔍 Why the GCD Gives the Maximum

Suppose the frequencies are:

```text id="n5q8vx"
a → 8
b → 12
c → 4
```

For `K` identical pieces to exist:

```text id="m7x2pr"
8 % K = 0
12 % K = 0
4 % K = 0
```

Therefore, `K` must be a common divisor of all frequencies.

The largest common divisor is:

```text id="q4w9ms"
GCD(8, 12, 4) = 4
```

So the maximum number of equal pieces is:

```text id="x8k3vn"
4
```

Each piece contains:

```text id="p6m1qr"
a → 2
b → 3
c → 1
```

---

# 📊 Complexity Analysis

## Time Complexity

We scan the string once:

```text id="v7q2mx"
O(N)
```

The number of distinct characters is limited by the alphabet, so calculating the GCD takes effectively constant additional time.

Therefore:

```text id="k4m8sp"
Time Complexity = O(N)
```

---

## Space Complexity

The frequency dictionary stores one entry per distinct character.

If the alphabet size is fixed:

```text id="n2x6qr"
O(1)
```

More generally:

```text id="w8m3vp"
O(K)
```

where `K` is the number of distinct characters.

For a lowercase English alphabet:

```text id="r5q9kx"
K <= 26
```

---

# 🧩 Pattern Used

* Frequency Counting
* GCD / Greatest Common Divisor
* Divisibility
* Hash Map / Dictionary
* Mathematical Observation

---

# 🎯 Pattern Recognition

This problem has the structure:

```text id="m8q2vx"
Rearrangement Allowed
        ↓
Original Positions Don't Matter
        ↓
Count Character Frequencies
        ↓
Need Equal Groups
        ↓
Every Frequency Must Be Divisible by K
        ↓
Maximum K = GCD of Frequencies
```

Whenever you see:

* A string/array can be rearranged.
* You need the maximum number of identical groups.
* Every item must be distributed equally.
* The original ordering is irrelevant.

Think:

```text id="x4m7qs"
Frequency Counting
+
GCD / Divisibility
```

---

# 🚀 Key Learning

> When items can be rearranged freely and must be divided into the maximum number of identical groups, count the frequency of every item and find the **GCD of those frequencies**.

For this problem:

```text id="q9v3mk"
String
   ↓
Frequency Count
   ↓
Character Frequencies
   ↓
GCD of Frequencies
   ↓
Maximum Number of Equal Pieces
```

The core formula is:

```text id="s6x1pn"
answer = GCD(frequency of every distinct character)
```

---

# 📚 Suitable For

* Infosys Coding Assessment
* String Problems
* Frequency Counting Practice
* GCD / Number Theory
* Hash Map / Dictionary Practice
* Mathematical Observation Problems
* Divisibility Problems
* Competitive Programming
* Coding Interviews

