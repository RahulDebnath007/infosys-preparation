# 1🧟 Monster Quest – Maximum Monsters Defeated (Bitmask Dynamic Programming)

## 📌 Problem Statement

You are playing an RPG game where you have to defeat **n monsters**.

Each monster has:

* **power[i]** → Minimum experience required to defeat the monster.
* **bonus[i]** → Experience gained after defeating the monster.

Initially, you have **e** experience points.

You can defeat the monsters in **any order**, but you can only fight a monster if your current experience is **greater than or equal to its power**.

The objective is to determine the **maximum number of monsters that can be defeated**.

---

# 💡 Approach

A brute-force solution would try every possible order of defeating monsters.

For **n** monsters, the number of possible orders is:

```text
n!
```

This quickly becomes infeasible.

### Key Observation

The current experience depends only on:

```text
Initial Experience
+
Sum of bonuses of defeated monsters
```

It does **not** depend on the exact order in which those monsters were defeated.

Therefore, instead of storing the order, we only need to store **which monsters have already been defeated**.

This leads to the **Bitmask Dynamic Programming (Subset DP)** approach.

---

# 🧠 Algorithm

1. Represent each set of defeated monsters as a **bitmask**.
2. Start with mask `000...0` (no monsters defeated).
3. For every reachable mask:

   * Calculate the current experience.
   * Count how many monsters have already been defeated.
   * Try defeating every remaining monster.
4. If enough experience is available:

   * Create a new mask.
   * Mark the new state as reachable.
5. Store the maximum number of defeated monsters.

---

# 🔍 Understanding Bitmask

Suppose:

```text
n = 4
```

Possible masks:

| Mask | Monsters Defeated |
| ---- | ----------------- |
| 0000 | None              |
| 0001 | Monster 0         |
| 0010 | Monster 1         |
| 0011 | Monster 0,1       |
| 0100 | Monster 2         |
| 1111 | All monsters      |

Each bit represents whether a monster has already been defeated.

---

# 📝 Code Explanation (Step-by-Step)

## Step 1

```python
def maxMonsters(n, e, power, bonus):
```

We create a function.

Parameters:

* `n` → Number of monsters
* `e` → Initial experience
* `power` → Minimum experience required to defeat each monster
* `bonus` → Experience gained after defeating each monster

---

## Step 2

```python
total_masks = 1 << n
```

This calculates:

```text
2^n
```

because each monster has two possibilities:

* Defeated
* Not defeated

For example:

```text
n = 3

1 << 3 = 8
```

There are **8 possible subsets (states)**.

---

## Step 3

```python
reachable = [False] * total_masks
```

This creates an array to store whether a particular state is reachable.

For `n = 3`

```text
[False, False, False, False, False, False, False, False]
```

Initially, we assume no state is reachable.

---

## Step 4

```python
reachable[0] = True
```

Mask

```text
000
```

means **no monsters have been defeated**.

This state is always reachable because we haven't started fighting yet.

---

## Step 5

```python
answer = 0
```

This variable stores the maximum number of monsters defeated.

Initially,

```text
answer = 0
```

---

## Step 6

```python
for mask in range(total_masks):
```

Iterate through every possible state.

For `n = 3`

```text
000
001
010
011
100
101
110
111
```

Each mask represents one subset of defeated monsters.

---

## Step 7

```python
if not reachable[mask]:
    continue
```

If the current state cannot be reached, there is no point processing it.

Skip to the next state.

This saves unnecessary computation.

---

## Step 8

```python
current_exp = e
defeated = 0
```

Reset

* Current Experience
* Number of defeated monsters

We'll calculate them again for the current mask.

---

## Step 9

```python
for i in range(n):
```

Visit every monster.

---

## Step 10

```python
if mask & (1 << i):
```

This checks whether monster **i** has already been defeated.

Example:

```text
mask = 1010
```

Check Monster 1

```text
1010
0010
----
0010
```

Result is non-zero.

Therefore,

**Monster 1 has already been defeated.**

Now check Monster 2

```text
1010
0100
----
0000
```

Result is zero.

