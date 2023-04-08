"""
abstraction: to abstract something 
    to hide implementation
for abstraction we have to import ABC class
abstract class which contains one or more abstract methods is abstract class
meaning of abstract method: it represents only few information but does not allocate background information

syntax:
from abc import ABC
# ABC:Abstract Base Class

polymorphism: one class derives the property of others
poly means may and morphism means forms
it can override methods 
2 types:
1)method overloading : one class have same name and methood property but different arguments
2)method overriding : one or two class have same name prporties

note: python does not support method overloading
"""

# from abc import ABC,abstractmethod
# # inherit ABC- Abstract Base Class
# class RBI(ABC):
#     def roi(self):
#         pass
# # child class
# class SBI(RBI):
#     def roi(self):
#         return 8.5 
# class BOI(RBI):
#     def roi(self):
#         return 6.5 
# obj=SBI()
# print(obj.roi())
# boi=BOI()
# print(boi.roi())


from abc import ABC,abstractmethod
# inherit ABC- Abstract Base Class
class vehicle(ABC):
    def wheels(self):
        pass
    def color(self):
        pass
# child class
class car(vehicle):
    def wheels(self):
        return 12
    def color(self):
        return "red"
    
class bike(vehicle):
    def wheels(self):
        return 10
    def color(self):
        return "blue"
    
class truck(vehicle):
    def wheels(self):
        return 14
    def color(self):
        return "black"
    
obj=car()
print(obj.wheels())
print(obj.color())

Bike=bike()
print(Bike.wheels())
print(Bike.color())

Truck=truck()
print(Truck.wheels())
print(Truck.color())


