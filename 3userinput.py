#input() = A function that prompts user to enter the data
#           Returns the entered data as String

name = input()
#So by default input() functions stores data as string
print(type(name))
print(f"Hello {name}")

age = input()
print(f"You are {age} years old")


# So as default type of input is string we need to typecast
age = int(input())
age = age + 1
print(f"You are {age} years old")