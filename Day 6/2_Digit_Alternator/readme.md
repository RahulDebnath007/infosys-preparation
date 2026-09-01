# 🔢 Digit Alternator

## 📌 Problem Overview

You are given a string `S` containing:

* Letters
* Digits
* Special characters

The string is guaranteed to contain:

* At least one special character
* At least one even digit
* At least one odd digit

The task is to rearrange the digits according to the number of special characters.

### Rule

1. Count the number of special characters.
2. If the number of special characters is **even**, start with an **even digit**.
3. If the number of special characters is **odd**, start with an **odd digit**.
4. Alternate between even and odd digits as long as both groups have elements.
5. When one group is exhausted, append all remaining digits from the other group.
6. Print the resulting digits without spaces.

---

# 🧩 Problem Statement

For example:

```text
A5c67r21i@p#8t
```

The digits are:

```text
5 6 7 2 1 8
```

The special characters are:

```text
@ #
```

There are:

```text
2 special characters
```

Since `2` is even, we start with an even digit.

The even digits are:

```text
6 2 8
```

The odd digits are:

```text
5 7 1
```

Alternating them gives:

```text
6 5 2 7 8 1
```

Therefore:

```text
652781
```

---

# 📥 Input

A single line containing the string:

```text
S
```

### Constraints

```text
3 ≤ |S| ≤ 10⁶
```

The string contains at least:

```text
1 special character
1 even digit
1 odd digit
```

---

# 📤 Output

Print the rearranged digits as a single string.

There should be:

* No spaces
* No additional characters

---

# 🧪 Example

### Input

```text
A5c67r21i@p#8t
```

### Output

```text
652781
```

---

# 🔍 Example Explanation

### Step 1 — Find Special Characters

The special characters are:

```text
@
#
```

Count:

```text
2
```

Since:

```text
2 % 2 == 0
```

the count is even.

Therefore:

```text
Start with EVEN
```

---

### Step 2 — Separate Digits

Even digits:

```text
6 2 8
```

Odd digits:

```text
5 7 1
```

---

### Step 3 — Alternate

Start with even:

```text
6
```

Then odd:

```text
5
```

Then even:

```text
2
```

Then odd:

```text
7
```

Then even:

```text
8
```

Then odd:

```text
1
```

Final result:

```text
652781
```

---

# 🧠 Intuition

The problem has two independent parts:

```text
String
  ↓
Count Special Characters
  ↓
Determine Starting Group
```

and:

```text
String
  ↓
Separate Digits
 ↙        ↘
Even      Odd
  ↓         ↓
     Alternate
        ↓
     Final String
```

The important observation is that we do **not** need to preserve the original positions of the digits.

We only need to preserve their order **within their respective groups**.

For example:

```text
Original digits:
5 6 7 2 1 8

Even:
6 2 8

Odd:
5 7 1
```

The even digits remain:

```text
6 → 2 → 8
```

and the odd digits remain:

```text
5 → 7 → 1
```

We simply merge the two sequences alternately.

---

# 🧠 Step 1 — Categorize Characters

We scan the string once.

For every character:

### If it is a digit

Use:

```python
ch.isdigit()
```

Then convert it to an integer:

```python
int(ch)
```

Check whether it is even:

```python
int(ch) % 2 == 0
```

If true:

```text
Even group
```

Otherwise:

```text
Odd group
```

---

### If it is not a letter or digit

It is considered a special character.

We increment:

```python
special_count += 1
```

The condition can be expressed as:

```python
not ch.isalnum()
```

---

# 💡 Step 2 — Determine the Starting Group

The problem gives us the rule:

```text
Special count is even → Start with even
Special count is odd  → Start with odd
```

We can represent this using:

```python
turn_even = (special_count % 2 == 0)
```

Therefore:

```text
special_count = 2
        ↓
turn_even = True
        ↓
Start with EVEN
```

or:

```text
special_count = 3
        ↓
turn_even = False
        ↓
Start with ODD
```

---

# 🔄 Step 3 — Alternate Digits

We maintain two lists:

```python
even = []
odd = []
```

Then repeatedly choose from the appropriate list.

If:

```python
turn_even == True
```

take the next even digit.

Otherwise:

```python
turn_even == False
```

take the next odd digit.

After every selection:

```python
turn_even = not turn_even
```

This switches between the two groups.

---

# 🚨 Step 4 — Handle Unequal Groups

The number of even and odd digits does not have to be equal.

For example:

```text
Even: 2 4 6 8
Odd:  1 3
```

Starting with even:

```text
2 1 4 3
```

At this point, the odd group is exhausted.

The remaining even digits:

```text
6 8
```

must be appended.

Final:

```text
214368
```

This is why we first alternate while **both groups contain digits**, and then append the leftover group.

---

# 🔄 Algorithm

1. Read the input string.
2. Initialize:

   ```python
   even = []
   odd = []
   special_count = 0
   ```
3. Traverse the string.
4. If the character is a digit:

   * Add it to `even` if it is even.
   * Otherwise add it to `odd`.
5. If the character is a special character, increment `special_count`.
6. Determine the starting group:

   ```python
   turn_even = (special_count % 2 == 0)
   ```
7. Alternate between even and odd digits while both lists contain elements.
8. Append any remaining digits.
9. Join the result and print it.

---

# 💻 Python 3 Solution

```python
S = input().strip()

even = []
odd = []
special_count = 0

# Categorize characters
for ch in S:
    if ch.isdigit():
        if int(ch) % 2 == 0:
            even.append(ch)
        else:
            odd.append(ch)
    elif not ch.isalnum():
        special_count += 1

# Determine which group starts
turn_even = (special_count % 2 == 0)

result = []

i = 0
j = 0

# Alternate while both groups have digits
while i < len(even) and j < len(odd):
    if turn_even:
        result.append(even[i])
        i += 1
    else:
        result.append(odd[j])
        j += 1

    turn_even = not turn_even

# Append remaining digits
result.extend(even[i:])
result.extend(odd[j:])

print("".join(result))
```

