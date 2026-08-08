def max_xor_sum(n, k, arr):
    BITS = 30  # Since A[i], K <= 10^9 < 2^30
    
    # Count how many elements in A have the b-th bit set to 1
    count1 = [0] * BITS
    for x in arr:
        for b in range(BITS):
            if (x >> b) & 1:
                count1[b] += 1
                
    # Calculate contribution for choosing 0 or 1 at bit b
    cost0 = [0] * BITS
    cost1 = [0] * BITS
    for b in range(BITS):
        cost0[b] = count1[b] * (1 << b)          # x_b = 0
        cost1[b] = (n - count1[b]) * (1 << b)    # x_b = 1
        
    # suffix_max[b] stores max possible sum for bits 0 to b-1 with full freedom
    suffix_max = [0] * (BITS + 1)
    for b in range(BITS):
        suffix_max[b + 1] = suffix_max[b] + max(cost0[b], cost1[b])
        
    max_ans = 0
    tight_sum = 0
    
    # Process bits from MSB (bit 29) to LSB (bit 0)
    for b in range(BITS - 1, -1, -1):
        k_bit = (k >> b) & 1
        
        if k_bit == 1:
            # Option 1: Set x_b = 0 -> x becomes strictly less than K
            # Lower bits can take maximum possible contributions freely
            candidate = tight_sum + cost0[b] + suffix_max[b]
            max_ans = max(max_ans, candidate)
            
            # Option 2: Set x_b = 1 -> x remains tight with K
            tight_sum += cost1[b]
        else:
            # Must set x_b = 0 to remain <= K
            tight_sum += cost0[b]
            
    # Consider x = K (matching K entirely)
    max_ans = max(max_ans, tight_sum)
    
    return max_ans


# Input Handling without 'import sys'
def main():
    try:
        n = int(input().strip())
        k = int(input().strip())
        arr = [int(input().strip()) for _ in range(n)]
        print(max_xor_sum(n, k, arr))
    except (EOFError, ValueError):
        return

if __name__ == '__main__':
    main()