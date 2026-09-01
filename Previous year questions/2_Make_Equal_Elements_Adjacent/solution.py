class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, value):
        i += 1

        while i <= self.n:
            self.bit[i] += value
            i += i & -i

    def sum(self, i):
        result = 0
        i += 1

        while i > 0:
            result += self.bit[i]
            i -= i & -i

        return result


def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    positions = {}

    for i, x in enumerate(arr):
        positions.setdefault(x, []).append(i)

    fenwick = Fenwick(n)

    # 1 = element is still present
    for i in range(n):
        fenwick.add(i, 1)

    answer = 0

    used = set()

    for i in range(n):
        x = arr[i]

        if x in used:
            continue

        j = positions[x][1]

        # Number of alive elements between i and j
        cost = fenwick.sum(j - 1) - fenwick.sum(i)

        answer += cost

        # Remove both elements
        fenwick.add(i, -1)
        fenwick.add(j, -1)

        used.add(x)

    print(answer)


solve()