def oddCollatz(n):
    
    odd_numbers = []
    
    
    while n != 1:
        if n % 2 != 0:  # Check if n is odd
            odd_numbers.append(n)
        
       
        if n % 2 == 0:
            n //= 2  # If even, divide by 2
        else:
            n = 3 * n + 1  # If odd, multiply by 3 and add 1
    
    
    odd_numbers.append(1)
    
    return odd_numbers
print(oddCollatz(3))