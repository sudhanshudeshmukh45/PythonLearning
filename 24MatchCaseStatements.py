# Match Case Statements: An alternative to using many 'elif' statements.
#                        Execute some code if value matches a 'case'
#                   Benefits : Cleaner and syntax is more readable


def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return " It is Monday"
        case 3:
            return "It is Tuesday"

        case _:
            return "Not Valid day"


print(day_of_week(7))