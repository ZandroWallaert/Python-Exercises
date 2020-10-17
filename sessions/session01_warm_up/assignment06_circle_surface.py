"""
# Area of a disk (circle)
Write a program that reads the radius of a circle (``float``), and computes and prints the area.
You can ignore negative radiuses by treating them as regular radiuses.


**Hint:** In Python you can represent π by using ``math.pi``. To use ``math.pi``, however, one needs
to import ``math`` first. (This is done for you in this file)
"""

import math

x = float(input())
solution = x * x * math.pi
print(solution)
