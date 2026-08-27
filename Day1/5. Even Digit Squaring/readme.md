# 🔢 Even Digit Squaring

> 🧩 **Pattern:** String Traversal + 1-Based Indexing + Arithmetic + Early Stopping
> 🎯 **Goal:** Take digits at **even positions**, square them, concatenate the results, and print the **first four digits**.

---

## 📌 Problem Statement

Given a string of digits `S`:

1. 🔍 Consider the digits at **even positions** using **1-based indexing**.
2. ⬜ Square each selected digit.
3. 🔗 Concatenate the squared values.
4. ✂️ Print only the **first four digits** of the resulting string.

### ⚠️ Important

The problem uses **1-based indexing**.

For:

```text
S = 5 6 2 4 3 8 1 2 7 5
    1 2 3 4 5 6 7 8 9 10
```

The even positions are:

```text
2, 4, 6, 8, 10
```

Therefore, we select:

```text
6, 4, 8, 2, 5
```

---

# 🧪 Sample

### 📥 Input

```text
5624381275
```

### 🔍 Position Mapping

```text
Digit:     5 6 2 4 3 8 1 2 7 5
Position:  1 2 3 4 5 6 7 8 9 10
               ↑   ↑   ↑   ↑    ↑
```

Selected digits:

```text
6 4 8 2 5
```

---

## 🧮 Square Each Selected Digit

```text
6² = 36
4² = 16
8² = 64
2² = 4
5² = 25
```

Concatenate:

```text
36 + 16 + 64 + 4 + 25
```

Result:

```text
361664425
```

We only need the first four digits:

```text
3616
```

### 📤 Output

```text
3616
```

---

# 📥 Input Format

A single line containing a string of digits `S`.

```text
S
```

---

# 📤 Output Format

Print a string containing the **first four digits** of the concatenated squared values.

---

# 🔢 Constraints

```text
4 ≤ |S| ≤ 10^5
0 ≤ S[i] ≤ 9
```

---

# 🧠 Core Idea

The entire problem follows this pattern:

```text
📥 Input String
      ↓
🔢 Find Even Positions
      ↓
🧮 Square Each Digit
      ↓
🔗 Concatenate Results
      ↓
✂️ Take First 4 Digits
      ↓
🎯 Output
```

---

# 1️⃣ 🔢 Understanding Even Positions

The problem says **even positions using 1-based indexing**.

Example:

```text
Position:  1  2  3  4  5  6  7  8
           ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓
String:    5  6  2  4  3  8  1  2
```

Even positions:

```text
2, 4, 6, 8
```

Selected digits:

```text
6, 4, 8, 2
```

---

# 2️⃣ 🐍 Convert 1-Based Position to Python Index

Python uses **0-based indexing**.

So:

```text
Problem Position → Python Index

1 → 0
2 → 1
3 → 2
4 → 3
5 → 4
```

Therefore, even positions correspond to Python indices:

```text
1, 3, 5, 7, ...
```

That's why we use:

```python
for i in range(1, len(S), 2):
```

### 🧠 Remember

> **Even 1-based positions = Odd 0-based indices**

This is one of the main traps in this problem.

---

# 3️⃣ 🧮 Square Each Digit

For every selected character:

```python
int(S[i])
```

converts it into an integer.

Then:

```python
int(S[i]) ** 2
```

squares it.

For example:

```text
S[i] = '8'

int('8') = 8

8 ** 2 = 64
```

We convert the result back to a string:

```python
str(int(S[i]) ** 2)
```

because we need to concatenate the results.

---

# 4️⃣ 🔗 Store the Squared Results

We create an empty list:

```python
res = []
```

Then:

```python
res.append(str(int(S[i]) ** 2))
```

For:

```text
6, 4, 8
```

the list becomes:

```text
['36', '16', '64']
```

---

# 5️⃣ ✂️ Only Keep the First Four Digits

The problem does **not** require the complete result.

We only need:

```text
🎯 First 4 digits
```

For example:

```text
Complete result:
361664425
```

We need:

```text
3616
```

So we use:

```python
"".join(res)[:4]
```

### 🔍 What does this do?

First:

```python
"".join(res)
```

converts:

```text
['36', '16', '64']
```

into:

```text
361664
```

Then:

```python
[:4]
```

takes:

```text
3616
```

---

# ⚡ 6️⃣ Early Stopping Optimization

Because we only need **four digits**, there is no reason to process the entire input once we already have enough output.

The code checks:

```python
if sum(len(x) for x in res) >= 4:
    break
```

Once at least four output digits have been generated:

```text
🛑 STOP PROCESSING
```

This is useful because:

```text
|S| ≤ 100000
```

The input could be very large.

### 🧠 Optimization Pattern

```text
Need only first K results
        ↓
Stop as soon as K results are available
```

---

# 💻 Complete Python 3 Solution

```python
S = input().strip()
res = []

for i in range(1, len(S), 2):
    res.append(str(int(S[i]) ** 2))

    if sum(len(x) for x in res) >= 4:
        break

print("".join(res)[:4])
```

