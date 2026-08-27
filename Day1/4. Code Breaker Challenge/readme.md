# 🔐 Code Breaker Challenge

> 🧩 **Pattern:** String Parsing + Validation + Maximum Selection + Indexing
> 🎯 **Goal:** Decode a sequence of `name:code` pairs into a final keyword.

---

## 📌 Problem Statement

You are given a sequence of:

```text
name:code
```

pairs separated by commas.

For each pair:

1. 🔍 Examine every digit in the `code`.
2. ✅ Keep only digits that are valid **1-based positions** in the `name`.
3. 🏆 Find the **largest valid digit**.
4. 🔤 Use that position to select a character from the `name`.
5. ❌ If no valid digit exists, append `X`.
6. 🔗 Concatenate all selected characters to form the final keyword.

---

# 🧪 Example

### 📥 Input

```text
Anchal:23581,Aman:57568,Sonakshi:34848
```

We process each pair separately.

### 🔹 Pair 1

```text
Anchal:23581
```

Name:

```text
A n c h a l
1 2 3 4 5 6
```

Code:

```text
2 3 5 8 1
```

Valid positions:

```text
2, 3, 5, 1
```

`8` is invalid because `Anchal` has only 6 characters.

Largest valid digit:

```text
5
```

Position `5` in `Anchal`:

```text
A n c h a l
        ↑
        5
```

Character:

```text
a
```

Result:

```text
a
```

---

### 🔹 Pair 2

```text
Aman:57568
```

Name:

```text
A m a n
1 2 3 4
```

Code:

```text
5 7 5 6 8
```

All digits are greater than `4`.

Therefore:

```text
❌ No valid position
```

Append:

```text
X
```

Result:

```text
X
```

---

### 🔹 Pair 3

```text
Sonakshi:34848
```

Name:

```text
S o n a k s h i
1 2 3 4 5 6 7 8
```

Code:

```text
3 4 8 4 8
```

Valid digits:

```text
3, 4, 8, 4, 8
```

Largest valid digit:

```text
8
```

Position `8`:

```text
S o n a k s h i
              ↑
              8
```

Character:

```text
i
```

Result:

```text
i
```

---

### 🎯 Final Keyword

Combine:

```text
a + X + i
```

Therefore:

```text
aXi
```

---

# 📥 Input Format

A single line containing one or more `name:code` pairs.

Pairs are separated by commas.

Example:

```text
name1:code1,name2:code2,name3:code3
```

---

# 📤 Output Format

Print a single string representing the decoded keyword.

---

# 🔢 Constraints

* 👤 Names contain only alphabetic characters.
* 🔢 Each code digit is between `0` and `9`.
* 📦 The input contains at least one `name:code` pair.

---

# 🧠 Core Idea

The entire problem can be remembered as:

```text
📥 Input
   ↓
✂️ Split by comma
   ↓
🔐 Split each pair by :
   ↓
🔢 Check code digits
   ↓
✅ Keep valid positions
   ↓
🏆 Find largest valid digit
   ↓
🔤 Get character from name
   ↓
❌ No valid digit → X
   ↓
🔗 Join results
   ↓
🎯 Final Keyword
```

---

# 🛠️ Step-by-Step Logic

## 1️⃣ ✂️ Split the Pairs

The input contains multiple pairs separated by commas.

```python
pairs = s.strip().split(",")
```

For:

```text
Anchal:23581,Aman:57568,Sonakshi:34848
```

we get:

```text
[
    "Anchal:23581",
    "Aman:57568",
    "Sonakshi:34848"
]
```

---

# 2️⃣ 🔐 Separate Name and Code

Each pair contains a colon:

```text
Anchal:23581
```

Split it using:

```python
name, code = pair.split(":")
```

Now:

```text
name = "Anchal"
code = "23581"
```

---

# 3️⃣ 🔍 Find the Largest Valid Digit

The important rule is:

> A code digit is valid only if it represents a valid **1-based position** in the name.

For example:

```text
Name = Anchal
Length = 6
```

Valid positions are:

```text
1 2 3 4 5 6
```

Therefore:

```text
1 → ✅
2 → ✅
3 → ✅
4 → ✅
5 → ✅
6 → ✅
7 → ❌
8 → ❌
9 → ❌
```

We initialize:

```python
max_digit = -1
```

Then examine every code digit:

```python
for ch in code:
    digit = int(ch)

    if 1 <= digit <= len(name):
        max_digit = max(max_digit, digit)
```

---

# 4️⃣ 🏆 Why Use `max()`?

Suppose:

```text
code = 23581
```

and the name has length `6`.

Valid digits are:

```text
2, 3, 5, 1
```

As we process them:

```text
max = -1
     ↓
2
     ↓
3
     ↓
5
     ↓
5
```

The final value is:

```text
max_digit = 5
```

This avoids storing all valid digits.

---

# 5️⃣ 🔤 Convert 1-Based Position to Python Index

This is an important exam concept.

The problem uses **1-based positions**:

```text
A n c h a l
1 2 3 4 5 6
```

But Python uses **0-based indexing**:

```text
A n c h a l
0 1 2 3 4 5
```

Therefore:

```python
name[max_digit - 1]
```

### Example

If:

```text
max_digit = 5
```

then:

```python
name[5 - 1]
```

becomes:

```python
name[4]
```

which gives:

```text
a
```

---

# 6️⃣ ❌ Handle No Valid Digit

Suppose:

```text
Aman:57568
```

`Aman` has length `4`.

Valid positions:

```text
1 2 3 4
```

