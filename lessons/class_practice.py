"""Practice with classes"""

import math


class Circle:
    radius: float

    def __init__(self, r: float):
        self.radius = r

    def area(self) -> float:
        return math.pi * (self.radius) ** 2


class Rectangle:
    width: float
    height: float

    def __init__(self, w: float, h: float):
        self.width = w
        self.height = h

    def area(self) -> float:
        return self.width * self.height


circ: Circle = Circle(r=2.0)
print(circ.area())
rect: Rectangle = Rectangle(w=4.0, h=5.5)
print(rect.area())
