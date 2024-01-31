from art import logo
from art import vs
from game_data import data
import random

answer = True
u_data = ['name', 'description', 'country']
account1 = data[random.randint(0, len(data) - 1)]
account2 = data[random.randint(0, len(data) - 1)]
while account2 == account1:
    account2 = data[random.randint(0, len(data))]["name", "description", "country"]


def higher_lower(choice):
    if (choice == "A" and account1["follower_count"] > account2["follower_count"]) or (
            choice == "B" and account2["follower_count"] > account1["follower_count"]):
        return answer == True
    else:
        return answer == False


def game():
    global answer
    global account1
    global account2
    score = 0
    print(logo)
    while answer:
        print(
            f"Compare A: {account1[u_data[0]]}, a {account1[u_data[1]]}, from {account1[u_data[2]]}."
            f"{vs}"
            f"Compare B: {account2[u_data[0]]}, a {account2[u_data[1]]}, from {account2[u_data[2]]}.")
        pl_choice = input("Who has more followers? Type 'A' or 'B':")
        answer = higher_lower(pl_choice)
        if answer == False:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
        score += 1
        account1 = account2
        account2 = data[random.randint(0, len(data) - 1)]
        print(f"You're right! Current score: {score}")


game()
