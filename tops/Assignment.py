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


# Module – 3 (Collections, functions and Modules)

# What is List? How will you reverse a list?
# Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.A built-in function called reverse() is used to reverse the list. 


# How will you remove last object from a list? Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?
# By using pop
# list1 = [1,2,3,4,5]
# list1.pop(-1)
# print(list1)  


# Differentiate between append () and extend () methods? 
# append() method adds a single element to the end of the list, while extend() method adds multiple elements to the end of the list.
# append() method modifies the original list by adding the new element as a single item, while extend() method modifies the original list by adding each element of the iterable as individual items to the end of the list.
# l1= [1, 2, 3]
# l2 = [4, 5, 6]
# l1.append(l2)
# print(l1)  
# l1.extend(l2)
# print(l1)  


# Write a Python function to get the largest number, smallest num and sum of all from a list.
# def list(input_list):
#     if len(input_list) == 0:
#         return None, None, None
#     else:
#         max_num = max(input_list)
#         min_num = min(input_list)
#         total_sum = sum(input_list)
#         return max_num, min_num, total_sum
# input_list = [22,33,44,55,66]
# max_num, min_num, total_sum = list(input_list)
# print("Max number:", max_num)  
# print("Min number:", min_num)  
# print("Total sum:", total_sum) 


# How will you compare two lists?
# by == operator
# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# list3 = [3, 2, 1]
# print(list1 == list2) 
# print(list1 == list3)


# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
# def count_strings(list_of_strings):
#     count = 0
#     for string in list_of_strings:
#         if len(string) >= 2 and string[0] == string[-1]:
#             count += 1
#     return count
# list_of_strings = ['python', 'programming', 'hello', 'madam', 'world', 'list']
# count = count_strings(list_of_strings)
# print(count)  


# Write a Python program to remove duplicates from a list.
# def remove_duplicates(lst):
#     return list(set(lst))
# lst = [1, 2, 3, 2, 4, 5, 1, 3]
# new_list = remove_duplicates(lst)
# print(new_list)  


# Write a Python program to check a list is empty or not.
# def is_list_empty(lst):
#     if not lst:
#         return True
#     else:
#         return False
# lst1 = []
# lst2 = [1, 2, 3]
# print(is_list_empty(lst1))  
# print(is_list_empty(lst2))  


# Write a Python function that takes two lists and returns true if they have at least one common member.
# def has_common_member(list1, list2):
#     for element in list1:
#         if element in list2:
#             return True
#     return False
# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8,9]
# list3 = [10,11,12,13]
# print(has_common_member(list1, list2))  
# print(has_common_member(list1, list3))  


# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.
# def generate_list():
#     squares_list = [x**2 for x in range(1, 31)]
#     first_five = squares_list[:5]
#     last_five = squares_list[-5:]
#     result_list = first_five + last_five
#     print(result_list)
# generate_list()


# Write a Python function that takes a list and returns a new list with unique elements of the first list. 
# def unique_list(lst):
#     return list(set(lst))
# my_list = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7 , 8, 8, 9, 9, 10]
# print(unique_list(my_list))  


# Write a Python program to convert a list of characters into a string.
# def list_to_string(char_list):
#     string = ''.join(char_list)
#     return string
# my_list = ['H', 'e', 'l', 'l', 'o',' ', 'W', 'o', 'r', 'l', 'd', '!']
# string = list_to_string(my_list)
# print(string)  


#  Write a Python program to select an item randomly from a list. 
# import random
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# random_item = random.choice(list)
# print(random_item)


# Write a Python program to find the second smallest number in a list.
# def second_smallest(lst):
#     smallest = min(lst)
#     new_lst = [x for x in lst if x != smallest]
#     second_smallest = min(new_lst)
#     return second_smallest
# my_list = [1,4,5,6,7,8,9,10]
# second_min = second_smallest(my_list)
# print(second_min) 


# Write a Python program to get unique values from a list 
# def unique_list(lst):
#     return list(set(lst))
# my_list = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7 , 8, 8, 9, 9, 10]
# print(unique_list(my_list))


#  Write a Python program to check whether a list contains a sub list
# def check_sublist(lst, sublist):
#     lst_str = str(lst)
#     sublist_str = str(sublist)
#     if sublist_str in lst_str:
#         return True
#     else:
#         return False
# my_list = [1, 2, 3, 4, 5, [6, 7, 8], 9, 10]
# sub_list = [6, 7, 8]
# contains_sublist = check_sublist(my_list, sub_list)
# print(contains_sublist)  


