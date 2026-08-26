# 🍕 Pizza With 3N Slices (DP + State Compression + Circular Array)

## 📌 Problem Statement

You are given a **circular pizza** consisting of **3n slices**.

- `slices[i]` represents the size of the i-th slice.
- You must select **exactly n slices**.
- Normally, selecting adjacent slices is not allowed.
- However, you have **K Tolerance Tokens**.

### Token Rule

Whenever two selected slices are adjacent, you spend **1 token**.

Since the pizza is circular:

```text
First Slice <----> Last Slice
```

are also considered adjacent.

Your task is to find the **maximum total size** of exactly `n` selected slices while using **at most K tokens**.

---

## Example 1

### Input

```text
n = 1
K = 0

slices = [10, 20, 30]
```

### Output

```text
30
```

### Explanation

We must select exactly one slice.

Possible selections:

```text
10
20
30
```

Maximum:

```text
30
```

---

# 🔍 How to Recognize the Pattern?

Whenever a problem contains:

### 1. Select Exactly X Elements

```text
Select exactly n slices
```

This usually creates a DP dimension:

```text
count
```

---

### 2. Maximize Something

```text
Maximum total slice size
```

DP stores:

```text
Maximum sum
```

---

### 3. Limited Resource

```text
At most K tokens
```

This creates another DP dimension:

```text
tokens used
```

---

### 4. Current Decision Depends on Previous Decision

Selecting current slice depends on whether previous slice was selected.

This creates:

```text
last
```

state.

---

## Therefore DP State Becomes

```text
DP[i][count][tokens][last]
```

---

# 🎯 DP State Meaning

```python
DP[i][count][tokens][last]
```

means:

After processing slices from:

```text
0 → i
```

- Selected exactly `count` slices
- Used exactly `tokens` adjacency tokens
- `last = 1` means current slice is selected
- `last = 0` means current slice is not selected

Store:

```text
Maximum total size achievable
```

---

# Why Do We Need "last"?

Suppose:

```text
20 30
```

If both are selected:

```text
1 1
```

they are adjacent.

So:

```text
Token Cost = 1
```

When processing current slice we need to know:

```text
Was previous slice selected?
```

Therefore:

```text
last = 0 or 1
```

---

# Why Two DP Runs?

The pizza is circular.

```text
10 20 30 40 50 60
↑              ↑
└──────────────┘
```

First and last slices are adjacent.

Normal left-to-right DP cannot automatically handle this.

Therefore we split into two cases.

---

## Case 1

### First Slice Selected

```python
run_dp(True)
```

---

## Case 2

### First Slice Not Selected

```python
run_dp(False)
```

Final Answer:

```python
max(case1, case2)
```

This is a very common technique for circular DP problems.

---

# DP Transitions

For every slice:

```text
Take
or
Don't Take
```

---

## Option 1: Don't Take Current Slice

```python
DP[i][c][k][0]
```

Nothing changes:

```text
count remains same
tokens remain same
```

Only:

```text
last = 0
```

---

## Option 2: Take Current Slice

If current slice is selected:

```text
count += 1
```

and:

```text
sum += slices[i]
```

---

### Adjacency Cost

If previous slice was selected:

```python
last == 1
```

Then:

```python
cost = 1
```

Else:

```python
cost = 0
```

---

### New State

```python
DP[i][c+1][k+cost][1]
```

---

# Visualization

Current State

```text
DP[i-1][c][k][last]
```

Two Choices:

```text
                 Current Slice
                       |
           ┌───────────┴───────────┐
           │                       │
       DON'T TAKE              TAKE
           │                       │
           ▼                       ▼

DP[i][c][k][0]       DP[i][c+1][k+last][1]

                          +
                     slices[i]
```

---

# Complete Python Code

```python
import sys
input = sys.stdin.readline

def solve(n: int, K: int, slices: list) -> int:
    L = 3 * n
    INF = float('-inf')

    def run_dp(take_first):

        DP = [[[[INF] * 2
                for _ in range(K + 1)]
                for _ in range(n + 1)]
                for _ in range(L)]

        if take_first:
            DP[0][1][0][1] = slices[0]
        else:
            DP[0][0][0][0] = 0

        for i in range(1, L):

            for c in range(n + 1):

                for k in range(K + 1):

                    for last in (0, 1):

                        val = DP[i - 1][c][k][last]

                        if val == INF:
                            continue

                        # Don't Take

                        if val > DP[i][c][k][0]:
                            DP[i][c][k][0] = val

                        # Take

                        if c + 1 <= n:

                            cost = 1 if last == 1 else 0

                            if k + cost <= K:

                                new_val = val + slices[i]

                                if new_val > DP[i][c + 1][k + cost][1]:

                                    DP[i][c + 1][k + cost][1] = new_val

        real_ans = INF

        for k in range(K + 1):

            for last in (0, 1):

                res = DP[L - 1][n][k][last]

                if res != INF:

                    extra_cost = 1 if (
                        take_first and last == 1
                    ) else 0

                    if k + extra_cost <= K:

                        real_ans = max(real_ans, res)

        return real_ans

    return max(
        run_dp(True),
        run_dp(False)
    )


if __name__ == "__main__":

    try:

        n = int(input())
        K = int(input())

        slices = list(
            map(int, input().split())
        )

        result = solve(
            n,
            K,
            slices
        )

        print(result)

    except (EOFError, ValueError):
        pass
```

---

# Dry Run

## Input

```text
n = 1
K = 0

slices = [10,20,30]
```

Length:

```text
L = 3
```

---

# Case 1

First Slice Selected

```python
DP[0][1][0][1] = 10
```

Meaning:

```text
Selected = 1 slice
Tokens = 0
Sum = 10
```

Since we already selected required:

```text
n = 1
```

we cannot select any more slices.

Final Result:

```text
10
```

---

# Case 2

First Slice Not Selected

Initialize:

```python
DP[0][0][0][0] = 0
```

---

Process Slice 20

Take:

```text
Count = 1
Tokens = 0
Sum = 20
```

State:

```python
DP[1][1][0][1] = 20
```

---

Process Slice 30

Take:

```text
Count = 1
Tokens = 0
Sum = 30
```

State:

```python
DP[2][1][0][1] = 30
```

---

Final Result

```text
Case 1 = 10

Case 2 = 30
```

Answer:

```text
max(10,30)
=
30
```

---

# Complexity Analysis

### DP Dimensions

```text
Position = 3n

Selected Count = n

Tokens = K

Last State = 2
```

---

### Time Complexity

```text
O(3n × n × K × 2)

≈ O(n²K)
```

Worst Case:

```text
n = 100
K = 100
```

Around:

```text
6 million states
```

which is acceptable.

---

### Space Complexity

```text
O(3n × n × K × 2)
```

Approximately:

```text
O(n²K)
```

---

# Key Takeaways

Whenever you see:

```text
Process elements one-by-one
```

→ Position State (`i`)

---

```text
Select exactly X items
```

→ Count State (`count`)

---

```text
Limited budget/resource
```

→ Resource State (`tokens`)

---

```text
Current choice depends on previous choice
```

→ Previous State (`last`)

---

```text
Circular Array
```

→ Run DP twice

```text
Case 1 → First Selected
Case 2 → First Not Selected
```

---

## Final DP State

```text
DP[i][count][tokens][last]
```

Meaning:

Among first `i+1` slices,

- selected `count` slices,
- used `tokens` tokens,
- current slice selected status = `last`,

and store:

```text
Maximum possible total size.
```

This is the core pattern used in this solution.