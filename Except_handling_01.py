# Definition
# An exception is an error that occurs during the execution of code. This error causes the code to
# raise an exception and if not prepared to handle it will halt the execution of the code.

# Examples

# Run each piece of code and observe the exception raised
# 1/0
# ZeroDivisionError occurs when you try to divide by zero.

# y = a + 5
# NameError in this case means that you tried to use the variable a when it was not defined.

# a = [1, 2, 3]
# a[10]
# IndexError in this case occurs when you try to access data from a list using an index that
# does not exist for this list.

# potential code before try catch

# try:
# code to try to execute
# except:
# code to execute if there is an exception

# code that will still execute if there is an exception

# In this example we are trying to divide a number given by the user, save the outcome in the variable a,
# and then we would like to print the result of the operation. When taking user input and dividing a
# number by it there are a couple of exceptions that can be raised. For example if we divide by zero,
# try running the following block of code, with b as a number an exception will only be Raised if b,
# is zero
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=", a)
except:
    print("There was an error")

# Try Except Specific

# A specific try except allows you to catch certain exceptions and also execute certain code depending
# on the exception. This is useful if you do not want to deal with some exceptions and the execution
# should halt, it can also help you find errors in your code that you might not know about, and it can
# help you differentiate responses to different exceptions. In this case the code after the try except
# might not run depending on the error.
# potential code before try catch

# try:
    # code to try to execute
#  except (ZeroDivisionError, NameError):
    # code to execute if there is an exception of the given types

# code that will execute if there is no exception or a one that we are handling

# potential code before try catch

# try:
    # code to try to execute
# except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
# except NameError:
    # code to execute if there is a NameError

# code that will execute if there is no exception or a one that we are handling

# potential code before try catch

# try:
    # code to try to execute
# except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
# except NameError:
    # code to execute if there is a NameError
# except:
    # code to execute if ther is any exception

# code that will execute if there is no exception or a one that we are handling

# This is the same example as above, but now we will add differentiated messages depending on the
# exception letting the user know what is wrong with the input.

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=", a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")

# else allows one to check if there was no exception when executing the try block. This is useful when
# we want to execute something only if there were no errors.
# potential code before try catch

# try:
    # code to try to execute
# except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
# except NameError:
    # code to execute if there is a NameError
# except:
    # code to execute if ther is any exception
# else:
    # code to execute if there is no exception

# code that will execute if there is no exception or a one that we are handling

# finally allows us to always execute something even if there is an exception or not. This is usually
# used to signify the end of the try except.

# potential code before try catch

# try:
    # code to try to execute
# except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
# except NameError:
    # code to execute if there is a NameError
# except:
    # code to execute if ther is any exception
# else:
    # code to execute if there is no exception
# finally:
    # code to execute at the end of the try except no matter what

# code that will execute if there is no exception or a one that we are handling

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=", a)

# Now lets let the user know that we are done processing their answer. Using the finally lets add a print.
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=", a)
finally:
    print("Processing Complete")
