"""
list and tuple:
both are collection datatypes.
list: list is a mutable data type which contain data members in single location.
it contains similar and dis-similar data elements at one location.
list is represented by []
list is indexable, orderable, mutable(change)

tuple:tuple is a collection data type.
tuple is indexable, orderable.
tuple is an immutable
tuple is represented by ()

"""
# t=(10,20,30)
# print(type(t))
# print(t)

# t=("python",)
# print(t)
# print(type(t))

# t=("python","java","android","flutter","react")
# print(t)
# for item in t:
#     print(item)

# t=("python","java","android","flutter","react")
# print(t)
# for item in t:
#     print(item,end=",")


# t=("python","java","android","flutter","react")
# print(t)
# print(len(t))


# t=("android","java","C","java","php")
# print(t.count("java"))

t=("android","java","C","java","php")
l1=list(t)       
l1[0]="flutter"
t=tuple(l1)
print(t)



# random

# import random
# n=random.randint(1,100)
# print(n)
# l1=["python","java","android","php"]
# print(random.choice(l1))