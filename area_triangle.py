# Python Program to find the area of a Triangle
# semi_perimeter = (side1+side2+side3)/2
# area = √(semi_perimeter*(semi_perimeter-side1)*(semi_perimeter-side2)*(semi_perimeter-side3))
#

import math

# inputs from the user
side1 = float(input('Enter first side: '))
side2 = float(input('Enter second side: '))
side3 = float(input('Enter third side: '))

# calculate the semi-perimeter
semi_perimeter = (side1 + side2 + side3)/2

# calculate the area
tarea = math.sqrt(semi_perimeter*(semi_perimeter-side1)*(semi_perimeter-side2)*(semi_perimeter-side3))

print('The area of the triangle is', tarea)