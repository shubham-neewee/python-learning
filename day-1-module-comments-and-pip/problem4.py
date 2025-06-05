# Write a python program to print the contents of the directory using the os module. Search online for the function which does that

# importing the os module
import os

# List the contents of the directory
path = 'C:/Users/Admin/Desktop/python-learning/Day 1'

# Adding the path by calling the path variable and using listdir function to list the files and storing the output as array in content variable
content = os.listdir(path)

#Printing the listed output stored in the content variable
print(content)
