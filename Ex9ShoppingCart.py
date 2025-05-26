foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you want to buy  (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("---------------Your Cart---------------")

for i in range(len(foods)):
    print(foods[i])

for i in range(len(prices)):
    total = total + prices[i]
print(f"Your total bill is S{total}")
