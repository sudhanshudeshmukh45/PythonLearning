#While Loop: Execute some code while some condition remains TRUE


age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be less than 0")
    age = int(input("Enter your age: "))

print(f"You are {age} Years")


