def extractDup(lst):
    result = []
    for i in range(len(lst)):
        count = 0
        is_duplicate = False
        for j in range(i):
            if lst[i] == lst[j]:
                is_duplicate = True
                break
        if is_duplicate:
            continue
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                count += 1
        if count > 1:
            result.append(lst[i])
    return result


print(extractDup([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]))