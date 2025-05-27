menu = {"Pizza":3.00,
        "Soda": 2.5,
        "Vadapav": 0.5,
        "PopCorn": 5.12,
        "lemonade":2.0,
        "fries":3.0,
        "burger":10.0}


cart = []
total = 0


print("-------- Menu -------- ")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("---------------------- ")

while True:
    food = input("Select an item (q to quit)")
    if food.lower() == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("--------- Your Order ----------")

for food in cart:
    total = total + menu.get(food)
    print(food,end=" ")

print()
print(f"Your total bill is ${total}")

