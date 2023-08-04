"""
Get input from the user dynamically.
"""

# input('prompt')

# user_name = input("Enter your name: ")
# print(f"Hello {user_name}, welcome to get user input python tutorial.")

# numeric input from the user.

# number_1 = int(input("Enter the first number: "))
# number_2 = int(input("Enter the second number: "))

# print(type(number_1))
# print(type(number_2))

# print(number_1 + number_2)

# 50, 60.50
# try:
#     percentage = float(input("Enter your percentage: "))

#     if percentage > 0 and percentage < 35:
#         print("Sorry! you have failed.")
#     elif percentage >= 35 and percentage < 60:
#         print("You have passed with second class.")
#     elif percentage >= 60 and percentage < 75:
#         print("You have passed with first class.")
#     elif percentage >= 75 and percentage <=100:
#         print("Hurray! you have passed with distinction.")
#     else:
#         print("Invalid input, please provide valid percentage.")
# except ValueError:
#     print("Invalid input. Please enter the percentage between 0 - 100.")


import sys


if len(sys.argv) == 3:
    print(sys.argv[0])
    user_name = sys.argv[1]
    course_name = sys.argv[2]

    print(f"{user_name} has enrolled for {course_name} course.")
else:
    print("Invalid parameters, this program accepts 3 parameters.")
