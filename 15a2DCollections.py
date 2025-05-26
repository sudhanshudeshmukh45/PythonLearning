# 2dlist = [list1,list2,list3]

fruits = ["Lime","Coconut","Banana","Apple"]
vegetables = ["Carrot","Onion","Cabbage","Spinach"]
meat = ["Chicken","Mutton","Fish"]

groceries = [fruits,vegetables,meat]

print(groceries[0][2])

for i in groceries:
    for j in i:
        print(j,end=" ")
    print()