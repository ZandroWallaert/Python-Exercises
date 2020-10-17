"""
# Isosceles 4
Write a program similar to "Isosceles 1".
This time triangle is right aligned and has its top on top.

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
        print(' '*aantalspatie+'*'*aantalster)
        aantalspatie -= 1
        aantalster += 1
        count += 1