#NestedLoop : A loop within another loop (outer,inner)
#                     OuterLoop:
#                           InnerLoop:

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns"))
symbol = input("Enter a symbol to use")

for rows in range(rows):
    for y in range(columns):
        print(symbol,end=" ")
    print()