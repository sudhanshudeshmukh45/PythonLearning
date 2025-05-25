#For Loops: Execute a block of code a fixed number of times. You can iterate over a range, string, sequence, etc.

for i in reversed(range(1,5,2)):
    print(i)

print("Happy New Year")

#-----------------------------------------------------------------------------------------------------------------------

id = "3212"

for i in id:
    print(i)

#-----------------------------------------------------------------------------------------------------------------------

for i in range(1,5):
    if i == 2:
        continue
    else:
        print(i)

#-----------------------------------------------------------------------------------------------------------------------

for i in range(1,5):
    if i == 3:
        break
    else:
        print(i)

print("Break Success")