"""
# Isosceles 1
Write a program that asks for the height of an isosceles right triangle.
This is a right triangle with the two legs (and their corresponding angles) equal.

Print such a triangle on screen using ``*``.
The triangle is left aligned and has its top on top.

Negative or zero heights are not accepted. Keep on asking for a correct height until a positive number is entered.

## Example
    > -3
    > 0
    > 5
    *
    **
    ***
    ****
    *****
"""

height = int(input())
while height < 1:
    height = int(input())
if height > 1:
    aantalspatie = height - 1
    aantalster = 1
    count = 0
    while height > count :
        print('*'*aantalster + ' '*aantalspatie)
        aantalspatie -= 1
        aantalster += 1
        count += 1