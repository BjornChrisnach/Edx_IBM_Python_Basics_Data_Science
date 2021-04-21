a_set = {"AC/DC", "Back in Black", "Thriller"}
a_set.add("NSYNC")
print(a_set)

a_set.remove("NSYNC")
print(a_set)

print("NSYNC" in a_set)
print("AC/DC" in a_set)

album_set_1 = {"AC/DC", "Back in Black", "Thriller"}
album_set_2 = {"AC/DC", "Back in Black", "The Dark Side of the Moon"}
album_set_3 = album_set_1 & album_set_2
print(album_set_3)
album_set_4 = album_set_1.union(album_set_2)
print(album_set_4)

print(album_set_3.issubset(album_set_1))
