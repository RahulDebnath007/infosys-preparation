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
