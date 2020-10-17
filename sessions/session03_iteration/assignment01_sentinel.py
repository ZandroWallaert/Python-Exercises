"""
# Sentinel
Keep on asking for input (``int``) until a zero is entered.
Print the number of (non-zero) inputs.

## Example:
    > 1
    > -2
    > 3
    > -4
    > 0
    4
"""
x = int(input())
count = 0
while x != 0:
    x = int(input())
    count += 1
print(count)