Therefore,

**Monster 2 has not been defeated.**

---

## Step 11

```python
current_exp += bonus[i]
```

If a monster has already been defeated,

add its bonus to the current experience.

Example

```text
Initial Experience = 100

Bonus = 20
```

New experience

```text
120
```

---

## Step 12

```python
defeated += 1
```

Increase the count of defeated monsters.

---

## Step 13

```python
answer = max(answer, defeated)
```

Store the maximum number of monsters defeated so far.

Example

```text
Current Answer = 3

Current Defeated = 4
```

New Answer

```text
4
```

---

## Step 14

```python
for i in range(n):
```

Again visit every monster.

This time,

check whether we can defeat another monster.

---

## Step 15

```python
if mask & (1 << i):
    continue
```

If the monster has already been defeated,

ignore it and move to the next monster.

---

## Step 16

```python
if current_exp >= power[i]:
```

Check whether enough experience is available.

Example

```text
Current Experience = 150

Monster Power = 120
```

Since

```text
150 >= 120
```

we can defeat the monster.

Then

```python
new_mask = mask | (1 << i)
```

creates a new state.

Example

Current Mask

```text
0010
```

Defeat Monster 0

```text
0001
```

Using OR operation

```text
0010
0001
----
0011
```

Now Monsters **0 and 1** have both been defeated.

---

## Step 17

```python
reachable[new_mask] = True
```

Mark the new state as reachable.

Later, when this mask is processed,

the algorithm will continue exploring from this new state.

Finally,

```python
return answer
```

returns the maximum number of monsters that can be defeated.

---

# Driver Code

```python
n = int(input())
e = int(input())

power = []
for _ in range(n):
    power.append(int(input()))

bonus = []
for _ in range(n):
    bonus.append(int(input()))

print(maxMonsters(n, e, power, bonus))
```

The driver code:

1. Reads the number of monsters.
2. Reads the initial experience.
3. Stores all monster powers in a list.
4. Stores all monster bonuses in another list.
5. Calls the `maxMonsters()` function.
6. Prints the maximum number of monsters that can be defeated.

---

# 📈 Dry Run

### Input

```text
n = 3

Experience = 100

Power = [101,100,304]

Bonus = [100,1,524]
```

Initial State

```text
Mask = 000

Experience = 100
```

Only Monster 1 can be defeated.

After defeating Monster 1

```text
Mask = 010

Experience = 101
```

Now Monster 0 becomes available.

After defeating Monster 0

```text
Mask = 011

Experience = 201
```

Monster 2 requires

```text
304 Experience
```

Cannot defeat.

Maximum monsters defeated:

```text
2
```

---

# 📊 Complexity Analysis

### Time Complexity

There are:

```text
2^n
```

possible masks.

For each mask:

* Calculate experience → **O(n)**
* Try every monster → **O(n)**

Overall:

```text
O(n × 2^n)
```

### Space Complexity

```text
O(2^n)
```

---

# 🧩 Pattern Used

* Dynamic Programming (DP)
* Bitmask DP (Subset DP)
* State Space Search

---

# 🚀 Key Learning

> If the future depends only on **which items have been selected**, and not on **the order** in which they were selected, a **Bitmask DP** solution is often appropriate.

---

# 📚 Suitable For

* Infosys Coding Assessment (small `n`)
* Bitmask DP Practice
* Dynamic Programming Interviews
* Competitive Programming

---

# 2 🔢 Count Arrays – Dynamic Programming on Sequences

## 📌 Problem Statement

You are given two integers:

- **N** → Maximum value allowed in the array.
- **K** → Length of the array.

Your task is to count the number of arrays of length **K** such that:

1. Every element is between **1** and **N**.
2. Every adjacent pair satisfies:

```text
a[i+1] % a[i] == 0
```

In other words, every next element must be divisible by the previous element.

Return the answer **modulo 10000**.

---

# 💡 Approach

A brute-force solution would generate every possible array of length **K**.

The total number of possible arrays is:

```text
N^K
```

This quickly becomes infeasible for larger values of **N** and **K**.

### Key Observation

