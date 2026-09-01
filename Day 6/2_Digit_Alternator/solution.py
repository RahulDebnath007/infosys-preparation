s = input().strip()
even, odd = [], []
special_count = 0

for c in s:
    if c.isdigit():
        d = int(c)
        if d % 2 == 0:
            even.append(c)
        else:
            odd.append(c)
    elif not c.isalnum():
        special_count += 1

res = []
i = j = 0
turn_even = (special_count % 2 == 0)

while i < len(even) and j < len(odd):
    if turn_even:
        res.append(even[i]); i += 1
    else:
        res.append(odd[j]); j += 1
    turn_even = not turn_even

res.extend(even[i:])
res.extend(odd[j:])
print("".join(res))