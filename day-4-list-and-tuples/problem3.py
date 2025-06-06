# Check that the tuple type cannot be changed in python
tuple1 = (1, 2, 3)
tuple[2] = 4 # This will raise a TypeError
print(tuple1) #TypeError: 'type' object does not support item assignment
