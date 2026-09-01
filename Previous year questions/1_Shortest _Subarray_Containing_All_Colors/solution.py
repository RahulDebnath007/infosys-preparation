def solve():
    n = int(input())
    c = int(input())
    arr = list(map(int, input().split()))

    freq = [0] * (c + 1)

    left = 0
    distinct = 0
    ans = float('inf')

    for right in range(n):
        x = arr[right]

        if freq[x] == 0:
            distinct += 1

        freq[x] += 1

        while distinct == c:
            ans = min(ans, right - left + 1)

            freq[arr[left]] -= 1

            if freq[arr[left]] == 0:
                distinct -= 1

            left += 1

    print(-1 if ans == float('inf') else ans)


solve()