# 🧠 Coding Problem Clues → Algorithm & Data Structure Cheat Sheet

A quick-reference guide for identifying the **most likely algorithm or data structure** from the wording of a coding problem.

The goal is simple:

> **Read the problem clue → recognize the pattern → choose the right technique.**

---

## 📌 Quick Pattern Recognition Table

| Problem Clue / Keyword                | Think About                            | Common Technique             |
| ------------------------------------- | -------------------------------------- | ---------------------------- |
| Frequency / count occurrences         | Store and count values                 | **HashMap / Dictionary**     |
| Sorted + pair                         | Find two values satisfying a condition | **Two Pointers**             |
| Longest contiguous segment            | Maintain a valid continuous range      | **Sliding Window**           |
| Minimum / maximum with sorted choices | Make the best local choice             | **Greedy**                   |
| "Minimum X such that..."              | Search for the smallest valid answer   | **Binary Search on Answer**  |
| Repeated subproblems                  | Reuse previously calculated results    | **Dynamic Programming (DP)** |
| Longest valid subsequence             | Build the best subsequence             | **LIS DP**                   |
| Select / don't select                 | Choose items under constraints         | **Knapsack DP**              |
| Choose exactly K + XOR                | Track number selected + XOR value      | **XOR DP**                   |
| Adjacent selection forbidden          | Previous choice affects current choice | **DP**                       |
| Circular selection                    | First and last elements are connected  | **Circular DP**              |
| Parentheses matching                  | Track opening brackets                 | **Stack**                    |
| Divisibility                          | Common factors / divisors              | **GCD / Number Theory**      |
| Digits in another base                | Convert representation                 | **Base Conversion**          |
| AND / OR / XOR conditions             | Manipulate individual bits             | **Bitwise Operations**       |

---

# 1. 🔢 Frequency / Count Occurrences → HashMap

### Clue

Look for phrases such as:

* Frequency of each element
* Count occurrences
* How many times does X appear?
* Most frequent element
* Duplicate elements
* Number of occurrences

### Think

You need to remember information about each value.

### Technique

**HashMap / Dictionary**

### Python

```python
freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1
```

Or:

```python
from collections import Counter

freq = Counter(arr)
```

### Example

```text
arr = [2, 3, 2, 5, 3, 2]

Frequency:
2 → 3
3 → 2
5 → 1
```

### Complexity

```text
Time:  O(N)
Space: O(N)
```

---

# 2. 🔄 Sorted + Pair → Two Pointers

### Clue

Look for:

* Find a pair
* Two numbers whose sum is X
* Pair with minimum difference
* Pair satisfying a condition
* Array is already sorted

### Think

If the array is sorted, use two positions:

```text
left →       ← right
```

### Technique

**Two Pointers**

### Example

Find two numbers whose sum is `10`.

```text
[1, 2, 4, 6, 8, 10]
 ↑           ↑
 L           R
```

If:

```text
arr[L] + arr[R] < 10
```

Move `L`.

If:

```text
arr[L] + arr[R] > 10
```

Move `R`.

### Python

```python
left = 0
right = len(arr) - 1

while left < right:
    total = arr[left] + arr[right]

    if total == target:
        return True
    elif total < target:
        left += 1
    else:
        right -= 1

return False
```

### Complexity

```text
Time:  O(N)
Space: O(1)
```

---

# 3. 🪟 Longest Contiguous Segment → Sliding Window

### Clue

Look for:

* Longest subarray
* Longest substring
* Maximum length
* Continuous / contiguous
* At most K
* At least K
* Window/range conditions

### Important

**Contiguous** means elements must be next to each other.

```text
[1, 2, 3, 4, 5]
    └──────┘
      window
```

### Technique

**Sliding Window**

### General Pattern

```python
left = 0

for right in range(len(arr)):

    # Add arr[right]

    while window_is_invalid:
        # Remove arr[left]
        left += 1

    # Update answer
```

### Complexity

Usually:

```text
Time:  O(N)
Space: O(K) or O(N)
```

---

# 4. 🤑 Minimum / Maximum with Sorted Choices → Greedy

### Clue

Look for:

* Minimum number of operations
* Maximum number of activities
* Choose the best option at every step
* Sort and select
* Minimum resources
* Maximum profit under simple local choices

### Think

Can making the **best local choice** lead to the global optimum?

If yes, **Greedy** may work.

### Typical pattern

```python
arr.sort()

for x in arr:
    # Make the best available choice
```

### Warning

Do **not** assume every optimization problem is greedy.

You need a reason why the local choice is safe.

If choosing something now affects many future possibilities, **DP or another technique may be required.**

