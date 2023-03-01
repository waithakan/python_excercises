#here we are going to prompt the user jto enter input so that we can calculate the area and perimeter
legth = int(input("Enter lenght of the rectangle :"))
width = int(input("Enter width of rectangle :"))
class Rectangle:
    def __init__(self, width, lenght):
        self.width = width
        self.length = lenght
    
    def area (self):
        return(self.width * self.length)
    
    def perimeter (self):
        return(2 * (self.width + self.length))
    
r = Rectangle(width, legth)
print("Area of rectangle is =", r.area())
print("Perimeter of the ractangle is = ", r.perimeter())