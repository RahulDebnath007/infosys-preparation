# 🧱 Magic Machine Drying Walls

## 📌 Problem Overview

There are `N` walls that need to dry.

For each wall:

* Wall `i` naturally requires `Xi` minutes to dry.
* A special machine can work on a wall for one minute.
* Every one minute of machine operation reduces the remaining drying time by `K`.
* There is only **one machine**.
* The machine can be moved to another wall after finishing its work on the current wall.
* The objective is to minimize the **total time required for all walls to finish**.

The machine operation itself consumes real time.

---

# 🧩 Problem Statement

Given:

```text id="a9k3v2"
N = number of walls
K = machine efficiency
X[i] = natural drying time of wall i
```

Find the minimum total time `T` such that every wall can be completely dried using natural drying and the single machine.

---

# 🔍 Important Observation

Suppose a wall naturally requires:

```text id="q5m8r2"
X minutes
```

and the machine works on it for one minute.

The machine:

```text id="7v2p9m"
reduces drying time by K
```

but the machine itself consumes:

```text id="3k8q1w"
1 minute
```

Therefore, the **net improvement** from one machine minute is:

```text id="m4p7c2"
K - 1
```

This is the key observation.

---

# 💡 Why `K - 1`?

Suppose:

```text id="x6q2m8"
K = 17
```

One machine minute gives:

```text id="5r8p1v"
17 minutes of drying progress
```

but costs:

```text id="9m3k7q"
1 minute of actual time
```

So the effective reduction in the required total time is:

```text id="p4v8m2"
17 - 1 = 16
```

Therefore:

```text id="7q2c5n"
effective improvement = K - 1
```

---

# 🎯 Pattern Used

## Binary Search on Answer

We do not directly calculate the minimum total time.

Instead, we ask:

> **Can all walls be completed within `T` minutes?**

This is a **feasibility problem**.

If we can finish everything within `T` minutes:

```text
possible(T) = True
```

Otherwise:

```text
possible(T) = False
```

The important property is **monotonicity**:

```text
If T is possible,
then every T' > T is also possible.
```

Therefore, we can binary-search for the smallest possible `T`.

---

# 🧠 Feasibility Check

Suppose we want everything to be completed within:

```text id="k7m2q4"
T minutes
```

Consider a wall whose natural drying time is:

```text id="p8v3m6"
X
```

If:

```text id="2q9c5r"
X <= T
```

then the wall can finish naturally within the target time.

No machine work is required.

Therefore:

```text id="m4x8q1"
required_machine_time = 0
```

---

## When `X > T`

The wall needs additional machine assistance.

The amount by which its natural drying time exceeds the target is:

```text id="c6p2v9"
X - T
```

Each machine minute provides a net improvement of:

```text id="r7m3q8"
K - 1
```

Therefore, the number of machine minutes required is:

```text id="j5k8m2"
ceil((X - T) / (K - 1))
```

---

# 🔢 Ceiling Division

In Python, we can calculate:

```text id="8q2m5v"
ceil(a / b)
```

using:

```python id="6r4p8x"
(a + b - 1) // b
```

Therefore:

```python id="1m7q3c"
need = (X - T + (K - 2)) // (K - 1)
```

because:

```text id="3v8m2p"
b = K - 1
```

and:

```text id="a5q9k1"
b - 1 = K - 2
```

---

# ⏱️ Machine Time Constraint

There is only **one machine**.

Therefore, if all walls need a total of:

```text id="f7m2q8"
required
```

machine minutes, we must have:

```text id="n4c8v1"
required <= T
```

because the machine cannot perform more than `T` minutes of work during a total time interval of `T`.

So:

```python id="x8m3q5"
return required <= T
```

determines whether the target time is feasible.

---

# 🔄 Binary Search

The minimum possible time is:

```text id="7m2p9q"
0
```

The maximum useful upper bound is:

```text id="c5v8m1"
max(X)
```

because without machine assistance, every wall can naturally finish by `max(X)`.

Therefore:

```python id="p3q7m9"
low = 0
high = max(x)
```

Then repeatedly calculate:

```python id="m8v2c4"
mid = (low + high) // 2
```

If `mid` is feasible:

```text id="r5q9m2"
high = mid
```

because we try to find an even smaller answer.

Otherwise:

```text id="k7p3v8"
low = mid + 1
```

because `mid` is too small.

At the end:

```text id="d2m8q5"
low
```

is the minimum feasible time.

---

# 💻 Python 3 Solution