---

# 5. 🔎 "Minimum X Such That..." → Binary Search on Answer

### Clue

Very important pattern:

> Find the minimum value of X such that a condition becomes true.

Examples:

* Minimum capacity required
* Minimum time required
* Minimum speed
* Minimum days
* Minimum maximum distance
* Smallest possible answer satisfying a condition

### Think

Can we check:

```text
Is X possible?
```

If yes/no changes monotonically:

```text
False False False False True True True
                      ↑
                 answer
```

Then use **Binary Search on Answer**.

### General Pattern

```python
low = minimum_possible
high = maximum_possible

while low < high:
    mid = (low + high) // 2

    if feasible(mid):
        high = mid
    else:
        low = mid + 1

return low
```

### Key Requirement

There must be a **monotonic feasibility condition**.

---

# 6. 🧠 Repeated Subproblems → Dynamic Programming

### Clue

Look for:

* Number of ways
* Minimum cost
* Maximum profit
* Optimal answer
* Choices at every step
* Same state appears repeatedly
* Previous decisions affect future decisions

### Think

If the same smaller problem is solved again and again, save its answer.

### Technique

**Dynamic Programming**

Two major ideas:

```text
1. State
2. Transition
```

Example:

```python
dp[i] = best answer up to index i
```

### DP Questions to Ask

When you see a problem, ask:

1. What is my **state**?
2. What choices do I have?
3. What is the **transition**?
4. What are the **base cases**?
5. What is the final answer?

---

# 7. 📈 Longest Valid Subsequence → LIS DP

### Clue

Look for:

* Longest increasing subsequence
* Longest decreasing subsequence
* Longest valid subsequence
* Elements don't have to be contiguous

### Important Difference

### Subarray

Elements must be continuous:

```text
[2, 5, 7, 3]
 └──────┘
```

### Subsequence

Elements can be skipped:

```text
[2, 5, 7, 3]
 ↑     ↑
```

### Basic LIS DP

```python
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

return max(dp)
```

### Complexity

```text
Time:  O(N²)
Space: O(N)
```

There is also an `O(N log N)` LIS technique using binary search.

---

# 8. 🎒 Select / Don't Select → Knapsack DP

### Clue

Look for:

* Choose items
* Select or skip
* Capacity limit
* Maximum value
* Minimum cost
* Each item can be selected or not
* Subset selection

### Think

Every item gives you two choices:

```text
             Item
            /    \
        Select    Don't Select
```

### Classic 0/1 Knapsack

```python
dp = [0] * (capacity + 1)

for weight, value in items:
    for c in range(capacity, weight - 1, -1):
        dp[c] = max(
            dp[c],
            dp[c - weight] + value
        )
```

### Important

For **0/1 Knapsack**, iterate capacity backwards.

```text
capacity → down to weight
```

This prevents using the same item multiple times.

---

# 9. 🔀 Choose Exactly K + XOR → XOR DP

### Clue

Look for:

* Select exactly K elements
* XOR of selected elements
* Maximum/minimum XOR
* Number of selected elements matters

### Think

You need to track **two things**:

```text
How many elements selected?
+
Current XOR
```

So a state can look like:

```text
dp[k][xor]
```

### Transition

For each number `x`:

```text
Don't select x
OR
Select x
```

If selected:

```text
new_xor = old_xor ^ x
```

### Important

XOR is not normal addition.

Remember:

```text
x ^ x = 0
x ^ 0 = x
```

---

# 10. 🚫 Adjacent Selection Forbidden → DP

### Clue

Look for:

* Cannot select adjacent elements
* No two neighboring elements
* Choose elements with at least one gap
* Maximum sum without consecutive elements

### Think

Your previous decision affects whether you can select the current element.

### Example

```text
[2, 7, 9, 3, 1]
```

You cannot select:

```text
7 and 9
```

because they are adjacent.

### DP

```python
dp[i] = best answer using elements up to i
```

Transition:

```text
Don't take i:
    dp[i-1]

Take i:
    arr[i] + dp[i-2]
```

Therefore:

```python
dp[i] = max(
    dp[i - 1],
    arr[i] + dp[i - 2]
)
```

This pattern appears frequently in **House Robber-style problems**.

---

# 11. 🔄 Circular Selection → Circular DP

### Clue

Look for:

* Circular array
* First and last elements are adjacent
* Cannot select neighboring elements
* Maximum/minimum selection in a circle

### Problem

For:

```text
[2, 7, 9, 3, 1]
```

Normally:

```text
2 and 1
```

are far apart.

But in a circular array:

```text
2 ↔ 1
```

