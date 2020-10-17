"""
# Area of a disk (circle)
Write a program that reads the radius of a circle (``float``), and computes and prints the area.
When a negative radius is supplied, the program replies with a ```?```.


**Hint:** In Python you can represent π by using ``math.pi``. To use ``math.pi``, however, one needs
to import ``math`` first. (This is done for you in this file)
"""

import math
a = float(input())
if a < 0:
    print('?')
else:
    print(a*a*math.pi)