import random
from hangman_words import words
from hangman_art import stages, logo

# giving player lives
lives = 6

# getting the random word from the list
chosen_word = words[random.randint(0, len(words) - 1)]

# print the logo
print(logo)

# make variables and lists that are going to be used in the "while loop"
game = True

check_list = []

blanks = []
blanks += len(chosen_word) * "_"

x = 0

while game:
    # ask player to guess the letter
    guess = input("Guess the letter.\n").lower()
    # check if player has already used the letter
    if guess in check_list:
        print("You have already used this letter.")
        print(*blanks)
    # check if player has guessed the letter
    elif guess in chosen_word:
        # fill all blanks replacing guessed letter
        for x in range(len(chosen_word)):
            if chosen_word[x] == guess:
                blanks[x] = guess
        print(*blanks)
        if "_" not in blanks:
            print("You won")
            game = False
    else:
        lives -= 1
        print("The letter you've guessed is not in the word. You lose one life")
        print(stages[lives])
        print(*blanks)
        if lives == 0:
            print(f"You lose\nThe correct word was {chosen_word}")
            game = False
    check_list += guess
