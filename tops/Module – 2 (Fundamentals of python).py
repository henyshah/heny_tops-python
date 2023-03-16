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
# def fibonacci_series(range_num):
#     a, b = 0, 1
#     fib_series = []
#     while b <= range_num:
#         fib_series.append(b)
#         a, b = b, a + b
#     return fib_series


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
# def check_integer_values(a, b):
#     if a == b or abs(a - b) == 5 or a + b == 5:
#         return True
#     else:
#         return False


# Write a python program to sum of the first n positive integers.
# n = int(input("Input a number: "))
# sum = (n * (n + 1)) / 2
# print("sum: ",sum)


#  Write a Python program to calculate the length of a string
# string = input("Enter a string: ")
# length = len(string)
# print("length:", length)


# Write a Python program to count the number of characters (character frequency) in a string
# string = input("Enter a string: ")
# frequency = {}
# for character in string:
#     if character in frequency:
#         frequency[character] += 1
#     else:
#         frequency[character] = 1
# print("Character frequency:")
# for character, count in frequency.items():
#     print(f"{character}: {count}")


# What are negative indexes and why are they used?
# The negative indexing is the act of indexing from the end of the list with indexing starting at -1 i.e. -1 gives the last element of list, -2 gives the second last element of list and so on.
# Negative Indexing is used in Python to begin slicing from the end of the string i.e. the last. Slicing gets a sub-string from a string. The slicing range is set as parameters i.e. start, stop and step.


# Write a Python program to count occurrences of a substring in a string.
# string = input("Enter a string: ")
# substring = input("Enter a substring: ")
# count = string.count(substring)
# print(f"The substring '{substring}'occurs {count} times in the string.")


# Write a Python program to count the occurrences of each word in a given sentence
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# frequency = {}
# for word in words:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1
# print("Word frequency:")
# for word, count in frequency.items():
#     print(f"{word}: {count}")


# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")
# new_string1 = string2[:2] + string1[2:]
# new_string2 = string1[:2] + string2[2:]
# result = new_string1 + " " + new_string2
# print("Result:", result)


# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.
# string = input("Enter a string: ")
# if len(string) >= 3:
#     if string[-3:] == 'ing':
#         string += 'ly'
#     else:
#         string += 'ing'
# print("Result:", string)


# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# string = input("Enter a string: ")
# not_index = string.find('not')
# poor_index = string.find('poor')
# if poor_index > not_index and not_index != -1 and poor_index != -1:
#     string = string[:not_index] + 'good' + string[poor_index+4:]
# print("Result:", string)


# Write a Python function that takes a list of words and returns the length of the longest one.
# def longest_word_length(words):
#     max_length = 0
#     for word in words:
#         if len(word) > max_length:
#             max_length = len(word)
#     return max_length
# words = ['apple', 'banana', 'cherry', 'strawberry']
# longest_length = longest_word_length(words)
# print("The length of the longest word is:", longest_length)


# Write a Python function to reverses a string if its length is a multiple of 4.
# def reverse_string_if_length_multiple_of_4(input_string):
#     if len(input_string) % 4 == 0:
#         return input_string[::-1]
#     else:
#         return input_string
# input_string = "Python"
# new_string = reverse_string_if_length_multiple_of_4(input_string)
# print(new_string)


# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
# def get_string(string):
#     if len(string) < 2:
#         return ''
#     else:
#         return string[:2] + string[-2:]
# print(get_string('Hello World'))
# print(get_string('Hi'))  
# print(get_string('A')) 


# Write a Python function to insert a string in the middle of a string.
# def insert_string_middle(original_string, string_to_insert):
#     """Inserts a string into the middle of another string."""
#     middle_index = len(original_string) // 2
#     return original_string[:middle_index] + string_to_insert + original_string[middle_index:]
# original_string = "Hello world"
# string_to_insert = "beautiful "
# new_string = insert_string_middle(original_string, string_to_insert)
# print(new_string)
