import math

class Shape:
    def area(self): # this write just for telling structured of inherited class look like and just its a Abstract type method just implementing
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height =height
    
    def area(self):
        return 0.5 * self.base * self.height

radius = float(input("Enter the radius of the circle: "))
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
shapes = [
    Circle(radius),
    Rectangle(length, width),
    Triangle(base, height)
]

c1 = Circle(radius)
print("Interspection:",c1.__class__.__name__) # this is a introspection function

for s in shapes:
    print(f"{s.__class__.__name__} Area: {s.area():.2f}")
