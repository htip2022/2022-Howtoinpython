#!/usr/bin/env python3

# print('pi:\u03C0')

# Area of a circle

import math
''' Circle Area = π*r^2'''

radio = int(input('Indicate radio of a circle: '))
pi = math.pi

# Method 01

area = pi * radio ** 2
print(f"circle area is = {area}")

# Method 02
area = pi * (math.pow(radio, 2))
print(f"circle area is = {area}")

area = round(area, 4)
print(f"circle area is = {area}")
