nums = list(map(int, input().split(",")))
fib_set = set()
a, b = 1, 1
fib_set.add(1)
while b <= 10**9:
    fib_set.add(b)
    a, b = b, a + b
count = sum(1 for num in nums if num in fib_set)
print(count if count > 2 else -1)
