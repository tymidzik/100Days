import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

options = [rock, paper, scissors]
computer_choose = options[random.randint(0, 2)]

player_choose_word = options[player_choose]

if player_choose >= 3 or player_choose < 0:
    print("You typed an invalid number, you lose!")
else:
    if player_choose_word == rock and computer_choose == paper or player_choose_word == scissors and computer_choose == rock or player_choose_word == paper and computer_choose == scissors:
        print(f"{player_choose_word}\nComputer chose:\n{computer_choose}\n You lose")
    elif player_choose_word == computer_choose:
        print(f"{player_choose_word}\nComputer chose:\n{computer_choose}\n Draw")
    else:
        print(f"{player_choose_word}\nComputer chose:\n{computer_choose}\n You win!")
