# Import required library

import pandas as pd

# Read data from CSV file
csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)

# Print first five rows of the dataframe
df.head()

# Read data from Excel File and print the first five rows
xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

df = pd.read_excel(xlsx_path)
df.head()

# Access to the column Length
x = df[['Length']]
print(x)

# Get the column as a series
x = df['Length']
print(x)

# Get the column as a dataframe
x = type(df[['Artist']])
print(x)

# Access to multiple columns
y = df[['Artist','Length','Genre']]
print(y)

# Access the value on the first row and the first column
print(df.iloc[0, 0])

# Access the value on the second row and the first column
print(df.iloc[1,0])

# Access the value on the first row and the third column
print(df.iloc[0,2])

# Access the value on the second row and the third column
print(df.iloc[1,2])

# Access the column using the name
print(df.loc[0, 'Artist'])

# Access the column using the name
print(df.loc[1, 'Artist'])

# Access the column using the name
print(df.loc[0, 'Released'])

# Access the column using the name
print(df.loc[1, 'Released'])

# Slicing the dataframe
print(df.iloc[0:2, 0:3])

# Slicing the dataframe using name
print(df.loc[0:2, 'Artist':'Released'])

# Quiz

# Use a variable q to store the column Rating as a dataframe
q = df[['Rating']]
print(q)

# Assign the variable q to the dataframe that is made up of the column Released and Artist:
q = df[['Released', 'Artist']]
print(q)

# Access the 2nd row and the 3rd column of df:
print(df.iloc[1, 2])

# Use the following list to convert the dataframe index df to characters and assign it to df_new;
# find the element corresponding to the row index a and column 'Artist'. Then select the rows a through
# d for the column 'Artist'
new_index=['a','b','c','d','e','f','g','h']

df_new=df
df_new.index=new_index
print(df_new.loc['a', 'Artist'])
print(df_new.loc['a':'d', 'Artist'])