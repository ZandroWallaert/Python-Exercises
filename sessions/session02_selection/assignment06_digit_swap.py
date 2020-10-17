"""
# Digit Swap
The one number (``int``) as input.
If the number has exactly two digits, the program swaps both digits.
Otherwise the number is printed as is.
The sign of the number is **always** preserved.

## Examples:
    > 1234
    1234

    > -1234
    -1234

    > -4
    -4

    > 6
    6

    > 34
    43

    > -12
    -21

    > -70
    -07
"""
number = int(input())

if number < 0:
    print('-', end='')
    number = -number
if 9 < number < 100:
    number1 = str(number % 10)
    number2 = str(number // 10)
    print(number1 + number2)
else:
    print(number)
