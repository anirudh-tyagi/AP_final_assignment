class InvalidKValueException(Exception):
    pass

def kMax(l, k):
    # Check if k is a valid index
    if k < 1 or k > len(l):
        raise InvalidKValueException("Invalid value for k.")

    # Sort the list in descending order and return the k-th largest element
    sorted_l = sorted(l, reverse=True)
    return sorted_l[k - 1]



print(kMax([10, 2, 4, 5, 7, 9], 3) )
