from math import gcd

S = input().strip()

frequency = {}

# Count frequency of each character
for ch in S:
    frequency[ch] = frequency.get(ch, 0) + 1

# Calculate GCD of all character frequencies
answer = 0

for count in frequency.values():
    answer = gcd(answer, count)

print(answer)