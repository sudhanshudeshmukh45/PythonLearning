operator = input("Enter your operator (+,-,/,*):")

number1 = float(input("Enter your first number:"))
number2 = float(input("Enter your second number:"))

if operator == "+":
    result = number1 + number2
    print(round(result,3))

elif operator == "-":
    result = number1 - number2
    print(round(result,3))

elif operator == "*":
    result = number1 * number2
    print(round(result,3))

elif operator == "/":
    result = number1 / number2
    print(round(result,3))

else:
    print(f"{operator} is Invalid Operator")