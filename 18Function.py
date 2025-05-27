#function  = A block of reusable code place() after the function name to invoke it

#Parameters:
#Definition: Variables listed in a function's definition.
#When: You define the function.

def greet(name):  # 'name' is a parameter
    print("Hello", name)
#Arguments:
#Definition: The actual values passed to a function when you call it.
#When: You call the function.

greet("Alice")  # "Alice" is an argument

# def happyBirthday(age):
#     print("Happy Birthday")
#     print("GBU")
#     print(f"You are {age} yrs old")
# happyBirthday(23)

def display_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Sudhanshu",100,"02/05")


def add(a,b):
    c = a + b
    return c

z = add(1,2)
print(z)


def full_name(first_name,last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return first_name+" "+last_name

full_name = full_name("Sudhanshu","Deshmukh")
print(full_name)