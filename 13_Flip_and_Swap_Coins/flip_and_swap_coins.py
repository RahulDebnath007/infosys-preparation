def minimize_string_ugliness(n, s, cash, a, b):
    MOD = 10**9 + 7
    s_list = list(s)
    
    # Store indices of '1's and '0's
    ones = [i for i, char in enumerate(s_list) if char == '1']
    zeros = [i for i, char in enumerate(s_list) if char == '0']
    
    # Case 1: Flipping is cheaper or equal to swapping
    if b <= a:
        # Greedily flip leftmost '1's into '0's
        max_flips = min(len(ones), cash // b)
        for i in range(max_flips):
            s_list[ones[i]] = '0'
            
    # Case 2: Swapping is cheaper than flipping
    else:
        def can_clear(k, current_cash):
            if k == 0: 
                return True, 0, []
            
            swaps = 0
            p1 = k - 1
            p2 = len(zeros) - 1
            limit_p2 = max(0, len(zeros) - k)
            used_zeros = []
            
            while p1 >= 0 and p2 >= limit_p2:
                # Pair leftmost '1's with rightmost '0's for valid swaps
                if ones[p1] < zeros[p2]:
                    swaps += 1
                    used_zeros.append(zeros[p2])
                    p1 -= 1
                    p2 -= 1
                else:
                    p1 -= 1
                    
            flips = k - swaps
            cost = (swaps * a) + (flips * b)
            return cost <= current_cash, swaps, used_zeros

        # Binary search for the maximum leftmost '1's (best_k) we can clear
        low, high = 0, len(ones)
        best_k = 0
        
        while low <= high:
            mid = (low + high) // 2
            possible, _, _ = can_clear(mid, cash)
            if possible:
                best_k = mid
                low = mid + 1
            else:
                high = mid - 1
                
        # Get swap and flip distribution for best_k
        _, max_possible_swaps, used_zeros = can_clear(best_k, cash)
        
        # Upgrade extra cash to Flips to eliminate '1's permanently
        min_flips_required = best_k - max_possible_swaps
        min_cost = (max_possible_swaps * a) + (min_flips_required * b)
        leftover_cash = cash - min_cost
        
        extra_flips = leftover_cash // (b - a)
        actual_flips = min(best_k, min_flips_required + extra_flips)
        actual_swaps = best_k - actual_flips
        
        # Update binary string
        for i in range(best_k):
            s_list[ones[i]] = '0'
            
        for i in range(actual_swaps):
            s_list[used_zeros[i]] = '1'

    # Calculate decimal value modulo 10^9 + 7
    ans = 0
    power = 1
    for i in range(n - 1, -1, -1):
        if s_list[i] == '1':
            ans = (ans + power) % MOD
        power = (power * 2) % MOD
        
    return ans


# Input
n = int(input().strip())
s = input().strip()
cash = int(input().strip())
a = int(input().strip())
b = int(input().strip())

# Output
print(minimize_string_ugliness(n, s, cash, a, b))