str=""
def distChar(s1, s2):
    # Find characters unique to each string
    unique_to_s1 = set(s1) - set(s2)
    unique_to_s2 = set(s2) - set(s1)

    # Combine unique characters and sort them
    result = ''.join(sorted(unique_to_s1.union(unique_to_s2)))

    return result


print(distChar("character", "alphabet"))
