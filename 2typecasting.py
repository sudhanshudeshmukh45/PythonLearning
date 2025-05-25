#Typecasting = The process of converting a variable from one data type to another str(), int(), float(), bool()

name = "Sudhanshu"
age = 23
cgpa = 7.98
isStudent = True

print(type(name))
print(type(age))
print(type(cgpa))
print(type(isStudent))

age = float(age)
print(age)
print(type(age))

cgpa = int(cgpa)
print(cgpa)
print(type(cgpa))

age = str(age)
print(age)
print(type(age))


name = bool(name)
print(name)