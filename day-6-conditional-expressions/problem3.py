#  A spam comment is defined as text containing following keywords
# "Make a lot of money" , "Random Text" , write a program to detect this text



p1 = "Make a lot of money" 
p2 = "Random Text" 
p3 = "Another text"

user_input_message = input("Enter the message : ")

if (p1 in user_input_message or p2 in user_input_message or p3 in user_input_message):
    print("This is a spam comment")
else:
    print("This is not a spam comment")