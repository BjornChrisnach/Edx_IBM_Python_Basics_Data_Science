# Create a 2D Numpy Array

# Import the libraries
import numpy as np 
import matplotlib.pyplot as plt

# Consider the list a, the list contains three nested lists each of equal size. 

# Create a list
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
print(a)

# We can cast the list to a Numpy Array as follow
# Convert list to Numpy Array
# Every element is the same type
A = np.array(a)
print(A)

# Show the numpy array dimensions
print(A.ndim)

# Attribute shape returns a tuple corresponding to the size or number of each dimension.
# Show the numpy array shape
print(A.shape)

# The total number of elements in the array is given by the attribute size.
# Show the numpy array size
print(A.size)

# We simply use the square brackets and the indices corresponding to the element we would like:
# Access the element on the second row and third column
print(A[1, 2])

# We can also use the following notation to obtain the elements: 
# Access the element on the second row and third column
print(A[1][2])

# We can access the element as follows
# Access the element on the first row and first column
print(A[0][0])

# This can be done with the following syntax 
# Access the element on the first row and first and second columns
print(A[0][0:2])

# Similarly, we can obtain the first two rows of the 3rd column as follows:
# Access the element on the first and second rows and third column
print(A[0:2, 2])

# The numpy array is given by X and Y
# Create a numpy array X
X = np.array([[1, 0], [0, 1]]) 
print(X)

# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
print(Y)

# We can add the numpy arrays as follows.
# Add X and Y
Z = X + Y
print(Z)

# We can perform the same operation in numpy as follows 
# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
print(Y)

# Multiply Y with 2
Z = 2 * Y
print(Z)

# We can perform element-wise product of the array X and Y as follows:
# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
print(Y)

# Create a numpy array X
X = np.array([[1, 0], [0, 1]]) 
print(X)

# Multiply X with Y
Z = X * Y
print(Z)

# We can also perform matrix multiplication with the numpy arrays A and B as follows: 
# First, we define matrix A and B:
# Create a matrix A
A = np.array([[0, 1, 1], [1, 0, 1]])
print(A)

# Create a matrix B
B = np.array([[1, 1], [1, 1], [-1, 1]])
print(B)

# Calculate the dot product
Z = np.dot(A,B)
print(Z)

# Calculate the sine of Z
print(np.sin(Z))

# We use the numpy attribute T to calculate the transposed matrix
# Create a matrix C
C = np.array([[1,1],[2,2],[3,3]])
print(C)

# Get the transposed of C
print(C.T)

# Quiz

# Consider the following list a, convert it to Numpy Array. 
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
A = np.array(a)
print(A)

# Calculate the numpy array size.
print(A.size)

# Access the element on the first row and first and second columns.
print(A[0][0:2])

# Perform matrix multiplication with the numpy arrays A and B.
B = np.array([[0, 1], [1, 0], [1, 1], [-1, 0]])
X = np.dot(A,B)
print(X)
