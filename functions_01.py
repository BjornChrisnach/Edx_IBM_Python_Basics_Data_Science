# There are two types of functions :

#    Pre-defined functions
#    User defined functions

# What is a Function?

# You can define functions to provide the required functionality. Here are simple rules to define a
# function in Python:

#     Functions blocks begin def followed by the function name and parentheses ().
#     There are input parameters or arguments that should be placed within these parentheses.
#     You can also define parameters inside these parentheses.
#     There is a body within every function that starts with a colon (:) and is indented.
#     You can also place documentation before the body.
#     The statement return exits a function, optionally passing back a value.

# An example of a function that adds on to the parameter a prints and returns the output as b:

# First function example: Add 1 to a and store as b
def add(a):
    b = a + 1
    print(a, "if you add one", b)
    return(b)


print(add(1))

# Get a help on add function
help(add)

# Call the function add()
add(1)

# Call the function add()
add(2)

# We can create different functions. For example, we can create a function that multiplies two numbers.
# The numbers will be represented by the variables a and b:
# Define a function for multiple two numbers


def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')


result = Mult(12, 2)
print(result)

# The same function can be used for different data types. For example, we can multiply two integers:
# Use mult() multiply two integers

print(Mult(2, 3))

# Use mult() multiply two floats
print(Mult(10.0, 3.14))

# We can even replicate a string by multiplying with an integer:
print(Mult(2, "Michael Jackson "))

# Function Definition


def square(a):

    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c)
    return(c)


square(2)

# Initializes Global variable
x = 3
# Makes function call and return function a y
y = square(x)
print(y)

# Directly enter a number as parameter
print(square(2))


# Define functions, one with return value None and other without return value
def MJ():
    print('Michael Jackson')


def MJ1():
    print('Michael Jackson')
    return(None)


MJ1()

# See what functions returns are

print(MJ())
print(MJ1())

# Define the function for combining strings


def con(a, b):
    return(a + b)


# Test on the con() function
print(con("This ", "is"))

# Consider the two lines of code in Block 1 and Block 2: the procedure for each block is identical.
# The only thing that is different is the variable names and values.

# Block 1
# a and b calculation block1
a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0
else:
    c1 = 5

print(c1)

# Block 2
# a and b calculation block2
a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0
else:
    c2 = 5

print(c2)

# We can replace the lines of code with a function. A function combines many instructions into a
# single line of code. Once a function is defined, it can be used repeatedly. You can invoke the same
# function many times in your program. You can save your function and use it in another program or use
# someone else’s function. The lines of code in code Block 1 and code Block 2 can be replaced by the
# following function:
# Make a Function for the calculation above


def Equation(a, b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0
    else:
        c = 5
    return(c)


print(Equation(1, 2))

# Code Blocks 1 and Block 2 can now be replaced with code Block 3 and code Block 4.
# Block 3:
a1 = 4
b1 = 5
c1 = Equation(a1, b1)

print(c1)

# Block 4:
a2 = 0
b2 = 0
c2 = Equation(a2, b2)

print(c2)

# Pre-defined functions

# There are many pre-defined functions in Python, so let's start with the simple ones.
# Build-in function print()
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5]
print(album_ratings)

# Use sum() to add every element in a list or tuple together
print(sum(album_ratings))

# Show the length of the list or tuple
print(len(album_ratings))

# Using if/else Statements and Loops in Functions
# The return() function is particularly useful if you have any IF statements in the function,
# when you want your output to be dependent on some condition:
# Function example


def type_of_album(artist, album, year_released):

    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"


x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)

# Print the list using for loop


def PrintList(the_list):
    for element in the_list:
        print(element)


# Implement the printlist function
PrintList(['1', 1, 'the man', "abc"])

# Setting default argument values in your custom functions
# Example for setting param with default value


def isGoodRating(rating=4):
    if(rating < 7):
        print("this album sucks it's rating is", rating)

    else:
        print("this album is good its rating is", rating)


