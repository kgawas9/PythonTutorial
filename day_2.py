"""
Examples to write print statement with dynamic parameters.
"""

# name = "Tom"
# age = 25
# email = 'tom@example.com'

# Method 1 : Using string concatenation

# print("Name: " + name + ", Age: " + str(age) + ", Email: " + email)

# Method 2 : Using %-formatting

# print("Name: %s, age: %d, email: %s" %(name, age, email))

# Method 3 : Using str.format()

# print("Name: {}, Age: {}, Email: {}".format(name, age, email))

# Method 4 : Using f string

fruits = ['Apple', 'Mango', 'Banana', 'Kiwi', 'Orange']

# for index, fruit in enumerate(fruits):
#     print(f"The index of {fruit} is {index}")

# Method 5 - Using format() with positional arguments

# print("Name: {1}, Email: {2}, Age: {0}".format(age, name, email))
# print("Name: {0}, Email: {1}, Age: {2}".format(name, email, age))

# print("On 0th index we have {0} fruit.".format(fruits[0]))

# Method 6 = Using format() with keyword arguments

name = "Tom"
age = 25
email = 'tom@example.com'

print("Name: {n}, Age: {a}, Email: {e}".format(n=name, a=age, e=email))