If the current number is:

```text
2
```

the next number can only be:

```text
2, 4, 6, 8, ...
```

Similarly,

```text
3 → 3, 6, 9, ...

4 → 4, 8, 12, ...
```

Each number can transition **only to its multiples**.

Instead of generating every possible array, we store previously computed answers using **Dynamic Programming**.

### DP State

```text
dp[length][last]
```

Meaning:

> Number of valid arrays of length **length** ending with **last**.

### Transition

For every valid ending number, extend the array to all of its multiples.

```python
for multiple in range(num, n + 1, num):
    dp[length + 1][multiple] += dp[length][num]
```

---

# 💻 Python Code

```python
MOD = 10000

def countArrays(n, k):

    # dp[length][number]
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    # Base case
    for num in range(1, n + 1):
        dp[1][num] = 1

    # Build DP
    for length in range(1, k):
        for num in range(1, n + 1):

            # Visit every multiple of num
            for multiple in range(num, n + 1, num):
                dp[length + 1][multiple] = (
                    dp[length + 1][multiple] + dp[length][num]
                ) % MOD

    # Sum all arrays of length k
    return sum(dp[k]) % MOD


# Driver Code
n = int(input())
k = int(input())

print(countArrays(n, k))
```

---

# 📝 Code Explanation (Step-by-Step)

## Step 1

```python
MOD = 10000
```

The answer can become very large.

Store every value modulo **10000**.

---

## Step 2

```python
def countArrays(n, k):
```

Create the function.

Parameters:

- `n` → Maximum number allowed.
- `k` → Required array length.

---

## Step 3

```python
dp = [[0] * (n + 1) for _ in range(k + 1)]
```

Create the DP table.

State:

```text
dp[length][last]
```

It stores the number of valid arrays of a given length ending with a particular number.

---

## Step 4

```python
for num in range(1, n + 1):
    dp[1][num] = 1
```

Initialize the base case.

Every number forms one valid array of length **1**.

Example:

```text
[1]
[2]
[3]
...
```

---

## Step 5

```python
for length in range(1, k):
```

Build arrays from smaller lengths to larger lengths.

---

## Step 6

```python
for num in range(1, n + 1):
```

Visit every possible ending number.

---

## Step 7

```python
for multiple in range(num, n + 1, num):
```

Visit every multiple of the current number.

Example:

If

```text
num = 2
```

The multiples are

```text
2
4
6
8
...
```

These are the only valid next elements.

---

## Step 8

```python
dp[length + 1][multiple]
```

Represents:

Number of arrays of length **length + 1** ending at **multiple**.

---

## Step 9

```python
dp[length][num]
```

Represents:

Number of arrays already built of length **length** ending at **num**.

---

## Step 10

```python
dp[length + 1][multiple] += dp[length][num]
```

Extend every existing valid array ending with **num** to **multiple**.

---

## Step 11

```python
% MOD
```

Take modulo **10000** after every update.

---

## Step 12

```python
return sum(dp[k]) % MOD
```

After building all arrays of length **k**, add every possible ending value.

---

## Step 13

```python
n = int(input())
k = int(input())
```

Read the input values.

---

## Step 14

```python
print(countArrays(n, k))
```

Call the function and print the final answer.

---
# 3🧩 Longest Increasing Subsequence with Bitwise Condition (Dynamic Programming)

## 📌 Problem Statement

You are given an array `A` of `N` integers.

Your task is to find the **Longest Increasing Subsequence (LIS)** such that for every adjacent pair of elements in the chosen subsequence, the following condition is satisfied:

```text
(A[i] & A[j]) * 2 < (A[i] | A[j])
```

where:

- `&` = Bitwise AND
- `|` = Bitwise OR

A valid pair must satisfy:

1. `A[i] < A[j]` (Increasing Order)
2. `(A[i] & A[j]) * 2 < (A[i] | A[j])`

Return the length of the longest such subsequence.

---

## 📝 Example

### Input

```text
5
15
6
5
12
1
```

### Output

```text
2
```

### Explanation

One possible valid subsequence is:

```text
5 12
```

