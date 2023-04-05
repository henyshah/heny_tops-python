# Module – 4 (Advance python programming)

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

# Write a Python program to read last n lines of a file. 


# Write a Python program to read a file line by line and store it into a list


# Write a Python program to read a file line by line store it into a variable. 


# Write a python program to find the longest words. 


# Write a Python program to count the number of lines in a text file. 


# Write a Python program to count the frequency of words in a file. 


# Write a Python program to write a list to a file. 


# Write a Python program to copy the contents of a file to another file.


# Explain Exception handling? What is an Error in Python?
# ANS. Exception:which disturbs the normal flow of the program.Exception which is handled by try and except block it is called exception handling.
# Errors are problems that occur in the program due to an illegal operation performed by the user or by the fault of a programmer, which halts the normal flow of the program. Errors are also termed bugs or faults


# How many except statements can a try-except block have? Name Some built-in exception classes: 
# ANS. There has to be at least one except statement.
# for example:
# ZeroDivisionError
# ValueError
# KeyError
# IndexError
# TypeError etc.....


# When will the else part of try-except-else be executed? 
# ANS. when no exception occurs.
# else:
    # without exception


# Can one block of except statements handle multiple exception? 
# ANS. YES


# When is the finally block executed?
# ANS. it always execute whether exception occurs or not.
# finally:
        # it always occurs


# What happens when „1‟== 1 is executed? 
# ANS.  it simply evaluates to false and does not raise any exception.


# How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets
# ANS. 
"""
try:
        exception code
    except:
            statement
    else:
            without exception
    finally:
            it always occurs
    """
# example:
try:
# variable definition
    a=10
    b=20
    ans=a+b
    print(ans)
except:
    print("invalid input")
else:
    print("Welcome to math world")
    # it always execute exception occurs or not
finally:
    print("THANK YOU FOR USING THIS APPLICATION")


# Write python program that user to enter only odd numbers, else will raise an exception. 
while True:
    try:
        num = int(input("enter an odd number: "))
        if num % 2 == 0:
            raise ValueError("Even numbers are not allowed.")
        break
    except ValueError as e:
        print(e)


# accept nos. from the user raise exception if user enter below zero value
# create class which inheriate exception
# user defined exception
class NegativeException(Exception):
    pass
# main program execution
# accept no. from the user
n=int(input("enter no. : "))
try:
    # check condition
    if n>0:
        print("positive")
    else:
        # raise exception
        raise NegativeException
except NegativeException:
    print("we can't accept negative nos.")


# accept two nos. from the user and raise exception one first no. smaller than second
# create class which inheriate exception
# user defined exception
class smallerException(Exception):
    pass
# main program execution
# accept no. from the user
n1=int(input("enter no.1 : "))
n2=int(input("enter no.2 : "))
try:
    # check condition
    if n1>n2:
        print("n1 is greater than n2")
    else:
        # raise exception
        raise smallerException
except smallerException:
    print("first number is smaller than second")


# What are oops concepts? Is multiple inheritance supported in java 
# ANS.oops: object oriented programming system
# · Object 
# · Class 
# · Inheritance 
# · Polymorphism 
# · Abstraction 
# · Encapsulation.
# NO, Java does not support Multiple Inheritance; however, Java interfaces help us achieve Multiple Inheritance of type in Java.


# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class 
# ANS.class: it contains data member and member function in single entity it is called class.
# syntax:     
    #  class <classname>:
    #  data member
    #  member function
# self represents current class properties
# create class of person
class person:
    # method
    def display(self):         #self represents current class properties 
        print("this is person method")
        # obj creation of person class
obj=person()
obj.display()


# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle 


# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle 


# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle 


# Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python? 


# What is Instantiation in terms of OOP terminology?
# ANS.The processes of creating a new object for a class using a new keyword. 


# What is used to check whether an object o is an instance of class A? 


# What relationship is appropriate for Course and Faculty? 


# What relationship is appropriate for Student and Person?