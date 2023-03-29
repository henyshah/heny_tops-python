# # wwite a python program it is even or odd
# # accept no. from the user
# n=int(input("enter no. : "))

# # check condition
# if n%2==0:
#     # output
#     print("even")
# else:
#     print("odd")


# # user defined exception
# # create class which inheriate exception
# # user defined exception
# class OddExxception(Exception):
#     pass
# # main program execution
# # accept no. from the user
# n=int(input("enter no. : "))
# try:
#     # check condition
#     if n%2==0:
#         print("even")
#     else:
#         # raise exception
#         raise OddExxception
# except OddExxception:
#     print("we can't accept odd nos.")


# # accept nos. from the user raise exception if user enter below zero value
# # create class which inheriate exception
# # user defined exception
# class PositiveExxception(Exception):
#     pass
# # main program execution
# # accept no. from the user
# n=int(input("enter no. : "))
# try:
#     # check condition
#     if n>0:
#         print("positive")
#     else:
#         # raise exception
#         raise PositiveExxception
# except PositiveExxception:
#     print("we can't accept negative nos.")


"""
OOPS: object oriented programming system

class: classs is a collection data type which contains data member function in a single entity.

syntax:
problem 
def addstudent: 
   pass
def add faculty:
   pass
def viewstudent:
   pass
"""

# # class creation
# class student:
#     # data members in class (variables)
#     name="heny"
#     subject="python"
#     technology="programming"
#     # member function in class 
#     # self:it represents current class properties
#     def display(self):
#         print("name= ",self.name)
#         print("name= ",self.subject)
# # obj creation 
# obj=student()
# obj.display()


# class creation
# class faculty:
#     # data members in class (variables)
#     name="anjali"
#     subject="python"
#     ct="enji"
#     # member function in class 
#     # self:it represents current class properties
#     def display(self):
#         print("name= ",self.name)
#         print("name= ",self.subject)
# # obj creation 
# obj=faculty()
# obj.display()


# # accept two nos. from the user and raise exception one first no. smaller than second
# # create class which inheriate exception
# # user defined exception
# class smallerException(Exception):
#     pass
# # main program execution
# # accept no. from the user
# n1=int(input("enter no.1 : "))
# n2=int(input("enter no.2 : "))
# try:
#     # check condition
#     if n1>n2:
#         print("n2 is greater than n1")
#     else:
#         # raise exception
#         raise smallerException
# except smallerException:
#     print("first number is smaller than second")


"""
we can create, read and write file using python

there are 4 modes in python file handling 

r : read mode
w : write mode
x : create mode
a : append mode

"""
# take one variable which opens file 
# f=open("myfile.txt","r")
# print(f.read())

# with open("myfile.txt","r") as f:
    # print(f.read())    


# # open any file in specific variable 
# f=open("mynewfile.txt","w")      # w- write mode
# # accept value from user
# name=input("enter name: ")
# # using of write() write file
# f.write("\n"+name)
# # close file
# f.close()

# #  open any file in specific variable 
# f=open("mynewfile.txt","a")      # w- append mode
# # accept value from user
# name=input("enter name: ")
# # using of write() write file
# f.write("\n"+name)
# # close file
# f.close()

# create blank file
f=open("blankfile.txt","x")
f.close()