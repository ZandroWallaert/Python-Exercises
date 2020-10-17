"""
# Average
Keep on asking for input (``float``) until a zero is entered.
Print the average of these (non-zero) inputs.
Your program should print ``no data` if no non-zero numbers were entered.

## Example:
    > 1.4
    > -2.1
    > 3.0
    > -4
    > 0
    -0.425
"""
array = []
x = 1
while x != 0:
    x = float(input())
    array.append(x)
if x == 0:
    del array[-1]
if (len(array)) == 0:
    print('no data')
else:
    average = sum(array)/(len(array))
    print(average)
