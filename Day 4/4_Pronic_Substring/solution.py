import math

def is_pronic(num):
    if num < 0:
        return False
    k = int(math.sqrt(num))
    return k * (k + 1) == num or (k - 1) * k == num

def main():
    s = input().strip()
    n = len(s)

    pronic_set = set()

    for i in range(n):
        num = 0
        for j in range(i, n):
            num = num * 10 + int(s[j])  
            if is_pronic(num):
                pronic_set.add(num)

    result = sorted(pronic_set)
    print(result)

if __name__ == "__main__":
    main()









