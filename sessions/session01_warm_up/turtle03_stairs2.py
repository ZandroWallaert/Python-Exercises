"""
Program the turtle to draw a stairs with 4 steps.
The height and width of these steps should be provided by the user.
"""

import turtle
print("Height?")
a = float(input())
print("Width?")
b = float(input())
turtle.left(90)
turtle.forward(a)
turtle.right(90)
turtle.forward(b)
turtle.left(90)
turtle.forward(a)
turtle.right(90)
turtle.forward(b)
turtle.left(90)
turtle.forward(a)
turtle.right(90)
turtle.forward(b)
turtle.left(90)
turtle.forward(a)
turtle.right(90)
turtle.forward(b)
turtle.right(90)
turtle.forward(a*4)
turtle.right(90)
turtle.forward(b*4)

turtle.exitonclick()
