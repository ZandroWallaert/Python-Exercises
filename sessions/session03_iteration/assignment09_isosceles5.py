"""
# Isosceles 5
Write a program similar to "Isosceles 2".
This time triangle is centered and has its top on top.
Watch out, not all triangle have a top with 1 star. Some have two stars.

## Example
    > -3
    > 0
    > 5
      *
     ***
    *****

    > -3
    > 0
    > 4
     **
    ****
"""

base = int(input())
count = 0
height = 1
while base < 1:
    base = int(input())
if base % 2 == 0:
    aantalsterren = (base%2)+2
    aantalspaties = int(base/2)-1
    height = int(base/2)
else:
    aantalsterren = base%2
    aantalspaties = int((base-1)/2)
    height = base%2+((base-1)/2)
while height > count:
    print(aantalspaties*' '+aantalsterren*'*')
    aantalspaties -= 1
    aantalsterren += 2
    count += 1