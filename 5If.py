# if = Do some code only IF some condition is true else do something else

age = int(input("Please Enter your age:"))

if age<=15:
    print("kid")
elif age>15 and age<=45:
    print("Adult")
else:
    print("old")