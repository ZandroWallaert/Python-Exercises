"""
# Check Sign (2)
Read one integer (int).
The program prints a ```+``` when the number is positive.
The program prints a ```-``` when the number is negative.
The program prints a ```0``` when the number is zero.
"""
a =int(input())
if a > 0:
    print('+')
elif a < 0:
    print('-')
elif a == 0:
    print('0')