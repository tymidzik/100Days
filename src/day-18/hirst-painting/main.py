# import colorgram
#
# colors = colorgram.extract('dot_painting.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
import turtle
import random

turtle.colormode(255)
color = [(207, 160, 82), (54, 89, 130), (145, 91, 40), (140, 27, 49), (222, 206, 108), (132, 176, 203),
         (45, 55, 104),
         (158, 46, 83), (169, 160, 39), (129, 189, 143), (83, 20, 44), (38, 43, 67), (186, 94, 107),
         (186, 140, 170),
         (85, 120, 180), (59, 39, 31), (88, 157, 92), (79, 153, 164), (195, 79, 73), (161, 201, 219), (45, 74, 77),
         (79, 74, 44), (57, 124, 121), (218, 176, 187), (167, 206, 168), (220, 182, 168)]
j = turtle.Turtle()
number_of_vertical_lines = 10
number_of_horizontal_lines = 10


def draw_line():
    for i in range(10):
        random_color = color[random.randint(0, len(color) - 1)]
        j.dot(15, random_color)
        j.pu()
        j.forward(30)
        j.pd()


def next_line(angle):
    j.pu()
    j.setheading(90)
    j.forward(30)
    j.setheading(angle)
    j.forward(30)


for i in range(int(number_of_vertical_lines/2)):
    draw_line()
    next_line(180)
    draw_line()
    next_line(0)
