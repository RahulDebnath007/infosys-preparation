N = int(input())
M = int(input())
K = int(input())

# obligations[day] = number of obligations on that day
obligations = [0] * (N + 1)

for _ in range(M):
    day = int(input())
    obligations[day] += 1

left = 1
current_obligations = 0
max_vacation = 0

for right in range(1, N + 1):

    # Add obligations on the current day
    current_obligations += obligations[right]

    # Too many obligations -> shrink window
    while current_obligations > K:
        current_obligations -= obligations[left]
        left += 1

    # Current window [left, right] is valid
    vacation_length = right - left + 1

    if vacation_length > max_vacation:
        max_vacation = vacation_length

print(max_vacation)