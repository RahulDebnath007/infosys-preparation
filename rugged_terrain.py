def can_make_decreasing(L, days):
    # Maximum reduction possible for one segment
    max_reduction = days * days

    # First segment remains unchanged
    previous = L[0]

    # Process remaining segments
    for i in range(1, len(L)):

        # We need:
        # previous > L[i] - reduction
        #
        # Therefore:
        # reduction >= L[i] - previous + 1
        required = max(0, L[i] - previous + 1)

        # Reduction 2 cannot be formed
        # from the available odd numbers.
        if required == 2:
            required = 3

        # D^2 - 2 also cannot be formed.
        if max_reduction >= 4 and required == max_reduction - 2:
            required += 1

        # Not enough reduction available
        if required > max_reduction:
            return False

        # Apply the minimum required reduction
        previous = L[i] - required

    return True


def minimum_days(L):

    # Check if already strictly decreasing
    for i in range(1, len(L)):
        if L[i - 1] <= L[i]:
            break
    else:
        return 0

    # Find an upper bound
    low = 0
    high = 1

    while not can_make_decreasing(L, high):
        high *= 2

    # Binary Search
    while low < high:

        mid = (low + high) // 2

        if can_make_decreasing(L, mid):
            high = mid
        else:
            low = mid + 1

    return low


# -------------------------
# Driver Code
# -------------------------

N = int(input())

L = []

for _ in range(N):
    L.append(int(input()))

print(minimum_days(L))