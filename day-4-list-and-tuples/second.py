# Tuples are similar to lists but are immutable, meaning they cannot be modified after creation.
# Tuples are denoted by parentheses () and are often used when a collection of items needs to
# be passed to a function without being modified.

a = ()
print(type(a))

tup_list  = (1,2,"Sid",45,43.8)
# tup_list[0] = 2 # 'tuple' object does not support item assignment
print(tup_list)

# Methods in tuple
num = tup_list.count(45) # This will give the number of times 45 occurs in the tuple
print(num)

# Index of Sid
i = tup_list.index("Sid")
print(i)

# Length of tuple 
print(len(tup_list))