Code:

```text
5 7 5 6 8
```

There are no valid positions.

Therefore:

```python
if max_digit == -1:
    result.append("X")
```

The result becomes:

```text
X
```

---

# 7️⃣ 🔗 Build the Final Keyword

For every pair, we append one character:

```python
result.append(...)
```

At the end:

```python
return "".join(result)
```

For example:

```text
['a', 'X', 'i']
```

becomes:

```text
aXi
```

---

# 💻 Complete Python 3 Solution

```python
def code_breaker(s):
    pairs = s.strip().split(",")
    result = []

    for pair in pairs:
        name, code = pair.split(":")
        max_digit = -1

        for ch in code:
            digit = int(ch)

            if 1 <= digit <= len(name):
                max_digit = max(max_digit, digit)

        if max_digit == -1:
            result.append("X")
        else:
            result.append(name[max_digit - 1])

    return "".join(result)


if __name__ == "__main__":
    s = input().strip()
    print(code_breaker(s))
```

---

# 🧪 Dry Run

### 📥 Input

```text
Anchal:23581,Aman:57568,Sonakshi:34848
```

### Pair 1

```text
Anchal:23581
```

```text
Length = 6
Valid digits = 2, 3, 5, 1
Largest = 5
Character = Anchal[4] = a
```

Result:

```text
a
```

---

### Pair 2

```text
Aman:57568
```

```text
Length = 4
Valid digits = none
```

Result:

```text
X
```

---

### Pair 3

```text
Sonakshi:34848
```

```text
Length = 8
Valid digits = 3, 4, 8, 4, 8
Largest = 8
Character = Sonakshi[7] = i
```

Result:

```text
i
```

---

### 🎯 Final Result

```text
aXi
```

---

# ⚠️ Important Concepts

## 🔹 1-Based vs 0-Based Indexing

This is probably the **most important trap** in this problem.

Problem:

```text
Position 1 → first character
```

Python:

```text
Index 0 → first character
```

Therefore:

```python
name[max_digit - 1]
```

### 🧠 Remember

> **Problem position → Python index = position - 1**

---

## 🔹 `0` Is Never a Valid Position

The problem uses **1-based positions**.

Therefore:

```text
0 ❌
1 ✅
2 ✅
...
```

That's why the condition is:

```python
if 1 <= digit <= len(name):
```

---

## 🔹 Invalid Large Digits Are Ignored

If:

```text
name = "Aman"
```

then:

```text
length = 4
```

A code like:

```text
9876
```

contains no valid position.

Therefore:

```text
X
```

---

# 🧩 Pattern Recognition

When you see:

> **"Process multiple items separated by commas."**

Think:

```python
s.split(",")
```

When you see:

> **"Separate two values using `:`."**

Think:

```python
pair.split(":")
```

When you see:

> **"Find the largest valid value."**

Think:

```python
max()
```

When you see:

> **"Position in the problem starts from 1."**

Think:

```python
position - 1
```

When you see:

> **"If no valid value exists, use X."**

Think:

```python
if max_digit == -1:
    result.append("X")
```

---

# 🧠 Exam Recognition Table

| 📝 Problem Clue                   | 💡 Think                |
| --------------------------------- | ----------------------- |
| Multiple pairs separated by comma | `split(",")`            |
| Name and code separated by `:`    | `split(":")`            |
| Find largest valid digit          | `max()`                 |
| Valid position                    | `1 ≤ digit ≤ len(name)` |
| 1-based position                  | `index = position - 1`  |
| No valid digit                    | Append `"X"`            |
| Build final string                | `"".join(result)`       |
| Process every pair                | `for` loop              |

---

# ⏱️ Complexity Analysis

Let:

* `P` = number of `name:code` pairs
* `C` = total number of digits across all codes
* `L` = maximum name length

For each code digit, we perform constant-time validation and maximum selection.

Therefore:

```text
⏱️ Time Complexity: O(C)
```

Building the final result requires:

```text
💾 Space Complexity: O(P)
```

The input itself requires storage proportional to its size.

---

# 🗺️ Complete Mental Model

```text
                 🔐 CODE BREAKER
                       │
                       ▼
                 📥 Read Input
                       │
                       ▼
               ✂️ Split by ","
                       │
                       ▼
                🔁 For each pair
                       │
                       ▼
                 ✂️ Split by ":"
                       │
                ┌──────┴──────┐
                ▼             ▼
              NAME           CODE
                │             │
                │             ▼
                │       🔢 Check digits
                │             │
                │             ▼
                │       ✅ Valid position?
                │             │
                │             ▼
                │       🏆 Largest digit
                │             │
                └──────┬──────┘
                       ▼
                🔤 Get character
                       │
                 No valid digit?
                    ↙       ↘
                  YES        NO
                   ↓          ↓
                  "X"    name[position-1]
                    \       /
                     \     /
                       ▼
                 🔗 Join results
                       │
                       ▼
                 🎯 KEYWORD
```

---

# ⭐ Final Takeaway

The entire problem can be reduced to:

```text
✂️ Split pairs
    ↓
🔐 Separate name + code
    ↓
🔢 Check every digit
    ↓
🏆 Find largest valid position
    ↓
🔤 Convert position → index
    ↓
❌ None → X
    ↓
🔗 Join characters
```

### 🚀 One-Line Memory Trick

> **Split → Validate → Max → Index-1 → Character → Join**

The biggest thing to remember for the exam is:

```python
name[max_digit - 1]
```

because the problem gives you a **1-based position**, while Python uses **0-based indexing**.
