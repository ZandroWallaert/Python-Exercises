"""
# Highest frequency (II)
Write a program that asks for numerical input (integers) between 0 and 99.
When the users inputs a number outside this interval the program stops asking input.

Finally, print the number that was entered the most.
You can print 0 if there was no valid input.
If multiple numbers apply, print the largest.

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
    3
"""
numbinp = int(input())
numbmost = 0
numblist = [0]*100
if 0 <= numbinp <= 99:
    while 0 <= numbinp <= 99:
        numblist[numbinp] += 1
        if numblist[numbinp] > numbmost:
            numbmost = numbinp
        elif numblist[numbinp] == numblist[numbmost]:
            if numbinp > numbmost:
                numbmost = numbinp
        numbinp = int(input())
    print(numbmost)
else:
    print("0")