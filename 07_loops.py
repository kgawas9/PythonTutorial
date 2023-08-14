"""
Description: Tutorial on python loops
1. For loop
2. While loop.
"""

# start 0, end 100-1 99, step = 1
# for number in range(1, 101, 1):   # start value, end value, step value
#     print(number, end=", ")


# output 1, 4, 7, 10
# for number in range(1, 11, 3):
#     print(number, end=", ")


# calculat the index of given item inside fruit list.

# lst_fruits = [
#     'Apple', 'Mango', 'Banana', 'Kiwi'
# ]

# index = 0
# for fruit in lst_fruits:
#     print(f"Index of {fruit} is {index}.")
#     index += 1      # index = index + 1

# print(type(enumerate(lst_fruits)))

# for index, fruit in enumerate(lst_fruits):
#     print(f"Index of {fruit} is {index}.")


# define dictionary - it holds the numbers and sum and multiplication on the dictionary values.
# get choice of operator from user.


# calulate('+', key1=10, key2=20, key3=30, key4=40)
# def calculate(operator, **numbers):
#     """
#     Calculate sum or multiplication on the dictionary values based on the operator selected by user.
#     """
#     print(type(numbers))
#     if operator == '+':
#         i_sum = 0
#         for value in numbers.values():
#             i_sum += value  # 10, 30, 60, 100
#         return i_sum

#     if operator == '*':
#         i_mult = 1
#         for value in numbers.values():
#             i_mult *= value
#         return i_mult


# def calculate(operator, **numbers):
#     """
#     Calculate sum or multiplication on the dictionary values based on the operator selected by user.
#     """
#     if operator == '+':
#         return sum(numbers.values())

#     if operator == '*':
#         i_mult = 1
#         for value in numbers.values():
#             i_mult *= value
#         return i_mult


# import math

# def calculate(operator, **numbers):
#     """
#     Calculate sum or multiplication on the dictionary values based on the operator selected by user.
#     """
#     if not numbers:
#         raise ValueError("No value provided to perform the operation.")

#     if operator == '+':
#         return sum(numbers.values())
#     elif operator == '*':
#         return math.prod(numbers.values())
#     else:
#         raise ValueError("Invalid operator.")


# dict_numbers = {
#     'key1': 10,
#     'key2': 20,
#     'key3': 30,
#     'key4': 40,
# }

# print(dict_numbers.values())

# user_input = input("Please enter the operator (+ or *):\t")

# result = calculate(user_input, **dict_numbers)
# print(result)


# syntx

# while condition:
    # code to be executed as long as the condition remains true


# number = 1
# while number <= 100:
#     print(number, end=", ")
#     number += 1


# example - to find even numbers between 1 to 100

number = 1
while number <= 100:
    if number %2 == 0:
        print(number, end=", ")

    number += 1
