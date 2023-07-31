"""
Python string slicing tutorial.

syntax:
string[start:end:step]
"""

# str_msg = "Hello world!"

# str_substring = str_msg[0:5]

# str_substring = str_msg[:]
# print(str_substring)

# str_substring = str_msg[0:len(str_msg)]
# print(str_substring)

# str_last_word = str_msg[6:12]
# print(str_last_word)

# str_last_word = str_msg[6:]
# print(str_last_word)

# Negative indexing

# str_msg = start index - 12 - 6 = 6
# str_msg = end index - 12 - 1 = 11

# str_msg[6:11] = 'world'

# str_substring = str_msg[-6:-1]
# print(str_substring)

# str_substring = str_msg[6:11]
# print(str_substring)

str_msg = "Hello world!"

str_substring = str_msg[::2]
print(str_substring)
