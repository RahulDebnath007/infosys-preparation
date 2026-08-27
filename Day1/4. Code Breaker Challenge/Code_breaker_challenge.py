def code_breaker(s):
    pairs = s.strip().split(",")
    result = []

    for pair in pairs:
        name, code = pair.split(":")
        max_digit = -1

        for ch in code:
            digit = int(ch)
            if 1 <= digit <= len(name):
                max_digit = max(max_digit, digit)

        if max_digit == -1:
            result.append("X")
        else:
            result.append(name[max_digit - 1])

    return "".join(result)


if __name__ == "__main__":
    s = input().strip()
    print(code_breaker(s))