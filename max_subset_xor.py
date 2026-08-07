def max_subset_xor(n, arr):
    max_limit = n // 2
    max_a = max(arr)
    
    # Upper bound power of 2 for XOR values
    max_val = 1 << max_a.bit_length()
    
    # dp[v] stores the minimum number of elements needed to reach XOR sum v
    # 121 acts as infinity since N <= 120
    dp = [121] * max_val
    dp[0] = 0
    reachable = [0]
    
    for x in arr:
        updates = []
        for v in reachable:
            nxt_cnt = dp[v] + 1
            if nxt_cnt <= max_limit:
                updates.append((v ^ x, nxt_cnt))
        
        # Apply updates to avoid using the same element x multiple times
        for nxt_v, nxt_cnt in updates:
            if dp[nxt_v] == 121:
                dp[nxt_v] = nxt_cnt
                reachable.append(nxt_v)
            elif nxt_cnt < dp[nxt_v]:
                dp[nxt_v] = nxt_cnt
                
    # Find the maximum XOR value achievable with at most N // 2 elements
    max_xor = 0
    for v in reachable:
        if dp[v] <= max_limit:
            if v > max_xor:
                max_xor = v
                
    return max_xor


# Input Handling without 'import sys'
def main():
    try:
        n = int(input().strip())
        arr = [int(input().strip()) for _ in range(n)]
        print(max_subset_xor(n, arr))
    except (EOFError, ValueError):
        return

if __name__ == '__main__':
    main()