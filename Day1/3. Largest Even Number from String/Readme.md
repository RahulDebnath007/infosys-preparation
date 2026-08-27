# 🔢 Largest Even Number from String

> 🧩 **Pattern:** String Processing + Filtering + Sorting + Greedy
> 🎯 **Goal:** Extract all digits from a mixed string and rearrange them to form the **largest possible even number**.

---

## 📌 Problem Statement

You are given a string `S` containing:

* 🔤 Alphabetic characters
* 🔢 Digits
* 🔣 Special characters

Your task is to:

1. 🔍 Extract all digits from the string.
2. 🔽 Arrange them to form the **largest possible number**.
3. ⚡ Ensure that the resulting number is **even**.
4. ❌ If no even number can be formed, print `-1`.

### 💡 Important Rule

A number is even if its last digit is one of:

```text
0 2 4 6 8
```

Therefore, the final digit of our answer **must be even**.

---

# 🧪 Example

### 📥 Input

```text
asdf@75483
```

### 🔍 Extract digits

```text
7 5 4 8 3
```

### 🔽 Sort in descending order

```text
8 7 5 4 3
```

If we simply use this:

```text
87543
```

❌ It is odd because the last digit is `3`.

We need an even digit at the end.

The smallest available even digit is:

```text
4
```

Move `4` to the end:

```text
87534
```

### 📤 Output

```text
87534
```

✅ Largest possible even number.

---

# 📥 Input Format

A single line containing a string `S`.

```text
S
```

---

# 📤 Output Format

Print the largest possible even number that can be formed.

If no even number can be formed, print:

```text
-1
```

---

# 🔢 Constraints

```text
1 ≤ |S| ≤ 1000
```

---

# 🧠 Core Idea

The problem can be broken into four steps:

```text
🔍 Extract Digits
       ↓
🔽 Sort Descending
       ↓
⚡ Find Smallest Even Digit
       ↓
🔄 Move It to the End
       ↓
🏆 Largest Even Number
```

---

# 1️⃣ 🔍 Extract All Digits

The input contains characters that are not necessarily digits.

For example:

```text
asdf@75483
```

We only need:

```text
75483
```

Python provides:

```python
ch.isdigit()
```

to check whether a character is a digit.

### 🐍 Code

```python
digits = [ch for ch in S if ch.isdigit()]
```

### 🔍 Example

```text
Input:
a7b5@4#8c3

Extracted:
7 5 4 8 3
```

---

# 2️⃣ 🔽 Sort Digits in Descending Order

To create the **largest possible number**, larger digits should appear toward the beginning.

So:

```text
7 5 4 8 3
```

becomes:

```text
8 7 5 4 3
```

### 🐍 Code

```python
digits = sorted(digits, reverse=True)
```

Now:

```text
digits = ['8', '7', '5', '4', '3']
```

---

# 3️⃣ ⚡ Find an Even Digit

A number is even when its final digit is:

```text
0, 2, 4, 6, 8
```

So we search the extracted digits for even digits.

```python
even_digits = [d for d in digits if int(d) % 2 == 0]
```

For:

```text
8 7 5 4 3
```

we get:

```text
8 4
```

Therefore, an even number **can** be formed.

---

# 4️⃣ 🏆 Choose the Smallest Even Digit

This is the most important part of the problem.

Suppose our digits are:

```text
8 7 5 4 3
```

The even digits are:

```text
8 4
```

Which one should go at the end?

We choose:

```text
4
```

### ❓ Why not `8`?

If we put `8` at the end:

```text
75438
```

But if we put `4` at the end:

```text
87534
```

Compare:

```text
87534
75438
```

Clearly:

```text
87534 > 75438
```

So we should preserve the largest digits for the most significant positions.

### 🧠 Greedy Rule

> **Keep the largest digits toward the front and use the smallest available even digit as the final digit.**

---

# 5️⃣ 🔄 Move the Even Digit to the End

After sorting:

```text
8 7 5 4 3
```

Select:

```text
4
```

Remove it:

```text
8 7 5 3
```

Append it:

```text
8 7 5 3 4
```

Final number:

```text
87534
```

---

# 🚨 What If There Is No Even Digit?

Consider:

```text
Input:
abc75391
```

Extracted digits:

```text
7 5 3 9 1
```

There is no:

```text
0 2 4 6 8
```

Therefore, no even number can be formed.

