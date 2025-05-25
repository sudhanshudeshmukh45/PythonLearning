distance = float(input("Enter the distance: "))

unit = input("Enter the Unit Km,m:")

if unit == 'Km':
    result = 100000 * distance
    print(f"{result} cm")

elif unit == 'm':
    result = 100 * distance
    print(f"{result} cm")

else:
    print("Invalid Unit")