# 🧮 Fibonacci Count

## 📌 Problem Overview

Given a list of integers `nums`, find the number of elements that are **Fibonacci numbers**.

A number is considered a Fibonacci number if it appears in the Fibonacci sequence:

```text
1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

After counting the Fibonacci numbers in the input:

* If the count is **greater than 2**, print the count.
* If the count is **2 or less**, print `-1`.

---

# 🧩 Problem Statement

Given a list of integers `nums`, determine how many elements belong to the Fibonacci sequence.

For example:

```text
nums = [3, 2, 5, 8, 9, 10, 11]
```

The Fibonacci numbers are:

```text
3, 2, 5, 8
```

There are:

```text
4
```

Fibonacci numbers.

Since `4 > 2`, the output is:

```text
4
```

---

## 📥 Input Format

A single line containing comma-separated integers.

```text
a₁,a₂,a₃,...,aₙ
```

### Constraints

```text
1 ≤ nums[i] ≤ 10⁹
1 ≤ |nums| ≤ 10⁵
```

---

## 📤 Output Format

Print the number of Fibonacci elements in the input.

If the count is `2` or fewer, print:

```text
-1
```

---

# 🧪 Sample Input

```text
3,2,5,8,9,10,11
```

## 🧪 Sample Output

```text
4
```

### Explanation

The Fibonacci sequence begins:

```text
1, 1, 2, 3, 5, 8, 13, ...
```

From the input:

```text
3, 2, 5, 8, 9, 10, 11
```

the Fibonacci numbers are:

```text
3, 2, 5, 8
```

Therefore:

```text
count = 4
```

Since:

```text
4 > 2
```

the answer is:

```text
4
```

---

# 💡 Approach

The solution can be divided into three steps:

1. Read the input.
2. Generate all Fibonacci numbers up to `10⁹`.
3. Count how many input values are Fibonacci numbers.

---

# 1️⃣ Read the Input

The input contains comma-separated values.

For example:

```text
3,2,5,8,9,10,11
```

We convert them into integers using:

```python
nums = list(map(int, input().split(",")))
```

This produces:

```python
[3, 2, 5, 8, 9, 10, 11]
```

---

# 2️⃣ Generate Fibonacci Numbers

The Fibonacci sequence is generated using two variables:

```python
a, b = 1, 1
```

Then repeatedly update:

```python
a, b = b, a + b
```

This produces:

```text
1
1
2
3
5
8
13
21
34
...
```

Since the maximum input value is:

```text
10⁹
```

we only need to generate Fibonacci numbers up to `10⁹`.

They are stored in a set:

```python
fib_set = set()
```

Using a set is important because checking:

```python
num in fib_set
```

takes **O(1) average time**.

---

# 3️⃣ Count Fibonacci Numbers

We iterate through the input list:

```python
count = sum(1 for num in nums if num in fib_set)
```

Every number that exists in `fib_set` contributes `1` to the count.

For:

```text
3,2,5,8,9,10,11
```

the checks are:

```text
3  → Fibonacci ✓
2  → Fibonacci ✓
5  → Fibonacci ✓
8  → Fibonacci ✓
9  → Not Fibonacci ✗
10 → Not Fibonacci ✗
11 → Not Fibonacci ✗
```

Therefore:

```text
count = 4
```

---

# 🔄 Algorithm

1. Read the comma-separated input.
2. Convert the values into integers.
3. Create an empty set `fib_set`.
4. Generate Fibonacci numbers starting with `1, 1`.
5. Continue until the Fibonacci number exceeds `10⁹`.
6. Store every generated Fibonacci number in the set.
7. Iterate through `nums`.
8. Count every number that exists in `fib_set`.
9. If the count is greater than `2`, print the count.
10. Otherwise, print `-1`.

---

# 💻 Python 3 Solution

```python
nums = list(map(int, input().split(",")))

# Generate Fibonacci numbers up to 10^9
fib_set = set()

a, b = 1, 1

fib_set.add(1)

while b <= 10**9:
    fib_set.add(b)
    a, b = b, a + b


# Count Fibonacci numbers in the input
count = sum(1 for num in nums if num in fib_set)