### 📤 Output

```text
-1
```

---

# 💻 Complete Python 3 Solution

```python
import sys

# Read input
S = sys.stdin.readline().strip()

# Extract digits and sort in descending order
digits = sorted(
    [ch for ch in S if ch.isdigit()],
    reverse=True
)

# Find even digits
even_digits = [d for d in digits if int(d) % 2 == 0]

# No even digit → impossible
if not even_digits:
    print(-1)

else:
    # Choose the smallest even digit
    last_digit = even_digits[-1]

    # Move it to the end
    digits.remove(last_digit)
    digits.append(last_digit)

    # Form the final number
    print("".join(digits))
```

---

# 🧪 Dry Run

## Example 1

### 📥 Input

```text
asdf@75483
```

### Step 1 — Extract digits

```text
7 5 4 8 3
```

### Step 2 — Sort descending

```text
8 7 5 4 3
```

### Step 3 — Find even digits

```text
8 4
```

### Step 4 — Choose smallest even digit

```text
4
```

### Step 5 — Move it to the end

```text
8 7 5 3 4
```

### 📤 Output

```text
87534
```

---

# 🧪 Dry Run — No Even Digit

### 📥 Input

```text
abc75391
```

### 🔍 Extract

```text
7 5 3 9 1
```

### ⚡ Even digits

```text
None ❌
```

Therefore:

```text
-1
```

---

# 🧩 Pattern Recognition

When you see:

> **"Extract digits from a string"**

Think:

```python
[ch for ch in S if ch.isdigit()]
```

When you see:

> **"Form the largest number"**

Think:

```python
sorted(digits, reverse=True)
```

When you see:

> **"Number must be even"**

Think:

```text
Last digit ∈ {0, 2, 4, 6, 8}
```

When you see:

> **"Largest possible number + even condition"**

Think:

```text
🏆 Greedy
```

---

# 🧠 Exam Recognition Table

| 📝 Problem Clue             | 💡 Think               |
| --------------------------- | ---------------------- |
| Extract numbers from string | 🔍 `.isdigit()`        |
| Largest possible number     | 🔽 Sort descending     |
| Number must be even         | ⚡ Even digit at end    |
| Preserve largest digits     | 🏆 Greedy              |
| No even digit               | ❌ `-1`                 |
| Rearrange characters        | 🔄 String manipulation |

---

# ⚠️ Important Insight

The key mistake to avoid is:

```text
❌ Sort digits and simply check if the result is even.
```

For example:

```text
Digits:
8 7 5 4 3

Descending:
87543
```

`87543` is odd.

You cannot just stop.

Instead:

```text
87543
   ↑
Need an even digit here
```

Take the **smallest available even digit**:

```text
4
```

and move it to the end:

```text
87534
```

That preserves the largest possible prefix.

---

# ⏱️ Complexity Analysis

Let `n = |S|`.

### 🔍 Extracting digits

```text
O(n)
```

### 🔽 Sorting

If there are `d` digits:

```text
O(d log d)
```

Since:

```text
d ≤ n
```

overall:

```text
⏱️ Time Complexity: O(n log n)
```

### 💾 Space Complexity

The digit list and sorted list require:

```text
O(n)
```

So:

```text
💾 Space Complexity: O(n)
```

---

# 🗺️ Complete Mental Model

```text
                 📥 INPUT STRING
                       │
                       ▼
                🔍 Extract digits
                       │
                       ▼
               🔽 Sort descending
                       │
                       ▼
              ⚡ Find even digits
                       │
              ┌────────┴────────┐
              │                 │
           NONE              EXISTS
              │                 │
              ▼                 ▼
           🖨️ -1        Choose smallest
                         even digit
                              │
                              ▼
                       🔄 Move to end
                              │
                              ▼
                         🏆 ANSWER
```

---

# ⭐ Final Takeaway

The entire problem can be remembered with one simple sequence:

```text
🔍 EXTRACT
    ↓
🔽 SORT DESCENDING
    ↓
⚡ FIND EVEN DIGIT
    ↓
🎯 PICK SMALLEST EVEN
    ↓
🔄 MOVE IT TO END
    ↓
🏆 PRINT
```

### 🚀 One-Line Memory Trick

> **For the largest even number: maximize the prefix, sacrifice the smallest even digit for the last position.**

This is a useful **Greedy + String Processing** pattern for coding assessments.
