'''def area(x, y):
    print("x * y =",x*y)
area(5, 4)'''
#program to find area of a circle using functions
'''import math
def area(radius):
    return math.pi * radius**2
print(area(7))'''
#second method
from math import pi
def area(radius):
    print("Area of the circle is = ", pi * radius **2)
radius = int(input("Enter the radius: "))
area(radius)