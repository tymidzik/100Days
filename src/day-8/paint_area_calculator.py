import math


def calculator(height, width):
    cans = math.ceil(height * width / 5)
    if cans > 1:
        nr = "cans"
    else:
        nr = "can"
    print(f"To paint this wall, you will need {cans} {nr} of paint.")


test_h = int(input("Height of wall:"))
test_w = int(input("Width of wall:"))

calculator(height=test_h, width=test_w)
