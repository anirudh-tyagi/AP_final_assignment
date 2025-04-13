def minIndexFirstString(str1, str2):
    # Iterate through str1 from the end
    for i in range(len(str1) - 1, -1, -1):
        # Check if the character in str1 exists in str2
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                return i
 
    return -1

str1 = "integer"
str2 = "tiger"
print(minIndexFirstString(str1, str2))  
