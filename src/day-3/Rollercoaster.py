# The rollercoaster

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("How old are you?\n"))
    if age > 18:
        print("You have to pay 12$.")
        bill = 12
    elif age < 12:
        print("You have to pay 5$.")
        bill = 5
    elif age <= 55 and age <= 45:
        print("YOU CAN RIDE FOR FREE!")
    else:
        print("You have to pay 7$.")
        bill = 7

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")
else:
    print("Sorry, but you can't ride the roller coaster.")
