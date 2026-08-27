S = input().strip()
res = []

for i in range(1, len(S), 2):
    res.append(str(int(S[i])**2))
    if sum(len(x) for x in res) >= 4:
        break

print("".join(res)[:4])
