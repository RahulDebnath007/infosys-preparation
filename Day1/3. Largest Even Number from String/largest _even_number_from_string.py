import sys

S = sys.stdin.readline().strip()

digits = sorted([ch for ch in S if ch.isdigit()], reverse=True)

even_digits = [d for d in digits if int(d) % 2 == 0]

if not even_digits:
    print(-1)
else:
    last_digit = even_digits[-1]

    digits.remove(last_digit)
    digits.append(last_digit)

    print("".join(digits))