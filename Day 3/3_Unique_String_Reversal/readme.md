# 🔄 Unique String Reversal

## 📌 Problem Overview

Given a string `S`, process it in two steps:

1. **Remove duplicate characters**, keeping only the **first occurrence** of each character.
2. **Reverse** the resulting string.

The final processed string should be printed.

---

## 🧩 Problem Statement

You are given a string `S`.

First, remove every duplicate character while preserving the order in which each character appears for the first time.

Then reverse the resulting string.

### Example

Consider:

```text
S = "google"
```

Removing duplicate characters:

```text
g o o g l e
↓
g o l e
```

The unique string is:

```text
"gole"
```

Reverse it:

```text
"elog"
```

Therefore, the output is:

```text
elog
```

---

## 📥 Input Format

The first and only line contains a string `S`.

```text
S
```

### Constraints

```text
1 ≤ |S| ≤ 10⁵
```

The string contains only **printable ASCII characters**.

---

## 📤 Output Format

Print the final string after:

1. Removing duplicate characters while keeping their first occurrence.
2. Reversing the resulting string.

---

# 🧪 Sample Input

```text
google
```

## 🧪 Sample Output

```text
elog
```

### Explanation

The original string is:

```text
g o o g l e
```

Keep only the first occurrence of every character:

```text
g o l e
```

So the unique string is:

```text
gole
```

Reverse it:

```text
elog
```

Therefore:

```text
Answer = elog
```

---

# 💡 Approach

The solution can be divided into two simple steps.

## Step 1 — Remove Duplicates

We iterate through the string from left to right.

A Python `set` called `seen` is used to keep track of characters that have already appeared.

```python
seen = set()
```

For every character:

* If it is not in `seen`, add it to the set.
* Append it to the `result` list.
* If it is already in `seen`, ignore it.

For example:

```text
Input:
google
```

Processing:

```text
g → new → keep
o → new → keep
o → duplicate → ignore
g → duplicate → ignore
l → new → keep
e → new → keep
```

Result:

```text
gole
```

---

## Step 2 — Reverse the Result

Once all duplicate characters have been removed, we have:

```text
gole
```

Python slicing can reverse the list:

```python
result[::-1]
```

This gives:

```text
elog
```

Finally, we use:

```python
"".join(...)
```

to convert the characters back into a string.

---

# 🔍 Algorithm

1. Read the input string `S`.
2. Create an empty set `seen`.
3. Create an empty list `result`.
4. Traverse every character in `S`.
5. If the character has not appeared before:

   * Add it to `seen`.
   * Append it to `result`.
6. Reverse `result`.
7. Join the characters into a string.
8. Print the final string.

---

# 💻 Python 3 Solution

```python
S = input().strip()

seen = set()
result = []

for ch in S:
    if ch not in seen:
        seen.add(ch)
        result.append(ch)

print("".join(result[::-1]))
```

---

# 🧠 Dry Run

Consider:

```text
S = "programming"
```

### Character Processing

| Character | Already Seen? | Action | Result     |
| --------- | ------------- | ------ | ---------- |
| `p`       | No            | Keep   | `p`        |
| `r`       | No            | Keep   | `pr`       |
| `o`       | No            | Keep   | `pro`      |
| `g`       | No            | Keep   | `prog`     |
| `r`       | Yes           | Ignore | `prog`     |
| `a`       | No            | Keep   | `proga`    |
| `m`       | No            | Keep   | `progam`   |
| `m`       | Yes           | Ignore | `progam`   |
| `i`       | No            | Keep   | `progami`  |
| `n`       | No            | Keep   | `progamin` |
| `g`       | Yes           | Ignore | `progamin` |

After removing duplicates:

```text
progamin
```

Reverse it:

```text
nimagorp
```

Final output:

```text
nimagorp
```

---

# ⚙️ Complexity Analysis

Let:

```text
N = length of the input string
```

### Time Complexity

We traverse the string once:

```text
O(N)
```

Set lookup and insertion take **O(1) average time**.

Reversing the resulting list also takes:

```text
O(N)
```

Therefore, the overall time complexity is:

```text
O(N)
```

### Space Complexity

We use:

* A `set` to store seen characters.
* A `list` to store unique characters.
* A final output string.

Therefore:

```text
O(N)
```

auxiliary space in the general analysis.

Because the input is restricted to **printable ASCII characters**, the number of distinct characters is actually bounded by the ASCII character set, but `O(N)` is the standard safe complexity statement for this implementation.

---

# 📌 Edge Cases

## 1. Single Character

Input:

```text
a
```

Output:

```text
a
```

---

## 2. All Characters Are Unique

Input:

```text
abcdef
```

No characters are removed.

After reversing:

```text
fedcba
```

Output:

```text
fedcba
```

---

## 3. All Characters Are Identical

Input:

```text
aaaaaa
```

Only the first `a` is kept:

```text
a
```

Reversing it still gives:

```text
a
```

Output:

```text
a
```

---

## 4. Mixed Uppercase and Lowercase

ASCII characters are case-sensitive.

For example:

```text
AaAa
```

contains two distinct characters:

```text
A
a
```

The unique string is:

```text
Aa
```

After reversal:

```text
aA
```

---

## 🔑 Key Concepts

This problem demonstrates:

* String traversal
* Duplicate removal
* Python `set`
* Preserving insertion order manually
* Lists
* String joining
* String/list reversal
* `[::-1]` slicing
* Time and space complexity

---

# 🎯 Key Takeaway

The main idea is:

```text
Original String
      ↓
Traverse characters
      ↓
Use Set to detect duplicates
      ↓
Keep first occurrence
      ↓
Unique String
      ↓
Reverse
      ↓
Final Output
```

For:

```text
google
```

the process is:

```text
google
  ↓
gole
  ↓
elog
```

So the answer is:

```text
elog
```

The combination of a **set for duplicate detection** and a **list for maintaining order** provides a simple and efficient `O(N)` solution.
