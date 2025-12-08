import numpy as np

# ==========================================
# 1. Creating Arrays
# ==========================================

# From list
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array from list:", arr1)

# 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# Array of zeros
zeros = np.zeros((3, 4))
print("Array of zeros:\n", zeros)

# Array of ones
ones = np.ones((2, 3))
print("Array of ones:\n", ones)

# Array with range
range_arr = np.arange(0, 10, 2)  # start, stop, step
print("Range array:", range_arr)

# Linearly spaced array
linear = np.linspace(0, 1, 5)  # start, stop, num_points
print("Linearly spaced:", linear)

# Identity matrix
identity = np.eye(3)
print("Identity matrix:\n", identity)

# Random arrays
random_arr = np.random.rand(2, 3)  # uniform [0, 1)
print("Random array:\n", random_arr)

random_int = np.random.randint(0, 10, (2, 3))  # random integers
print("Random integers:\n", random_int)

print("\n")

# ==========================================
# 2. Array Properties
# ==========================================

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Array:\n", arr)
print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
print("Size (total elements):", arr.size)
print("Data type:", arr.dtype)
print("Item size (bytes):", arr.itemsize)
print("\n")

# ==========================================
# 3. Array Indexing and Slicing
# ==========================================

arr = np.array([10, 20, 30, 40, 50])
print("Original array:", arr)
print("Element at index 2:", arr[2])
print("Slice [1:4]:", arr[1:4])
print("Last element:", arr[-1])
print("Every 2nd element:", arr[::2])

# 2D array indexing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:\n", arr2d)
print("Element [1,2]:", arr2d[1, 2])
print("First row:", arr2d[0, :])
print("Second column:", arr2d[:, 1])
print("Sub-array:\n", arr2d[0:2, 1:3])
print("\n")

# ==========================================
# 4. Array Operations (Element-wise)
# ==========================================

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print("a:", a)
print("b:", b)
print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
print("a / b:", a / b)
print("a ** 2:", a ** 2)
print("Square root of a:", np.sqrt(a))
print("Exponential of a:", np.exp(a))
print("\n")

# ==========================================
# 5. Universal Functions (ufuncs)
# ==========================================

arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Sin:", np.sin(arr))
print("Cos:", np.cos(arr))
print("Log:", np.log(arr))
print("Absolute:", np.abs([-1, -2, 3]))
print("\n")

# ==========================================
# 6. Statistical Functions
# ==========================================

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Data:\n", data)
print("Sum:", np.sum(data))
print("Sum along axis 0 (columns):", np.sum(data, axis=0))
print("Sum along axis 1 (rows):", np.sum(data, axis=1))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard deviation:", np.std(data))
print("Variance:", np.var(data))
print("Min:", np.min(data))
print("Max:", np.max(data))
print("Min index:", np.argmin(data))
print("Max index:", np.argmax(data))
print("\n")

# ==========================================
# 7. Array Reshaping
# ==========================================

arr = np.arange(12)
print("Original array:", arr)
print("Reshaped (3x4):\n", arr.reshape(3, 4))
print("Reshaped (2x6):\n", arr.reshape(2, 6))
print("Flattened:", arr.reshape(3, 4).flatten())
print("Raveled:", arr.reshape(3, 4).ravel())

# Transpose
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\nOriginal matrix:\n", matrix)
print("Transposed:\n", matrix.T)
print("\n")

# ==========================================
# 8. Stacking and Splitting Arrays
# ==========================================

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Vertical stack
vstack = np.vstack((a, b))
print("Vertical stack:\n", vstack)

# Horizontal stack
hstack = np.hstack((a, b))
print("Horizontal stack:", hstack)

# Splitting
arr = np.arange(9)
split = np.split(arr, 3)
print("Split array into 3:", split)
print("\n")

# ==========================================
# 9. Boolean Indexing
# ==========================================

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("Array:", arr)
print("Elements > 4:", arr[arr > 4])
print("Elements divisible by 2:", arr[arr % 2 == 0])
print("Elements between 3 and 7:", arr[(arr > 3) & (arr < 7)])
print("\n")

# ==========================================
# 10. Matrix Operations
# ==========================================

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix multiplication (dot product):\n", np.dot(A, B))
print("Element-wise multiplication:\n", A * B)
print("Matrix determinant:", np.linalg.det(A))
print("Matrix inverse:\n", np.linalg.inv(A))
print("\n")

# ==========================================
# 11. Broadcasting
# ==========================================

arr = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10
print("Array:\n", arr)
print("Add scalar 10:\n", arr + scalar)

vector = np.array([1, 2, 3])
print("Add vector [1,2,3]:\n", arr + vector)
print("\n")

# ==========================================
# 12. Copying Arrays
# ==========================================

original = np.array([1, 2, 3, 4])
view = original.view()  # Creates a view
copy = original.copy()  # Creates a copy

original[0] = 999
print("Original:", original)
print("View:", view)  # Changes with original
print("Copy:", copy)  # Doesn't change
print("\n")

# ==========================================
# 13. Sorting
# ==========================================

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print("Original:", arr)
print("Sorted:", np.sort(arr))
print("Sorted indices:", np.argsort(arr))

arr2d = np.array([[3, 2, 1], [6, 5, 4]])
print("\n2D array:\n", arr2d)
print("Sort along axis 1:\n", np.sort(arr2d, axis=1))
print("\n")

# ==========================================
# 14. Unique and Set Operations
# ==========================================

arr = np.array([1, 2, 2, 3, 3, 3, 4, 4, 5])
print("Array:", arr)
print("Unique values:", np.unique(arr))
print("Unique with counts:", np.unique(arr, return_counts=True))

# Set operations
a = np.array([1, 2, 3, 4, 5])
b = np.array([3, 4, 5, 6, 7])
print("\nArray a:", a)
print("Array b:", b)
print("Intersection:", np.intersect1d(a, b))
print("Union:", np.union1d(a, b))
print("Difference (a-b):", np.setdiff1d(a, b))
print("\n")

# ==========================================
# 15. Saving and Loading
# ==========================================

arr = np.array([1, 2, 3, 4, 5])

# Save to file
np.save('array.npy', arr)
print("Array saved to 'array.npy'")

# Load from file
loaded = np.load('array.npy')
print("Loaded array:", loaded)

# Save as text
np.savetxt('array.txt', arr)
print("Array saved to 'array.txt'")

# Load from text
loaded_txt = np.loadtxt('array.txt')
print("Loaded from text:", loaded_txt)