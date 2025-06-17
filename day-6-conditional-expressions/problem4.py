# Write a program to find whether a given username contains 10 characters or not.

username = input("Enter your username: ")
print("The lenght of the user name is : ",len(username))

if len(username) == 10:
    print("The username contains 10 characters.")
elif len(username) < 10:
    print("The username is less than 10 characters.")
else:
    print("The username is greater than 10 character.")