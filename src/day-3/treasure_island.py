print('''
  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
                                                                           
                                                                           
           88           88                                 88  
           ""           88                                 88  
                        88                                 88  
 ,adPPYba, 88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
a8P_____88 88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
8PP""""""" 88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
"8b,   ,aa 88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
 `"Ybbd8"' 88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8  
''')

print("Welcome to Treasure Iland\n Your mission is to find the treasure.")

way = input("Do you want to go left or right?").lower()
if way == "left":
    print("You fall into a hole.\n GAME OVER")
else:
    swim = input("You get to a lake. Do you swim to island or wait for boat?").lower()
    if swim == "swim":
        print("You got attacked by trout.\n GAME OVER")
    else:
        door = input("You got to island. You see 3 doors. Which do you choose-red, yellow, blue?").lower()
        if door == "red":
            print("YOU WIN")
        elif  door == "blue":
            print("You've been eaten by beasts.\n GAME OVER")
        else:
            print("You getr burned by fire.\n GAME OVER")