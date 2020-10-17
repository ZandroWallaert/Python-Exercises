"""
Program the turtle to ask for a new color (string).
Change the color of the turtle and make it move differently depending on the color.
You can choose which colors you want to support and which drawings you want to make
(you are the programmer now, you make the decisions).

**Hint:** Lookup how the change the color of the turtle.
(http://lmgtfy.com/?q=python+turtle+change+color)
"""
import turtle
color = str(input("Give me a color to draw with (green, red, magenta, black) "))
if color == 'green':
    turtle.color("green")
    turtle.shape("square")
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
elif color == 'red':
    turtle.color("red")
    turtle.shape("triangle")
    turtle.left(45)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(-135)
    turtle.forward(70.71)
elif color == 'magenta':
    turtle.color("magenta")
    turtle.shape("circle")
    turtle.circle(100)
elif color == 'black':
    turtle.color("black")
    turtle.shape("turtle")
    turtle.left(20)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.left(30)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.left(40)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
turtle.exitonclick()
