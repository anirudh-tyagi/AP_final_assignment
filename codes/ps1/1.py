def checkPalindrome(s):
    # Find the length manually
    length = 0
    for _ in s:
        length += 1

    # Compare characters from both ends
    start = 0
    end = length - 1

    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1

    return True

# Example usage
word = input("Enter a word: ")
if checkPalindrome(word):
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")