# A set is a unique collection of objects in Python. You can denote a set with a curly bracket {}.
#  Python will automatically remove duplicate items:

# Create a set
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)

# Convert list to set
album_list = ["Michael Jackson", "Thriller", 1982, "00:42:19", "Pop, Rock", "R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)
print(album_set)

# Convert list to set
music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul",
                    "progressive rock", "soft rock", "R&B", "disco"])
print(music_genres)

# Let us go over set operations, as these can be used to change the set. Consider the set A:
# Sample set
set_A = set(["Thriller", "Back in Black", "AC/DC"])
# Add element to set
set_A.add("NSYNC")
print(set_A)
# Try to add duplicate element to the set
set_A.add("NSYNC")
print(set_A)

# Remove the element from set
set_A.remove("NSYNC")
print(set_A)

# Verify if the element is in the set
print("AC/DC" in set_A)

# Remember that with sets you can check the difference between sets, as well as the symmetric difference, intersection, and union:
# Sample Sets
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set(["AC/DC", "Back in Black", "The Dark Side of the Moon"])

# You can find the intersect of two sets as follow using &:
intersection = album_set1 & album_set2
print(intersection)

# Find the difference in set1 but not set2
print(album_set1.difference(album_set2))
# The elements in album_set2 but not in album_set1 is given by:
print(album_set2.difference(album_set1))

# Use intersection method to find the intersection of album_list1 and album_list2
print(album_set1.intersection(album_set2))

# Find the union of two sets
print(album_set1.union(album_set2))

# Check if superset
print(set(album_set1).issuperset(album_set2))
# Check if subset
print(set(album_set2).issubset(album_set1))
# Check if subset
print(set({"Back in Black", "AC/DC"}).issubset(album_set1))
# Check if superset
print(album_set1.issuperset({"Back in Black", "AC/DC"}))

# Quiz.
# Convert the list ['rap','house','electronic music', 'rap'] to a set:
list_x = set(["rap", "house", "electronic  music", "rap"])
print(list_x)

# Consider the list A = [1, 2, 2, 1] and set B = set([1, 2, 2, 1]), does sum(A) = sum(B)
A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
print(A == B)
print("the sum of A is:", sum(A))
print("the sum of B is:", sum(B))

# Create a new set album_set3 that is the union of album_set1 and album_set2:
# Write your code below and press Shift+Enter to execute
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set(["AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)
print(album_set3)

# Find out if album_set1 is a subset of album_set3:
print(album_set1.issubset(album_set3))
