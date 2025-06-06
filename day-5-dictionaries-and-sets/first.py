marks = {
    "Harry" : 100,
    "Shubham" : 200,
    "Sachin" : 300
}

print(marks,type(marks))

# Properties of dictionary
# it is unordered
# it is mutable
# it is indexed
# Cannot contain duplicate keys

marks.update({"Hari" : 99})
marks.update({"Harry" : 99})
print(marks)