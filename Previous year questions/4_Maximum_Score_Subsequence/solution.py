from math import isqrt


def divisor_count(x):
    count = 0

    for d in range(1, isqrt(x) + 1):
        if x % d == 0:
            count += 1

            if d * d != x:
                count += 1

    return count


def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    best = {}
    answer = 0

    for x in arr:
        candidates = [
            x - 1,
            x + 1,
            2 * x,
            3 * x
        ]

        if x % 2 == 0:
            candidates.append(x // 2)

        if x % 3 == 0:
            candidates.append(x // 3)

        previous = 0

        for y in candidates:
            previous = max(previous, best.get(y, 0))

        current = previous + divisor_count(x)

        best[x] = max(best.get(x, 0), current)
        answer = max(answer, current)

    print(answer)


solve()