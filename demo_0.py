"""
Problem
-------
print out the area of a circle to 3 decimal places in feet squared

"""

# first pass attempt
# how do we find the area of a circle? pi * radius** 2
# lets just get the area and print it then work from there

from math import pi

radius = int(input('Enter the radius of a circle: '))

area = pi * radius**2

print(f'{area:.3f} ft\u00B2')
