from collections import Counter

X = int(input().strip())
L = list(map(int, input().split()))

freq = sorted(Counter(L).values())  

unique = len(freq)
for f in freq:
    if X >= f:
        X -= f
        unique -= 1
    else:
        break

print(unique)