# import colorgram
#
#
# colors = colorgram.extract('image.jpg', 30)
# colors_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     colors_list.append(new_color)
#
# print(colors_list)

import turtle as t
from turtle import Screen
from random import choice

colors_list = [(201, 164, 112), (152, 75, 49), (221, 201, 138), (171, 153, 42), (56, 95, 126), (139, 31, 19), (134, 163, 184), (197, 93, 73), (48, 121, 88), (98, 75, 77), (142, 178, 148), (75, 41, 33), (165, 145, 156), (15, 99, 71), (234, 175, 164), (54, 45, 47), (32, 61, 77), (145, 21, 25), (21, 83, 89), (182, 205, 175), (85, 147, 127), (44, 66, 87), (178, 94, 98), (222, 177, 184), (8, 68, 51), (108, 127, 151)]
t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.ht()
tim.setheading(225)
tim.forward(400)
tim.setheading(0)
x_coordinate = tim.xcor()
y_coordinate = tim.ycor()

for _ in range(10):
    for _ in range(10):
        color = choice(colors_list)
        tim.dot(20, color)
        tim.forward(50)
    y_coordinate += 50
    tim.goto(x_coordinate, y_coordinate)





screen = Screen()
screen.exitonclick()


