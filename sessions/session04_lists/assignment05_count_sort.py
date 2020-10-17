"""
# Count sort
Write a program that asks for numerical input (integers) between 0 and 99.
When the users inputs a number outside this interval the program stops asking input.

Finally, print all the number that where entered from small to large.
Numbers that were entered multiple times, however, are only printed once.


## Example
    > 3
    > 2
    > 1
    > 3
    > 5
    > 3
    > 1
    > -10
    1
    2
    3
    5
"""

number = int(input("number "))
array = []
array.append(number)
while 0 <= number and number <= 99:
    number = int(input("number "))
    array.append(number)
del array[-1]
array = sorted(array)
def remove(duplicate):
	final_list = []
	for num in duplicate:
		if num not in final_list:
			final_list.append(num)
	return final_list
print(remove(array))