Since:

- `5 < 12`
- `(5 & 12) = 4`
- `(5 | 12) = 13`
- `4 × 2 = 8`
- `8 < 13` ✅

Therefore, the answer is **2**.

---

# 💡 Approach

This problem is a **variation of the Longest Increasing Subsequence (LIS)**.

For every element, we try to extend a valid subsequence ending at a previous element.

### Step 1

Create a DP array.

```text
dp[i]
```

represents:

> Length of the longest valid subsequence ending at index `i`.

Initially,

```text
dp[i] = 1
```

because every element alone forms a subsequence of length `1`.

---

### Step 2

For every element `i`, check every previous element `j`.

If both conditions are satisfied:

```text
A[j] < A[i]
```

and

```text
(A[j] & A[i]) * 2 < (A[j] | A[i])
```

then update

```text
dp[i] = max(dp[i], dp[j] + 1)
```

---

### Step 3

The answer is

```text
max(dp)
```

because the longest subsequence can end at any index.

---

## ✅ Time Complexity

```text
O(N²)
```

Every pair of elements is checked once.

## ✅ Space Complexity

```text
O(N)
```

Only one DP array is used.

---

# 💻 Python Code

```python
def longest_valid_subsequence(n, arr):
    # dp[i] = Length of longest valid subsequence ending at index i
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            # Check increasing condition and bitwise condition
            if arr[j] < arr[i] and ((arr[j] & arr[i]) * 2 < (arr[j] | arr[i])):
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# Input
n = int(input())
arr = [int(input()) for _ in range(n)]

# Output
print(longest_valid_subsequence(n, arr))
```

---

# 🔍 Step-by-Step Code Explanation

## Step 1: Function Definition

```python
def longest_valid_subsequence(n, arr):
```

Creates a function that takes:

- `n` → Number of elements
- `arr` → Input array

---

## Step 2: Initialize DP

```python
dp = [1] * n
```

Initially every element itself forms a subsequence.

Example:

```text
Array: 15 6 5 12 1

DP:    1 1 1 1 1
```

---

## Step 3: Traverse Every Element

```python
for i in range(n):
```

Treat `arr[i]` as the last element of the subsequence.

---

## Step 4: Check All Previous Elements

```python
for j in range(i):
```

Try extending the subsequence ending at every previous index.

---

## Step 5: Verify the Conditions

```python
if arr[j] < arr[i] and ((arr[j] & arr[i]) * 2 < (arr[j] | arr[i])):
```

Two conditions are checked:

1. Increasing order
2. Bitwise condition

Only if both are true can `arr[i]` follow `arr[j]`.

---

## Step 6: Update DP

```python
dp[i] = max(dp[i], dp[j] + 1)
```

Extend the previous subsequence and keep the maximum length.

---

## Step 7: Return the Answer

```python
return max(dp)
```

The longest valid subsequence may end at any position, so return the maximum value in the DP array.

---

# 🧪 Dry Run

For the input:

```text
15
6
5
12
1
```

Initially:

```text
DP = [1, 1, 1, 1, 1]
```

Processing `12`:

- `15 → 12` ❌ (Not increasing)
- `6 → 12` ✅
- `5 → 12` ✅

Updated DP:

```text
DP = [1, 1, 1, 2, 1]
```

Maximum value:

```text
2
```

Hence the answer is:

```text
2
```

---

# 🎯 Pattern Recognition

Whenever a problem asks for:

- Longest subsequence
- Elements remain in original order
- Maximum length
- An additional condition between consecutive selected elements

it is often an **LIS Dynamic Programming variation**.

General template:

```python
dp = [1] * n

for i in range(n):
    for j in range(i):
        if can_extend(arr[j], arr[i]):
            dp[i] = max(dp[i], dp[j] + 1)

answer = max(dp)
```

Only the `can_extend()` condition changes from one problem to another.

# 4 Problem Name: Minimize Binary String Ugliness

## 📄 Problem Statement

You are given a binary string $S$ of length $N$ consisting only of `'0'`s and `'1'`s. The **ugliness** of a binary string is defined as the decimal integer value that the string represents.

