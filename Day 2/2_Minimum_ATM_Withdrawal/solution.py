def minWithdrawals(atm, X):
    total = sum(atm)
    target = total - X

    if target < 0:
        return -1
    if target == 0:
        return len(atm)

    n = len(atm)
    left, currSum, maxLen = 0, 0, -1

    for right in range(n):
        currSum += atm[right]

        while currSum > target and left <= right:
            currSum -= atm[left]
            left += 1

        if currSum == target:
            maxLen = max(maxLen, right - left + 1)

    return -1 if maxLen == -1 else n - maxLen


if __name__ == "__main__":
    n = int(input().strip())

    atm = list(map(int, input().split()))
    while len(atm) < n:   
        atm.extend(map(int, input().split()))

    X = int(input().strip())
    print(minWithdrawals(atm, X))