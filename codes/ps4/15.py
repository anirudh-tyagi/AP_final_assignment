def subPali(s):
    max_len = 0
    n = len(s)

    for center in range(n):
        # Odd length palindromes
        l, r = center, center
        while l >= 0 and r < n and s[l] == s[r]:
            max_len = max(max_len, r - l + 1)
            l -= 1
            r += 1

        # Even length palindromes
        l, r = center, center + 1
        while l >= 0 and r < n and s[l] == s[r]:
            max_len = max(max_len, r - l + 1)
            l -= 1
            r += 1

    return max_len
print(subPali('abcde'))  