"""
# Isosceles 2
Write a program similar to "Isosceles 1".
This time the triangle is left aligned and has its top at the bottom.

## Example
    > -3
    > 0
    > 5
    *****
    ****
    ***
    **
    *
"""

height = int(input())

while height < 1:
    height = int(input())
if height > 1:
    aantalsterren = height
    aantalspaties = 0
    count = 0
    while height > count:
        print(aantalsterren*'*'+aantalspaties*' ')
        aantalsterren -= 1
        aantalspaties += 1
        count += 1
