#using functions to get the area of a sphere
from math import pi
'''def area(radius):
    return 4 * math.pi * radius**2
print(area(45))'''
def area(radius):
    print("Area of the sphere is = ", 4*pi*radius**2)
radius = int(input("Enter the radius:"))
area(radius)