# Write a Python program to split a list into different variables
# my_list = [1, 2, 3, 4, 5]
# a, b, c, d, e = my_list
# print(a)  
# print(b)  
# print(c)  
# print(d) 
# print(e)  


#  What is tuple? Difference between list and tuple.
# A tuple is a collection of ordered, immutable elements enclosed in parentheses () and separated by commas. Tuples are similar to lists, but they are immutable, which means that once a tuple is created, you cannot modify its elements.
# Lists are mutable, which means you can add, remove, or modify elements after the list has been created. Tuples, on the other hand, are immutable, which means that once a tuple is created, you cannot modify its elements
# Lists are defined using square brackets [], while tuples are defined using parentheses ().
# Example of a list
# my_list = [1, 2, 3, 4, 5]
# Example of a tuple
# my_tuple = (1, 'two', 3.0, [4, 5])


#  Write a Python program to create a tuple with different data types.
# tuple = ('hello', 42, True, [1, 2, 3], {'a': 1, 'b': 2})
# print(tuple)


#  Write a Python program to create a tuple with numbers
# tuple = (1, 2, 3, 4, 5)
# print(tuple)


#  Write a Python program to convert a tuple to a string.
# tuple = ('h', 'e', 'l', 'l', 'o')
# string = ''.join(tuple)
# print(string)


# Write a Python program to check whether an element exists within a tuple. 
# tuple = ('apple', 'banana', 'cherry', 'orange')
# if 'banana' in tuple:
#     print('banana exists in the tuple')
# else:
#     print('banana does not exist in the tuple')


#  Write a Python program to find the length of a tuple.
# tuple = ('1', '2', '3', '4')
# tuple_length = len(tuple)
# print('The length of the tuple is:', tuple_length)


#  Write a Python program to convert a list to a tuple.
# list = ['apple', 'banana', 'cherry', 'orange']
# tuple = tuple(list)
# print('The tuple converted from the list is:',tuple)


# Write a Python program to reverse a tuple.
# tuple = (1, 2, 3, 4, 5)
# reversed_tuple = tuple[::-1]
# print( reversed_tuple)


#  Write a Python program to replace last value of tuples in a list. 
# my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# new_list = []
# for tuple in my_list:
#     new_list.append(tuple[:-1] + (10,))
# print('Original list:', my_list)
# print('New list:', new_list)


#  Write a Python program to find the repeated items of a tuple.
# my_tuple = (1, 2, 3, 2, 4, 5, 3, 6, 2)
# repeated_items = []
# for item in my_tuple:
#     if my_tuple.count(item) > 1 and item not in repeated_items:
#         repeated_items.append(item)
# print('Tuple:', my_tuple)
# print('Repeated items:', repeated_items)


#  Write a Python program to remove an empty tuple(s) from a list of tuples. 
# my_list = [(1, 2), (), (3, 4), (), (5,6), ()]
# new_list = [t for t in my_list if t]
# print("Original list:", my_list)
# print("New list:", new_list)


# Write a Python program to unzip a list of tuples into individual lists.
# my_list = [(1, 'a'), (2, 'b'), (3, 'c')]
# numbers, letters = zip(*my_list)
# print("Original list:", my_list)
# print("Numbers:", numbers)
# print("Letters:", letters)


# Write a Python program to convert a list of tuples into a dictionary.
# list = [("apple", 5), ("banana", 2), ("orange", 7)]
# dict = dict(list)
# print("Original list:", list)
# print("Dictionary:",dict)


#  How will you create a dictionary using tuples in python? 
# To create a dictionary using tuples in Python, you can pass a list of tuples to the dict() constructor function. Each tuple in the list should contain exactly two elements, where the first element is the key and the second element is the value.
# list = [("apple", 5), ("banana", 2), ("orange", 7)]
# dict = dict(list)
# print("Original list:", list)
# print("Dictionary:",dict)


# Write a Python script to sort (ascending and descending) a dictionary by value. 
# my_dict = {"apple": 5, "banana": 2, "orange": 7}
# asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))
# desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
# print("Original dictionary:", my_dict)
# print("Sorted dictionary (ascending):",asc)
# print("Sorted dictionary (descending):",desc)


# Write a Python script to concatenate following dictionaries to create a new one.
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# dict3 = {'e': 5, 'f': 6}
# new_dict = {}
# new_dict.update(dict1)
# new_dict.update(dict2)
# new_dict.update(dict3)
# print("New dictionary:", new_dict)


