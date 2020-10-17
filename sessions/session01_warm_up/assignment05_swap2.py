"""
# The Swap Trick (Advanced)
Write a program that reads two integer inputs into the two variables ``a`` and ``b``.
Make sure that the contents of ``a`` and ``b`` are swapped before printing.
You are not allowed to create any other variable.

You can update this Python program, but are not allowed to change it!
**Hint:** Make use of the fact that ``a`` and ``b`` are numbers.
"""

a = int(input())  # do not remove this line
b = int(input())  # do not remove this line

# Write your program here:
a = a + b
b = a - b
a = a - b

print(a, b)  # do not remove this line
