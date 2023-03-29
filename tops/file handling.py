# What is File function in python? What is keywords to create and write file
# ANS. Python file object provides methods and attributes to access and manipulate files. Using file objects, we can read or write any files. Whenever we open a file to perform any operations on it, Python returns a file object.
# we can create, read and write file using python
# there are 4 modes in python file handling 
# r : read mode
# w : write mode
# x : create mode
# a : append mode

# Write a Python program to read an entire text file
# ANS.# take one variable which opens file 
f=open("myfile.txt","r")
print(f.read())

# Write a Python program to append text to a file and display the text. 
# ANS.open any file in specific variable 
f=open("mynewfile.txt","a")      # w- append mode
# accept value from user
name=input("enter name: ")
# using of write() write file
f.write("\n"+name)
# close file
f.close()

# Write a Python program to read first n lines of a file.
# accept line from the user
n = int(input("\n\t\tEnter Lines To Read : "))
# open any file in specific variable 
f = open("myfile.txt","r")
# use for loop
for i in range(n):
	# read line
	print(f.readline())

# Write a Python program to read last n lines of a file.
# accept line from the user
n = int(input("\n\t\tEnter Lines To Read : "))
# open any file in specific variable 
f = open("myfile.txt","r")
# use for loop
for i in range(n):
	# read line
	print(f.readline())
