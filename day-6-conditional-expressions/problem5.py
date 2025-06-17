# Write a program which finds out whether the given name is present in the list or not

userlist = ["Shubham", "Siddharth", "Sachin" , "Mohit", "Arshad"]
# print(type(userlist))

user = input("Enter the name: ")

if user in userlist:
    print("Name is present in the list")
else:
    print("Name not present in the list")

