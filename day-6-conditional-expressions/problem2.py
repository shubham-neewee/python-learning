# Write a program to find whether the student is pass or failed. if it requires a total of 40% and least 33% in each subject to pass
# Assume 3 subject and take marks as input from the user

subject1 = int(input("Enter the marks obtained in Maths : "))
subject2 = int(input("Enter the marks obtained in Science : "))
subject3 = int(input("Enter the marks obtained in English : "))

# Calculate the total marks and percentage
total_marks = subject1 + subject2 + subject3
percentage = total_marks * 100 / 300
print("Your total percentage is : ", percentage)

if (percentage >= 40) and (subject1 >= 33) and (subject2 >= 33) and (subject3 >= 33):
    print("You are pass")
else:
    print("You are failed")

