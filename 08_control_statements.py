"""
Description: Tutorial on control statements.
1. break
2. continue
3. else
"""

# Break statement - example

# my_list = ["apple", "mango", "banana", "cherry", "date"]

# index = 0
# for fruit in my_list:
#     # print(f"Index of {fruit} is {index}.")
#     print(f"{fruit}")
#     if fruit == 'cherry':
#         print(f"Index of cherry is {index}")
#         break

#     index += 1


# calculate percentage of student

# 1. get the user name and marks as input from the user
# 2. calculate student percentage
# 3. prompt to the user if user wants to continue or not
# 4. based on user given input - decide further continuation or not

# CONST_MARKS = 600

# def calc_student_percentage(stud_marks):
#     """Calculate student percentage based on the given marks."""
#     # percentage = (stud_marks / CONST_MARKS) * 100
#     # return percentage
#     return (stud_marks / CONST_MARKS) * 100

# while True:
#     student_name = input("Enter the student name: ")
#     student_marks = float(input("Enter the student marks: "))

#     student_percentage = calc_student_percentage(stud_marks=student_marks)
#     print(f"The percentage of {student_name} is {student_percentage}.")

#     user_input = input("Do you want to continue?: ")

#     if not user_input.lower() == 'yes':
#         break

# print("The program executed successfully.")


# continue statement

# loop the numbers between 1 to 100 and move the odd numbers in odd_number_list

# odd_numbers_list = []

# for number in range(1, 101):
#     if number % 2 == 0:
#         continue

#     odd_numbers_list.append(number)

# print(odd_numbers_list)
# print("Program executed successfully")


# else statement

my_fruit_list = ["mango", "apple", "cherry", "kiwi"]

for fruit in my_fruit_list:
    print(fruit)
    if fruit == 'banana':
        break
else:
    print("Banana could not found in the given list.")



