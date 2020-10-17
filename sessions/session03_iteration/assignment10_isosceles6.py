"""
# Isosceles 6
Write a program similar to "Isosceles 5".
This time the triangle is centered and has its top at the bottom.

## Example
    > -3
    > 0
    > 5
    *****
     ***
      *

    > -3
    > 0
    > 4
    ****
     **
"""

base = int(input())
count = 0
height = 1
while base < 1:
    base = int(input())
if base%2 == 0:
    aantalspaties = 0
    aantalsterren = base
    height = base/2
else:
    aantalspaties = 0
    aantalsterren = base
    height = base%2+((base-1)/2)
while height > count:
    print(aantalspaties*' '+aantalsterren*'*')
    aantalspaties += 1
    aantalsterren -= 2
    count += 1
