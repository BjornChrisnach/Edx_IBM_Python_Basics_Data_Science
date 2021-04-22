
# Import the library

import matplotlib.pyplot as plt
%matplotlib inline


class Circle(object):
    def __init__(self, radius=3, color="red"):
        self.radius = radius
        self.color = color

    def add_radius(self, r):
        self.radius = self.radius + r

    def drawCircle(self):
        pass


class Rectangle(object):
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

    def drawRectangle(self):
        pass


# red_circle = Circle(10, "red")
print(red_circle.radius)
print(red_circle.color)
red_circle.color = "blue"
print(red_circle.color)
c1 = Circle(2, "red")
c1.add_radius(8)
red_circle = Circle()
blue_circle = Circle(10, "blue")

# dir(NameOfObject)
yellow_circle = Circle(10, "yellow")
