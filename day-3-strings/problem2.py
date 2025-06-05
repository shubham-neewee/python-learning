# Write a program to fill in the letter template given below with name and date
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter)
print(letter.replace("<|Name|>","Shubham").replace("<|Date|>","31/07/2000"))
