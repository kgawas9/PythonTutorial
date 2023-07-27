"""
Hello, this will help you to undrstand the functionlity used on the module level.
"""

def some_fun():
    """This function currently return none and later you can provide the implementation into it."""
    pass

print(dir(some_fun))

print(some_fun.__doc__)

# str_welcome_msg = "Welcome to python programming."

# print(str_welcome_msg)

























"""
Examples of print statements with dynamic values.
"""

# Method 1 - Using string concatenation

name = 'Tom'
age = 30
email = 'tom@example.com'

# print('Name: ' + name + ', Age: ' + str(age) + ', Email: ' + email)

# Method 2 - Using % formatting

# print("Name: %s, Age: %d, Email: %s" %(name, age, email))

# Method 3 - Using string format str.format()

# print("Name: {}, Age: {}, Email: {}".format(name, age, email))

# Method 4 - Using f string

# fruits = ["Apple", "Banana", "Orange", "Mango"]

# for index, fruit in enumerate(fruits):
#     print(f"The index of {fruit} is {index}.")

# Method 5 - Using format() with positional arguments

# print("Name: {0}, Age: {1}, Email: {2}".format(name, age, email))

# Method 6 - Using format() with keyword arguments

print("Name: {n}, Age: {a}, Email: {e}".format(n=name, a=age, e=email))