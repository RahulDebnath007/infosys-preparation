import math

nums = list(map(int, input().split(",")))
num_set = set(nums)

def divisor_sum(n):
    if n == 0 or n == 1:
        return 0
    s = 1
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
    return s

res = [num for num in nums if divisor_sum(num) in num_set]
print(" ".join(map(str, res)) if res else -1)
