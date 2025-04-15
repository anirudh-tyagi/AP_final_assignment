class DimensionMismatchException(Exception):
    pass

def matMul(A, B, m, n, p):
    # Check if the number of columns in A matches the number of rows in B
    if n != len(B) // p:
        raise DimensionMismatchException("Dimensions do not match for matrix multiplication.")

    # Initialize the result matrix with zeros (m * p)
    result = [0] * (m * p)

    # Perform matrix multiplication
    for i in range(m):
        for j in range(p):
            sum_product = 0
            for k in range(n):
                sum_product += A[i * n + k] * B[k * p + j]
            result[i * p + j] = sum_product

    return result


A = [1, 2, 0, 4, 0, 5, 0, 7, 9]  
B = [1, 2, 0, 4, 0, 5, 0, 7, 9]  
m = 3  # Rows of A
n = 3  # Columns of A (and rows of B)
p = 3  # Columns of B

result = matMul(A, B, m, n, p)
print(result)  
