def minop(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    # Create a 2D array to store results of subproblems
    dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    # Fill dp[][] in bottom up manner
    for i in range(len1 + 1):
        for j in range(len2 + 1):

            # If first string is empty, insert all characters of second string
            if i == 0:
                dp[i][j] = j

            # If second string is empty, remove all characters of first string
            elif j == 0:
                dp[i][j] = i

            # If last characters are the same, ignore and move diagonally
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            # If last characters are different, consider all three operations
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],    # Insert
                    dp[i - 1][j],    # Remove
                    dp[i - 1][j - 1] # Replace
                )

    return dp[len1][len2]
print(minop("python", "pythons"))   
