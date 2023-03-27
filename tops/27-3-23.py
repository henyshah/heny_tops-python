"""
Exception:which disturbs the normal flow of the program.
       exception which is handled by try and except block it is called exception handling.

       syntax:
       try:
           exception code
       except:
            statement
        else:
            without exception
        finally:
            it always occurs
"""

# without exception handlig code 
# print(a)  # this is an exception handling as a variable is not declared.
 

# exception handling code
# try:
#     print(a)
# except:
#     print("variable declaration not done")


# try:
# # accept nos. from users
#     n1=int(input("enter no. 1: "))
#     n2=int(input("enter no. 2: "))
# # calculation
#     ans=n1/n2
# # display output 
#     print(ans)
# except ValueError:
#     print("invalid input-only 0-9 required")
# except ZeroDivisionError:
#     print("cannot be divided by zero")
# except:
#     print("invalid input")


# try:
# # variable definition
#     a=10
#     b=20
#     ans=a+b
#     print(ans)
# except:
#     print("invalid input")
# else:
#     print("Welcome to math world")
#     # it always execute exception occurs or not
# finally:
#     print("THANK YOU FOR USING THIS APPLICATION")


# # list define
# l1=[10,20,30,40,50]
# # display list
# print(l1)
# try:
# # access specific element from the list
#     print(l1[9])
# except:
#     print("list index out of bound")
# else:
#     # display list
#     print(l1)


# try:
#     print(a)
# except Exception as e:
#     print(e)


# # import sys module
# import sys
# # exception handling block
# try:
#     print(a)
# except:
#     print("subject= ",sys.exc_info()[0])
#     print("message= ",sys.exc_info()[1])