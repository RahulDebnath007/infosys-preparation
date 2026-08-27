# 🪞 Palindrome Sum

> 🧩 **Pattern:** Palindrome + Searching + Simulation
> 🎯 **Goal:** Find the nearest palindromes around `N`, add them, and repeat until their sum is also a palindrome.

---

## 📌 Problem Statement

Given an integer `N`, find two special palindromic numbers:

* 🔽 **`num1`** → the largest palindrome **smaller than `N`**
* 🔼 **`num2`** → the smallest palindrome **greater than `N`**

Then calculate:

```text
final_number = num1 + num2
```

If `final_number` is a palindrome:

```text
✅ Print it and stop.
```

Otherwise:

```text
❌ Decrease N by 1
🔁 Repeat the entire process
```

---

## 🧪 Example

For:

```text
N = 123
```

The largest palindrome smaller than `123` is:

```text
121
```

The smallest palindrome greater than `123` is:

```text
131
```

Calculate:

```text
121 + 131 = 252
```

Since `252` is a palindrome:

```text
🎯 Answer = 252
```

---

# 📥 Input Format

A single line containing an integer `N`.

```text
N
```

---

# 📤 Output Format

Print the palindrome `final_number`.

---

# 🔢 Constraints

```text
1 ≤ N ≤ 10^4
```

---

# 🧠 Core Idea

The problem combines **three important concepts**:

```text
🔍 Search for previous palindrome
          +
🔍 Search for next palindrome
          +
🔁 Repeat until sum is palindrome
```

The overall flow is:

```text
              🔢 N
               │
       ┌───────┴───────┐
       ▼               ▼
 🔽 Previous       🔼 Next
  Palindrome       Palindrome
       │               │
       └───────┬───────┘
               ▼
          ➕ Add them
               │
               ▼
       🔍 Is sum palindrome?
          │           │
        YES           NO
          │            │
          ▼            ▼
       🛑 STOP      N = N - 1
                       │
                       └──────→ 🔁 Repeat
```

---

# 🛠️ Step-by-Step Logic

## 1️⃣ Check if a Number is a Palindrome

First, we need a helper function to determine whether a number is a palindrome.

```python
def is_palindrome(num):
    s = str(num)
    return s == s[::-1]
```

### 🔍 Example

For:

```text
121
```

we get:

```text
s     = "121"
s[::-1] = "121"
```

Therefore:

```text
"121" == "121"
```

✅ `True`

For:

```text
123
```

we get:

```text
"123" != "321"
```

❌ `False`

---

# 2️⃣ 🔽 Find the Previous Palindrome

We need the **largest palindrome smaller than `N`**.

Start at:

```text
N - 1
```

and move downward.

```python
def largest_palindrome_less(N):
    for i in range(N - 1, -1, -1):
        if is_palindrome(i):
            return i
```

### Example

For:

```text
N = 123
```

the search looks like:

```text
122 ❌
121 ✅
```

Therefore:

```text
num1 = 121
```

### 🧠 Key Pattern

```text
Start at N - 1
      ↓
Move downward
      ↓
First palindrome = answer
```

Because we search from the largest candidate downward, the **first palindrome found is automatically the largest palindrome smaller than `N`**.

---

# 3️⃣ 🔼 Find the Next Palindrome

Now we need the **smallest palindrome greater than `N`**.

Start at:

```text
N + 1
```

and move upward until a palindrome is found.

```python
def smallest_palindrome_greater(N):
    i = N + 1

    while True:
        if is_palindrome(i):
            return i
        i += 1
```

### Example

For:

```text
N = 123
```

the search looks like:

```text
124 ❌
125 ❌
126 ❌
...
130 ❌
131 ✅
```

Therefore:

```text
num2 = 131
```

### 🧠 Key Pattern

```text
Start at N + 1
      ↓
Move upward
      ↓
First palindrome = answer
```

---

# 4️⃣ ➕ Calculate the Palindrome Sum

Once we have both values:

```python
num1 = largest_palindrome_less(N)
num2 = smallest_palindrome_greater(N)
```

calculate:

```python
final_number = num1 + num2
```

Then check:

```python
if is_palindrome(final_number):
```

---

# 5️⃣ 🔁 Repeat if Necessary

If the sum is not a palindrome:

```python
N -= 1
```

Then perform the entire process again.

