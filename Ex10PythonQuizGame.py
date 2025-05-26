questions = ("How many elements are there in periodic table?: ",
             "How many bones are there in human  body?: ")

options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. 206","B. 202","C. 209","D. 204"))

answers = ("C","A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter A,B,C,D: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num = question_num + 1

print("--------------------------")
print("         Results          ")
print("--------------------------")

print("answers: ",end="")
for answer in answers:
    print(answer,end="")
print()


print("guesses: ",end="")
for guess in guesses:
    print(guess,end="")
print()

score = int(score/len(questions)*100)
print(f"Your Score is {score}%")