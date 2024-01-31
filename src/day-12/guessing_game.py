from art import logo
import random

win = False

print(logo)


def guess():
    global guessed
    print(f"You have {attempts} attempts remaining to guess the number")
    guessed = int(input("Make a guess:"))


def more_or_less():
    global win
    print(guessed)
    if guessed < random_number:
        print("Too low.")
        if attempts > 1:
            print("Try again.\n")
    elif guessed > random_number:
        print("Too high.")
        if attempts > 1:
            print("Try again.\n")
    else:
        print(f"You got it! The answer was {random_number}!")
        win = True


print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
random_number = random.randint(0, 101)
print(f"psst, the number is {random_number}")

if choice == "easy":
    attempts = 10
else:
    attempts = 5

go = True

while go:
    if attempts != 0:
        guess()
        more_or_less()
        if win:
            break
    else:
        print("You've run out of guesses, you lose.")
        break
    attempts -= 1
