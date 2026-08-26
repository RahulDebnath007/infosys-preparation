# 9 🏔️ Rugged Terrain – Minimum Days to Create a Strictly Descending Slope

[![Repository](https://img.shields.io/badge/Repository-infosys--preparation-blue?logo=github)](https://github.com/RahulDebnath007/infosys-preparation)

## 📌 Problem Statement

You need to build a road across a rugged terrain.

There are `N` terrain segments, and the sea level of the `i-th` segment is:

```text
L[i]
```

The final terrain must be **strictly downward sloping**.

Therefore, for every:

```text
2 <= i <= N
```

we must have:

```text
L[i - 1] > L[i]
```

To achieve this, a digging team can reduce the sea level of selected segments.

On day `D`, if a segment is scheduled for digging, its sea level is reduced by:

```text
2D - 1
```

meters.

A segment can be scheduled:

* On multiple days
* Along with other segments
* On different combinations of days

The task is to find the **minimum number of days** required to transform the terrain into a strictly decreasing sequence.

---

# 💡 Approach

The problem asks for the **minimum number of days**.

Trying every possible number of days directly would be inefficient.

Instead, we use:

```text
Binary Search on Answer
+
Greedy Feasibility Check
```

The binary search asks:

> **"Can the terrain be made strictly decreasing using at most `D` days?"**

If the answer is:

```text
YES
```

then `D` days are sufficient, and we try a smaller number.

If the answer is:

```text
NO
```

then we need more days.

This works because if `D` days are sufficient, then any larger number of days will also be sufficient.

Therefore, feasibility is **monotonic**:

```text
Days:       0  1  2  3  4  5  6 ...
Possible:   N  N  N  Y  Y  Y  Y ...
                         ↑
                    Minimum Answer
```

The first `Y` is the answer.

---

# 🔑 Key Observation

On day `D`, the reduction is:

```text
2D - 1
```

The first few days give:

```text
Day 1 → 1
Day 2 → 3
Day 3 → 5
Day 4 → 7
...
```

These are consecutive odd numbers.

The sum of the first `D` odd numbers is:

```text
1 + 3 + 5 + ... + (2D - 1) = D²
```

Therefore, if we use all `D` available days on a segment, the maximum possible reduction is:

```text
D²
```

For example, with `D = 3`:

```text
1 + 3 + 5 = 9
```

So the maximum reduction is:

```text
3² = 9
```

---

# 🧠 Important Detail: Possible Reductions

A segment does not have to be scheduled on every available day.

It can be scheduled on any subset of the days.

For `D = 3`, the available reductions are:

```text
1, 3, 5
```

Possible totals are:

```text
0
1
3
4
5
6
8
9
```

Therefore, with `D` days, the achievable reductions are almost all values from:

```text
0 to D²
```

with two exceptions for `D >= 2`:

```text
2
D² - 2
```

So the achievable reductions are:

```text
0 ... D²
```

except:

```text
2
D² - 2
```

For example, when:

```text
D = 4
```

the maximum reduction is:

```text
16
```

and the only unavailable values are:

```text
2
14
```

This observation allows us to find the smallest valid reduction for each segment efficiently.

---

# 🎯 Feasibility Check

Suppose we want to check whether `D` days are sufficient.

For each terrain segment, we choose a reduction so that the resulting terrain remains strictly decreasing.

Suppose the previous final height is:

```text
previous
```

and the current original height is:

```text
L[i]
```

We need:

```text
previous > L[i] - reduction
```

Rearranging:

```text
reduction > L[i] - previous
```

Therefore, the minimum required reduction is:

```text
L[i] - previous + 1
```

If this value is negative, no reduction is needed:

```python
required = max(0, L[i] - previous + 1)
```

Then we choose the smallest achievable reduction greater than or equal to `required`.

Choosing the smallest possible reduction is a **greedy strategy** because it keeps the current segment as high as possible while still satisfying the condition.

---

# 🧠 Why Greedy Works

Suppose the previous final height is:

```text
10
```

and the current terrain height is:

```text
12
```

We need:

```text
10 > 12 - reduction
```

Therefore:

```text
reduction >= 3
```

If reduction `3` is achievable, use `3`.

The new height becomes:

```text
12 - 3 = 9
```

There is no reason to use a larger reduction such as `5` because:

```text
9
```

already satisfies:

```text
10 > 9
```

Using the smallest valid reduction keeps the current terrain as high as possible.

This greedy choice is repeated from left to right.

---

# 🔍 Handling Unavailable Reductions

Suppose:

```text
D = 3
```

Then:

```text
D² = 9
```

The unavailable reductions are:

```text
2
7
```

Suppose the required reduction is:

```text
2
```

We cannot use `2`.

The next achievable reduction is:

```text
3
```

So we use:

```text
3
```

Similarly, if:

```text
required = 7
```

we must use:

```text
8
```

because `7` cannot be achieved.

If the required reduction is greater than:

```text
D²
```

then `D` days are not sufficient.

---

# 📝 Algorithm

1. Check whether the terrain is already strictly decreasing.
2. If it is already decreasing, return `0`.
3. Binary search the minimum number of days.
4. For each candidate number of days `D`:

   * Calculate the maximum possible reduction:

     ```text
     D²
     ```
   * Start with the first terrain segment.
   * Process the remaining segments from left to right.
   * Calculate the minimum reduction required to make the current segment smaller than the previous final segment.
   * Adjust the required reduction if it is one of the unavailable values.
   * If the required reduction exceeds `D²`, return `False`.
   * Otherwise, calculate the current final height.
5. If the entire terrain can be made strictly decreasing, `D` is feasible.
6. Binary search for the smallest feasible `D`.

---

# 📝 Code Explanation

## Step 1 — Feasibility Function

```python
def can_make_decreasing(L, days):
```

This function checks whether the terrain can be transformed into a strictly decreasing sequence using at most `days` days.

It returns:

```text
True
```

if possible, otherwise:

```text
False
```

---

## Step 2 — Maximum Reduction

```python
max_reduction = days * days
```

The maximum reduction available to one segment is:

```text
1 + 3 + 5 + ... + (2D - 1)
```

which equals:

```text
D²
```

Therefore:

```python
max_reduction = days * days
```

---

## Step 3 — Initialize Previous Height

```python
previous = L[0]
```

The first segment does not have a segment before it.

Therefore, we can keep it unchanged.

Its final height becomes:

```text
L[0]
```

---

## Step 4 — Process the Remaining Segments

```python
for i in range(1, len(L)):
```

Process every segment from the second segment to the last.

For every segment, we need:

```text
final[i - 1] > final[i]
```

---

## Step 5 — Calculate Required Reduction

```python
required = L[i] - previous + 1
```

We calculate how much reduction is required.

We need:

```text
previous > L[i] - reduction
```

Therefore:

```text
reduction > L[i] - previous
```

Since the reduction is an integer:

```text
reduction >= L[i] - previous + 1
```

---

## Step 6 — Prevent Negative Reduction

```python
required = max(0, required)
```

If the current segment is already below the previous final height, no digging is necessary.

Example:

```text
previous = 10
L[i] = 7
```

Then:

```text
7 - 10 + 1 = -2
```

We cannot have a negative reduction.

Therefore:

```text
required = 0
```

---

## Step 7 — Handle Reduction `2`

```python
if required == 2:
    required = 3
```

For `days >= 2`, a reduction of exactly `2` cannot be produced from the available odd-day reductions.

Therefore, if we need at least `2`, the next possible reduction is `3`.

---

## Step 8 — Handle `D² - 2`

```python
if required == max_reduction - 2:
    required += 1
```

The value:

```text
D² - 2
```

is also unavailable.

For example:

```text
days = 4
max_reduction = 16
```

Then:

```text
max_reduction - 2 = 14
```

Reduction `14` cannot be achieved.

So we use:

```text
15
```

---

## Step 9 — Check Maximum Available Reduction

```python
if required > max_reduction:
    return False
```

If the required reduction is greater than the maximum available reduction, the current number of days is insufficient.

For example:

```text
days = 3
max_reduction = 9
```

If:

```text
required = 10
```

then:

```text
10 > 9
```

Therefore, three days are not enough.

---

## Step 10 — Apply the Reduction

```python
previous = L[i] - required
```

Apply the chosen reduction to the current segment.

The resulting height becomes:

```text
L[i] - required
```

This becomes the `previous` height for the next iteration.

---

## Step 11 — Successful Feasibility Check

```python
return True
```

If every segment was successfully processed, the terrain can be made strictly decreasing using the given number of days.

---

# 🔎 Binary Search

Now we need to find the minimum number of days.

We know:

```text
0 days
```

may be enough if the terrain is already strictly decreasing.

As the number of days increases, the maximum possible reduction also increases.

Therefore, feasibility is monotonic.

Example:

```text
0 → False
1 → False
2 → False
3 → True
4 → True
5 → True
...
```

We need to find the first `True`.

This is exactly what **Binary Search on Answer** is designed for.

---

## Binary Search Variables

```python
low = 0
high = some_upper_bound
```

We repeatedly calculate:

```python
mid = (low + high) // 2
```

Then check:

```python
can_make_decreasing(L, mid)
```

If it returns `True`:

```python
high = mid
```

because we want to try fewer days.

Otherwise:

```python
low = mid + 1
```

because more days are required.

---

# 🧪 Dry Run

## Sample Input 1

```text
2
3
3
```

So:

```text
L = [3, 3]
```

The terrain is:

```text
3 → 3
```

It is not strictly decreasing because:

```text
3 > 3
```

is false.

---

### Check 0 Days

No digging is possible:

```text
3 → 3
```

Not valid.

Therefore:

```text
0 days = False
```

---

### Check 1 Day

On day `1`, the reduction is:

```text
2(1) - 1 = 1
```

Reduce the second segment:

```text
3 - 1 = 2
```

Final terrain:

```text
3 → 2
```

Now:

```text
3 > 2
```

is true.

Therefore:

```text
1 day = True
```

The minimum answer is:

```text
1
```

---

# 🧪 Dry Run – Sample 2

Input:

```text
2
5
-3
```

Terrain:

```text
5 → -3
```

Check:

```text
5 > -3
```

This is already true.

Therefore no digging is required.

```text
Answer = 0
```

---

# 🔍 Example of the Greedy Process

Suppose:

```text
L = [5, 8, 4]
```

and we want to check:

```text
days = 2
```

Maximum reduction:

```text
2² = 4
```

Possible reductions are:

```text
0, 1, 3, 4
```

### First Segment

```text
previous = 5
```

### Second Segment

Current height:

```text
8
```

We need:

```text
5 > 8 - reduction
```

Therefore:

```text
reduction >= 4
```

Reduction `4` is achievable.

New height:

```text
8 - 4 = 4
```

So:

```text
previous = 4
```

### Third Segment

Current height:

```text
4
```

We need:

```text
4 > 4 - reduction
```

Therefore:

```text
reduction >= 1
```

Reduction `1` is achievable.

New height:

```text
4 - 1 = 3
```

Final terrain:

```text
5 → 4 → 3
```

Therefore, `2` days are sufficient.

---

# 💻 Complete Code

```python
def can_make_decreasing(L, days):
    if days == 0:
        for i in range(1, len(L)):
            if L[i - 1] <= L[i]:
                return False
        return True

    max_reduction = days * days

    previous = L[0]

    for i in range(1, len(L)):
        # Minimum reduction required to make:
        # previous > L[i] - reduction
        required = max(0, L[i] - previous + 1)

        # 2 cannot be represented as a sum of
        # distinct odd numbers.
        if required == 2:
            required = 3

        # days^2 - 2 is also not achievable.
        if required == max_reduction - 2 and max_reduction >= 4:
            required += 1

        # Required reduction is too large.
        if required > max_reduction:
            return False

        # Apply the minimum possible reduction.
        previous = L[i] - required

    return True


def minimum_days(L):
    # Already strictly decreasing
    if all(L[i - 1] > L[i] for i in range(1, len(L))):
        return 0

    low = 0
    high = 1

    # Find an upper bound that is definitely feasible.
    while not can_make_decreasing(L, high):
        high *= 2

    # Binary Search for the minimum feasible number of days.
    while low < high:
        mid = (low + high) // 2

        if can_make_decreasing(L, mid):
            high = mid
        else:
            low = mid + 1

    return low


# Driver Code
N = int(input())

L = []

for _ in range(N):
    L.append(int(input()))

print(minimum_days(L))
```

---

# 📊 Complexity Analysis

## Time Complexity

The feasibility check processes every terrain segment once:

```text
O(N)
```

Binary Search performs approximately:

```text
O(log Answer)
```

checks.

Therefore:

```text
O(N log Answer)
```

The upper bound is determined by the magnitude of the terrain values.

Since:

```text
|L[i]| <= 10⁹
```

the number of binary-search iterations is relatively small.

---

## Space Complexity

The algorithm stores the terrain array:

```text
O(N)
```

Additional working space is:

```text
O(1)
```

Therefore:

```text
Overall Space = O(N)
```

---

# 🧩 Pattern Used

* Binary Search on Answer
* Greedy Algorithm
* Feasibility Check
* Mathematical Observation
* Monotonic Predicate

---

# 🎯 Pattern Recognition

This problem has the following structure:

```text
Find the minimum X
such that a condition becomes possible.
```

Instead of directly calculating the answer, ask:

```text
Can I solve the problem using X days?
```

If:

```text
X days → possible
```

then:

```text
X + 1 days → also possible
```

This creates a monotonic condition:

```text
False False False False True True True True
                         ↑
                    Minimum Answer
```

Whenever you see:

* Minimum possible value
* Maximum possible value
* "Can it be done with X?"
* A monotonic yes/no condition
* Large search space

you should consider:

```text
Binary Search on Answer
```

---

# 🚀 Key Learning

> When a problem asks for the **minimum number of operations/days/resources** and you can efficiently check whether a particular value is sufficient, use **Binary Search on Answer**.

For this problem:

```text
Candidate Answer
       ↓
Number of Days
       ↓
Calculate Maximum Reduction
       ↓
Greedy Feasibility Check
       ↓
Can the terrain become strictly decreasing?
       ↓
YES → Search Left
NO  → Search Right
```

The core pattern is:

```text
Binary Search
+
Greedy Validation
```

---

# 📚 Suitable For

* Infosys Coding Assessment
* Binary Search Practice
* Binary Search on Answer
* Greedy Algorithm Practice
* Mathematical Observation Problems
* Array Problems
* Competitive Programming
* Coding Interviews
* Pattern Recognition Practice
