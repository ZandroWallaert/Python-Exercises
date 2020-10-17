"""
# Highest frequency (II)
Write a program that asks for numerical input (integers) between 0 and 99.
When the users inputs a number outside this interval the program stops asking input.

Finally, print the number that was entered the most.
You can print 0 if there was no valid input.
Print all numbers that apply (small to large).

## Examples:

    > 3
    > 2
    > 1
    > 3
    > 5
    > 3
    > 1
    > -10
    3

    > 1
    > 3
    > 2
    > 1
    > 3
    > 5
    > 3
    > 1
    > 678
    1
    3
"""
lijst = [0]*100

getal = int(input("Geef een getal in:"))
if getal <= -1 or getal >= 100:
    print("0")
else:

    while getal > -1 and getal < 100:
        lijst[getal] += 1
        getal = int(input("Geef een getal in:"))

    count = 0
    grootsteGetal = 0
    index = 0
    laatsteCount = 0
    laatsteGetal = 0
    while count != 100:
        if lijst[count] >= laatsteCount:
            laatsteCount = lijst[count]
            laatsteGetal = count
        count += 1

    #laatsteCount is het aantal keer dat is gedaan
    RijGetallen = ""
    count = 0
    while count != 100:
        if lijst[count] == laatsteCount:
            RijGetallen += str(count) + " "
        count += 1
    print(RijGetallen[:-1])