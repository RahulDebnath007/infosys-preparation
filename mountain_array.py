N = int(input())

arr = []

for _ in range(N):
    arr.append(int(input()))

frequency = {}

for i in range(N):

    # Distance from the nearest end
    level = min(i, N - 1 - i)

    # Base value required for arr[i]
    base = arr[i] - level

    frequency[base] = frequency.get(base, 0) + 1

# Maximum number of elements that can remain unchanged
max_kept = max(frequency.values())

# Remaining elements need to be changed
answer = N - max_kept

print(answer)