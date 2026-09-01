def solve():
    s = input().strip()

    balance = 0
    minimum = 0
    maximum = 0

    for ch in s:
        if ch == '1':
            balance += 1
        else:
            balance -= 1

        minimum = min(minimum, balance)
        maximum = max(maximum, balance)

    print(max(maximum, -minimum))


solve()