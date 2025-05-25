#Logical Operators: Evaluate multiple conditions (or, and, not)
#                or: At least one condition must be true
#                and: both Conditions must be true
#                not: inverts the condition (not False, not True)

temp = float(input("Enter the temperature:"))
is_raining = False

if temp>35 or temp<0 or is_raining:
    print("Cancel the event")

else:
    print("Event is ON")

#-----------------------------------------------------------------------------------------------------------------------

temp1 = float(input("Enter the temperature:"))
is_sunny = True

if temp1>=25 and is_sunny:
    print("Its Hot Outside 🥵")
    print("Its Sunny 🔆")

else:
    print("Its Cool ❄️")

#-----------------------------------------------------------------------------------------------------------------------