---

# 🔍 Code Breakdown

## Categorization

```python
for ch in S:
    if ch.isdigit():
```

We first determine whether the character is a digit.

Then:

```python
if int(ch) % 2 == 0:
```

separates even and odd digits.

---

## Count Special Characters

```python
elif not ch.isalnum():
    special_count += 1
```

A special character is a character that is neither:

```text
Letter
```

nor:

```text
Digit
```

---

# 🎯 Determine Starting Group

```python
turn_even = (special_count % 2 == 0)
```

This is a compact representation of the problem's rule.

### Even number of special characters

```text
2 % 2 = 0
```

Therefore:

```text
turn_even = True
```

Start with even.

### Odd number of special characters

```text
3 % 2 = 1
```

Therefore:

```text
turn_even = False
```

Start with odd.

---

# 🔄 Alternation Logic

```python
while i < len(even) and j < len(odd):
```

We continue alternating only while both groups have remaining digits.

If the current turn is even:

```python
result.append(even[i])
i += 1
```

Otherwise:

```python
result.append(odd[j])
j += 1
```

Then:

```python
turn_even = not turn_even
```

switches the turn.

---

# ➕ Append Remaining Digits

Suppose:

```text
Even = [6, 2, 8, 4]
Odd  = [5, 7]
```

After alternating:

```text
6 5 2 7
```

The odd group is exhausted.

The remaining even digits are:

```text
8 4
```

So:

```python
result.extend(even[i:])
```

adds them to the result.

Similarly:

```python
result.extend(odd[j:])
```

handles any remaining odd digits.

---

# 📊 Dry Run

Consider:

```text
S = A5c67r21i@p#8t
```

### Categorization

| Character Type     | Values    |
| ------------------ | --------- |
| Even digits        | `6, 2, 8` |
| Odd digits         | `5, 7, 1` |
| Special characters | `@, #`    |

Special count:

```text
2
```

Therefore:

```text
Start = Even
```

---

### Alternation

| Turn | Selected |
| ---- | -------- |
| 1    | `6`      |
| 2    | `5`      |
| 3    | `2`      |
| 4    | `7`      |
| 5    | `8`      |
| 6    | `1`      |

Final:

```text
652781
```

---

# 🧪 Another Example

Suppose:

```text
Input:
a1@2#3$4
```

Special characters:

```text
@ # $
```

Count:

```text
3
```

Since `3` is odd:

```text
Start with ODD
```

Digits:

```text
Odd  = 1, 3
Even = 2, 4
```

Alternate:

```text
1 2 3 4
```

Output:

```text
1234
```

---

# 🧪 Unequal Digit Groups

Suppose:

```text
Input:
1a2@3#4$6
```

Special characters:

```text
@ # $
```

Count:

```text
3
```

Start with odd.

Groups:

```text
Odd  = 1, 3
Even = 2, 4, 6
```

Alternation:

```text
1 2 3 4
```

Odd digits are exhausted.

Append remaining even digits:

```text
6
```

Final:

```text
12346
```

---

# ⚙️ Complexity Analysis

Let:

```text
N = len(S)
```

We scan the input string once to classify characters.

Then we process each digit at most once while constructing the result.

### Time Complexity

```text
O(N)
```

### Space Complexity

We store:

* Even digits
* Odd digits
* Result

Therefore the auxiliary space is:

```text
O(N)
```

Final:

```text
Time:  O(N)
Space: O(N)
```

Since:

```text
N ≤ 10⁶
```

an `O(N)` solution is necessary and appropriate.

---

# 🧠 Pattern Recognition

This problem combines several simple techniques:

```text
String Traversal
       +
Character Classification
       +
Counting
       +
Two-Pointer Style Merging
```

The important pattern is:

```text
Input String
     ↓
Separate into Groups
   ↙       ↘
Even       Odd
   ↘       ↙
    Alternate
       ↓
   Append Leftovers
       ↓
     Result
```

---

# 🔑 Key Takeaways

### 1. Scan the String Once

Use one traversal to identify:

```text
Even digits
Odd digits
Special characters
```

---

### 2. Use Lists to Preserve Order

The digits within each group should remain in the order they appeared.

Therefore:

```python
even.append(ch)
odd.append(ch)
```

is sufficient.

---

### 3. Special Character Count Determines the First Pick

```python
turn_even = (special_count % 2 == 0)
```

This directly implements the problem rule.

---

### 4. Alternate While Both Groups Exist

```python
while i < len(even) and j < len(odd):
```

This prevents accessing an exhausted group.

---

### 5. Append Leftovers

Once alternation is impossible:

```python
result.extend(even[i:])
result.extend(odd[j:])
```

adds whatever remains.

---

# 🎯 Final Mental Model

Think of the problem as two queues of digits:

```text
EVEN QUEUE             ODD QUEUE

6 → 2 → 8              5 → 7 → 1
```

If the number of special characters is even:

```text
EVEN → ODD → EVEN → ODD → ...
```

Result:

```text
6 5 2 7 8 1
```

If the number of special characters is odd:

```text
ODD → EVEN → ODD → EVEN → ...
```

Once one queue becomes empty:

```text
Alternate
    ↓
One group exhausted
    ↓
Append remaining group
    ↓
Final answer
```

The core idea is simple:

> **Separate the digits into even and odd groups, determine which group starts from the special-character count, then merge the two groups alternately while preserving their original order.**
