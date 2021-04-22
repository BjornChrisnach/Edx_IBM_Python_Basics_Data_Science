# Download Data

# import urllib.request
# url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
# filename = 'Example1.txt'
# urllib.request.urlretrieve(url, filename)

# Download Example file

#!wget -O /resources/data/Example1.txt https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt

# Read the Example1.txt

example1 = "Example1.txt"
file1 = open(example1, "r")
# Print the path of file
print(file1.name)

# Print the mode of file, either 'r' or 'w'
print(file1.mode)

# Read the file

FileContent = file1.read()
print(FileContent)

# Type of file content
type(FileContent)

file1.close()

# Open file using with
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

# Verify if the file is closed
print(file1.closed)

# Iterate through the lines

with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1

with open(example1, "r") as file1:
    FileasList = file1.readlines()

# Print the first line
print(FileasList[0])
# Print the second line
print(FileasList[1])
# Print the third line
print(FileasList[2])
