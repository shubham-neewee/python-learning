# Write a program to take eight numbers are input from the user and display all unique numbers in the list.

# Take 8 numbers as input from the user
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
num5 = int(input("Enter number 5: "))
num6 = int(input("Enter number 6: "))
num7 = int(input("Enter number 7: "))
num8 = int(input("Enter number 8: "))

# Store the numbers in a list
user_input = [num1, num2, num3, num4, num5, num6, num7, num8]

# Convert the list to a set to get unique numbers
unique_numbers = set(user_input)

# Display the unique numbers
print("Unique numbers are:", unique_numbers)