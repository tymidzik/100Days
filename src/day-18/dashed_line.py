from turtle import Turtle, Screen

joe = Turtle()

for i in range(15):
    joe.forward(10)
    joe.up()
    joe.forward(10)
    joe.down()

screen = Screen()
screen.exitonclick()