```python id="7m4q8p"
def solve():
    n = int(input())
    k = int(input())

    x = [int(input()) for _ in range(n)]

    # If K = 1, the machine provides no net improvement.
    if k == 1:
        print(max(x))
        return

    def possible(T):
        required = 0

        for value in x:

            # This wall can finish naturally within T.
            if value > T:

                # Machine minutes required
                need = (value - T + (k - 2)) // (k - 1)

                required += need

                # One machine cannot work for more than T minutes.
                if required > T:
                    return False

        return required <= T

    low = 0
    high = max(x)

    while low < high:
        mid = (low + high) // 2

        if possible(mid):
            high = mid
        else:
            low = mid + 1

    print(low)


solve()
```

---

# 🔍 Code Explanation

## Step 1 — Read Input

```python id="q8m2v5"
n = int(input())
k = int(input())
x = [int(input()) for _ in range(n)]
```

We store the natural drying time of every wall.

---

# Step 2 — Handle `K = 1`

```python id="m5p8q2"
if k == 1:
    print(max(x))
    return
```

This case is important.

If:

```text id="v3q7m1"
K = 1
```

one minute of machine work reduces the drying requirement by exactly one minute, but the machine also consumes one minute.

Therefore:

```text id="8k2m5p"
net improvement = K - 1
               = 0
```

The machine gives no benefit.

So the optimal answer is simply:

```text id="c4q9v2"
max(X)
```

---

# Step 3 — Feasibility Function

```python id="r8m3q6"
def possible(T):
```

This function answers:

> Can every wall be completed within `T` minutes?

---

# Step 4 — Calculate Required Machine Time

```python id="p7q2m8"
if value > T:
    need = (value - T + (k - 2)) // (k - 1)
```

Only walls with:

```text id="n5v8c3"
value > T
```

need machine assistance.

The excess drying time is:

```text id="j4m7q2"
value - T
```

and each machine minute gives:

```text id="x8p3v5"
K - 1
```

net improvement.

---

# Step 5 — Accumulate Machine Usage

```python id="c6m2q9"
required += need
```

Because there is only one machine, all machine operations must be performed sequentially.

So we add the required machine time for every wall.

---

# Step 6 — Early Termination

```python id="r3v8m5"
if required > T:
    return False
```

If the machine already needs more than `T` minutes, the target `T` is impossible.

There is no reason to continue checking the remaining walls.

This is an optimization.

---

# Step 7 — Check Feasibility

```python id="k5q2m8"
return required <= T
```

If the total machine workload fits inside `T` minutes, then the target is feasible.

---

# Step 8 — Binary Search

```python id="m8v4p2"
low = 0
high = max(x)
```

We search between:

```text id="q7c3m9"
0
```

and:

```text id="v2p8k5"
maximum natural drying time
```

---

# Step 9 — Find the Minimum

```python id="x4m7q2"
while low < high:
    mid = (low + high) // 2
```

If:

```python id="n8p3v6"
possible(mid)
```

is true:

```python id="j5q9m2"
high = mid
```

Otherwise:

```python id="c7m2v8"
low = mid + 1
```

When:

```text id="r4p8q1"
low == high
```

we have found the smallest feasible time.

---

# 🔬 Example Walkthrough

Suppose:

```text id="k2m8q5"
X = [35]
K = 17
```

The effective improvement per machine minute is:

```text id="p7v3m9"
K - 1
= 17 - 1
= 16
```

---

## Try `T = 2`

The wall naturally requires:

```text id="x5q8m2"
35 minutes
```

We need to reduce it to `2`.

Required reduction:

```text id="m3p7v9"
35 - 2 = 33
```

Each machine minute provides `16` units of net improvement.

Therefore:

```text id="q8m2c5"
ceil(33 / 16)
= 3
```

machine minutes are required.

But:

```text id="v4p9m1"
3 > 2
```

The machine would need more time than the target allows.

Therefore:

```text id="f7q3m8"
T = 2 → impossible
```

---

# ✅ Try `T = 3`

Required reduction:

```text id="m2q8v5"
35 - 3 = 32
```

Machine minutes:

```text id="c7p3m9"
ceil(32 / 16)
= 2
```

Now:

```text id="x8m4q2"
2 <= 3
```

So the target is feasible.

Therefore:

```text id="r5v9m3"
Answer = 3
```

---

# 📊 Dry Run

For:

```text id="8m3q7p"
X = [35]
K = 17
```

