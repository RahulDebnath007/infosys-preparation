import sys
input = sys.stdin.readline

def solve(n: int, K: int, slices: list) -> int:
    L = 3 * n
    INF = float('-inf')

    def run_dp(take_first):
        DP = [[[[INF] * 2 for _ in range(K + 1)] for _ in range(n + 1)] for _ in range(L)]

        if take_first:
            DP[0][1][0][1] = slices[0]
        else:
            DP[0][0][0][0] = 0

        for i in range(1, L):
            for c in range(n + 1):
                for k in range(K + 1):
                    for last in (0, 1):
                        val = DP[i - 1][c][k][last]
                        if val == INF:
                            continue

                        if val > DP[i][c][k][0]:
                            DP[i][c][k][0] = val

                        if c + 1 <= n:
                            cost = 1 if last == 1 else 0
                            if k + cost <= K:
                                new_val = val + slices[i]
                                if new_val > DP[i][c + 1][k + cost][1]:
                                    DP[i][c + 1][k + cost][1] = new_val

        real_ans = INF
        for k in range(K + 1):
            for last in (0, 1):
                res = DP[L - 1][n][k][last]
                if res != INF:
                    extra_cost = 1 if (take_first and last == 1) else 0
                    if k + extra_cost <= K:
                        if res > real_ans:
                            real_ans = res

        return real_ans

    return max(run_dp(True), run_dp(False))


if __name__ == "__main__":
    try:
        n = int(input())
        K = int(input())
        slices = list(map(int, input().split()))
        result = solve(n, K, slices)
        print(result)
    except (EOFError, ValueError):
        pass