are neighbors.

### Standard Trick

Break the problem into two cases:

### Case 1

Don't take the first element.

```text
arr[1:]
```

### Case 2

Don't take the last element.

```text
arr[:-1]
```

Then:

```python
answer = max(
    solve(arr[1:]),
    solve(arr[:-1])
)
```

This converts a circular DP problem into two normal linear DP problems.

---

# 12. 🧱 Parentheses Matching → Stack

### Clue

Look for:

* Balanced parentheses
* Matching brackets
* `()`, `{}`, `[]`
* Nested expressions
* Last opened → first closed

### Think

This is **LIFO**:

```text
Last In
First Out
```

Exactly what a stack provides.

### Python

```python
stack = []

pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

for ch in s:
    if ch in "([{":
        stack.append(ch)

    else:
        if not stack or stack[-1] != pairs[ch]:
            return False

        stack.pop()

return len(stack) == 0
```

### Complexity

```text
Time:  O(N)
Space: O(N)
```

---

# 13. ➗ Divisibility → GCD / Number Theory

### Clue

Look for:

* Divisible by
* Common divisor
* Greatest common divisor
* Least common multiple
* Factors
* Remainder
* Multiples

### GCD

Python:

```python
from math import gcd

g = gcd(a, b)
```

### Euclidean Algorithm

```text
gcd(a, b)
=
gcd(b, a % b)
```

Continue until:

```text
b = 0
```

Then:

```text
gcd(a, 0) = a
```

### LCM

```python
from math import gcd

lcm = a // gcd(a, b) * b
```

Using division first helps avoid unnecessary overflow in languages with fixed-width integers.

---

# 14. 🔢 Digits in Another Base → Base Conversion

### Clue

Look for:

* Binary
* Octal
* Decimal
* Hexadecimal
* Base K
* Convert number to another base
* Digits represented in another base

### Decimal → Binary

```python
bin(n)
```

### Decimal → Base B

Repeatedly divide by `B` and collect remainders.

Example:

```text
13 in base 2

13 ÷ 2 → remainder 1
 6 ÷ 2 → remainder 0
 3 ÷ 2 → remainder 1
 1 ÷ 2 → remainder 1
```

Read remainders backwards:

```text
1101
```

Therefore:

```text
13₁₀ = 1101₂
```

---

# 15. 🧮 AND / OR / XOR Conditions → Bitwise

### Clue

Look for:

* AND
* OR
* XOR
* Binary representation
* Set bits
* Toggle bits
* Bitmask
* Power of two
* Subset represented using bits

### Operators

```text
&   AND
|   OR
^   XOR
~   NOT
<<  Left Shift
>>  Right Shift
```

### Useful Properties

```text
x ^ x = 0
x ^ 0 = x
```

AND:

```text
1 & 1 = 1
otherwise = 0
```

OR:

```text
0 | 0 = 0
otherwise = 1
```

### Check if a number is a power of 2

```python
n > 0 and (n & (n - 1)) == 0
```

Example:

```text
8  = 1000
7  = 0111

8 & 7 = 0000
```

So `8` is a power of 2.

---

# 🧠 Master Decision Tree

When you read a coding problem, don't immediately start coding.

First ask:

```text
                    START
                      |
                      v
             What does the problem ask?
                      |
       +--------------+--------------+
       |              |              |
       v              v              v
    Counting        Pair/Range      Choices
       |              |              |
    HashMap       Sorted?         Repeated states?
                     |              |
                  Two Pointer        |
                                    DP
```

Then check the special clues:

```text
Frequency/count
       ↓
   HashMap

Sorted + pair
       ↓
 Two Pointers

Longest contiguous
       ↓
 Sliding Window

Minimum/maximum + local choices
       ↓
 Greedy

"Minimum X such that..."
       ↓
 Binary Search on Answer

Repeated subproblems
       ↓
 DP

Longest subsequence
       ↓
 LIS

Select / Don't Select
       ↓
 Knapsack DP

Exactly K + XOR
       ↓
 XOR DP

Adjacent forbidden
       ↓
 Linear DP

Circular + adjacent restriction
       ↓
 Circular DP

Matching parentheses
       ↓
 Stack

Divisibility
       ↓
 GCD / Number Theory

Different base
       ↓
 Base Conversion

AND / OR / XOR
       ↓
 Bitwise
```

---

# ⚠️ Important: Clues Are Not Proof

A problem containing a keyword does **not automatically mean** you should use that algorithm.

For example:

```text
"minimum"
```

does **not** automatically mean Greedy.

It could be:

```text
Greedy
DP
Binary Search on Answer
BFS
Dijkstra
```

