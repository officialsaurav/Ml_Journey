import numpy as np 
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Indexing: [row, column]
print(matrix[0, 1])  # Output: 2


# Slicing: [rows_range, columns_range]
print(matrix[:, 1:3]) 
# Output:

# [[2, 3],

#  [5, 6]]
# Reshaping: Changing dimensions without changing the data
new_matrix = matrix.reshape(3, 2)

print(new_matrix)
