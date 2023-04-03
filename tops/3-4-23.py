"""
encapsulation:it wraps data in single entity
it protects the data from outside of the class

getter and setter method 
getter method to get data and setter method to set data
"""

# class student:
#     # setter method 
#     def setId(self,id):
#         self.id=id
#     # getter method 
#     def getId(self):
#         return self.id
#     def setName(self,name):
#         self.name=name
#     def getName(self):
#         return self.name
# obj=student()
# # set data
# id=int(input("enter id : "))
# obj.setId(id)
# # get id using getter method 
# print(obj.getId())
# # set name - using setter
# name=input("enter name: ")
# obj.setName(name)
# # get data
# print(obj.getName())


# class faculty:
#     # setter method 
#     def setId(self,id):
#         self.id=id
#     # getter method 
#     def getId(self):
#         return self.id
#     def setName(self,name):
#         self.name=name
#     def getName(self):
#         return self.name
#     def setTechnology(self,technology):
#         self.technology=technology
#     def getTechnology(self):
#         return self.technology
# obj=faculty()
# # set data
# id=int(input("enter id : "))
# obj.setId(id)
# # get id using getter method 
# print(obj.getId())
# # set name - using setter
# name=input("enter name: ")
# obj.setName(name)
# # get data
# print(obj.getName())
# technology=input("enter technology: ")
# obj.setTechnology(technology)
# print(obj.getTechnology())


# # private mode: access modifier (visibility mode) which is accessible within the class
# # product name class
# class product:
#     # constructor
#     def __init__(self):
#         self.__mobile=15000   # private 
#         self.laptop=25000
#     # display method
#     def display(self):
#         print("mobile",self.__mobile)
#         print("laptop",self.laptop)
#     # object
# obj=product()
# obj.display()
# # change mobile and laptop price
# obj.__mobile=15000   
# obj.laptop=35000
# obj.display()


# private mode: access modifier (visibility mode) which is accessible within the class
# product name class
class product:
    # constructor
    def __init__(self):
        self.__mobile=15000   # private 
        self.laptop=25000
    # display method
    def display(self):
        print("mobile",self.__mobile)
        print("laptop",self.laptop)
        # data change using method
    def changeData(self,mobileNewPrice):
        self.__mobile=mobileNewPrice
    # object
obj=product()
obj.display()
# change mobile and laptop price
obj.__mobile=18000   
obj.laptop=35000
obj.display()
print("change data using method")
# change method
obj.changeData(19000)
obj.display()