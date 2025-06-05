# Operators in Python
# 1. Arithmetic Operators
# 2. Comparison Operators
# 3. Logical Operators
# 4. Assignment Operators
# 5. Bitwise Operators

# when we write 7 + 4 = 11 here 7 and 4 are called operands and 11 is called results
# 7 + 4 is called expression
# 7 + 4 is called expression and + is called operator


# 1. Arithmetic Operators
a = 7
b= 4 
c = a + b
print("The Sum of arithmetic operators : ",c)

# Assignment Operator
aa = 7 # assign 7 to aa
print(aa)

bb = 6-4 # assign 2 to bb (after calculation)
print(bb)


cc = 0
cc += 3 # assign 5 to cc (after calculation)
print(cc)


# 2. Comparison Operators -- here the return value is always boolean
dd = 7
ee = 4
print(dd > ee) # True
print(dd < ee) # False

# when we say >= it means greater than 'or' equal to
print(dd >=ee) # True

# when we say != it means not equal to
print(dd != ee) # True

# when we say == it means equal to
print(dd == ee) # False


# Logical Operators

e = True or False
print(e)


# Truth Table for or
# 1 1 = 1
# 1 0 = 1
# 0 1 = 1
# 0 0 = 0
# Truth Table for and
# 1 1 = 1
# 1 0 = 0
# 0 1 = 0
# 0 0 = 0

print(not(True))