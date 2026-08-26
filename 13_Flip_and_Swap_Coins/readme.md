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
