#FormatSpecifiers = {value:flags} format a value based on what flags are inserted


price1 = 34443.14159
price2 = -93376.452
price3 = 22354.34


# Below code will display precision to 2 decimals

print(f"Price1 is ${price1:.2f}")
print(f"Price2 is ${price2:.2f}")
print(f"Price3 is ${price3:.2f}")


# Below code will enter space

print(f"Price1 is ${price1:10}")
print(f"Price2 is ${price2:10}")
print(f"Price3 is ${price3:10}")

#Left Justify

print(f"Price1 is ${price1:<10}")
print(f"Price2 is ${price2:<10}")
print(f"Price3 is ${price3:<10}")

#Right Justify

print(f"Price1 is ${price1:>10}")
print(f"Price2 is ${price2:>10}")
print(f"Price3 is ${price3:>10}")

#Centered

print(f"Price1 is ${price1:^10}")
print(f"Price2 is ${price2:^10}")
print(f"Price3 is ${price3:^10}")

#Positive Values will be com e with positive sign and negative number will come with negative sign
print(f"Price1 is ${price1:+}")
print(f"Price2 is ${price2:+}")
print(f"Price3 is ${price3:+}")

#Thousands Separator : (,)
#Below Example with multiple format specifiers

print(f"Price1 is ${price1:+,.2f}")
print(f"Price2 is ${price2:+,.2f}")
print(f"Price3 is ${price3:+,.2f}")