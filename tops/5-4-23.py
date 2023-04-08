"""
inheritance: one class derives properties of another class
 it provides reusabilities 
 by using of inheritance we can reduce our code

 types:
 1)single level inheritance
 2)multi level inheritance
 3)multiple inheritance
 4)heierarchical inheritance
 5)hybrid inheritance
 """

# single level inheritance
# class parent:
#     def home(self):
#         print("Ahmedabad")
# class Child(parent):    #ineritance
#     def car(self):
#         print("I HAVE CAR")
#         # obj declaration
# obj = Child()
# obj.home()
# obj.car()


# multi level inheritance
# class grantparent:
#     def land(self):
#         print("LAND IN GUJARAT")
# class parent(grantparent):
#     def house(self):
#         print("HOME IN AHMEDABAD")
# class child(parent):
#     def car(self):
#         print("PURCHASES OWN CAR")
# obj=child()
# obj.land()
# obj.house()
# obj.car()


# multiple inheritance
"""
A             B
|             |
---------------
       |
       v
       C
"""
# parent class
# class A:
#     def displayA(self):
#         self.num1=10
# # parent class
# class B:
#     def displayB(self):
#         self.num2=20
# # multiple inheritance
# class C(A,B):
#     def displayRes(self):
#         ans=self.num1+self.num2
#         print("num1= ",self.num1)
#         print("num1= ",self.num2)
#         print("ans= ",ans)
# obj=C()
# obj.displayA()
# obj.displayB()
# obj.displayRes()


# heierarchical inheritance
"""
       A
       |
---------------
B             C       
"""
# parent class
# class parent:
#     def home(self):
#         print("Ahmedabad")
# class Child1(parent):    #ineritance
#     def car(self):
#         print("I HAVE CAR")
#         # obj declaration
# class Child2(parent):    #ineritance
#     def bike(self):
#         print("I HAVE BIKE")
#           # obj declaration
# obj1 = Child1()
# obj2= Child2()
# obj1.home()
# obj1.car()
# obj2.home()
# obj2.bike()


# 5)hybrid heritance
"""
       A
       |
---------------
B             C 
---------------
       |
       D
"""
# parent class
class parent:
    def home(self):
        print("Ahmedabad")
class Child1(parent):    #ineritance
    def car(self):
        print("I HAVE CAR")
        # obj declaration
class Child2(parent):    #ineritance
    def bike(self):
        print("I HAVE BIKE")
class Child3(Child1,Child2):    #ineritance
    def bike(self):
        print("WOOHOO")
          # obj declaration
obj = Child3()
obj.home()
obj.car()
