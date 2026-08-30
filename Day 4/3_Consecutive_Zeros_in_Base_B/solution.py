def to_base(N, B):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while N > 0:
        res = digits[N % B] + res
        N //= B
    return res

def find_max_consecutive_zeros(s):
    count = max_zero = 0
    has_zero = False
    for c in s:
        if c == '0':
            count += 1
            has_zero = True
            max_zero = max(max_zero, count)
        else:
            count = 0
    return max_zero if has_zero else -1

N = int(input())
B = int(input())
print(find_max_consecutive_zeros(to_base(N, B)))
