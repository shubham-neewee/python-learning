# Write a program to find greatest of 4 numbers entered by the user

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"Number 1 is the greatest, the number is {num1}")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(f"Number 2 is the greatest, the number is {num2}")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(f"Number 3 is the greatest, the number is {num3}")
elif num4 > num1 and num4 > num2 and num4 > num3:
    print(f"Number 4 is the greatest, the number is {num4}")

else:
    print("All numbers are equal.")
