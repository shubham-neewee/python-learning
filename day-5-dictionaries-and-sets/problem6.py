# Create an empty dictionary allow 4 friends to enter their favourite language as value and use key as thier names. Assume that the names 
# as unique

dictionary = {}

friend1 = input("Enter the name : ")
lang1 = input("Enter the language : ")
dictionary[friend1] = lang1

friend2 = input("Enter the name : ")
lang2 = input("Enter the language : ")
dictionary[friend2] = lang2

friend3 = input("Enter the name : ")
lang3 = input("Enter the language : ")
dictionary[friend3] = lang3

friend4 = input("Enter the name : ")
lang4 = input("Enter the language : ")
dictionary[friend4] = lang4

print(dictionary)