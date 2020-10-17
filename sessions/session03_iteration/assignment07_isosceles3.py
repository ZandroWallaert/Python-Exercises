"""
# Isosceles 3
Write a program similar to "Isosceles 1".
This time the triangle is right aligned and has its top at the bottom.

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
        print(aantalspaties*' '+aantalsterren*'*')
        aantalsterren -= 1
        aantalspaties += 1
        count += 1
