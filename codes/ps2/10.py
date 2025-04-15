def separate(s):
    result = []
    i = 0
    while i < len(s):
        current = s[i]
        group = current
        i += 1
        while i < len(s) and s[i] == current:
            group += s[i]
            i += 1
        result.append(group)
    return result

def moveDups(s):
    result = []
    for i in range(len(s)):
        found = False
        for j in range(len(result)):
            if result[j][0] == s[i]:
                result[j] += s[i]
                found = True
                break
        if not found:
            result.append(s[i])
    return result

# Example calls
print("separate('cartoon'):", separate("cartoon"))     # ['c','a','r','t','oo','n']
print("moveDups('network'):", moveDups("network"))     # ['n','e','t','w','o','r','k']
print("moveDups('aabbec'):", moveDups("aabbec"))       # ['aa','bb','e','c']
print("moveDups('cecbbaaa'):", moveDups("cecbbaaa"))   # ['cc','e','bb','aaa']
