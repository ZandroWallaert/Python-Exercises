"""
# Odd or Even
Make a program print ``odd`` or ``even`` depending on the input (``int``).

**Hint:** A number is even when it is divisible by two. Use the ``%```operator.

## Examples
    > 2
    even

    > 3
    odd
"""
a = int(input())
if a%2 == 0:
    print('even')
else:
    print('odd')