def splitsum(l):
    return [sum(x**2 for x in l if x > 0), sum(x**3 for x in l if x < 0)]


l = [1, -2, 3, -4, 5]
print(splitsum(l)) 
