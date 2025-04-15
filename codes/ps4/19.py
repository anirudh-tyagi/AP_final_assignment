class LengthMismatchException(Exception):
    pass

def weave(list1, list2):
    # Raise exception if the lists have unequal lengths
    if len(list1) != len(list2):
        raise LengthMismatchException("The lists have unequal lengths.")
    
    # Weave the lists
    result = []
    for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])
    
    return result

print(weave([1, 2, 3], [4, 5, 6]))  # Output: [1, 4, 2, 5, 3, 6]

#  Unequal-length lists (raises LengthMismatchException)
try:
    print(weave([1, 2], [3, 4, 5]))  # Raises exception
except LengthMismatchException as e:
    print(e)  # Output: The lists have unequal lengths.