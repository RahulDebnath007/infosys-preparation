# 13 ⚔️ Heroes vs Villains – Minimum Villains to Remove

## 📌 Problem Statement

There are `M` heroes, and every hero starts with the same health `H`.

There are `N` villains, where the `i-th` villain has health `V[i]`.

Heroes fight the villains **one by one in their given order**.

When a hero with current health `X` fights a villain with health `V[i]`:

* If `X > V[i]`, the villain is defeated and the hero's health becomes `X - V[i]`.
* If `X < V[i]`, the hero is defeated and the villain survives.
* If `X = V[i]`, both the hero and villain are defeated.

The heroes win only when **all remaining villains are defeated**.

You are allowed to remove villains **only from the front** of the sequence.

The task is to determine the **minimum number of villains that must be removed** so that the remaining villains can be defeated using at most `M` heroes.

---

## 💡 Key Observation

Because villains can only be removed from the **front**, the remaining villains must always form a **suffix** of the original array.

For example:

```text
Villains = [4, 1, 2, 3, 1]
```

Possible remaining sequences are:

```text
[4, 1, 2, 3, 1]
[1, 2, 3, 1]
[2, 3, 1]
[3, 1]
[1]
[]
```

Therefore, instead of directly searching for the minimum number of removals, we can search for the:

> **Longest suffix that can be defeated using at most `M` heroes.**

Once the longest feasible suffix is found, everything before it must be removed.

---

## 🧠 Greedy Approach

All heroes have the same initial health:

```text
H
```

A hero can defeat a consecutive group of villains as long as the total health of those villains does not exceed `H`.

For example:

```text
H = 10
Villains = [3, 2, 4]
```

The total health is:

```text
3 + 2 + 4 = 9
```

So one hero can defeat the complete group.

The problem can therefore be viewed as:

```text
Partition the suffix into consecutive groups
where each group's sum <= H
```

We process the villains **from right to left** because we are trying to construct the longest feasible suffix.

---

## 🔍 Why Process From the Right?

Suppose:

```text
H = 10
Villains = [3, 4, 5, 2]
```

Starting from the right:

```text
2
```

Add `5`:

```text
5 + 2 = 7
```

Add `4`:

```text
4 + 5 + 2 = 11
```

This exceeds `H = 10`.

Therefore, `4` cannot belong to the same hero's group.

We start another hero:

```text
[3, 4] [5, 2]
```

The group sums are:

```text
3 + 4 = 7
5 + 2 = 7
```

So two heroes are sufficient.

---

## 🔑 Important Edge Case

If a villain has health greater than `H`:

```text
V[i] > H
```

then no hero can defeat that villain.

Therefore, that villain cannot be part of the remaining suffix.

Since only a prefix can be removed, the entire prefix through that villain must be removed.

---

## 📝 Algorithm

1. Read `N`, `M`, and `H`.
2. Read the health values of all villains.
3. Start processing from the last villain.
4. Maintain:

   * `heroes_used` → number of heroes required.
   * `current_health_used` → total villain health assigned to the current hero.
5. For every villain from right to left:

   * If `V[i] > H`, the villain cannot be defeated, so remove the prefix through index `i`.
   * Otherwise, try adding the villain to the current hero.
   * If the total remains `<= H`, keep it in the current group.
   * Otherwise, start a new hero group.
6. If `heroes_used > M`, the current suffix is impossible.
7. Remove the prefix through the current index.
8. If the complete array is processed successfully, answer is `0`.

---

## 💻 Complete Python Code

```python
N = int(input())
M = int(input())
H = int(input())

villains = []

for _ in range(N):
    villains.append(int(input()))

# We want the longest feasible suffix,
# so process villains from right to left.

heroes_used = 1
current_health_used = 0

for i in range(N - 1, -1, -1):

    villain = villains[i]

    # A villain with health greater than H
    # can never be defeated by any hero.
    if villain > H:
        print(i + 1)
        break

    # Try to assign this villain to the current hero.
    if current_health_used + villain <= H:
        current_health_used += villain

    else:
        # Need another hero.
        heroes_used += 1
        current_health_used = villain

        # We have run out of heroes.
        if heroes_used > M:
            print(i + 1)
            break

else:
    # Every villain can be defeated.
    print(0)
```

---

## 🧪 Dry Run

### Sample Input

```text
4
4
3
3
1
3
3
```

Initial values:

```text
N = 4
M = 4
H = 3

Villains = [3, 1, 3, 3]
```

Process from right to left.

### Villain `3`

```text
current = 0 + 3 = 3
```

One hero is enough.

### Next Villain `3`

```text
3 + 3 = 6
```

Since:

```text
6 > 3
```

we need another hero.

```text
heroes_used = 2
current = 3
```

### Next Villain `1`

```text
3 + 1 = 4
```

Again:

```text
4 > 3
```

Start another hero:

```text
heroes_used = 3
current = 1
```

### Next Villain `3`

```text
1 + 3 = 4
```

Again a new hero is required:

```text
heroes_used = 4
current = 3
```

We used exactly `4` heroes.

Therefore, the complete array is feasible.

### Output

```text
0
```

---

## 📊 Complexity Analysis

### Time Complexity

Every villain is processed exactly once.

```text
O(N)
```

No sorting is required.

### Space Complexity

The villain array stores `N` values:

```text
O(N)
```

Apart from the input array, only a few variables are used.

---

## 🧩 Pattern Used

This problem combines several important competitive-programming patterns:

* Greedy Algorithm
* Suffix Processing
* Prefix Removal
* Consecutive Partitioning
* Simulation
* Two-Pointer-style Feasibility

---

## 🎯 Pattern Recognition

The problem follows this structure:

```text
Can remove only from the front
          ↓
Remaining elements form a suffix
          ↓
Need minimum removals
          ↓
Find longest feasible suffix
          ↓
Process from the right
          ↓
Greedily partition villains among heroes
          ↓
Maximum M heroes allowed
          ↓
Minimum prefix removed
```

Whenever you see:

* Elements must remain in their original order.
* You can remove only a prefix.
* The objective is to minimize removals.
* The remaining suffix must satisfy a feasibility condition.

Think:

```text
Longest Feasible Suffix
+
Greedy / Two-Pointer Processing
```

---

## 🚀 Key Learning

The main idea to remember is:

> **When a problem allows removing only from the front and asks for the minimum number of removals, think in terms of finding the longest feasible suffix.**

For this problem:

```text
Villains
   ↓
Remove a prefix
   ↓
Keep a suffix
   ↓
Process suffix from right to left
   ↓
Greedily partition villains among heroes
   ↓
Maximum M heroes allowed
   ↓
Minimum prefix removed
```

The core greedy condition is:

```python
if current_health_used + villain <= H:
    current_health_used += villain
else:
    heroes_used += 1
    current_health_used = villain
```

If:

```text
heroes_used > M
```

then the current suffix is impossible and the required prefix must be removed.

---

## 📚 Suitable For

* Infosys Coding Assessment
* Greedy Algorithm Practice
* Array Problems
* Prefix/Suffix Problems
* Two-Pointer-style Problems
* Simulation Problems
* Partitioning Problems
* Competitive Programming
* Coding Interviews

---

## ⭐ Tags

```text
#Python
#Greedy
#Arrays
#Suffix
#Prefix
#Simulation
#TwoPointers
#CompetitiveProgramming
#Infosys
#CodingInterview
```