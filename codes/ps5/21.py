def moveZeros(lst):
    return [x for x in lst if x != 0] + [0] * lst.count(0)
print(moveZeros([1, 2, 0, 4, 0, 5, 0])) 
