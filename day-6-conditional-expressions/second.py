# Multilpe conditions - elif
# elif is used to specify a new condition if the first condition is not met
age = int(input("Enter your age : "))
if age >= 18:
    print("You are an adult")

elif age >= 13:
    print("You are a teenager")

elif age < 0:
    print("this is not possible")

else:
    print("You are a kid")