# What is string in python

# Sting in python is a sequence of characters. It is a collection of characters that can be of
# any length. It can be a single character or a group of characters. It is a sequence of
# unicode characters.

# Strings in python can be enclosed in single quotes or double quotes.
# Strings in python are immutable, meaning that once a string is created, it cannot be changed.
# Strings in python can be created using the following methods:
# 1. Using single quotes: 'Hello, World!'
# 2. Using double quotes: "Hello, World!"
# 3. Using triple quotes: '''Hello, World!''' or """Hello, World!
# 4. Using the str() function: str('Hello, World!')
# 5. Using the repr() function: repr('Hello, World!')
# 6. Using the format() function: 'Hello, {}!'.format('World')
# 7. Using f-strings: f'Hello, {World}!'


# String Slicing
# String slicing is a way to extract a subset of characters from a string. It is done using
# square brackets and the index of the character you want to start and end with. The syntax
# for string slicing is: string[start:stop:step].
# The start index is the position where you want to start extracting characters. The stop index
# is the position where you want to stop extracting characters. The step is the increment
# between each character.
# For example: 'Hello, World!'[0:5] will return 'Hello'.
# If you omit the start index, it will start from the beginning of the string.
# If you omit the stop index, it will go to the end of the string.
# If you omit the step, it will return every character in the string.

name = "Shubham"
nameshort = name[0:4] # returns 'Shub'

print("Length of string : ",len(name)) 
print(nameshort) 

# Negative indexing
# Negative indexing is a way to access characters from the end of the string. It starts from    
# -1, which is the last character in the string, -2 is the second last character
# and so on.

negslicing = name[-3:-1]
print("The negative slicing of the string is : ", negslicing)

numberlist = "1234567890"
print(numberlist[1:6:2])   # returns '2346'  # returns every second character starting from index 1 to 6



