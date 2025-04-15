class Vector:
    def __init__(self, elements):
        if not isinstance(elements, list):
            raise ValueError("Vector elements must be provided as a list.")
        self._elements = elements

    def __str__(self):
        # Return a formatted string representing the vector
        return f"{len(self._elements)}-dimensional vector: ({', '.join(map(str, self._elements))})"

    # Scaling the vector by a scalar
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError("Scalar must be a real number.")
        return Vector([x * scalar for x in self._elements])

    def __rmul__(self, scalar):
        # Handle multiplication when scalar is on the left side
        return self.__mul__(scalar)

    # Add two vectors
    def __add__(self, other):
        if len(self._elements) != len(other._elements):
            raise ValueError("Vectors must have the same dimension for addition.")
        return Vector([x + y for x, y in zip(self._elements, other._elements)])

    # Subtract two vectors
    def __sub__(self, other):
        if len(self._elements) != len(other._elements):
            raise ValueError("Vectors must have the same dimension for subtraction.")
        return Vector([x - y for x, y in zip(self._elements, other._elements)])

    # Dot product of two vectors
    def __matmul__(self, other):
        if len(self._elements) != len(other._elements):
            raise ValueError("Vectors must have the same dimension for dot product.")
        return sum(x * y for x, y in zip(self._elements, other._elements))


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

# Print the vectors
print(v1)  

# Scaling the vector
v1_scaled = 2 * v1
print(v1_scaled) 

v1_scaled = v1 * 3
print(v1_scaled)  


v3 = v1 + v2
print(v3)  

v4 = v1 - v2
print(v4)  


dot_product = v1 @ v2
print(dot_product)  # 32
