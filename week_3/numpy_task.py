import numpy as np
from datetime import datetime, timedelta


# Task1: Create a vector with values ranging from 10 to 49. Reverse the vector.
vector = np.arange(10, 50)
reversed_vector = vector[::-1]
#Print the otuputs of the generated vector and its reverse
print("1. Original vector (head):", vector[:5])
print("   Reversed vector (head):", reversed_vector[:5])

# Task2: To Create a 5x5 array with random values and find min and max values
np.random.seed(42)  # For reproducibility
random_matrix_5x5 = np.random.random((5, 5))
min_val = random_matrix_5x5.min()
max_val = random_matrix_5x5.max()
print(f"\n2. 5x5 Array Min: {min_val:.4f}, Max: {max_val:.4f}")

# Task3: To Normalize a 5x5 random matrix (Subtract mean, divide by standard deviation)
matrix_to_norm = np.random.random((5, 5))
normalized_matrix = (matrix_to_norm - matrix_to_norm.mean()) / matrix_to_norm.std()
print("\n3. Normalized 5x5 Matrix (Mean ~0, Std ~1):\n", normalized_matrix.round(2))

# Task 4: Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
matrix_5x3 = np.ones((5, 3))
matrix_3x2 = np.ones((3, 2))
product_matrix = np.dot(matrix_5x3, matrix_3x2)  # or matrix_5x3 @ matrix_3x2
print(f"\n4. Matrix Product Shape (should be 5x2): {product_matrix.shape}")

# Task 5: How to get the dates of yesterday, today, and tomorrow
today = np.datetime64('today', 'D')
yesterday = today - np.timedelta64(1, 'D')
tomorrow = today + np.timedelta64(1, 'D')
#Print out the dates of yesterday, today, and tomorrow
print(f"\n5. Dates -> Yesterday: {yesterday}, Today: {today}, Tomorrow: {tomorrow}")

# Task 6: Extract the integer part of a random array using 5 different methods
rand_arr = np.uniform_arr = np.random.uniform(1, 10, 5)
print(f"\n6. Original random array: {rand_arr.round(2)}")
print("   Method 1 (np.floor):", np.floor(rand_arr))
print("   Method 2 (np.trunc):", np.trunc(rand_arr))
print("   Method 3 (astype(int)):", rand_arr.astype(int))
print("   Method 4 (np.around - 0.5):", np.around(rand_arr - 0.5))
print("   Method 5 (mod operator):", rand_arr - (rand_arr % 1))

# Task 7: Create a structured array representing a position (x, y) and a color (r, g, b)
pos_color_dtype = [('position', [('x', float), ('y', float)]),
                   ('color', [('r', int), ('g', int), ('b', int)])]
structured_arr = np.array([((1.5, 2.0), (255, 0, 0)), 
                           ((3.1, 4.2), (0, 255, 0))], dtype=pos_color_dtype)
print("\n7. Structured Array Example:\n", structured_arr)

# Task 8: Consider a generator function that generates 10 integers and use it to build an array
def integer_generator():
    for i in range(10):
        yield i * 3

array_from_gen = np.fromiter(integer_generator(), dtype=int)
print("\n8. Array from Generator:", array_from_gen)

# Task 9: To check the equality of 2 Random arrays
array_a = np.array([1, 2, 3])
array_b = np.array([1, 2, 3])
are_equal = np.array_equal(array_a, array_b)
print(f"\n9. Are Array A and Array B equal? {are_equal}")

# Task 10: To find the point-by-point distances of a given random array
coordinates = np.random.random((10, 2))  # using 10 for compact print preview
# Using broadcasting to find pairwise Euclidean distances between all points
distances = np.sqrt(np.sum((coordinates[:, np.newaxis, :] - coordinates[np.newaxis, :, :]) ** 2, axis=-1))
print(f"\n10. Pairwise Distance Matrix Shape: {distances.shape}")

# Task 11: Subtract the mean of each row of a matrix
matrix = np.random.rand(3, 3)
row_centered_matrix = matrix - matrix.mean(axis=1, keepdims=True)
print("\n11. Row-centered Matrix:\n", row_centered_matrix.round(2))

# Task12: How to sort an array by the nth column?
unsorted_matrix = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
n = 1  # sorting by the 2nd column (index 1)
sorted_matrix = unsorted_matrix[unsorted_matrix[:, n].argsort()]
print(f"\n12. Matrix sorted by column {n}:\n", sorted_matrix)

# Task 13: Compute a matrix rank
matrix_to_rank = np.eye(4)  # Identity matrix has rank 4
rank = np.linalg.matrix_rank(matrix_to_rank)
print(f"\n13. Matrix Rank: {rank}")

# Task 14: Consider a 16x16 array, how to get the block-sum (block size is 4x4)?
arr_16 = np.ones((16, 16))
block_sum = np.add.reduceat(np.add.reduceat(arr_16, np.arange(0, 16, 4), axis=0), np.arange(0, 16, 4), axis=1)
print(f"\n14. Block-sum shape (should be 4x4): {block_sum.shape}\n", block_sum)