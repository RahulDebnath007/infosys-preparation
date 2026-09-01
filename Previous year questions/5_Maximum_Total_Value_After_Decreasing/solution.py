def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    MOD = 10**9 + 7
    answer = 0

    for day, value in enumerate(arr):
        answer += max(0, value - day)

    print(answer % MOD)


solve()