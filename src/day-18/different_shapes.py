from turtle import Turtle
from random import choice

joe = Turtle()
sides = 3
colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan",
          "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]

while True:
    for i in range(sides):
        joe.color(choice(colors))
        joe.forward(100)
        joe.left(360/sides)
    sides += 1
