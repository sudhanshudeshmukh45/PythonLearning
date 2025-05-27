import random
low = 1
high = 100
answer = random.randint(low,high)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {low} and {high}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < low or guess > high:
            print("That number is outside the range")
            print(f"Please Select a number between {low} and {high}")

        elif guess < answer:
            print("Too Low! Try Again!")

        elif guess > answer:
            print("Too High! Try Again!")

        else:
            print(f"CORRECT! The Answer was {answer}")
            print(f"Number og guesses {guesses}")
            is_running = False


    else:
        print("Invalid Guess")
        print(f"Please Select a number between {low} and {high}")