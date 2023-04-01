"""
oops: object oriented programming system
class: it contains data member and member function in single entity it is called class.
syntax:     
     class <classname>:
     data member
     member function

object: object is a variable or instance of class.
syntax:
     obj=classname()
"""

# # create class of person
# class person:
#     # method
#     def display(self):         #self represents current class properties 
#         print("this is person method")
#         # obj creation of person class
# obj=person()
# obj.display()


# # class creation
# class Student:
#     # dictionary = we use as a database
#     db = {}
#     # input method = which accept value from student user
#     def input(self):
#         username = input("Enter name : ")
#         email = input("Enter email : ")
#         password = input("Enter password : ")
#         # storing data in db
#         # here email is key and password is value
#         # e.g.- a@gmail.com : 123456
#         self.db[email] = password       
#     def display(self):
#         # display all students
#         for k in self.db.keys():
#             print("email = ",k)
# # object creation of student class
# s1 = Student()
# status = True
# while status:
#     s1.input()
#     choice = input("Do you want to add more students: ")
#     if choice=='n':
#         status = False
# s1.display()


# # class creation
# class Faculty:
#     # dictionary = we use as a database
#     db = {}
#     # input method = which accept value from student user
#     def input(self):
#         username = input("Enter name : ")
#         email = input("Enter email : ")
#         password = input("Enter password : ")
#         # storing data in db
#         # here email is key and password is value
#         # e.g.- a@gmail.com : 123456
#         self.db[email] = password   
#     def display(self):
#         # display all students
#         for k in self.db.keys():
#             print("email = ",k)
# # object creation of student class
# s1 = Faculty()
# status = True
# while status:
#     s1.input()
#     choice = input("Do you want to add more students: ")
#     if choice=='n':
#         status = False
# s1.display()


# class creation
class Student:
    # dictionary = we use as a database
    db = {}

    # input method = which accept value from student user
    def input(self):
        username = input("Enter name : ")
        email = input("Enter email : ")
        password = input("Enter password : ")
        # storing data in db
        # here email is key and password is value
        # e.g.- a@gmail.com : 123456
        self.db[email] = password
       
    def display(self):
        # display all students
        for k in self.db.keys():
            print("email = ",k)

# # object creation of student class
# s1 = Student()
# status = True
# while status:
#     s1.input()
#     choice = input("Do you want to add more students: ")
#     if choice=='n':
#         status = False
# s1.display()

s1 = Student()
status = True
while status:
    # Menu
    data = """
                press 1 for student registration
                press 2 for Faculty registration
                press 3 to view all student
                press 4 for exit
            """
    print(data)
    user_input = int(input("Enter your choice: "))
    if user_input == 1:
        s1.input()
    elif user_input == 2:
        # faculty input
        print("==> Faculty input")
    elif user_input == 3:
        # student display
        print("==> Student display")
        s1.display()
    else:
        status = False
    choice = input("Do you want to add more students: ")
    if choice=='n':
        status = False
