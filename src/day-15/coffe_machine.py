MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def machine(inp):
    for item in MENU[inp]["ingredients"]:
        resources[item] -= MENU[inp]["ingredients"][item]


def check_ingr(inp):
    if inp == "off":
        breakpoint()
    elif inp == "report":
        print(f"Milk:{resources['milk']}")
        print(f"Water:{resources['water']}")
        print(f"Coffe:{resources['coffee']}")
        print(f"Profit:{profit}")
        interface()
    else:
        for item in MENU[inp]["ingredients"]:
            if MENU[inp]["ingredients"][item] > resources[item]:
                print(f"Sorry there is not enough {item}")
                interface()


def process_coins():
    total = float(input("Please insert coins.\n How many quarters?:")) * 0.25
    total += float(input("How many dimes?:")) * 0.1
    total += float(input("How many nickels?:")) * 0.05
    total += float(input("How many pennies?:"))
    return total


def interface():
    global profit
    go = True
    while go:
        u_inp = input("What would you like? (espresso/latte/cappuccino) ")
        check_ingr(u_inp)
        total = process_coins()
        if total < MENU[u_inp]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            interface()
        profit += MENU[u_inp]["cost"]
        change = float(total - MENU[u_inp]["cost"])
        print(f"here is {change:.2f}$ change.\nHere is your {u_inp} ☕. Enjoy!")
        machine(u_inp)


interface()
