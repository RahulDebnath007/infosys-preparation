def longest_valid_subsequence(n, arr):
    # dp[i] = Length of the longest valid subsequence ending at index i
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            # Check both conditions:
            # 1. Increasing sequence
            # 2. Bitwise condition
            if arr[j] < arr[i] and ((arr[j] & arr[i]) * 2 < (arr[j] | arr[i])):
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# Input
n = int(input())
arr = [int(input()) for _ in range(n)]

# Output
print(longest_valid_subsequence(n, arr))