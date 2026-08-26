N = int(input())
M = int(input())
H = int(input())

villains = []

for _ in range(N):
    villains.append(int(input()))

# We want the longest feasible suffix,
# so process villains from right to left.

heroes_used = 1
current_health_used = 0

for i in range(N - 1, -1, -1):

    villain = villains[i]

    # A villain with health greater than H
    # can never be defeated by any hero.
    if villain > H:
        print(i + 1)
        break

    # Try to assign this villain to the current hero.
    if current_health_used + villain <= H:
        current_health_used += villain

    else:
        # Need another hero.
        heroes_used += 1
        current_health_used = villain

        # We have run out of heroes.
        if heroes_used > M:
            print(i + 1)
            break

else:
    # Every villain can be defeated.
    print(0)