# Apply the condition
print(count if count > 2 else -1)
```

---

# 🧠 Dry Run

Consider:

```text
nums = [3, 2, 5, 8, 9, 10, 11]
```

### Fibonacci Set

The generated set contains values such as:

```text
{1, 2, 3, 5, 8, 13, 21, 34, ...}
```

### Check Each Number

| Number | Fibonacci? | Count |
| -----: | :--------: | ----: |
|    `3` |      ✅     |     1 |
|    `2` |      ✅     |     2 |
|    `5` |      ✅     |     3 |
|    `8` |      ✅     |     4 |
|    `9` |      ❌     |     4 |
|   `10` |      ❌     |     4 |
|   `11` |      ❌     |     4 |

Final:

```text
count = 4
```

Since:

```text
4 > 2
```

the output is:

```text
4
```

---

# 📌 Why Use a Set?

A naive approach could generate Fibonacci numbers and search through a list every time.

That would make membership checking slower.

Instead:

```python
fib_set = set()
```

allows us to perform:

```python
num in fib_set
```

in **O(1) average time**.

This matters because:

```text
|nums| ≤ 10⁵
```

so we may perform up to `100,000` membership checks.

---

# 🔢 Why Precompute Fibonacci Numbers?

The input values can be as large as:

```text
10⁹
```

But there are only a small number of Fibonacci numbers up to `10⁹`.

The sequence grows rapidly:

```text
1
1
2
3
5
8
13
21
34
55
89
...
```

Therefore, generating the Fibonacci sequence once and storing it in a set is much more efficient than calculating the Fibonacci sequence separately for every input value.

---

# ⚠️ Important Note About Duplicates

The problem asks for the number of **elements** that are Fibonacci numbers, not the number of **distinct** Fibonacci values.

For example:

```text
1,2,2,3,5
```

contains:

```text
1 → Fibonacci
2 → Fibonacci
2 → Fibonacci
3 → Fibonacci
5 → Fibonacci
```

Therefore:

```text
count = 5
```

The duplicate `2` is counted twice because it appears twice in the input list.

The `fib_set` is only used to efficiently determine whether a number belongs to the Fibonacci sequence.

---

# 📊 Example With Too Few Fibonacci Numbers

Input:

```text
10,20,30,2
```

Only `2` is Fibonacci.

Therefore:

```text
count = 1
```

Since:

```text
count ≤ 2
```

the required output is:

```text
-1
```

---

# 📊 Another Example

Input:

```text
1,2,3
```

All three values are Fibonacci numbers:

```text
1 → ✓
2 → ✓
3 → ✓
```

Therefore:

```text
count = 3
```

Since:

```text
3 > 2
```

output:

```text
3
```

---

# ⚙️ Complexity Analysis

Let:

```text
N = number of elements in nums
```

and let `F` be the number of Fibonacci numbers up to `10⁹`.

There are only a small number of such Fibonacci values because the sequence grows exponentially.

### Fibonacci Generation

Generating the Fibonacci set takes:

```text
O(F)
```

time.

Since `F` is very small compared with `N`, this is effectively constant for the given constraints.

### Counting

We check every input number once:

```text
O(N)
```

Each set lookup takes **O(1) average time**.

Therefore, overall:

```text
Time Complexity: O(N + F)
```

which is effectively:

```text
O(N)
```

### Space Complexity

The input list requires:

```text
O(N)
```

space.

The Fibonacci set requires:

```text
O(F)
```

space.

Therefore:

```text
Space Complexity: O(N + F)
```

which is effectively:

```text
O(N)
```

for the given constraints.

---

# 🔑 Key Concepts

This problem demonstrates:

* Fibonacci sequence
* Set data structure
* Fast membership testing
* Precomputation
* List processing
* Generator expressions
* Input parsing
* Conditional output
* Time complexity optimization

---

# 🎯 Key Takeaway

The main idea is **precomputation + set lookup**.

Instead of asking for every number:

> "Is this number Fibonacci?"

individually using an expensive method, we first generate all Fibonacci numbers within the allowed range:

```text
Generate Fibonacci numbers
        ↓
     Store in Set
        ↓
   Read input values
        ↓
Check membership in O(1)
        ↓
      Count matches
        ↓
 count > 2 ?
    ↙       ↘
  Yes        No
   ↓          ↓
 print count  print -1
```

For the sample:

```text
3,2,5,8,9,10,11
```

the Fibonacci values are:

```text
3, 2, 5, 8
```

so:

```text
count = 4
```

and the final answer is:

```text
4
```

The important pattern to remember is:

> **When the valid values come from a small, known mathematical sequence, precompute them into a set and use fast membership checks.**
