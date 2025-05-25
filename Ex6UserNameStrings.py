#Validate User Input Exercise
#1. Username is no more than 12 characters
#2. Username must not contain spaces
#3. Username must not contain digits

Username = input("Enter your username: ")

if len(Username)>12:
    print("Username invalid")

elif not Username.find(" ")==-1:
    print("Your Username can't contain spaces")

elif not Username.isalpha():
    print("Your Username can't contain numbers")

else:
    print(f"Welcome {Username}")

