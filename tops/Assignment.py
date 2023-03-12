# Python Assignment
# Module – 1 (SDLC)

# What is Software?
# ANS. Software is a a set of instructions, data or programs used to operate computers and execute specific tasks.

# What are the types of Applications?
# ANS. 1. Web Development
#      2. Machine Learning and Artificial Intelligence
#      3. Data Science
#      4. Game Development
#      5. Audio and Visual Applications
#      6. Software Development
#      7. CAD Applications
#      8. Business Applications
#      9. Desktop GUI
#      10. Web Scraping Application

# What is programing?
# ANS. Programming is the process or activity of writing computer programs.

# What is Python?
# ANS. Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis.


# Module – 2 (Fundamentals of python)

# Write a Python program to check if a number is positive, negative or zero.
# n=int(input("enter number: "))
# if n>0:
#     print("\npositive number")
# elif n==0:
#     print("\nzero")
# else:
#     print("\nnegative number")

# Write a Python program to get the Factorial number of given number.
# import math 
# def factorial(n):
#     return(math.factorial(n))
# num = 5
# print("Factorial of", num, "is",
#       factorial(num))

# Write a Python program to get the Fibonacci series of given range.

# How memory is managed in Python?
# ANS. Python uses a portion of the memory for internal use and non-object memory.Another part of the memory is used for Python object such as int, dict, list, etc.

# What is the purpose continue statement in python?
# ANS. The continue statement is used to end the current iteration in a for loop or a while loop, and continues to the next iteration.

# Write python program that swap two number with temp variable and without temp variable.
# x = 5
# y = 10
# temp = x
# x = y
# y = temp
# print('The value of x after swapping: {}'.format(x))
# print('The value of y after swapping: {}'.format(y))

# Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.
# n = int(input("Enter number : "))
# if (n%2)==0:
#     print("\nIt is even")
# else: 
#     print("\nIt is odd")

# Write a Python program to test whether a passed letter is a vowel or not.
# l = input("Enter alphabet: ")
# if l in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
# 	print("%s is a vowel." % l)
# else:
# 	print("%s is a consonant." % l) 

# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
# def sum_three(x, y, z):
#     if x == y or y == z or x==z:
#         sum = 0
#     else:
#         sum = x + y + z
#     return sum
# print(sum_three(1, 2, 3))

# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5

# Write a python program to sum of the first n positive integers.
# n = int(input("Input a number: "))
# sum = (n * (n + 1)) / 2
# print("sum: ",sum)

#  Write a Python program to calculate the length of a string
# string = input("Enter a string: ")
# length = len(string)
# print("length:", length)