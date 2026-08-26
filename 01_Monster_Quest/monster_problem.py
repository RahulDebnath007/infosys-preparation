def maxMonsters(n,e,power,bonus):
    total_masks = 1 << n
    reachable = [False] * total_masks
    reachable[0] = True
    answer = 0
    for mask in range(total_masks):
        if not reachable[mask]:
            continue
        current_exp = e
        defeated = 0
        for i in range(n):
            if mask & (1<<i):
                current_exp += bonus[i]
                defeated +=1
        answer = max(answer,defeated)
        for i in range(n):
            if mask & (1<<i):
                continue
            if current_exp >= power[i]:
                new_mask = mask | (1<<i)
                reachable[new_mask] =True
    return answer

n = int(input())
e = int(input())

power = []
for _ in range(n):
    power.append(int(input()))

bonus = []
for _ in range(n):
    bonus.append(int(input()))

print(maxMonsters(n, e, power, bonus))
