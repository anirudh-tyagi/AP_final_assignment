class UpperCaseException(Exception):
    pass

def evenIndexCapital(s):
    
    for char in s:
        if 'A' <= char <= 'Z': 
            raise UpperCaseException("Input string contains uppercase letters.")

    res = ""  
    for i in range(len(s)):
        if i % 2 == 0:  
            res += chr(ord(s[i]) - 32) 
        else:
            res += s[i]  
    return res

# Example usage
try:
    s = "hello"
    print(evenIndexCapital(s))  # Output: "HeLlO"
except UpperCaseException as e:
    print(e)