```text
N
 ↓
Find previous palindrome
 ↓
Find next palindrome
 ↓
Add
 ↓
Palindrome?
 ├── YES → 🛑 Print
 └── NO  → N -= 1 → 🔁 Repeat
```

---

# 💻 Complete Python 3 Solution

```python
def is_palindrome(num):
    s = str(num)
    return s == s[::-1]


def largest_palindrome_less(N):
    for i in range(N - 1, -1, -1):
        if is_palindrome(i):
            return i


def smallest_palindrome_greater(N):
    i = N + 1

    while True:
        if is_palindrome(i):
            return i

        i += 1


N = int(input())

while True:
    num1 = largest_palindrome_less(N)
    num2 = smallest_palindrome_greater(N)

    final_number = num1 + num2

    if is_palindrome(final_number):
        print(final_number)
        break

    N -= 1
```

---

# 🧪 Dry Run

## 📥 Input

```text
123
```

### 🔽 Find `num1`

Largest palindrome `< 123`:

```text
122 ❌
121 ✅
```

Therefore:

```text
num1 = 121
```

### 🔼 Find `num2`

Smallest palindrome `> 123`:

```text
124 ❌
125 ❌
...
131 ✅
```

Therefore:

```text
num2 = 131
```

### ➕ Add

```text
121 + 131 = 252
```

### 🔍 Check

```text
252 → palindrome ✅
```

### 📤 Output

```text
252
```

---

# ⚠️ Important Detail

The two searches have **different directions**.

### Previous palindrome

```python
for i in range(N - 1, -1, -1):
```

⬇️ Move downward.

### Next palindrome

```python
i = N + 1

while True:
    ...
    i += 1
```

⬆️ Move upward.

Remember:

```text
🔽 num1 → largest palindrome BELOW N
🔼 num2 → smallest palindrome ABOVE N
```

---

# 🧩 Pattern Recognition

When a coding question says:

> **"Find the largest palindrome smaller than N."**

Think:

```text
🔽 Search backward
```

When it says:

> **"Find the smallest palindrome greater than N."**

Think:

```text
🔼 Search forward
```

When it says:

> **"Repeat until a condition becomes true."**

Think:

```text
🔁 Simulation
```

---

# 🧠 Exam Recognition Table

| 📝 Problem Clue        | 💡 Think                |
| ---------------------- | ----------------------- |
| Check palindrome       | 🔍 String + Reverse     |
| Largest value below N  | 🔽 Search backward      |
| Smallest value above N | 🔼 Search forward       |
| Repeat until condition | 🔁 Simulation           |
| Sum of two values      | ➕ Arithmetic            |
| `N -= 1` and retry     | 🔄 Iterative simulation |

---

# ⏱️ Complexity Analysis

Let `k` be the number of outer iterations and `d` the number of digits.

For each value of `N`, the program searches for nearby palindromes.

Each palindrome check takes approximately:

```text
O(d)
```

Because:

```python
str(num)
```

and:

```python
s[::-1]
```

operate on the digits.

For the given constraint:

```text
N ≤ 10^4
```

the brute-force search is small and easily practical.

### 💾 Space Complexity

```text
O(d)
```

for the temporary string used during palindrome checking.

---

# 🗺️ Complete Mental Model

```text
                 🔢 INPUT N
                     │
                     ▼
          🔽 Find palindrome < N
                     │
                     ▼
          🔼 Find palindrome > N
                     │
                     ▼
                 ➕ ADD
                     │
                     ▼
          🔍 Is the SUM palindrome?
                /           \
              YES            NO
               │              │
               ▼              ▼
          🖨️ PRINT         N = N - 1
               │              │
               ▼              │
             🛑 STOP          │
                              │
                              └──→ 🔁 REPEAT
```

---

# ⭐ Final Takeaway

This problem is not really about complicated palindrome mathematics.

It is a **search + simulation** problem.

Remember the sequence:

```text
🔽 Search backward
      ↓
🔼 Search forward
      ↓
➕ Add
      ↓
🔍 Check palindrome
      ↓
❌ Not palindrome → N -= 1
      ↓
🔁 Repeat
      ↓
✅ Palindrome → Print
```

### 🚀 One-Line Memory Trick

> **Previous Palindrome + Next Palindrome → Add → Check → Decrease N → Repeat**

This pattern is worth remembering for coding assessments because the same **search + condition + simulation** structure can appear with numbers other than palindromes.