# Test the value with default value and with input
isGoodRating()
isGoodRating(10)


# Global variables

# So far, we've been creating variables within functions, but we have not discussed variables outside
# the function. These are called global variables. Let's try to see what printer1 returns:
# Example of global variable
artist = "Michael Jackson"


def printer1(artist):
    internal_var1 = artist
    print(artist, "is an artist")


printer1(artist)
# try runningthe following code
# printer1(internal_var1)

# <b>We got a Name Error:  <code>name 'internal_var' is not defined</code>. Why?</b>
# It's because all the variables we create in the function is a <b>local variable</b>, meaning that
# the variable assignment does not persist outside the function. But there is a way to create
# <b>global variables</b> from within a function as follows:
artist = "Michael Jackson"


def printer(artist):
    global internal_var
    internal_var = "Whitney Houston"
    print(artist, "is an artist")


printer(artist)
printer(internal_var)

# Scope of a Variable

# The scope of a variable is the part of that program where that variable is accessible. Variables
# that are declared outside of all function definitions, such as the myFavouriteBand variable in the code
# shown here, are accessible from anywhere within the program. As a result, such variables are said
# to have global scope, and are known as global variables. myFavouriteBand is a global variable, so it
# is accessible from within the getBandRating function, and we can use it to determine a band's rating.
# We can also use it outside of the function, such as when we pass it to the print function to display it:

# Example of global variable

myFavouriteBand = "AC/DC"


def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0


print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:", getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)

# Take a look at this modified version of our code. Now the myFavouriteBand variable is defined within
# the getBandRating function. A variable that is defined within a function is said to be a local variable
# of that function. That means that it is only accessible from within the function in which it is defined.
# Our getBandRating function will still work, because myFavouriteBand is still defined within the function.
# However, we can no longer print myFavouriteBand outside our function, because it is a local variable of
# our getBandRating function; it is only defined within the getBandRating function:
# Example of local variable


def getBandRating(bandname):
    myFavouriteBand = "AC/DC"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0


print("AC/DC's rating is: ", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
print("My favourite band is", myFavouriteBand)

# Finally, take a look at this example. We now have two myFavouriteBand variable definitions. The first
# one of these has a global scope, and the second of them is a local variable within the getBandRating
# function. Within the getBandRating function, the local variable takes precedence. Deep Purple will
# receive a rating of 10.0 when passed to the getBandRating function. However, outside of the
# getBandRating function, the getBandRating s local variable is not defined, so the myFavouriteBand
# variable we print is the global variable, which has a value of AC/DC:
# Example of global variable and local variable with the same name

myFavouriteBand = "AC/DC"


def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0


print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)

# Collections and Functions
# When the number of arguments are unknown for a function, They can all be packed into a tuple as shown:


def printAll(*args):  # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args))
    for argument in args:
        print(argument)


# printAll with 3 arguments
printAll('Horsefeather', 'Adonis', 'Bone')
# printAll with 4 arguments
printAll('Sidecar', 'Long Island', 'Mudslide', 'Carriage')

# Similarly, The arguments can also be packed into a dictionary as shown:


def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])


printDictionary(Country='Canada', Province='Ontario', City='Toronto')

# Functions can be incredibly powerful and versatile. They can accept (and return) data types, objects
# and even other functions as arguements. Consider the example below:


def addItems(list):
    list.append("Three")
    list.append("Four")


myList = ["One", "Two"]

addItems(myList)

print(myList)

# Quiz
#
# Come up with a function that divides the first input by the second input:


def seperate_2_inputs(inp1, inp2):
    return(inp1/inp2)
# given solution


def div(a, b):
    return(a/b)

# Use the con function for the following question


def con(a, b):
    return(a + b)


# example:
print(con(2, 2))

# Can the con function we defined before be used to concatenate lists or tuples?
# Yes, for example:
print(con(['a', 1], ['b', 1]))
