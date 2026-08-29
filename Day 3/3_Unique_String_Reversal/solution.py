S = input().strip()
seen = set()
result = []

for ch in S:
    if ch not in seen:
        seen.add(ch)
        result.append(ch)

print("".join(result[::-1]))