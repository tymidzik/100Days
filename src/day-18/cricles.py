from turtle import Turtle
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


j = Turtle()
j.speed("fastest")
circles = 90

for i in range(circles):
    random_color()
    j.circle(100)
    j.left(360/circles)
