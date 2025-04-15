class DimensionMismatchException(Exception):
    pass

def printMat(matrix, rows, cols):
    
    if len(matrix) != rows * cols:
        raise DimensionMismatchException("Dimensions do not match the number of elements in the matrix.")
    
    # Print the matrix in row-major order
    for i in range(rows):
        row = matrix[i * cols:(i + 1) * cols]  # Extract the row
        print(' '.join(map(str, row)))  # Print the row elements


matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rows = 3
cols = 3
printMat(matrix, rows, cols)
