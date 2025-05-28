#*args = allows you to pass multiple non-key argument
#*args stores the arguments as tuple
# * unpacking operator This important while we can change parameter args as something else like nums


def add(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add(1,5,2,51,1))

#**kwargs = allows you to pass multiple keyword arguments
# It will pack them in dictionary

def print_address(**kwargs):
    for key in kwargs.items():
        for values in key:
            print(values, end=" ")
        print()


print_address(street="345",
              apartment = "Raddison",
              area = "Hinjewadi",
              city = "Malkapur",
              state = "Maharashtra",
              country = "India")
