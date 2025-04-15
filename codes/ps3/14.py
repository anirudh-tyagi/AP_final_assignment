def equivalent(str1, str2):
    def get_rotations(s):
        return [s[i:] + s[:i] for i in range(len(s))]

    max_len = 0
    best_sub = ""

    n = len(str1)

    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = str1[i:j]
            rotations = get_rotations(sub)
            for rot in rotations:
                if rot in str2:
                    if len(sub) > max_len or (len(sub) == max_len and sub < best_sub):
                        max_len = len(sub)
                        best_sub = sub
                    break  # No need to check other rotations if one matches

    return best_sub
print(equivalent('hdjkoul', 'pokoudj')) 
