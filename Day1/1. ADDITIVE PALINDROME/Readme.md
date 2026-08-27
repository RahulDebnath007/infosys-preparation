# 🔄 Additive Palindrome

> 🧩 **Pattern:** String Manipulation + Number Reversal + Simulation
> 🎯 **Goal:** Keep adding a number to its reverse until the result becomes a palindrome.

---

## 📌 Problem Statement

Given a positive integer `num`, repeatedly perform the following operation:

```text
num + reverse(num)
```

Continue the process until the resulting number becomes a **palindrome**.

### 💡 Example

Starting with `195`:

```text
195 + 591 = 786
786 + 687 = 1473
1473 + 3741 = 5214
5214 + 4125 = 9339
```

Since `9339` is a palindrome, the process stops.

---

## 📝 Input Format

A single line containing a positive integer:

```text
num
```

---

## 📤 Output Format

Print the resulting palindrome number.

---

## 🔢 Constraints

```text
1 ≤ num ≤ 10^4
```

---

# 🧠 Core Concept

The problem follows a simple **simulation pattern**:

```text
       ┌──────────────┐
       │    Number    │
       └──────┬───────┘
              ↓
      🔄 Reverse Number
              ↓
       ➕ Add Both
              ↓
      🔍 Is Palindrome?
          ↙         ↘
        YES          NO
         ↓            ↓
      🛑 STOP       🔄 Repeat
```

---

# 🛠️ Step-by-Step Logic

## 1️⃣ Check for Palindrome

A number is a palindrome if it reads the same from both directions.

### ✅ Palindromes

```text
121
1331
9339
```

### ❌ Not Palindromes

```text
123
195
786
```

### 🐍 Python

```python
def is_palindrome(num):
    return str(num) == str(num)[::-1]
```

### 🔍 How does it work?

For:

```text
num = 195
```

Convert it to a string:

```text
"195"
```

Reverse it:

```text
"591"
```

Compare:

```text
"195" == "591"
```

Result:

```text
False ❌
```

For:

```text
num = 9339
```

we get:

```text
"9339" == "9339"
```

Result:

```text
True ✅
```

---

# 2️⃣ 🔄 Reverse the Number

We need the reverse of the current number before every addition.

```python
def reverse_number(num):
    return int(str(num)[::-1])
```

### Example

```text
195
 ↓
"195"
 ↓
"591"
 ↓
591
```

So:

```text
reverse_number(195) → 591
```

---

# 3️⃣ 🔁 Repeat the Operation

Now repeatedly add the number to its reverse.

```python
while not is_palindrome(num):
    num += reverse_number(num)
```

The loop continues while the number is **not** a palindrome.

As soon as a palindrome is produced, the loop stops.

---

# 💻 Complete Solution

```python
def is_palindrome(num):
    return str(num) == str(num)[::-1]


def reverse_number(num):
    return int(str(num)[::-1])


def find_palindrome(num):
    iterations = 0

    while not is_palindrome(num):
        num += reverse_number(num)
        iterations += 1

        # Safety limit
        if iterations > 1000:
            break

    return num


num = int(input())

print(find_palindrome(num))
```

---

# 🧪 Dry Run

### 📥 Input

```text
195
```

### 🔄 Iteration 1

```text
Current number = 195
Reverse        = 591

195 + 591 = 786
```

❌ `786` is not a palindrome.

---

### 🔄 Iteration 2

```text
Current number = 786
Reverse        = 687

786 + 687 = 1473
```

❌ `1473` is not a palindrome.

---

### 🔄 Iteration 3

```text
Current number = 1473
Reverse        = 3741

1473 + 3741 = 5214
```

❌ `5214` is not a palindrome.

---

### 🔄 Iteration 4

```text
Current number = 5214
Reverse        = 4125

5214 + 4125 = 9339
```

✅ `9339` is a palindrome.

### 🎯 Final Output

```text
9339
```

---

# ⚠️ Important Edge Case

What happens if the input is **already a palindrome**?

### 📥 Input

```text
121
```

Check:

```text
121 == reverse(121)
```

```text
121 == 121
```

✅ Already a palindrome.

Therefore, no operation is required.

### 📤 Output

```text
121
```

---

# 🧩 Problem Pattern

This is mainly a:

### 🔹 String Manipulation

Used for reversing and checking the number.

```python
str(num)[::-1]
```

### 🔹 Simulation

The operation is repeatedly performed until a condition becomes true.

```python
while not is_palindrome(num):
```

### 🔹 Palindrome Checking

Compare the original value with its reverse.

```python
str(num) == str(num)[::-1]
```

---

# 🧠 Recognition Rule

When you see:

> 🔄 **"Keep reversing and adding until the number becomes a palindrome."**

Immediately think:

```text
🔄 Reverse
   ↓
➕ Add
   ↓
🔍 Check Palindrome
   ↓
🔁 Repeat
```

### 🚨 Exam Shortcut

Remember this core structure:

```python
while not is_palindrome(num):
    num += reverse_number(num)
```

That's the heart of the problem.

---

# ⏱️ Complexity Analysis

Let:

* `k` = number of iterations
* `d` = number of digits

Each iteration performs reversal, comparison, and addition.

Therefore:

```text
⏱️ Time Complexity  : O(k × d)
💾 Space Complexity : O(d)
```

The `1000` iteration limit is simply a **safety safeguard**.

---

# 📚 What You Should Learn From This Problem

This problem is useful because it combines several common coding patterns:

| 🎯 Concept          | 💡 What to Remember              |
| ------------------- | -------------------------------- |
| 🔄 Reverse          | `str(num)[::-1]`                 |
| 🔍 Palindrome       | Original == Reverse              |
| 🔁 Simulation       | Repeat until condition           |
| ➕ Arithmetic        | Add number + reverse             |
| 🧩 Helper Functions | Break logic into small functions |

---

# 🗺️ Mental Model

```text
             START
               │
               ▼
        🔢 Read number
               │
               ▼
      🔍 Is it palindrome?
          │           │
        YES           NO
          │            │
          ▼            ▼
       🛑 STOP     🔄 Reverse
                       │
                       ▼
                  ➕ Add
                       │
                       ▼
                  🔁 Repeat
```

---

# ⭐ Final Takeaway

Don't overcomplicate this problem.

The complete thought process is:

```text
🔢 Number
   ↓
🔄 Reverse it
   ↓
➕ Add both
   ↓
🔍 Check palindrome
   ↓
❌ Not palindrome → Repeat
   ↓
✅ Palindrome → Print
```

### 🧠 Remember:

> **Reverse → Add → Check → Repeat**

This is a classic **simulation + palindrome** pattern that can appear in coding assessments and placement exams.