#  Write a Python script to check if a given key already exists in a dictionary. 
# my_dict = {"apple": 3, "banana": 2, "orange": 4}
# if "apple" in my_dict:
#     print("Key 'apple' already exists in the dictionary.")
# else:
#     print("Key 'apple' does not exist in the dictionary.")
# if "cherry" in my_dict:
#     print("Key 'cherry' already exists in the dictionary.")
# else:
#     print("Key 'cherry' does not exist in the dictionary.")


#  How Do You Traverse Through A Dictionary Object In Python? 
# Using a loop.
# my_dict = {"apple": 1, "banana": 2, "cherry": 3}
# for key in my_dict:
#     print(key, my_dict[key])


#  How Do You Check The Presence Of A Key In A Dictionary?
# Using in operator
# my_dict = {"apple": 3, "banana": 2, "orange": 4}
# if "apple" in my_dict:
#     print("Key 'apple' already exists in the dictionary.")
# else:
#     print("Key 'apple' does not exist in the dictionary.")
# if "cherry" in my_dict:
#     print("Key 'cherry' already exists in the dictionary.")
# else:
#     print("Key 'cherry' does not exist in the dictionary.")


# Write a Python script to print a dictionary where the keys are numbers between 1 and 15.
# my_dict = {}
# for i in range(1, 16):
#     my_dict[i] = i*i
# print(my_dict)


#  Write a Python program to check multiple keys exists in a dictionary .
#  Using all() function along with a list comprehension to check if multiple keys exist in a dictionary.
# def check_keys(dict_obj, keys_list):
#     return all(key in dict_obj for key in keys_list)
# my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# keys_to_check = ['name', 'city', 'country']
# result = check_keys(my_dict, keys_to_check)
# if result:
#     print("All keys exist in the dictionary")
# else:
#     print("One or more keys not found in the dictionary")



# Write a Python script to merge two Python dictionaries 
# To merge two Python dictionaries, update() method or the dictionary unpacking ** operator is used.
# dict1 = {'a': 10, 'b': 20}
# dict2 = {'c': 30, 'd': 40}
# dict1.update(dict2)
# print(dict1)

# dict1 = {'a': 10, 'b': 20}
# dict2 = {'c': 30, 'd': 40}
# merged_dict = {**dict1, **dict2}
# print(merged_dict)



# Write a Python program to map two lists into a dictionary 
# keys = ['apple', 'banana', 'orange']
# values = [3, 6, 4]
# fruit_dict = dict(zip(keys, values))
# print(fruit_dict)


# Write a Python program to combine two dictionary adding values for common keys. d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400} Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}). 
# from collections import Counter
# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# result = Counter(d1) + Counter(d2)
# print(result)


# Write a Python program to print all unique values in a dictionary. 
# my_dict = {"a": 1, "b": 2, "c": 3, "d": 2, "e": 4, "f": 3}
# unique_values = set()
# for value in my_dict.values():
#     unique_values.add(value)
# print("Unique values:", unique_values)


# Why Do You Use the Zip () Method in Python?
# We use zip() method to simplify the code when we need to iterate over two or more lists at the same time. Instead of using a for loop to iterate over each list separately, we can use zip() to iterate over both lists simultaneously.The zip() method can also be used to create a dictionary from two lists, where one list contains keys and the other list contains values.


# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Sample data: {'1': ['a','b'], '2': ['c','d']} Expected Output: ac ad bc bd
# import itertools
# data = {'1': ['a', 'b'], '2': ['c', 'd']}
# combinations = list(itertools.product(*[data[key] for key in data]))
# for combination in combinations:
#     print(''.join(combination), end=' ')


#  Write a Python program to find the highest 3 values in a dictionary.
# my_dict = {"a": 10, "b": 5, "c": 20, "d": 15, "e": 30}
# sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
# highest_values = [value for key, value in sorted_dict[:3]]
# print("The highest 3 values in the dictionary are:", highest_values)


# Write a Python program to combine values in python list of dictionaries. Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, o {'item': 'item1', 'amount': 750}] Expected Output:Counter ({'item1': 1150, 'item2': 300}
# from collections import Counter
# data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# result = Counter()
# for d in data:
#     result[d['item']] += d['amount']
# print(result)


# Write a Python program to create a dictionary from a string. Note: Track the count of the letters from the string. Sample string: 'w3resource' Expected output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1} 
# string = "w3resource"
# char_count = {}
# for char in string:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
# print(char_count)


