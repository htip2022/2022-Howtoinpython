#!/usr/bin/env python3

# Pythagoras Theorem
''' c = square root(a^2 + b^2)'''
import math

a = int(input('Length of the leg A of a right triangle a: '))
b = int(input('Length of the leg B of a right triangle b: '))
# print(math.sqrt(25))

leg_a = math.pow(a, 2)
leg_b = math.pow(b, 2)
leg_c = leg_a + leg_b
c = math.sqrt(leg_c)
print(f"Length of the hypotenuse C is = {c}")
hypotenuseC = round(c, 4)
print(f"Length of the hypotenuse C is = {hypotenuseC}")
