"""
Tutorial on accepting user input dynamically during program runtime.
"""

# input()

# user_name = input("Enter your name: ")
# print(f"Hello {user_name}, welcome to user input tutorial in python programming.")

# addition

# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))

# print(type(number1))
# print(type(number2))

# print(number1 + number2)

# try:
#     percentage = float(input("Enter your percentage: "))

#     if percentage >= 0 and percentage < 35:
#         print("Sorry! you have failed.")
#     elif percentage >= 35 and percentage < 60:
#         print("You have passed with second class.")
#     elif percentage >= 60 and percentage < 75:
#         print("You have passed with first class.")
#     elif percentage >= 75 and percentage <= 100:
#         print("Hurray!, you have passed with distinction.")
#     else:
#         print("Invalid input. please enter percentage between 0 - 100")

# except ValueError:
#     print("Invalid input. please enter percentage between 0 - 100")


import sys

if len(sys.argv) == 3:
    user_name = sys.argv[1]
    user_age = sys.argv[2]

    print(f"Script ran successfully by {user_name} and user has provided his/her age is {user_age}.")

else:
    print("Script error - this script accepts 3 arguments.")

#python user_input.py user_name user_age