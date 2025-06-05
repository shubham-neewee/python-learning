# Write a program to detect double space in a string

a = "This is a string with  double space"
print(a)

# This will find the double space in the string - it will return true if double space is present, will return false if there are no double space
print(a.find("  "))

# if the below return -1 then double space is not present if it returns a value then double space is present