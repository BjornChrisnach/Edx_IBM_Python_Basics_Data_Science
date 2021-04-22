# Import the libraries

import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
# %matplotlib inline

# Plotting functions

def Plotvec1(u, z, v):
    
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

# Create a python list
a = ["0", 1, "two", "3", 4]

# Print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
print(a)

# Print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

# Check the type of the array
type(a)

# Check the type of the values stored in numpy array
a.dtype

# Create a numpy array
b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])

# Check the type of array
type(b)

# Check the value type
b.dtype

# Create numpy array
c = np.array([20, 1, 2, 3, 4])
print(c)

# Assign the first element to 100
c[0] = 100
print(c)

# Assign the 5th element to 0
c[4] = 0
print(c)

# Slicing the numpy array
d = c[1:4]
print(d)

# Set the fourth element and fifth element to 300 and 400
c[3:5] = 300, 400
print(c)

# Create the index list
select = [0, 2, 3]

# Use List to select elements
d = c[select]
print(d)

# Assign the specified elements to new value
c[select] = 100000
print(c)

# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
print(a)

# Get the size of numpy array
print(a.size)

# Get the number of dimensions of numpy array
print(a.ndim)

# Get the shape/size of numpy array
print(a.shape)

# Create a numpy array
a = np.array([1, -1, 1, -1])

# Get the mean of numpy array
mean = a.mean()
print(mean)

# Get the standard deviation of numpy array
standard_deviation=a.std()
print(standard_deviation)

# Create a numpy array
b = np.array([-1, 2, 3, 4, 5])
print(b)

# Get the biggest value in the numpy array
max_b = b.max()
print(max_b)

# Get the smallest value in the numpy array
min_b = b.min()
print(min_b)

# Consider the numpy array u:
u = np.array([1, 0])
print(u)

# Consider the numpy array v:
v = np.array([0, 1])
print(v)

# We can add the two arrays and assign it to z:
z = u + v
print(z)

# The operation is equivalent to vector addition:
# Plot numpy arrays
Plotvec1(u, z, v)

# Array Multiplication
# Consider the vector numpy array y:
# Create a numpy array
y = np.array([1, 2])
print(y)

# We can multiply every element in the array by 2:
# Numpy Array Multiplication
z = 2 * y
z

# Product of Two Numpy Arrays¶
# Consider the following array u:
# Create a numpy array
u = np.array([1, 2])
print(u)

# Consider the following array v:
# Create a numpy array
v = np.array([3, 2])
print(v)

# The product of the two numpy arrays u and v is given by:
# Calculate the production of two numpy arrays
z = u * v
print(z)

# Dot Product
# The dot product of the two numpy arrays u and v is given by:
# Calculate the dot product
np.dot(u, v)

# Adding Constant to a Numpy Array
# Consider the following array:
# Create a constant to numpy array

u = np.array([1, 2, 3, -1]) 
print(u)

# Adding the constant 1 to each element in the array:
# Add the constant to array
u + 1

# Mathematical Functions
# We can access the value of pi in numpy as follows :
# The value of pi
np.pi

# Create the numpy array in radians
x = np.array([0, np.pi/2 , np.pi])

# We can apply the function sin to the array x and assign the values to the array y; 
# this applies the sine function to each element in the array: 

# Calculate the sin of each elements
y = np.sin(x)
print(y)

# A useful function for plotting mathematical functions is linspace. Linspace returns evenly spaced numbers
# over a specified interval. We specify the starting point of the sequence and the ending point of the 
# sequence. The parameter "num" indicates the Number of samples to generate, in this case 5:

# Makeup a numpy array within [-2, 2] and 5 elements
np.linspace(-2, 2, num=5)

# If we change the parameter num to 9, we get 9 evenly spaced numbers over the interval 
# from -2 to 2:

# Makeup a numpy array within [-2, 2] and 9 elements
np.linspace(-2, 2, num=9)

# We can use the function linspace to generate 100 evenly spaced samples from the interval 0 to 2π:

# Makeup a numpy array within [0, 2π] and 100 elements 
x = np.linspace(0, 2*np.pi, num=100)

# We can apply the sine function to each element in the array x and assign it to the array y: 

# Calculate the sine of x list
y = np.sin(x)

# Plot the result
plt.plot(x, y)

# Quiz
# Implement the following vector subtraction in numpy: u-v

u = np.array([1, 0])
v = np.array([0, 1])
u - v

# Multiply the numpy array z with -2:
z = np.array([2, 4])
-2 * z

# Consider the list [1, 2, 3, 4, 5] and [1, 0, 1, 0, 1], and cast both lists to a numpy array then
# multiply them together:
a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 0, 1, 0, 1])
a * b

# Convert the list [-1, 1] and [1, 1] to numpy arrays a and b. Then, plot the arrays as vectors using
# the fuction Plotvec2 and find the dot product:
a = np.array([-1, 1])
b = np.array([1, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a,b))

# Convert the list [1, 0] and [0, 1] to numpy arrays a and b. Then, plot the arrays as vectors using the
# function Plotvec2 and find the dot product:
a = np.array([1, 0])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))

# Convert the list [1, 1] and [0, 1] to numpy arrays a and b. Then plot the arrays as vectors using the 
# fuction Plotvec2 and find the dot product:
a = np.array([1, 1])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))
print("The dot product is", np.dot(a, b))

# Why are the results of the dot product for [-1, 1] and [1, 1] and the dot product for [1, 0] and [0, 1]
# zero, but not zero for the dot product for [1, 1] and [0, 1]?

# The vectors used for question 4 and 5 are perpendicular. As a result, the dot product is zero.

