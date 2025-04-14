class InvalidInputException(Exception):
    pass

def change(str):
    # Validate input
    for char in str:
        if char not in ('R', 'G'):
            raise InvalidInputException("Input string contains invalid characters. Only 'R' and 'G' are allowed.")


    count_R = 0
    count_G = 0
    for char in str:
        if char == 'R':
            count_R += 1
        elif char == 'G':
            count_G += 1

    # Return the minimum changes needed
    return min(count_R, count_G)


print(change("RRGGG"))
