# Write a program to create a dictionary of hindi words with values as their english translation. Provide user with an option to look it up!
words = {
    "Help" : "Madad",
    "Hello" : "Namaste",
    "Goodbye" : "Alvida",
    "Thank you" : "Dhanyavad",
    "How are you?" : "Aap kaise hain?"
}

user_input = input("Enter the word you want to look up: ")
print(words[user_input])