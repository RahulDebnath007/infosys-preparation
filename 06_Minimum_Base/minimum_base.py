def check_all_digits_same(M: int, B: int) -> bool:
    first_digit = M % B
    M //= B
    while M > 0:
        if M % B != first_digit:
            return False
        M //= B
    return True


def min_base_identical_digits(M: int) -> int:
    if M <= 2:
        return M + 1

    limit = int(M**0.5)

    for B in range(2, limit + 1):
        if check_all_digits_same(M, B):
            return B

    best_B = M - 1

    for d0 in range(1, limit + 1):
        if M % d0 == 0:
            B1 = (M // d0) - 1
            if d0 < B1:
                best_B = min(best_B, B1)

            k = M // d0
            if k <= limit:
                B2 = (M // k) - 1
                if k < B2:
                    best_B = min(best_B, B2)

    return best_B


# --- TAKING INPUT HERE ---
if __name__ == "__main__":
    # Convert string input to integer
    M = int(input("Enter a number M: "))

    # Calculate result
    ans = min_base_identical_digits(M)

    # Print result
    print(f"Minimum Base: {ans}")