"""
Program the turtle to draw a stairs with 4 steps.
The height and width of these steps should be provided by the user.
Can you do this using only ``forward`` and ``left``?
"""

import turtle

print("Height?")
a = float(input())
print("Width?")
b = float(input())
turtle.left(90)
turtle.forward(a)
turtle.left(270)
turtle.forward(b)
turtle.left(90)
turtle.forward(a)
turtle.left(270)
turtle.forward(b)
turtle.left(90)
turtle.forward(a)
turtle.left(270)
turtle.forward(b)
turtle.left(90)
turtle.forward(a)
turtle.left(270)
turtle.forward(b)
turtle.left(270)
turtle.forward(a*4)
turtle.left(270)
turtle.forward(b*4)

turtle.exitonclick()