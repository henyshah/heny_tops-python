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
