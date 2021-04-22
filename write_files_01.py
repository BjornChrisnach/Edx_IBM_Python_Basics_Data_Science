# File1 = open("./examples2.txt," "w")

# with open("./examples2.txt", "w") as File1:

#     File1.write("This is line A\n")
#     File1.write("This is line B\n")

# lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
# with open("./examples2.txt", "w") as File1:
#     for line in lines:
#         File1.write(line)

# with open("Example1.txt", "r") as readfile:
#     with open("Example3.txt", "w") as writefile:
#         for line in readfile:
#             writefile.write(line)

# Write line to file
# exmp2 = './examples2.txt'
# with open(exmp2, 'w') as writefile:
#     writefile.write("This is line A")

# # Read file
# with open(exmp2, 'r') as testwritefile:
#     print(testwritefile.read())

# # Write lines to file
# with open(exmp2, 'w') as writefile:
#     writefile.write("This is line A\n")
#     writefile.write("This is line B\n")

# # Check whether write to file
# with open(exmp2, 'r') as testwritefile:
#     print(testwritefile.read())

# # Sample list of text

# Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
# # Write the strings in the list to text file

# with open('c', 'w') as writefile:
#     for line in Lines:
#         print(line)
#         writefile.write(line)

# # Verify if writing to file is successfully executed
# with open('examples2.txt', 'r') as testwritefile:
#     print(testwritefile.read())

# with open('examples2.txt', 'w') as writefile:
#     writefile.write("Overwrite\n")
# with open('examples2.txt', 'r') as testwritefile:
#     print(testwritefile.read())

# # Write a new line to text file

# with open('examples2.txt', 'a') as testwritefile:
#     testwritefile.write("This is line C\n")
#     testwritefile.write("This is line D\n")
#     testwritefile.write("This is line E\n")

# # Verify if the new line is in the text file
# with open('examples2.txt', 'r') as testwritefile:
#     print(testwritefile.read())

# with open('examples2.txt', 'a+') as testwritefile:
#     testwritefile.write("This is line E\n")
#     print(testwritefile.read())

with open('examples2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )


with open('examples2.txt', 'r+') as testwritefile:
    data = testwritefile.readlines()
    testwritefile.seek(0,0) #write at beginning of file
   
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    #testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())

# Let's copy the file <b>Example2.txt</b> to the file <b>Example3.txt</b>:
# Copy file to another
with open('examples2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)


# Verify if the copy is successfully executed
with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())