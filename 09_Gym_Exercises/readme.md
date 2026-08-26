# 12 🏋️ Gym Exercises – Minimum Exercises to Become Tired

[![Repository](https://img.shields.io/badge/Repository-infosys--preparation-blue?logo=github)](https://github.com/RahulDebnath007/infosys-preparation)

**Pattern:** Greedy + Sorting

---

## 📌 Problem Statement

You are given an initial amount of energy `E`.

There are `N` exercises in the gym. The `i-th` exercise drains `A[i]` units of energy.

You become tired when your energy becomes **less than or equal to `0`**.

Each unique exercise can be performed **at most 2 times** because other people also need to use the machines.

The task is to find the **minimum number of exercise performances** required to make the energy reach `0` or below.

If performing every exercise twice still does not make the energy reach `0` or below, return:

```text
-1
```

---

# 💡 Approach

The goal is to minimize the **number of exercises performed**.

Every exercise has a positive energy-drain value.

Therefore, to become tired using the fewest exercises, we should always choose the exercise that removes the **largest amount of energy** first.

This leads to a:

```text
Greedy + Sorting
```

approach.

Because every exercise can be performed at most twice, each value can contribute at most two times.

For example:

```text
A = [1, 2]
```

The available exercise performances are conceptually:

```text
[1, 1, 2, 2]
```

Sorting them in descending order gives:

```text
[2, 2, 1, 1]
```

We then perform exercises in this order until:

```text
energy <= 0
```

---

# 🔑 Key Observation

Suppose the initial energy is:

```text
E = 10
```

and the exercises are:

```text
A = [2, 4, 7]
```

Each exercise can be performed twice.

So the maximum possible energy drain is:

```text
2 + 2 + 4 + 4 + 7 + 7
```

or:

```text
2 × (2 + 4 + 7) = 26
```

If:

```text
26 < 10
```

then becoming tired is impossible.

Otherwise, we should use the largest drains first.

After sorting:

```text
[7, 4, 2]
```

we conceptually perform:

```text
7, 7, 4, 4, 2, 2
```

and stop as soon as the energy reaches `0` or below.

---

# 🧠 Why Greedy Works

We want the **minimum number of exercises**.

Every exercise has a positive energy drain.

Therefore, if one available exercise removes more energy than another, choosing the larger one cannot require more exercises than choosing the smaller one.

For example:

```text
Energy required = 10

Available drains:
3, 5, 8
```

Choosing the largest values first:

```text
8 + 5 = 13
```

requires only:

```text
2 exercises
```

Choosing smaller values first could require more exercises.

Therefore:

> When the objective is to reach a target using the minimum number of positive-value operations, taking the largest available contribution first is optimal.

The **at most 2 times** restriction is handled by allowing each exercise exactly two opportunities.

---

# 🔍 Handling the "At Most 2 Times" Rule

Suppose:

```text
A = [5, 3, 2]
```

Each exercise can be used at most twice.

Therefore, the available contributions are:

```text
5, 5
3, 3
2, 2
```

After sorting the original values:

```text
5, 3, 2
```

we can simply process each value twice:

```text
5
5
3
3
2
2
```

There is no need to create a separate array containing duplicate values.

This saves additional memory.

---

# 📝 Algorithm

1. Read the initial energy `E`.
2. Read the number of exercises `N`.
3. Read all exercise energy-drain values.
4. Sort the array in descending order.
5. For every exercise:

   * Perform it once.
   * If energy is still positive, perform it a second time.
   * After every performance, increase the exercise count.
6. If energy becomes `0` or below, return the count.
7. If every exercise has been performed twice and energy is still positive, return `-1`.

---

# 📝 Code Explanation

## Step 1 — Read Energy

```python id="g4m8vx"
E = int(input())
```

Read the initial energy.

For example:

```text
E = 6
```

---

## Step 2 — Read Number of Exercises

```python id="k7q2mp"
N = int(input())
```

Read the number of unique exercises.

---

## Step 3 — Read the Exercise Values

```python id="p9x3vw"
A = []

for _ in range(N):
    A.append(int(input()))
```

Store the energy drain of every exercise.

For example:

```text
1
2
```

becomes:

```text
[1, 2]
```

---

## Step 4 — Sort in Descending Order

```python id="m6r1qs"
A.sort(reverse=True)
```

We want the largest energy drains first.

For:

```text
[1, 2]
```

the result is:

```text
[2, 1]
```

---

## Step 5 — Initialize Counters

```python id="v8k4zn"
count = 0
energy = E
```

`count` stores the number of exercise performances.

`energy` stores the current remaining energy.

---

## Step 6 — Process Every Exercise

```python id="q3m7xc"
for x in A:
```

Process exercises from largest drain to smallest drain.

---

## Step 7 — Perform the Exercise Once

```python id="n5w2kp"
energy -= x
count += 1
```

Reduce the energy by `x` and increase the number of performances.

---

## Step 8 — Check Whether We Are Tired

```python id="r9v4mq"
if energy <= 0:
    print(count)
    break
```

If the energy has reached `0` or below, we are tired.

The current count is therefore the minimum number of exercises required.

---

## Step 9 — Perform the Same Exercise a Second Time

```python id="t6x1ns"
energy -= x
count += 1
```

Each unique exercise can be performed at most twice, so we now use its second allowed performance.

---

## Step 10 — Check Again

```python id="b8q3wm"
if energy <= 0:
    print(count)
    break
```

If energy is now `0` or below, print the number of performances.

---

## Step 11 — Handle the Impossible Case

```python id="s2m7vx"
else:
    print(-1)
```

The `else` belongs to the `for` loop.

It executes only when the loop finishes normally, meaning:

* Every exercise was used twice.
* Energy is still greater than `0`.
* Therefore, becoming tired is impossible.

So we return:

```text
-1
```

---

# 💻 Complete Code

```python id="q8m3vz"
E = int(input())
N = int(input())

A = []

for _ in range(N):
    A.append(int(input()))

# Sort exercises by energy drain in descending order
A.sort(reverse=True)

count = 0
energy = E

# Each exercise can be performed at most 2 times
for x in A:

    # First time
    energy -= x
    count += 1

    if energy <= 0:
        print(count)
        break

    # Second time
    energy -= x
    count += 1

    if energy <= 0:
        print(count)
        break

else:
    # All exercises have been performed twice,
    # but energy is still positive.
    print(-1)
```

---

# 🧪 Dry Run

## Sample Input 1

```text
6
2
1
2
```

Initial values:

```text
Energy = 6
Exercises = [1, 2]
```

After sorting:

```text
[2, 1]
```

Now process the exercises.

### Exercise `2` — First Time

```text
Energy = 6 - 2
       = 4

Count = 1
```

### Exercise `2` — Second Time

```text
Energy = 4 - 2
       = 2

Count = 2
```

### Exercise `1` — First Time

```text
Energy = 2 - 1
       = 1

Count = 3
```

### Exercise `1` — Second Time

```text
Energy = 1 - 1
       = 0

Count = 4
```

Now:

```text
Energy <= 0
```

Therefore:

```text
Answer = 4
```

---

# 🧪 Dry Run — Sample 2

Input:

```text
10
2
1
2
```

Maximum possible energy drain:

```text
2 + 2 + 1 + 1 = 6
```

Initial energy:

```text
10
```

Even after using every exercise twice:

```text
10 - 6 = 4
```

Energy is still positive.

Therefore, we cannot become tired.

Output:

```text
-1
```

---

# 🧪 Dry Run — Sample 3

Input:

```text
2
3
1
5
2
```

Initial:

```text
Energy = 2
```

Exercises:

```text
[1, 5, 2]
```

Sort descending:

```text
[5, 2, 1]
```

Perform the largest exercise:

```text
Energy = 2 - 5
       = -3
```

We are immediately tired.

Therefore:

```text
Answer = 1
```

---

# 🔍 Why Choosing the Largest Exercise First Is Optimal

Suppose the current energy is:

```text
10
```

and available exercise drains are:

```text
8, 5, 3
```

If we choose `8` first:

```text
10 - 8 = 2
```

One more exercise with drain `5` gives:

```text
2 - 5 = -3
```

So:

```text
2 exercises
```

are enough.

The general principle is:

> To minimize the number of positive contributions needed to reach a target, use the largest available contributions first.

The restriction that each exercise can be used at most twice does not break this greedy strategy because each exercise simply has two available opportunities.

---

# 📊 Complexity Analysis

## Time Complexity

Sorting the `N` exercises takes:

```text
O(N log N)
```

Then every exercise is processed at most twice:

```text
O(N)
```

Therefore:

```text
Time Complexity = O(N log N)
```

---

## Space Complexity

The array stores `N` exercise values:

```text
O(N)
```

No additional array is required for the second usage of each exercise.

Therefore:

```text
Space Complexity = O(N)
```

---

# 🧩 Pattern Used

* Greedy Algorithm
* Sorting
* Limited-Usage Selection
* Target Sum / Threshold Problem

---

# 🎯 Pattern Recognition

This problem has the structure:

```text
Need minimum number of operations
        ↓
Each operation has a positive contribution
        ↓
Need contribution >= target
        ↓
Each item has limited usage
        ↓
Maximize contribution per operation
        ↓
Sort in descending order
        ↓
Take the largest contribution first
```

Whenever you see:

* A target that must be reached.
* Positive values.
* The goal is to use the **minimum number of items/operations**.
* Each item has a limited number of uses.

Think:

```text
Greedy + Sorting
```

---

# 🚀 Key Learning

> When you need to reach a target using the minimum number of positive contributions, choosing the largest available contribution first is a natural greedy strategy.

For this problem:

```text
Energy
   ↓
Need to reduce it to <= 0
   ↓
Sort exercises by drain descending
   ↓
Use each exercise at most twice
   ↓
Stop as soon as energy <= 0
```

The core operation is:

```python id="f4m8qx"
A.sort(reverse=True)
```

followed by using each value at most two times.

If all exercises are exhausted and energy is still positive:

```text
answer = -1
```

---

# 📚 Suitable For

* Infosys Coding Assessment
* Greedy Algorithm Practice
* Sorting Problems
* Array Problems
* Target Sum / Threshold Problems
* Limited-Usage Selection Problems
* Competitive Programming
* Coding Interviews