---

# 🧪 Dry Run

### 📥 Input

```text
5624381275
```

### Step 1 — Select Even Positions

```text
Position:  1 2 3 4 5 6 7 8 9 10
Digit:     5 6 2 4 3 8 1 2 7 5
              ↑   ↑   ↑   ↑    ↑
```

Selected:

```text
6 4 8 2 5
```

---

### Step 2 — Square

```text
6² = 36
4² = 16
8² = 64
2² = 4
5² = 25
```

---

### Step 3 — Concatenate

```text
361664425
```

---

### Step 4 — Take First Four

```text
3616
```

### 📤 Output

```text
3616
```

---

# 🧪 Another Example

### 📥 Input

```text
123456
```

Positions:

```text
Position: 1 2 3 4 5 6
Digit:    1 2 3 4 5 6
             ↑   ↑   ↑
```

Selected:

```text
2 4 6
```

Square:

```text
2² = 4
4² = 16
6² = 36
```

Concatenate:

```text
41636
```

First four digits:

```text
4163
```

### 📤 Output

```text
4163
```

---

# ⚠️ Important Edge Cases

## 🔹 Case 1 — Squared Digit Has One Digit

If the selected digit is:

```text
2
```

then:

```text
2² = 4
```

Only **one output digit** is produced.

---

## 🔹 Case 2 — Squared Digit Has Two Digits

For:

```text
8
```

we get:

```text
8² = 64
```

So two digits are added to the concatenated result.

---

## 🔹 Case 3 — Zero

If:

```text
0² = 0
```

the output contains:

```text
0
```

Zero is a valid digit and must not be ignored.

---

# 🧩 Pattern Recognition

When you see:

> **"Take characters at even positions."**

Think:

```python
range(1, len(S), 2)
```

because the problem uses 1-based indexing.

---

When you see:

> **"Square each digit."**

Think:

```python
int(S[i]) ** 2
```

---

When you see:

> **"Concatenate the results."**

Think:

```python
"".join(res)
```

---

When you see:

> **"Only output the first four digits."**

Think:

```python
[:4]
```

---

When you see:

> **"Stop once enough output is generated."**

Think:

```text
⚡ Early Stopping
```

---

# 🧠 Exam Recognition Table

| 📝 Problem Clue             | 💡 Think              |
| --------------------------- | --------------------- |
| Even positions              | `range(1, len(S), 2)` |
| 1-based indexing            | Position − 1          |
| Square digit                | `** 2`                |
| Convert character to number | `int()`               |
| Convert result to string    | `str()`               |
| Concatenate strings         | `"".join()`           |
| First 4 characters          | `[:4]`                |
| Stop when enough output     | `break`               |
| Large input                 | ⚡ Early stopping      |

---

# 🚨 Most Important Trap

Do **not** write:

```python
for i in range(0, len(S), 2):
```

That selects:

```text
1st, 3rd, 5th, 7th...
```

positions.

But the problem asks for:

```text
2nd, 4th, 6th, 8th...
```

So the correct code is:

```python
for i in range(1, len(S), 2):
```

### 🧠 Memorize This

```text
1-based even position
        ↓
0-based odd index
        ↓
start = 1
step  = 2
```

---

# ⏱️ Complexity Analysis

Let `n = |S|`.

Normally, we might process approximately:

```text
n / 2
```

characters.

However, because we stop once four output digits are available, only a small prefix may need to be processed.

### ⏱️ Time Complexity

Worst case:

```text
O(n)
```

With early stopping, practical work is usually much smaller.

### 💾 Space Complexity

The result list stores only the squared values needed to produce four output digits:

```text
O(1)
```

with respect to the input size, because we stop after generating enough output.

---

# 🗺️ Complete Mental Model

```text
                 📥 STRING S
                      │
                      ▼
            🔢 Start at index 1
                      │
                      ▼
             ➡️ Move by 2
                      │
                      ▼
              🧮 Square digit
                      │
                      ▼
               🔤 Convert to str
                      │
                      ▼
               🔗 Add to result
                      │
                      ▼
             ❓ Have 4 digits?
                /         \
              YES          NO
               │            │
               ▼            │
            🛑 STOP         │
                            │
                            └──→ 🔁 Next even position
                      │
                      ▼
                 ✂️ [:4]
                      │
                      ▼
                  🎯 OUTPUT
```

---

# ⭐ Final Takeaway

The entire problem can be remembered as:

```text
🔢 EVEN POSITION
      ↓
🧮 SQUARE
      ↓
🔗 CONCATENATE
      ↓
✂️ FIRST 4
```

### 🚀 One-Line Memory Trick

> **1-based even position → Python index 1,3,5,... → square → join → take `[:4]`.**

The most important line for the exam is:

```python
for i in range(1, len(S), 2):
```

because it correctly converts the problem's **1-based even positions** into Python's **0-based indices**.
