# advanced for example
squares = ["red", "yellow", "green"]
for i, square in enumerate(squares):
    print("index " + str(i) + ", " + str(square))

# while example
squares = ["orange", "orange", "purple", "orange", "blue"]
new_squares = []
i = 0
while(squares[i] == "orange"):
    new_squares.append(squares[i])

    i = i + 1

print(new_squares)

# If we would like to generate an object that contains elements ordered from 0 to 2 we simply
# use the following command:

# Use the range
# range(3)

# The for loop enables you to execute a code block multiple times. For example, you would use this
# if you would like to print out every element in a list. Let's try to use a for loop to print all
# the years presented in the list dates:
# For loop example

dates = [1982, 1980, 1973]
N = len(dates)

for i in range(N):
    print(dates[i])

# In this example we can print out a sequence of numbers from 0 to 7:
# Example of for loop
for i in range(0, 8):
    print(i)

# Exmaple of for loop, loop through list
for year in dates:
    print(year)

# Use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

# We can access the index and the elements of a list as follows:
# Loop through the list and iterate on both index and element value

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)

# Let’s say we would like to iterate through list dates and stop at the year 1973, then print out
# the number of iterations. This can be done with the following block of code:
# While Loop Example
dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):
    print(year)
    i = i + 1
    year = dates[i]


print("It took ", i, "repetitions to get out of loop.")

# Quiz
# Write a for loop the prints out all the element between -5 and 5 using the range function.
for i in range(-5, 6):
    print(i)

# Print the elements of the following list: Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
# Make sure you follow Python conventions.
genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for genre in genres:
    print(genre)

# Write a for loop that prints out the following list: squares=['red', 'yellow', 'green', 'purple', 'blue']
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print(square)

# Write a while loop to display the values of the Rating of an album playlist stored in the list
# PlayListRatings. If the score is less than 6, exit the loop. The list PlayListRatings is given
# by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
play_list_ratings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]

i = 1
rating = play_list_ratings[0]

while(i < len(play_list_ratings) and rating >= 6):
    print(rating)
    rating = play_list_ratings[i]
    i = i + 1

# Write a while loop to copy the strings 'orange' of the list squares to the list new_squares.
# Stop and exit the loop if the value on the list is not 'orange':
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0

while(i < len(squares) and squares[i] == "orange"):
    new_squares.append(squares[i])
    print(new_squares)
    i = i + 1