# Write a Python function to calculate the factorial of a number (a nonnegative integer) 
# def factorial(n): 
#     p=1 
#     i=1 
#     while i<=n: 
#        p= p*i 
#        i+=1 
#     return p 


# Write a Python function to check whether a number is in a given range.
# function
# def check_range(number, range_tuple):
    # return range_tuple[0] <= number <= range_tuple[1]

# def test_range(n):
#     if n in range(10,20):
#         print( "Number %s is in the range"%str(n))
#     else :
#         print("The number is outside the given range.")
# test_range(15)


# Write a Python function to check whether a number is perfect or not. 
# def is_perfect(num):
#     sum_of_divisors = 0
#     for i in range(1, num):
#         if num % i == 0:
#             sum_of_divisors += i
#     if sum_of_divisors == num:
#         return True
#     else:
#         return False


# Write a Python function that checks whether a passed string is palindrome or not 
# def is_palindrome(s):
#     s = s.replace(" ", "").lower()
#     reversed_s = s[::-1]
#     if s == reversed_s:
#         return True
#     else:
#         return False


# How Many Basic Types Of Functions Are Available In Python? 
# There are two basic types of functions available in Python:
# (1) Built-in functions: These are the functions that are already defined in Python and can be used directly without any need for defining them. Examples include print(), len(), range(), etc.
# (2) User-defined functions: These are the functions that are defined by the user to perform a specific task. They can be called multiple times within a program, and they improve the reusability of the code.


# How can you pick a random item from a list or tuple? 
# To pick a random item from a list or tuple. The random.choice() function can be used to select a random item from a list or tuple.
# import random
# my_list = [1, 2, 3, 4, 5]
# random_item = random.choice(my_list)
# print(random_item)


# How can you pick a random item from a range? 
# The randint() function from the random module. The randint() function takes two arguments: the lower and upper bounds of the range (inclusive), and returns a randomly selected integer from that range.
# import random
# random_number = random.randint(1, 10)  
# print(random_number)


# How can you get a random number in python? 
# By using random module
# import random
# random_number = random.randint(1, 10)  
# print(random_number)


# How will you set the starting value in generating random numbers? 
# By setting the starting value of a random number generator by using the seed() function from the random module. The seed() function takes an integer value as its argument, which will be used as the starting point for the random number generator.


# How will you randomizes the items of a list in place? 
# To randomize the items of a list in place, we can use the shuffle function from the random module.
# import random
# my_list = [1, 2, 3, 4, 5]
# random.shuffle(my_list)
# print(my_list)


# Write a Python program to read a random line from a file. 
# import random
# filename = "example.txt"
# with open(filename, "r") as file:
#     lines = file.readlines()
#     random_line = random.choice(lines)
#     print(random_line)


# Write a Python program to convert degree to radian 
# import math
# def degree_to_radian(degrees):
#     return degrees * math.pi / 180.0
# degrees = 90.0
# radians = degree_to_radian(degrees)
# print(f"{degrees} degrees is equal to {radians:.2f} radians")


# Write a Python program to calculate the area of a trapezoid 
# def area_of_trapezoid(base1, base2, height):
#     area = ((base1 + base2) / 2) * height
#     return area
# base1 = 3
# base2 = 4
# height = 5
# area = area_of_trapezoid(base1, base2, height)
# print("Area of the trapezoid is:", area)


# Write a Python program to calculate the area of a parallelogram 
# base = float(input("Enter the base of the parallelogram: "))
# height = float(input("Enter the height of the parallelogram: "))
# area = base * height
# print("The area of the parallelogram is:", area)


# Write a Python program to calculate surface volume and area of a cylinder 
# import math
# radius = float(input("Enter the radius of the cylinder: "))
# height = float(input("Enter the height of the cylinder: "))
# surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
# volume = math.pi * radius ** 2 * height
# print("The surface area of the cylinder is:", surface_area)
# print("The volume of the cylinder is:", volume)


# Write a Python program to returns sum of all divisors of a number. 
# def sum_divisors(num):
#     divisors = []
#     for i in range(1, num+1):
#         if num % i == 0:
#             divisors.append(i)
#     return sum(divisors)


# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers. 
# decimal_numbers = [3.14, 2.718, 1.618, 0.999, 4.669]
# max_number = max(decimal_numbers)
# min_number = min(decimal_numbers)
# print("The maximum number is:", max_number)
# print("The minimum number is:", min_number)
