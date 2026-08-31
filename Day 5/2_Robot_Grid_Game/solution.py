from math import comb

def robot_grid(n, m, x, y):
    total = comb(n + m - 2, n - 1)
    to_block = comb(x + y - 2, x - 1) * comb((n - x) + (m - y), n - x)
    return total - to_block

n = int(input().strip())
m = int(input().strip())
x = int(input().strip())
y = int(input().strip())

print(robot_grid(n, m, x, y))
