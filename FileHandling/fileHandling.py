# File Handling Modes
# Ref: https://www.geeksforgeeks.org/reading-writing-text-files-python/

import os
current_path = os.path.dirname(os.path.abspath(__file__))
print(os.path.abspath(__file__))
print(current_path)

# a file named "geek", will be opened with the reading mode.
file = open(f"{current_path}/test.txt", 'r')
# This will print every line one by one in the file
for line in file:
	print (line)


# Python code to illustrate read() mode
file = open(f"{current_path}/test.txt", 'r')
print (file.read())


# Python code to illustrate read() mode character wise
file = open(f"{current_path}/test.txt", 'r')
print (file.read(5))

# Python code to create a file
file = open(f"{current_path}/geek.txt",'w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()


# Python code to illustrate append() mode
file = open(f"{current_path}/geek.txt",'a')
file.write("This will add this line")
file.close()


with open(f"{current_path}/file.txt", "w") as f:
    f.write("Hello World!!!")