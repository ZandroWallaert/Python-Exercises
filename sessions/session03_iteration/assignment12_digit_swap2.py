"""
# Full Digit Swap Extra
Take one integer as input.
Output the number with the digits reversed but keep the sign.
Leading zeros are not allowed.

## Examples:
    > 1234
    4321

    > -4321
    -1234

    > -700
    -7
"""

n = int(input())
teken = 1
if n < 0:
    teken = -1
    n = -n
res = 0
while n != 0:
    res = res * 10 + n % 10
    n //= 10
print(teken * res)