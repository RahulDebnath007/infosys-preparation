def longest_prefix_suffix(s: str) -> int:
    n = len(s)
    lps = [0] * n
    length, i = 0, 1

    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    ans = lps[-1]
    if ans > n // 2:  
        ans = n // 2
    return ans


s = input().strip()
print(longest_prefix_suffix(s))
