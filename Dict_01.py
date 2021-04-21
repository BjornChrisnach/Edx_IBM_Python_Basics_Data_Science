# Create the dictionary
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}

# The keys can be strings:
print(Dict["key1"])

# Keys can also be any immutable object such as a tuple:
print(Dict[(0, 1)])

# Create a sample dictionary
release_year_dict = {"Thriller": "1982", "Back in Black": "1980",
                     "The Dark Side of the Moon": "1973", "The Bodyguard": "1992",
                     "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976",
                     "Saturday Night Fever": "1977", "Rumours": "1977"}

# You can retrieve the values based on the names:
print(release_year_dict["Thriller"])
print(release_year_dict['The Bodyguard'])

# Get all the keys in dictionary
# new_list = []
new_list_keys = release_year_dict.keys()
print(new_list_keys)
# Get all the values in dictionary
new_list_values = release_year_dict.values()
print(new_list_values)

# Append value with key into dictionary
release_year_dict["Graduation"] = 2007
new_list_keys = release_year_dict.keys()
print(new_list_keys)
new_list_values = release_year_dict.values()
print(new_list_values)

# Delete entries by key
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
new_list_keys = release_year_dict.keys()
print(new_list_keys)
new_list_values = release_year_dict.values()
print(new_list_values)

# Verify the key is in the dictionary
print('The Bodyguard' in release_year_dict)

# Question sample dictionary
soundtrack_dic = {"The Bodyguard": "1992", "Saturday Night Fever": "1977"}

# In the dictionary soundtrack_dic what are the keys ?
print(soundtrack_dic.keys())  # "The Bodyguard", "Saturday Night Fever"

# In the dictionary <code>soundtrack_dic</code> what are the values ?
print(soundtrack_dic.values())  # "1992", "1977"

# Create a dictionary album_sales_dict where the keys are the album name and the sales
# in millions are the values. The Albums Back in Black, The Bodyguard and Thriller have the
# following music recording sales in millions 50, 50 and 65 respectively:
album_sales_dict = {"Back in Black": 50, "The Bodyguard": 50, "Thriller": 65}

# Use the dictionary to find the total sales of Thriller:
print(album_sales_dict["Thriller"])

# Find the names of the albums from the dictionary using the method keys():
print(album_sales_dict.keys())

# Find the values of the recording sales from the dictionary using the method values:
print(album_sales_dict.values())
