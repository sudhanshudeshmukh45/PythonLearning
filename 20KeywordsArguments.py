#Keywords Argument: an argument preceded by an identifier , helps with readability
#order of argument doesn't matter as we define identifier

def HappyBirthday(Name,Age,Grade):
    print(f"Happy Birthday! {Name} of Grade {Grade}, You turned {Age} old")

HappyBirthday("Sudhanshu",25,10)

HappyBirthday(Age=25,Name="Rahul",Grade=12)