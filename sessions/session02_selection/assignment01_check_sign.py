"""
# Check Sign
Read one integer (int).
The program prints a ```+``` when the number is positive or zero.
The program prints a ```-``` when the number is negative.
"""

a = int(input())
if a >= 0:
    print('+')
elif a < 0:
    print('-')