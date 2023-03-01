# #We are using class to find the area of a circle
# create a class called circle and initialize it with radius
# create two methods that will compute area and perimeter 
from math import pi
class Circle: 
        def __init__(self,  radius):
         self.radius = radius

        def area(self):
                return(self.radius ** 2 * pi)#formula to calculte area of a circle
        def perimeter (self):
              return(2*(self.radius * pi))


C = Circle(4)
print("Area of the circle is = ",C.area())
print("Area of the circle is = ",C.perimeter())