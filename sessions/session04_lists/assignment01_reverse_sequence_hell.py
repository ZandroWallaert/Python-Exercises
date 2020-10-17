"""
# Reverse sequence hell
Write a program that asks for 100 numerical inputs and outputs them in reverse order.
"""
array = []
count = 0
while count < 100:
    i = input("Give me a number ")
    count += 1
    array.append(i)
array.reverse()
print(*array, sep="\n")