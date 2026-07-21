MOD=10000
def countArrays(n,k):
    dp = [[0]*(n+1) for _ in range(k+1)]
    for num in range(1,n+1):
        dp[1][num] = 1
    for length in range(1,k):
        for num in range(1,n+1):
           for nultiple in range(num,n+1,num):
                dp[length+1][multiple]= (dp[length+1][multiple]+ dp[length][num]) % MOD

    return sum(dp[k]) % MOD


# Driver Code
n = int(input())
k = int(input())

print(countArrays(n, k))            