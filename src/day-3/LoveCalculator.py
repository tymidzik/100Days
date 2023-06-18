print("Welcome to the Love Calculator!")
name = input("What is your name?\n")
their_name = input("What is their name?\n")

combined_names = their_name + name

names_lower_case = combined_names.lower()

true_score = names_lower_case.count("t") + names_lower_case.count("r") + names_lower_case.count(
    "u") + names_lower_case.count("e")

love_score = names_lower_case.count("l") + names_lower_case.count("o") + names_lower_case.count(
    "v") + names_lower_case.count("e")

score = int(f"{true_score}{love_score}")

if score <= 10 or score >= 90:
    interpretation = ", you go together like coke and mentos"
elif score >= 40 and score <= 50:
    interpretation = ", you are alright toghether"
else:
    interpretation = ""

print(f"Your score is {score}{interpretation}.")