**Examples:**
* `"101"` represents `5`
* `"0000"` represents `0`
* `"01010"` represents `10`

There are two types of operations you can perform on the string:
1. **Swap:** Swap any two characters by paying a cost of **$A$** coins.
2. **Flip:** Flip any character (turn `'1'` $\rightarrow$ `'0'` or `'0'` $\rightarrow$ `'1'`) by paying a cost of **$B$** coins.

Initially, you are given **`CASH`** coins. Your task is to **minimize the ugliness** of the string by performing these operations. After each operation, your remaining coins decrease by the operation's cost. 

Since the output can be very large, return the final decimal value **modulo $10^9 + 7$**.

### Constraints
* $1 \le N \le 10^5$
* $1 \le \text{CASH} \le 10^5$
* $1 \le A \le 10^5$
* $1 \le B \le 10^5$

---

## 🎯 Used Pattern & Algorithmic Concepts

1. **Greedy Strategy (Most Significant Bit Priority):** 
   In binary representation, the leftmost bits hold exponentially higher value ($2^{N-1}, 2^{N-2}, \dots$). Thus, we must always prioritize clearing `'1'`s from **left to right**.
2. **Binary Search on Answer / Capacity:** 
   When swapping is cheaper than flipping, finding the maximum number of leftmost `'1'`s ($K$) we can eliminate within our budget is non-trivial. We binary search over $K \in [0, \text{count of '1's}]$.
3. **Two-Pointer Strategy:** 
   To check if clearing $K$ `'1'`s is affordable, we use two pointers to greedily pair the leftmost `'1'`s with the rightmost available `'0'`s.

---

## 💡 Approach to Solve

1. **Identify Operation Cost Cases:**
   * **Case 1 ($B \le A$ - Flipping is Cheaper or Equal):**
     Swapping never makes sense because destroying a `'1'` costs less than or equal to moving it. We greedily flip the leftmost `'1'`s into `'0'`s as long as we have enough `CASH`.
   
   * **Case 2 ($A < B$ - Swapping is Cheaper):**
     * Use **Binary Search** to find the maximum number of leftmost `'1'`s ($K$) that can be eliminated within our budget.
     * In each search step, greedily pair the $K$ target `'1'`s with the rightmost `'0'`s using two pointers. If a `'1'` is to the left of a `'0'`, we swap them; otherwise, we must flip it.
     * **Budget Optimization:** Once the maximum $K$ is found, any leftover cash is used to "upgrade" Swaps into Flips (costing $B - A$ extra coins per upgrade) to eliminate `'1'`s permanently instead of moving them to the right.

2. **Calculate Final Decimal Value:**
   Traverse the updated binary string from right to left, adding powers of 2 ($2^0, 2^1, 2^2, \dots$) modulo $10^9 + 7$ wherever a `'1'` remains.

---

## 💻 Python Code
## 🔍 Line-by-Line Code Explanation

### 1. Function Initialization & Index Tracking
* `def minimize_string_ugliness(n, s, cash, a, b):` — Defines the main function accepting length `n`, binary string `s`, initial `cash`, swap cost `a`, and flip cost `b`.
* `MOD = 10**9 + 7` — Modulo constant to prevent integer overflow with large numbers.
* `s_list = list(s)` — Converts the immutable binary string into a mutable list of characters so bits can be updated in-place.
* `ones = [...]` — Creates a list storing all 0-based index positions where `'1'` appears in `s`.
* `zeros = [...]` — Creates a list storing all 0-based index positions where `'0'` appears in `s`.

---

### 2. Case 1 Logic ($B \le A$)
* `if b <= a:` — Checks if flipping is cheaper or equal to swapping.
* `max_flips = min(len(ones), cash // b)` — Calculates the maximum number of `'1'`s we can afford to flip, capped at the total count of available `'1'`s.
* `for i in range(max_flips): s_list[ones[i]] = '0'` — Directly flips the leftmost `'1'`s into `'0'`s.

---