Similarly:

```text
"longest"
```

could mean:

```text
Sliding Window
LIS
DP
Two Pointers
Graph algorithms
```

The clue only gives you a **starting hypothesis**.

You still need to verify the constraints and structure of the problem.

---

# 🔥 What to Check Before Choosing an Algorithm

## 1. Is the data contiguous?

If yes, consider:

```text
Sliding Window
Prefix Sum
Two Pointers
```

---

## 2. Can elements be skipped?

If yes, consider:

```text
Subsequence
DP
LIS
Knapsack
```

---

## 3. Is the array sorted?

If yes, consider:

```text
Two Pointers
Binary Search
Greedy
```

---

## 4. Does the same state appear repeatedly?

If yes:

```text
DP / Memoization
```

---

## 5. Is the answer a number and can you check feasibility?

If yes, ask:

```text
Can I binary search the answer?
```

---

## 6. Does the previous choice affect the current choice?

If yes, consider:

```text
DP
```

---

## 7. Is the structure circular?

If yes, think:

```text
Circular DP
Circular Sliding Window
Modulo
```

depending on the actual problem.

---

# ⏱️ Complexity Cheat Sheet

| Technique               |           Typical Complexity |
| ----------------------- | ---------------------------: |
| HashMap                 |                       `O(N)` |
| Two Pointers            |                       `O(N)` |
| Sliding Window          |                       `O(N)` |
| Greedy + Sorting        |                 `O(N log N)` |
| Binary Search           |                   `O(log N)` |
| Binary Search on Answer |      `O(log Answer × Check)` |
| Basic DP                |     `O(N)` / `O(N × K)` etc. |
| LIS DP                  |                      `O(N²)` |
| LIS optimized           |                 `O(N log N)` |
| Knapsack DP             |            `O(N × Capacity)` |
| Stack                   |                       `O(N)` |
| GCD                     |            `O(log min(a,b))` |
| Bitwise operations      | Usually `O(1)` per operation |

---

# 🎯 Exam Strategy

When you get a new problem:

### Step 1 — Read the constraints

Look at:

```text
N ≤ ?
Values ≤ ?
Time limit?
```

Constraints often tell you the expected complexity.

---

### Step 2 — Identify the keyword

Ask:

```text
Frequency?
Pair?
Contiguous?
Minimum?
Subsequence?
Select/skip?
Circular?
XOR?
Parentheses?
Divisibility?
```

---

### Step 3 — Identify the pattern

Map it:

```text
Frequency → HashMap
Pair → Two Pointer
Contiguous → Sliding Window
Minimum X → Binary Search on Answer
Repeated states → DP
Select/skip → Knapsack DP
Circular → Circular DP
Matching → Stack
XOR → Bitwise/XOR DP
```

---

### Step 4 — Write the brute-force idea first

Before optimizing, understand what the obvious solution would do.

Then ask:

> **What is making the brute-force solution slow?**

That question usually reveals the optimization.

---

### Step 5 — Check edge cases

Always test:

```text
N = 0
N = 1
All elements equal
Already sorted
Reverse sorted
Minimum values
Maximum values
Duplicate values
Answer at first position
Answer at last position
No valid answer
```

---

# 🏆 Final Mental Model

Don't memorize 100 algorithms independently.

Instead, memorize **patterns**.

```text
COUNT
  ↓
HashMap

PAIR
  ↓
Two Pointers

CONTIGUOUS
  ↓
Sliding Window

BEST LOCAL CHOICE
  ↓
Greedy

MINIMUM X SUCH THAT...
  ↓
Binary Search on Answer

REPEATED STATES
  ↓
DP

LONGEST SUBSEQUENCE
  ↓
LIS

SELECT / SKIP
  ↓
Knapsack DP

EXACTLY K + XOR
  ↓
XOR DP

ADJACENT FORBIDDEN
  ↓
DP

CIRCULAR
  ↓
Circular DP

MATCHING
  ↓
Stack

DIVISIBILITY
  ↓
GCD / Number Theory

BASE
  ↓
Base Conversion

AND / OR / XOR
  ↓
Bitwise
```

## ⭐ The Most Important Rule

> **Don't choose an algorithm because of one keyword. Choose it because the problem's structure matches the algorithm.**

The fastest way to improve coding-round performance is to repeatedly practice:

```text
Problem
   ↓
Identify clue
   ↓
Identify pattern
   ↓
Choose algorithm
   ↓
Write solution
   ↓
Check complexity
   ↓
Test edge cases
```

That pattern-recognition skill is more valuable in a timed coding round than memorizing isolated solutions.
