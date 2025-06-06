# Sets in python
# A set is an unordered collection of unique elements.
# It is a mutable data type that does not allow duplicate values.
# Sets are used to store a collection of unique items.
# Sets are not indexed meaning you cannot access them by index.



s = {1,24,23,56,45,33,5,44,44}
print(s)  
print(type(s)) 


# Methods in sets
s.add(566)
print(s)

s.remove(33)
print(s)


# Unions in sets
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

print(s1.union(s2))

# Intersection in sets
print(s1.intersection(s2))

# Difference in sets
print(s1.difference(s2))

# Subset in sets
print(s1.issubset(s2))

# Superset in sets
print(s1.issuperset(s2))

# Checking if an element is in a set
print(5 in s1)  # True
print(9 in s1)  # False