from turtle import Turtle, Screen

j = Turtle()
screen = Screen()
j.speed("fastest")


def move_forwards():
    j.forward(10)


def move_backwards():
    j.backward(10)


def turn_left():
    j.left(5)


def turn_right():
    j.right(5)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=screen.resetscreen)
screen.exitonclick()
