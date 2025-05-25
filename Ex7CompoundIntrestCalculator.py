principle = 0
rate = 0
time = 0

while principle <=0:
    principle = float(input("Enter your principle amount: "))
    if principle <=0:
        print("Principle cannot be less than or equal to zero")

while rate <=0:
    rate = float(input("Enter your intrest rate : "))
    if rate <=0:
        print("Intrest Rate cannot be less than or equal to zero")

while time <=0:
    time = int(input("Enter time in years: "))
    if time <=0:
        print("Time cannot be less than or equal to zero Years")


totalAmount = principle * pow((1+rate/100),time)

print(f"Balance after {time} years: ${totalAmount:,.2f}")