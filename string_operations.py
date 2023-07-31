"""
Perform string operation.
"""

# 1. concatenation (+) operator

# str1 = "Hello"
# str2 = "Welcome to python string operations tutorial."

# message = str1 + ", " + str2
# print(message)

# 2. Length - len()

# message = "Hello, world!"
# print(f"total characters available in {message} are : {len(message)}.")

# 3. Lower case - lower()
# str1 = "Hello, WORLD!."
# print(str1.lower())

# 4. Upper case - upper()
# print(str1.upper())

# fruits = ['banana', 'mango', 'apple', 'kiwi', 'orange']
# BANANA has 6 characters.

# for fruit in fruits:
#     print(f"{fruit.upper()} has {len(fruit)} characters.")

# 5. Replace - replace()

# message = "Hello, welcome to python programming."

# new_message = message.replace("python", "java")
# print(new_message)

# new_message = message.replace("o", "kg")
# print(new_message)

# 6. Trim - strip(), lstrip(), rstrip()
# msg = "     Hello, world!    "

# print(f"Before removing white spaces we have {len(msg)} characters.")
# print(msg.strip())
# print(f"After removing white spaces we have {len(msg.strip())} characters.")

# print(msg.lstrip())
# print(msg.rstrip())

# 7. Split - split()
# text = "banana,mango,orage"

# fruits = text.split(",")
# print(fruits)

# 8. join - join()

# str_fruits = "-".join(fruits)
# print(str_fruits)

# 9. in operator.

msg = "Hello world!"

if 'hello'.capitalize() in msg:
    print("Search completed.")
else:
    print("Cannot find a search value within the string.")
