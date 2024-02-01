import random
from turtle import Turtle, Screen

race = False
screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -100
all_turtles = []

for turtle_index in range(0, 6):
    j = Turtle(shape="turtle")
    j.color(colors[turtle_index])
    j.pu()
    j.goto(x=-230, y=y)
    all_turtles.append(j)
    y += 40

if user_bet:
    race = True

while race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.fillcolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")
            race = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
