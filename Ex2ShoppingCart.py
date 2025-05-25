item = input("What you would like to buy:")

quantity = int(input(f"How much quantity:"))

price = float(input(f"What is the price:"))

totalcost = quantity * price

print(f"Your total bill is ${totalcost}")