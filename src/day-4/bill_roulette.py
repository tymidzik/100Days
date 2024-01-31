import random

print("Welcome to the Bill Roulette!")

names_string = input("Give me everybody's names splited by a comma.\n")
names = names_string.split(", ")

number = random.randint(0, len(names) - 1)

name = names[number]

print(f"{name} is going to buy the meal today.")
