# function:function is a block of code that code is used again and again.
# using function we can reduce ou function provide reusabilities.
# in python there are 2 steps to implement:
# (1)fuction definition
# (2)function calling


# def myfun():
#     print("hello")
#     print("welcome to python")
# myfun()
# myfun()
# myfun()


# def greetings():
#     msg=input("enter your msg: ")
#     print(msg)
# greetings()


# def add():
#     num1=int(input("enter number 1: "))
#     num2=int(input("enter number 2: "))
#     ans=num1+num2
#     print(ans)
# def mul():
#     num1=int(input("enter number 1: "))
#     num2=int(input("enter number 2: "))
#     ans=num1*num2
#     print(ans)
# def menu():
#     data="""
#  MENU
#  press 1 for addition 
#  press 2 for multiplication   
#     """
#     print(data)
#     choice=int(input("enter your choice: "))
#     if choice==1:
#         add()
#     elif choice==2:
#         mul()
# menu()


# function categories:
# there are 4 types of categories:
# (1)function without parameters and function without return types
# (2)fuction with parameters and fuction without return types
# (3)function without parametrs and function with return types
# (4)function with parameter and function with return types


# write a program which accepts value from user and check entered no. is even or odd and entered number is positive or negative.
# def even_odd():
#     n=int(input("enter number: "))
#     if (n%2==0):
#         print("even")
#     else:
#         print("odd")  
# def pos_neg():
#     n=int(input("enter number: "))
#     if (n>0):
#         print("positive")
#     else:
#         print("negative")      
# even_odd()
# pos_neg()


# function with parameter and function with return type 
# def myfun(num1,num2):
#     print(num1)                       
#     print (num2)
# myfun(10,20)


# swapping
# def swap(num1,num2):
#     print(num1)
#     print(num2)
#     num1,num2=num2,num1
#     print(num1)
#     print(num2)
# swap(100,200)



# extra task jay bhavani
def show_menu(menu):
    print("Menu:")
    for k, v in menu.items():
        print(f"{k} Rs. {v}")

def create_cart(menu):
    cart = {}
    status = True
    while status:
        product_name = str(input("Enter product: "))
        qty = int(input("Enter number of qty: "))
        price = qty * menu[product_name]
        cart[product_name] = price
        choice = input("Do you want to purchase more products? Press y for yes and n for no")
        if choice == 'n' or choice=='N':
            status = False
            break
    return cart

jay_bhavani = {
    "vadapav": 30,
    "dabeli": 20,
    "bhel": 70,
}

show_menu(jay_bhavani)
cart = create_cart(jay_bhavani)
print("Cart:", cart)
