"""
Program the turtle to show all possible RGB colors.
"""

# Explore RGB colour
from turtle import *


def square(a, c):
    fillcolor(c)
    begin_fill()
    for i in range(4):
        forward(a)
        left(90)
    end_fill()


def rg_square(a, blue=0, N=10):
    # N+1 little squares wide so ...
    a = a / (N + 1)
    start = position()
    for i in range(N + 1):
        green = i / N
        # Go to start of row i
        setposition(start + (0, i * a))
        for j in range(N + 1):
            # Draw square j on row i
            red = j / N
            c = (red, green, blue)
            square(a, c)
            forward(a)
    setposition(start)


from time import sleep


def rgb_cube(a, N=10):
    for b in range(N):
        blue = (b + 1) / N
        rg_square(a, blue, N)
        sleep(1)
        update()


# Program
hideturtle()
penup()
bgcolor((0, 0, 0))
tracer(0)

rgb_cube(200)
turtle.exitonclick()