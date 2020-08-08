# polygon

""" import turtle

poly = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
    poly.forward(side_length)
    poly.right(angle)
turtle.done """

import turtle

ninja = turtle.Turtle()
ninja.speed(100)
for i in range(180):
    ninja.forward(100)
    ninja.right(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0,0)
    ninja.pendown()
    ninja.right(2)
turtle.done()
