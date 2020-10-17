"""
Write the functions ```gcd``` (greatest common divisor), ```swap_digits```, ```factorial```, ```avg``` (average),
```largest_prime```, and ```variation```.

All these functions should be written such that the tests succeed.
Take a look at your previous programs for the algorithms.
The focus of this exercise, is to decide which parameters to use and what your function should return.
"""
from math import *

def gcd(x, y):
    r = x % y
    while r != 0:
        x = y
        y = r
        r = x % y
    return y

def swap_digits(n):
    sign = 1
    if n < 0:
        sign = -1
        n = -n

    res = 0
    while n != 0:
        res = res * 10 + n % 10
        n //= 10

    return sign * res

def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def avg(numbers):
    som = 0
    aantal = 0
    for i in range(len(numbers)):
        som += numbers[i]
        aantal += 1
    if aantal == 0:
        return nan
    else:
        return som / aantal

def largest_prime(n):
    isPrime = [True] * (n + 1)
    maxPrime = nan
    for i in range(2, n + 1):
        if isPrime[i]:
            maxPrime = i
            multiples = (n + 2) // i
            for j in range(2, multiples):
                isPrime[j * i] = False
    return maxPrime

def variation(n, k):
    if n < 0 or k < 0: return 0
    res = 1
    for i in range(n - k + 1, n + 1):
        res *= i
    return res
