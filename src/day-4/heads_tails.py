import random

print("Welcome to the game Heads or Tails.")

player_choice = input("Choose Heads or Tails. h or t\n").lower()

result = random.randint(0, 1)
print(result)

if player_choice == "h" and result == 1 or player_choice == "t" and result == 0:
    print("You win!")
else:
    print("You lost.")
