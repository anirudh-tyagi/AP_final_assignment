def delVowels(s):
    vowels = "aeiouAEIOU"
    result = ""
    for char in s:
        if char not in vowels:
            result += char
    return result

print(delVowels("Hello World!"))