### 3. Helper Function `can_clear(k, current_cash)`
* `if k == 0: return True, 0, []` — Base case: clearing zero elements requires 0 coins and is always feasible.
* `p1 = k - 1` — Pointer for the $k$-th `'1'` from the left.
* `p2 = len(zeros) - 1` — Pointer starting at the absolute rightmost `'0'`.
* `limit_p2 = max(0, len(zeros) - k)` — Bound to restrict pointer checks to at most $k$ zeros from the right end.
* `while p1 >= 0 and p2 >= limit_p2:` — Loop to greedily pair leftmost `'1'`s with rightmost `'0'`s.
* `if ones[p1] < zeros[p2]:` — Valid swap condition (ensures the `'1'` moves rightward).
* `swaps += 1; used_zeros.append(...); p1 -= 1; p2 -= 1` — Records the swap, saves the target `'0'` index, and decrements both pointers.
* `else: p1 -= 1` — If the `'1'` is already to the right of the `'0'`, swapping doesn't help, so it must be flipped instead.
* `flips = k - swaps` — Calculates required flips for non-swappable `'1'`s.
* `cost = (swaps * a) + (flips * b)` — Calculates the total coin cost for clearing $k$ bits.
* `return cost <= current_cash, swaps, used_zeros` — Returns boolean feasibility, total swaps performed, and zero indices used.

---

### 4. Binary Search & Budget Optimization
* `low, high = 0, len(ones)` — Binary search boundaries ranging from $0$ to the total count of `'1'`s.
* `while low <= high:` — Standard binary search loop to find maximum clearable bits.
* `mid = (low + high) // 2` — Midpoint candidate $k$.
* `possible, _, _ = can_clear(mid, cash)` — Tests if clearing `mid` bits fits within the available budget.
* `if possible: best_k = mid; low = mid + 1` — Records valid $k$ and attempts to clear more bits in the upper half.
* `else: high = mid - 1` — Reduces search range if `mid` is unaffordable.
* `_, max_possible_swaps, used_zeros = can_clear(best_k, cash)` — Retrieves the exact swap distribution for `best_k`.
* `leftover_cash = cash - min_cost` — Calculates remaining unused coins.
* `extra_flips = leftover_cash // (b - a)` — Upgrades planned swaps into flips using leftover cash (each upgrade costs $B - A$ extra coins).
* `actual_flips` & `actual_swaps` — Final counts of flips and swaps to perform.
* `for i in range(best_k): s_list[ones[i]] = '0'` — Clears the first `best_k` positions to `'0'`.
* `for i in range(actual_swaps): s_list[used_zeros[i]] = '1'` — Marks the target landing positions on the far right as `'1'`s.

---

### 5. Decimal Value Calculation
* `ans = 0; power = 1` — Initializes result accumulator and binary weight multiplier ($2^0$).
* `for i in range(n - 1, -1, -1):` — Iterates right-to-left over the modified binary string.
* `if s_list[i] == '1': ans = (ans + power) % MOD` — Adds the current positional weight modulo $10^9 + 7$ whenever a `'1'` is present.
* `power = (power * 2) % MOD` — Doubles the positional weight for the next bit position to the left.
* `return ans` — Returns the final minimized decimal value.


# Problem Name: Maximize Subset XOR with Size Constraint

---

## 📄 Problem Statement

Khaled has an array $A$ of $N$ elements, where $N$ is guaranteed to be an **even integer**. He wants to choose at most $\frac{N}{2}$ elements from array $A$ (not necessarily consecutive) to **maximize the bitwise XOR sum** of the chosen elements.

**Example 1:**
* $A = [2, 4, 6, 8]$, $N = 4$
* Khaled can choose subset $[2, 4, 8]$ (size 3 $> \frac{N}{2}$, invalid) or subset $[8]$ or $[2, 4]$ (size $2 \le \frac{N}{2}$).
* Max valid subset XOR within size $\le 2$ is $7$ for sample inputs.

### Constraints
* $1 \le N \le 120$ ($N$ is even)
* $1 \le A[i] \le 10^6$

---

## 🎯 Used Pattern & Algorithmic Concepts

