import os
from art import logo

print(logo)

users = {}


def user_inputs():
    name = input("What is your name?\n")
    if name in users:
        name += " " + input("What is your last name?\n")
    bid = input("What is your bid?\n")
    users[name] = bid
    other_bidders = input("Are there any other bidders? yes or no\n").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    if other_bidders == "yes":
        user_inputs()
    else:
        highest_price()


def highest_price():
    winner = 0
    for i in users:
        winning_number = 0
        print(users[i])
        if winning_number < int(users[i]):
            winner = i
    print(f"The winner is {winner}.")


user_inputs()
