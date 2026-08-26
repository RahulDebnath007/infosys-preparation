import sys

input = sys.stdin.readline


def solve(N: int, M: int, P: list) -> int:
    if N == 0:
        return 0

    if N == 1:
        return 1

    up0, down0 = 1, 1
    up1, down1 = 1, 1

    last_up0, last_down0 = P[0], P[0]
    last_up1, last_down1 = P[0], P[0]

    for i in range(1, N):
        x = P[i]

        new_up0, new_down0 = up0, down0
        new_up1, new_down1 = up1, down1

        new_last_up0, new_last_down0 = last_up0, last_down0
        new_last_up1, new_last_down1 = last_up1, last_down1

        # 1. Standard UP step
        if x - last_down0 >= M:
            if down0 + 1 > new_up0:
                new_up0 = down0 + 1
                new_last_up0 = x
            elif down0 + 1 == new_up0:
                new_last_up0 = min(new_last_up0, x)

        if x - last_down1 >= M:
            if down1 + 1 > new_up1:
                new_up1 = down1 + 1
                new_last_up1 = x
            elif down1 + 1 == new_up1:
                new_last_up1 = min(new_last_up1, x)

        # 2. Standard DOWN step
        if last_up0 - x >= M:
            if up0 + 1 > new_down0:
                new_down0 = up0 + 1
                new_last_down0 = x
            elif up0 + 1 == new_down0:
                new_last_down0 = max(new_last_down0, x)

        if last_up1 - x >= M:
            if up1 + 1 > new_down1:
                new_down1 = up1 + 1
                new_last_down1 = x
            elif up1 + 1 == new_down1:
                new_last_down1 = max(new_last_down1, x)

        # 3. Mulligan UP step
        if x - last_up0 >= M:
            if up0 + 1 > new_up1:
                new_up1 = up0 + 1
                new_last_up1 = x
            elif up0 + 1 == new_up1:
                new_last_up1 = min(new_last_up1, x)

        # 4. Mulligan DOWN step
        if last_down0 - x >= M:
            if down0 + 1 > new_down1:
                new_down1 = down0 + 1
                new_last_down1 = x
            elif down0 + 1 == new_down1:
                new_last_down1 = max(new_last_down1, x)

        # Starting element
        if new_up0 == 1:
            new_last_up0 = min(new_last_up0, x)

        if new_down0 == 1:
            new_last_down0 = max(new_last_down0, x)

        if new_up1 == 1:
            new_last_up1 = min(new_last_up1, x)

        if new_down1 == 1:
            new_last_down1 = max(new_last_down1, x)

        up0, down0, up1, down1 = (
            new_up0,
            new_down0,
            new_up1,
            new_down1
        )

        last_up0, last_down0 = (
            new_last_up0,
            new_last_down0
        )

        last_up1, last_down1 = (
            new_last_up1,
            new_last_down1
        )

    return max(up0, down0, up1, down1)


# ============================================================
# DRIVER CODE
# ============================================================

if __name__ == "__main__":

    N = int(input())
    M = int(input())

    P = []

    for _ in range(N):
        P.append(int(input()))

    result = solve(N, M, P)

    print(result)