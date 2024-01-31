import turtle
from turtle import Turtle
import random

j = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


j.pensize(10)
j.speed("fastest")
directions = [0, 90, 180, 270]

while True:
    j.color(random_color())
    j.setheading(random.choice(directions))
    j.forward(30)
