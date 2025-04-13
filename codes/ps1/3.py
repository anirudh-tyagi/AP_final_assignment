def firstLetters(s):
    result=s[0]
    for i in range(1,len(s)):
        if s[i-1]==" ":
            result+=s[i]

    return result

# Example usage     
s = "hello other world"
print(firstLetters(s)) 