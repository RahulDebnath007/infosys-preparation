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



# 👨‍💻 Author

**Rahul Debnath**

If you found this repository useful, feel free to ⭐ the project and connect with me on GitHub!
