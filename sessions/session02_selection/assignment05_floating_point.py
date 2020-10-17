"""
# Oh-point-three
Write a program that takes two numbers (``float``) as input.
The program outputs ``equal`` if the sum of both numbers equals 0.3 or ``not equal`` in the other case.

**Hint:** reflect on how a computer stores decimal numbers when your program behaves unexpectedly.

## Examples:
    > 0.5
    > -0.2
    equal

    > 0.3
    > 0
    equal

    > 0.4
    > -0.2
    not equal
"""
a = float(input())
b = float(input())
if a + b == 0.3:
    print('equal')
else:
    print('not equal')