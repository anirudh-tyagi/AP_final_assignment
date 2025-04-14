def shift(s, ccount=0, acount=0):
    # Helper function to check if a value is a non-negative integer
    def is_non_negative_integer(val):
        return isinstance(val, int) and val >= 0

    # Raise exceptions for invalid inputs
    if not isinstance(s, str):
        raise TypeError("s must be a string.")
    if not is_non_negative_integer(ccount):
        raise ValueError("ccount must be a non-negative integer.")
    if not is_non_negative_integer(acount):
        raise ValueError("acount must be a non-negative integer.")

    n = 0
    for _ in s:
        n += 1

    # Handle cases where acount or ccount >= length of string
    acount %= n if n > 0 else 1
    ccount %= n if n > 0 else 1

    # Left rotation by acount
    rotated = ''
    for i in range(n):
        rotated += s[(i + acount) % n]

    # Right rotation by ccount on the rotated string
    result = ''
    for i in range(n):
        result += rotated[(i - ccount + n) % n]

    return result

print(shift('NinjaHattori',ccount=0 ,acount =3))
  