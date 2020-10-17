"""
# Euclid
Write a program that reads two positive integers (no need to check the input).
Print out the largest divisor that both numbers have in common (greatest common divisor, GCD or "grootste gemene deler")

**Hint:** use Euclid's algorithm:
    https://en.wikipedia.org/wiki/Euclidean_algorithm
    https://nl.wikipedia.org/wiki/Algoritme_van_Euclides#Het_algoritme
"""

x = int(input())
y = int(input())
r = x % y
while r != 0:
    x = y
    y = r
    r = x % y
print(y)