1. **Dynamic Programming / BFS State Expansion:**
   Instead of brute-forcing $2^N$ subsets, we keep track of achievable XOR sum values `v` and the **minimum number of elements** needed to form `v`.
2. **Bitwise Properties & Bounded State Space:**
   Since $A[i] \le 10^6 < 2^{20}$, any XOR combination is strictly less than $2^{20} = 1,048,576$. This small state space allows ultra-fast lookup.
3. **Subset Size Constraint ($\le \frac{N}{2}$):**
   Transitions are pruned whenever the required element count exceeds $\frac{N}{2}$.

---

## 💡 Approach to Solve

1. **Determine State Space Upper Bound:**
   Calculate `max_val = 1 << max(A).bit_length()`, which represents the next power of 2 above $\max(A)$. All possible subset XOR sums fall within $[0, \text{max\_val} - 1]$.

2. **Initialize DP & Reachable List:**
   * Create array `dp` of size `max_val` initialized to infinity (`121`), where `dp[0] = 0`.
   * Maintain a list `reachable = [0]` to store currently discovered XOR sum states.

3. **Process Each Element $x \in A$:**
   * Iterate over all previously `reachable` XOR values $v$.
   * Compute new XOR value `nxt_v = v ^ x` and count `nxt_cnt = dp[v] + 1`.
   * If `nxt_cnt <= N // 2`, queue `(nxt_v, nxt_cnt)` in an `updates` list.
   * Apply all `updates` after scanning to ensure element $x$ is used at most once per turn.

4. **Extract Maximum XOR:**
   Iterate through all `reachable` values and pick the maximum value $v$ satisfying `dp[v] <= N // 2`.

---

## 🔍 Line-by-Line Code Explanation

### 1. Function Initialization & Bound Setup
* `def max_subset_xor(n, arr):` — Defines the solver function accepting length `n` and array `arr`.
* `max_limit = n // 2` — Upper limit on the number of elements allowed in the subset.
* `max_a = max(arr)` — Finds the maximum element in `arr`.
* `max_val = 1 << max_a.bit_length()` — Calculates the smallest power of 2 greater than `max_a` to bound the `dp` size.
* `dp = [121] * max_val` — Initializes DP array with `121` (representing infinity, since $N \le 120$).
* `dp[0] = 0` — Base case: an empty subset has XOR sum `0` and size `0`.
* `reachable = [0]` — List of currently reachable XOR sums.

---

### 2. State Expansion Loop
* `for x in arr:` — Loops over each number in `arr`.
* `updates = []` — Temporary list to store new valid state transitions for current element `x`.
* `for v in reachable:` — Loops through all currently discovered XOR values.
* `nxt_cnt = dp[v] + 1` — Increment element count required for candidate state `v ^ x`.
* `if nxt_cnt <= max_limit:` — Prunes states that exceed the maximum allowed subset size $\frac{N}{2}$.
* `updates.append((v ^ x, nxt_cnt))` — Stores candidate transition `(nxt_v, nxt_cnt)`.

---

### 3. Applying State Updates
* `for nxt_v, nxt_cnt in updates:` — Iterates over generated state updates.
* `if dp[nxt_v] == 121:` — Checks if `nxt_v` has never been reached before.
* `dp[nxt_v] = nxt_cnt; reachable.append(nxt_v)` — Sets minimum count and adds `nxt_v` to `reachable`.
* `elif nxt_cnt < dp[nxt_v]:` — If `nxt_v` was reached before but current path uses fewer elements, update `dp[nxt_v] = nxt_cnt`.

---

### 4. Maximizing Answer & Input Handling
* `max_xor = 0` — Variable to track the maximum valid XOR sum found.
* `for v in reachable:` — Iterates over all reached states.
* `if dp[v] <= max_limit and v > max_xor: max_xor = v` — Updates `max_xor` if `v` satisfies size constraint and is greater.
* `return max_xor` — Returns the maximum XOR sum achieved.




# 👨‍💻 Author

**Rahul Debnath**

If you found this repository useful, feel free to ⭐ the project and connect with me on GitHub!
