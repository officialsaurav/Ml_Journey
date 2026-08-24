import numpy as np 
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise Arithmetic
print(a + b)  # Output: [5, 7, 9]
print(a * 2)  # Output: [2, 4, 6] (Scalar arithmetic)

# Universal Functions (ufuncs)
print(np.sqrt(a))  # Calculates square root for every element
print(np.sin(a))   # Calculates sine value for every element
print(np.exp(a))   # Calculates exponential for every element