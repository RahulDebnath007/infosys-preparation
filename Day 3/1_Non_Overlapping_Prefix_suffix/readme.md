# 🔗 Non-Overlapping Prefix-Suffix

## 📌 Problem Overview

Given a string `S`, find the **length of the longest prefix that is also a suffix**, with one important condition:

> The prefix and suffix **must not overlap**.

A prefix is a substring starting from the beginning of the string, while a suffix is a substring ending at the end of the string.

### Example

Consider:

```text
S = "ababa"
```

The prefix:

```text
"aba"
```

is also a suffix:

```text
"aba"
```

However, they overlap at the middle character:

```text
a b a b a
↑─────↑
```

Therefore, `"aba"` is **not valid**.

The longest valid prefix-suffix is:

```text
"a"
```

So the answer is:

```text
1
```

---

## 🧩 Problem Statement

Find the length of the longest proper prefix of `S` that is also a suffix of `S`, such that the prefix and suffix occupy **completely separate positions** in the string.

---

## 📥 Input Format

A single line containing a string `S`.

```text
S
```

### Constraints

```text
1 ≤ |S| ≤ 10⁵
```

---

## 📤 Output Format

Print the length of the longest prefix that is also a suffix **without overlapping**.

---

## 🧪 Sample Input 1

```text
abcdabc
```

## 🧪 Sample Output 1

```text
3
```

### Explanation

The prefix:

```text
abc
```

and the suffix:

```text
abc
```

are equal.

Their positions are:

```text
a b c d a b c
└─────┘
        └─────┘
```

The prefix occupies indices `0–2`, while the suffix occupies indices `4–6`.

They do not overlap.

Therefore:

```text
Answer = 3
```

---

# 💡 Approach

This problem can be solved efficiently using the **KMP (Knuth-Morris-Pratt) algorithm**, specifically its **LPS (Longest Prefix which is also Suffix)** array.

## What is the LPS Array?

For every index `i`:

```text
lps[i]
```

stores the length of the longest proper prefix of:

```text
S[0...i]
```

that is also a suffix of:

```text
S[0...i]
```

For example:

```text
S = "ababa"
```

The LPS array is:

```text
Index:  0 1 2 3 4
String: a b a b a
LPS:    0 0 1 2 3
```

Therefore:

```text
lps[-1] = 3
```

This tells us that `"aba"` is both a prefix and a suffix.

However, `"aba"` overlaps in `"ababa"`.

So we need an additional condition.

---

# 🚫 Handling the Non-Overlap Condition

If the prefix has length `L`, then:

* Prefix occupies indices `0 ... L-1`
* Suffix occupies indices `N-L ... N-1`

For them to **not overlap**:

```text
L ≤ N - L
```

Therefore:

```text
2L ≤ N
```

which gives:

```text
L ≤ N / 2
```

So the maximum possible valid length is:

```text
⌊N / 2⌋
```

We can therefore take:

```python
min(lps[-1], n // 2)
```

This removes any overlapping prefix-suffix.

---

# 🔍 Algorithm

1. Read the string `S`.
2. Create an `lps` array of size `N`.
3. Build the LPS array using KMP preprocessing.
4. Get the longest prefix-suffix length from:

```python
lps[-1]
```

5. Limit the answer to `N // 2` to guarantee that the prefix and suffix do not overlap.
6. Print the result.

---

# 🧠 Dry Run

Consider:

```text
S = "ababa"
```

Length:

```text
N = 5
```

### Step 1 — Build LPS

```text
S:    a b a b a
LPS:  0 0 1 2 3
```

Therefore:

```text
lps[-1] = 3
```

The longest prefix-suffix is:

```text
"aba"
```

But its length is:

```text
3
```

The maximum non-overlapping length is:

```text
N // 2
= 5 // 2
= 2
```

Therefore:

```text
answer = min(3, 2)
       = 2
```

⚠️ **Important:** Simply taking `min(lps[-1], n // 2)` is **not sufficient in general**.

For `"aaaaa"`:

```text
lps[-1] = 4
n // 2 = 2
```

The answer is `2`, which works.

But consider strings where the longest LPS is too large and a shorter valid border is needed. The correct solution should follow the LPS border chain until finding a border whose length is at most `N // 2`.

Therefore, the robust implementation is given below.

---

# 💻 Python 3 Solution

```python
def longest_prefix_suffix(s: str) -> int:
    n = len(s)

    if n == 0:
        return 0

    # Build the LPS array
    lps = [0] * n

    length = 0
    i = 1

    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1

        elif length != 0:
            length = lps[length - 1]

        else:
            lps[i] = 0
            i += 1

    # Longest border of the entire string
    ans = lps[-1]

    # Move through shorter borders until
    # we find one that does not overlap.
    while ans > n // 2:
        ans = lps[ans - 1]

    return ans


s = input().strip()
print(longest_prefix_suffix(s))
```

---

# ⚙️ Why Follow the LPS Chain?

Suppose:

```text
lps[-1] = 7
```

but:

```text
N // 2 = 4
```

The border of length `7` overlaps, so we cannot simply use it.

Instead, we look at:

```text
lps[7 - 1]
```

which gives the next-longest border.

We continue:

```text
7 → smaller border → smaller border → ...
```

until:

```text
border_length ≤ N // 2
```

This guarantees that we find the **longest valid non-overlapping border**, rather than merely cutting the length down to `N // 2`.

---

# 📊 Complexity Analysis

### Time Complexity

Building the LPS array takes:

```text
O(N)
```

Following the LPS chain also takes at most:

```text
O(N)
```

Therefore, the overall complexity is:

```text
O(N)
```

### Space Complexity

The LPS array contains `N` elements:

```text
O(N)
```

Therefore:

```text
Time:  O(N)
Space: O(N)
```

---

# 🔑 Key Concepts

This problem teaches several important string-processing concepts:

* **Prefix**
* **Suffix**
* **Proper Prefix**
* **String Borders**
* **KMP Algorithm**
* **LPS Array**
* **Pattern Matching**
* **Non-overlapping Substrings**

---

# 📚 Important Insight

The key observation is:

> The standard KMP LPS array finds the longest prefix that is also a suffix, but it does **not** care whether they overlap.

Therefore, after constructing the LPS array, we must enforce:

```text
prefix length ≤ N // 2
```

If the longest border is too large, we use the **LPS border chain** to find the next-longest valid border.

The final idea is:

```text
Build LPS
   ↓
Get longest border
   ↓
Does it overlap?
   ↓
Yes → Follow LPS chain
   ↓
Find longest border ≤ N // 2
   ↓
Print answer
```

---

# 📝 Edge Cases

### Single Character

```text
Input:
a

Output:
0
```

There cannot be a non-empty prefix and suffix that are both non-overlapping.

### No Matching Prefix-Suffix

```text
Input:
abcd

Output:
0
```

There is no non-empty prefix that is also a suffix.

### Completely Repeating String

```text
Input:
aaaaaa

Output:
3
```

The prefix:

```text
aaa
```

and suffix:

```text
aaa
```

do not overlap.

### Odd-Length String

For:

```text
N = 5
```

the maximum possible non-overlapping border length is:

```text
5 // 2 = 2
```

---

# 🚀 Takeaway

When a problem asks for:

> **"Longest prefix that is also a suffix"**

think:

```text
KMP → LPS
```

When it additionally says:

> **"Prefix and suffix must not overlap"**

think:

```text
LPS + length ≤ N // 2
```

And if the longest LPS is too large:

```text
Follow the LPS border chain
```

This gives an efficient:

```text
O(N)
```

solution suitable for:

```text
N ≤ 10⁵
```
