"""
Program the turtle to ask a number.
Regardless of the sign of the number (positive or negative),
the turtle should move a distance, proportionally to the input.
For example: -100 or 100 will make the turtle move further to the right than -5 or 5.

Then make a 45° turn - upwards when the input was positive, downwards when the input was negative.
Finally, move the turtle again over the same distance as before in its new direction.

For positive input the turtle draws something like this:
    /
>--/

For negative input the turtle draws something like this:
>--\
    \

"""
import turtle
number = int((input("Give me a number ")))
turtle.forward(abs(number))
if number < 0:
    turtle.left(135)
    turtle.forward(number)
else:
    turtle.left(45)
    turtle.forward(number)
turtle.exitonclick()
