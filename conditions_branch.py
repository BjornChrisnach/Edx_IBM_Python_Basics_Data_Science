# Comparison operations compare some value or operand and, based on a condition, they produce a Boolean.
# When comparing two values you can use these operators:

#    equal: ==
#    not equal: !=
#    greater than: >
#    less than: <
#    greater than or equal to: >=
#    less than or equal to: <=

# Let's assign a a value of 5. Use the equality operator denoted with two equal == signs to determine
# if two values are equal. The case below compares the variable a with 6.
# Condition Equal
a = 5
print(a == 6)

# Greater than Sign
i = 6
print(i > 5)
# Greater than Sign
i = 2
print(i > 5)

# The inequality test uses an exclamation mark preceding the equal sign, if two operands are not equal
# then the condition becomes True. For example, the following condition will produce True as long as
# the value of i is not equal to 6:
# Inequality Sign
i = 2
print(i != 6)
# Inequality Sign
i = 6
print(i != 6)

# Use Equality sign to compare the strings
print("ACDC" == "Michael Jackson")
# Use Inequality sign to compare the strings
print("ACDC" != "Michael Jackson")

# Inequality operation is also used to compare the letters/words/symbols according to the ASCII value
# of letters. The decimal value shown in the following table represents the order of the character:
# For example, the ASCII code for ! is 33, while the ASCII code for + is 43. Therefore + is larger
# than ! as 43 is greater than 33.
# Similarly, the value for A is 65, and the value for B is 66 therefore:
# Compare characters
print('B' > 'A')
# Compare characters
print('BA' > 'AB')

# If statement example
age = 19
#age = 18

# expression that can be true or false
if age > 18:

    # within an indent, we have the expression that is run if the condition is true
    print("you can enter")

# The statements after the if statement will run regardless if the condition is true or false
print("move on")

# Else statement example
age = 18
# age = 19

if age > 18:
    print("you can enter")
else:
    print("go see Meat Loaf")

print("move on")

# Elif statment example
age = 18

if age > 18:
    print("you can enter")
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf")

print("move on")

# Condition statement example
album_year = 1983
album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")

# Condition statement example
album_year = 1983
# album_year = 1970
if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")

print('do something..')

# Logical operators
#
# Sometimes you want to check more than one condition at once. For example, you might want to check
# if one condition and another condition is True. Logical operators allow you to combine or modify
# conditions.
#
#    and
#    or
#    not

# Condition statement example
album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print("Album year was in between 1980 and 1989")

print("")
print("Do Stuff..")

# Condition statement example
album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")

# Condition statement example
album_year = 1983

if not (album_year == '1984'):
    print("Album year is not 1984")

# Quiz

# Write an if statement to determine if an album had a rating greater than 8. Test it using the
# rating for the album “Back in Black” that had a rating of 8.5. If the statement is true print
# "This album is Amazing!"
rating = 8.5
if rating > 8:
    print("This album is Amazing!")

# Write an if-else statement that performs the following. If the rating is larger then eight print
# “this album is amazing”. If the rating is less than or equal to 8 print “this album is ok”.
rating = 8.5
if rating > 8:
    print("this album is amazing")
elif rating <= 8:
    print("this album is ok")

# Write an if statement to determine if an album came out before 1980 or in the years: 1991 or 1993.
# If the condition is true print out the year the album came out.
# Write your code below and press Shift+Enter to execute
release = 1977
if release < 1980 or release == 1991 or release == 1993:
    print("The album came out in the year ", release)
#   print("The album came out in the year %d", %release) #my syntaxing corrects to % release io %release
