class InvalidArgumentException(Exception):
    pass

def shift(s, ccount=0, acount=0):
    if not (isinstance(ccount, int) and isinstance(acount, int)) or ccount < 0 or acount < 0:
        raise InvalidArgumentException("ccount and acount must be non-negative integers.")

    n = len(s)
    if n == 0 or (ccount == 0 and acount == 0):
        return s

    # Perform left rotation by ccount
    ccount %= n
    left_rotated = s[ccount:] + s[:ccount]

    # Perform right rotation by acount
    acount %= n
    right_rotated = left_rotated[-acount:] + left_rotated[:-acount]

    return right_rotated