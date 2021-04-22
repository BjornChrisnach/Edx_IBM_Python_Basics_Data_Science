# File1 = open("/resources/data/examples2.txt", "r")
# File1 = open("./examples2.txt", "r")
# print(File1.name)
# print(File1.mode)
# File1.close()

with open("examples2.txt", "r") as File1:
    # file_stuff = File1.readlines()
    # print(file_stuff)

    # file_stuff = File1.readline()
    # print(file_stuff)
    # file_stuff = File1.readline()
    # print(file_stuff)

    # for line in File1:
    #     print(line)

    file_stuff = File1.readline(16)
    print(file_stuff)
    file_stuff = File1.readline(5)
    print(file_stuff)
    file_stuff = File1.readline(9)
    print(file_stuff)

print(File1.closed)
# print(file_stuff)
