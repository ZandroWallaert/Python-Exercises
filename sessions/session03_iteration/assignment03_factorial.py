"""
# Factorial
Ask for a positive number (``int``) as input and output its factorial.

The factorial of a number n is n! with n! = n * (n-1) * ... * 3 * 2 * 1
"""
import math

number = int(input("positive number: "))
if number < 0:
    result = 1
else:
    result = math.factorial(number)
print(result)