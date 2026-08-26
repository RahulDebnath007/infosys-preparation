import sys
input = sys.stdin.readline

def solve(N: int, B: int, s: str) -> int:
    ends_at = [[] for _ in range(N)]
    
    # 1. Precompute Odd Beacons
    for i in range(N):
        max_reach = 0
        while i - max_reach >= 0 and i + max_reach < N and s[i - max_reach] == s[i + max_reach]:
            max_reach += 1
        
        for rad in range(1, max_reach + 1):
            L = 2 * rad - 1
            r = i + rad - 1
            ends_at[r].append(L)

    # 2. Precompute Even Beacons
    for i in range(N - 1):
        max_reach = 0
        while i - max_reach >= 0 and i + 1 + max_reach < N and s[i - max_reach] == s[i + 1 + max_reach]:
            max_reach += 1
            
        for rad in range(1, max_reach + 1):
            L = 2 * rad
            r = i + rad
            ends_at[r].append(L)

    # 3. Dynamic Programming Table
    dp = [[-1] * (B + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(1, N + 1):
        r = i - 1
        for k in range(B + 1):
            # Option 1: Skip placing a beacon at index r
            if dp[i - 1][k] != -1:
                dp[i][k] = max(dp[i][k], dp[i - 1][k])
            
            # Option 2: Place a beacon of length L ending at index r
            if k > 0:
                for L in ends_at[r]:
                    if i - L >= 0 and dp[i - L][k - 1] != -1:
                        dp[i][k] = max(dp[i][k], dp[i - L][k - 1] + L)

    return max(0, dp[N][B])

if __name__ == "__main__":
    try:
        N = int(input())
        B = int(input())
        s = input().strip()
        result = solve(N, B, s)
        print(result)
    except (EOFError, ValueError):
        pass