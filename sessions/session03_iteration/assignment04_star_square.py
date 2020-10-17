"""
# Star Square
Write a program that asks for two numerical inputs (``int``): the height and the width of a rectangle.
Print such a rectangle on screen using ``*``.

The program has no output if either the height or the width is negative.

## Example:
    > 4
    > 3
    ***
    ***
    ***
    ***
"""

height = int(input())
width = int(input())
hcount = 0
while height > hcount:
        print(width*("*"))
        hcount += 1