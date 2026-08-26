E = int(input())
N = int(input())

A = []

for _ in range(N):
    A.append(int(input()))

# Sort exercises by energy drain in descending order
A.sort(reverse=True)

count = 0
energy = E

# Each exercise can be performed at most 2 times
for x in A:

    # First time
    energy -= x
    count += 1

    if energy <= 0:
        print(count)
        break

    # Second time
    energy -= x
    count += 1

    if energy <= 0:
        print(count)
        break

else:
    # All exercises have been performed twice,
    # but energy is still positive.
    print(-1)