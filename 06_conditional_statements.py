"""
Developer: KGTechs
Date: 08/08/2023
Description: Tutorial on conditional statements in python
"""

# if statement

# user_age = int(input("Enter your age: "))

# if user_age >= 18:
#     print("You are eligible for Voting.")


# if-else statement

# print(user_age >= 18)

# if user_age >= 18:
#     print("You are eligible for Voting.")
# else:
#     print("You are not eligible for Voting.")


# elif (else if) statement

# student_percentage = float(input("Enter your percentage: "))

# print(student_percentage >= 75 and student_percentage <= 100)
# print(student_percentage >= 60)
# print(student_percentage >=35)

# if student_percentage >= 75 and student_percentage <= 100:
#     print("Hurray! you have passed with distinction.")
# elif student_percentage >= 60:
#     print("You have passed with first class.")
# elif student_percentage >= 35:
#     print("You have passed with second class.")
# elif student_percentage >= 0:
#     print("Sorry! you have failed.")
# else:
#     print("Sorry! invalid input. please enter the valid percentage.")


# nested-if statements

# is_debit_card_exist = input("Do you have debit card?: ")

# if is_debit_card_exist == 'yes':
#     pin_details = int(input("Enter your pin: "))
#     # statement
#     if pin_details == 4444:
#         print("You can withdraw the money from ATM.")
#     else:
#         print("Incorrect password, please enter the valid password.")
# else:
#     print("You are not allowed to withdraw the money from ATM.")


# int_a = 123
# int_b = 123

# print(id(int_a))
# print(id(int_b))

# print(int_a is int_b)
# print(int_a == int_b)

# lst1 = [1, 2, 3]
# lst2 = lst1
# lst3 = [1, 2, 3]

# print(id(lst1))
# print(id(lst2))
# print(id(lst3))

# print(lst1 is lst2)

# print(lst1 is not lst3)

# in operator

# fruit_list = ['apple', 'mango', 'banana', 'kiwi']

# user_input = input("Enter the fruit name which you want to search in the list: ")

# if user_input in fruit_list:
#     print(f"{user_input} is available inside fruit list.")
# else:
#     print(f"{user_input} is not available inside fruit list.")


# if user_input not in fruit_list:
#     print(f"{user_input} is not available inside fruit list.")
# else:
#     print(f"{user_input} is available inside fruit list.")


# or operator

user_voting_card = input("Do you have voting card?: ")
applied_for_voting_card = input("Have you applied for voting card?: ")

if user_voting_card == 'yes' or applied_for_voting_card == 'yes':
    print("You are eligible for voting.")
else:
    print("You are not eligible for voting.")
