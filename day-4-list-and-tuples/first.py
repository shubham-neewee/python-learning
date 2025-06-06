# Lists and Tuples
# Lists are ordered collections of items that can be of any data type, including strings, integers,
# floats, and other lists. Lists are denoted by square brackets [] and are mutable, meaning
# they can be modified after creation.

friends = ["Apple", "Orange", False , 1 , "Rohan" , 435.09]
print(friends)
print(friends[0])

friends[0] = "Grapes" # Unlike strings lists are mutable
print(friends[0])


#  List methods
# 1. append() - Adds an element to the end of the list.
# 2. extend() - Adds multiple elements to the end of the list.
# 3. insert() - Inserts an element at a specified position in the list.
# 4. remove() - Removes the first occurrence of the specified element from the list.
# 5. pop() - Removes and returns the element at the specified position in the list.
# 6. index() - Returns the index of the first occurrence of the specified element in the list.
# 7. count() - Returns the number of occurrences of the specified element in the list.
# 8. sort() - Sorts the list in-place.
# 9. reverse() - Reverses the list in-place.
# 10. copy() - Returns a shallow copy of the list.
# 11. clear() - Removes all elements from the list.
# 12. list() - Converts the list to a list.
# 13. len() - Returns the number of elements in the list.
# 14. max() - Returns the maximum item in the list.
# 15. min() - Returns the minimum item in the list.
# 16. sum() - Returns the sum of all items in the list.
# 17. any() - Returns True if at least one element of the list is true.
# 18. all() - Returns True if all elements of the list are true.
# 19. enumerate() - Returns an enumerate object that iterates over the list in parallel with its index.
dost = ["Sapta", "Yash", "Aditya", "Mohan"]
print(dost)

# The below proves that list are mutable meaning we can make change to the original list -- append meaning to add to the end
dost.append("Harish")
print(dost)



numbers = [1,3,5,75,57,78,9,92,9,90,6]
numbers.sort
print(numbers)

numbers.insert(3,66)
print(numbers)

numbers.pop(8)
print(numbers)

numbers.remove(6)
print(numbers)
