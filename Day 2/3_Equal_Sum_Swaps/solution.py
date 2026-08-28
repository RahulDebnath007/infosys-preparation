A = list(map(int, input().split()))
B = list(map(int, input().split()))

sumA, sumB = sum(A), sum(B)
diff = sumA - sumB

if diff % 2 != 0:
    print(-1)
    exit()

target = diff // 2
setB = set(B)

even_pairs = []
odd_pairs = []

for a in A:
    b = a - target
    if b in setB:
        pair = f"{a},{b}"
        if (a * b) % 2 == 0:
            even_pairs.append(pair)
        else:
            odd_pairs.append(pair)

if not even_pairs and not odd_pairs:
    print(-1)
else:
    print(",".join(even_pairs + odd_pairs))
