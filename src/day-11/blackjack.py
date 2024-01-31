from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def more_or_less(player_score, computer_score):
    if (computer_score < player_score <= 21) or (computer_score > 21 >= player_score):
        print("You won")
    elif computer_score == player_score or computer_score > 21 < player_score:
        print("draw")
    else:
        print("You lost")


def play():
    player_cards = [cards[random.randint(0, len(cards) - 1)], cards[random.randint(0, len(cards) - 1)]]
    computer_cards = [cards[random.randint(0, len(cards) - 1)], cards[random.randint(0, len(cards) - 1)]]
    computer_score = sum(computer_cards)
    player_score = sum(player_cards)
    # if player wants another card
    wants_card = True
    while wants_card:
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        get_card = input("Type 'y' to get another card or 'n' to pass: ")
        if get_card == "n":
            wants_card = False
        else:
            player_cards.append(cards[random.randint(0, len(cards) - 1)])
            player_score = sum(player_cards)
    # if computer score is less than 17
    while computer_score > 17:
        computer_cards.append(cards[random.randint(0, len(cards) - 1)])
        computer_score = sum(computer_cards)
    # lost or won
    print(
        f"Your final hand: {player_cards}, final score: {player_score}\n"
        f"Computer final hand: {computer_cards}, final score: {computer_score}"
    )
    more_or_less(player_score, computer_score)


# to start the game
go = True
while go:
    wants_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if wants_to_play == "y":
        print(logo)
        play()
    else:
        go = False