| Target `T` | Required Machine Time | Feasible? |
| ---------: | --------------------: | :-------: |
|        `0` |                     3 |     ❌     |
|        `1` |                     3 |     ❌     |
|        `2` |                     3 |     ❌     |
|        `3` |                     2 |     ✅     |
|        `4` |                     2 |     ✅     |
|        `5` |                     2 |     ✅     |

The first feasible value is:

```text id="m7q2v8"
3
```

Therefore:

```text id="p4c9m1"
Answer = 3
```

---

# 🧠 Why Binary Search Works

The feasibility function is monotonic.

For example:

```text id="5q8m2v"
T = 0 → ❌
T = 1 → ❌
T = 2 → ❌
T = 3 → ✅
T = 4 → ✅
T = 5 → ✅
...
```

Once a target time becomes feasible, every larger target is also feasible.

So the answer has the form:

```text id="c3m7q9"
❌ ❌ ❌ ❌ ✅ ✅ ✅ ✅
                  ↑
              minimum
```

Binary search finds this first `✅`.

---

# ⚠️ Common Mistakes

## 1. Using `K` Instead of `K - 1`

A common mistake is:

```text id="m8q2v5"
need = ceil((X - T) / K)
```

This ignores the fact that machine operation itself consumes one minute.

The correct net improvement is:

```text id="p7m3q9"
K - 1
```

Therefore:

```text id="c4v8m2"
need = ceil((X - T) / (K - 1))
```

---

## 2. Forgetting the Single Machine

You cannot independently allocate machine time to every wall.

The total machine usage must satisfy:

```text id="q5m8v3"
sum(required machine minutes) <= T
```

because there is only one machine.

---

## 3. Forgetting `K = 1`

When:

```text id="n2m7q8"
K = 1
```

we get:

```text id="c5v9m1"
K - 1 = 0
```

which would cause division by zero.

More importantly, the machine provides no net benefit.

So handle it separately.

---

## 4. Using `sum(X)` as the Upper Bound

The machine can work while natural drying progresses, so using:

```text id="j8q3m5"
sum(X)
```

as the binary-search upper bound is unnecessarily large.

A safe upper bound is:

```text id="v7m2p9"
max(X)
```

because all walls can naturally finish by that time.

---

## 5. Forgetting Ceiling Division

Suppose:

```text id="x4m8q2"
X - T = 33
K - 1 = 16
```

Then:

```text id="r3p7m9"
33 / 16 = 2.0625
```

We need **3** machine minutes, not 2.

Therefore we need ceiling division:

```python id="c8q2m5"
(a + b - 1) // b
```

---

# 🧩 Pattern Recognition

This problem is a strong example of:

## Binary Search on Answer

Use this pattern when:

1. You are asked to **minimize or maximize a value**.
2. You can write a function:

   ```text
   possible(T)
   ```
3. The function is **monotonic**.

Here:

```text id="p3m8q5"
T = total time
```

and:

```text id="k7q2v9"
possible(T)
```

checks whether all walls can finish within `T`.

---

# 🔑 Key Formula

For every wall:

```text id="f5m8q2"
if X <= T:
    machine_needed = 0
```

Otherwise:

```text id="q3v7m9"
machine_needed
=
ceil((X - T) / (K - 1))
```

Total machine requirement:

```text id="m8p2q5"
required
=
Σ machine_needed
```

Feasibility:

```text id="c4v9m7"
required <= T
```

---

# 🎯 Final Mental Model

Think of the solution as:

```text id="q8m3v5"
             Guess T
                ↓
       Can all walls finish
           within T?
                ↓
        ┌───────┴───────┐
        ↓               ↓
       YES              NO
        ↓               ↓
   Try smaller       Try larger
        ↓               ↓
        └───────┬───────┘
                ↓
        Binary Search
                ↓
       Minimum feasible T
```

For each wall:

```text id="m5q8v2"
Natural time = X
Target time  = T
      ↓
If X > T
      ↓
Excess = X - T
      ↓
Net machine improvement = K - 1
      ↓
Machine minutes =
ceil(excess / (K - 1))
```

---

# 🚀 One-Line Exam Recall

> **Binary-search the total time `T`; for every wall requiring extra reduction, calculate `ceil((X-T)/(K-1))` machine minutes and check whether their total fits within `T`.**

### Pattern

```text id="7m2q8v5"
Binary Search on Answer
```

### Key Observation

```text id="c5p9m3"
Machine's net improvement = K - 1
```

### Feasibility Condition

```text id="x8q2m7"
Σ ceil((X - T)/(K - 1)) <= T
```

for walls where `X > T`.

### Complexity

```text id="r4m8q2"
Time  → O(N log(max(X)))
Space → O(N)
```
