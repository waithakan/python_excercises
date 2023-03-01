#program to use  class calculate the area and perimeter of a rectangle 
#create a class called Rectangle and initialize it with legth and width
# create two methods that will compute area and perimeter 
class Rectangle:
    def __init__(self, width, lenght):
        self.width = width
        self.length = lenght
    
    def area (self):
        return(self.width * self.length)
    
    def perimeter (self):
        return(2 * (self.width + self.length))
    
r = Rectangle(45, 198)
print("Area of rectangle is =", r.area())
print("Perimeter of the ractangle is = ", r.perimeter())