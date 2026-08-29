import numpy as np

# Create a 2x3 matrix (2 rows, 3 columns)
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6]])

print(matrix)
# Output:
# [[1 2 3]
#  [4 5 6]]
# Assuming a 2x3 matrix

print(matrix.ndim)   # Dimensions: Returns 2

print(matrix.shape)  # Shape: Returns (2, 3) (rows, columns)

print(matrix.size)   # Total elements: Returns 6
