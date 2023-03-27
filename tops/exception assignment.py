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
