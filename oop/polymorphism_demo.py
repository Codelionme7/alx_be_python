# polymorphism_demo.py
import math

class Shape:
    def area(self):
        """
        Calculates the area of the shape.
        Raises an error if the subclass doesn't implement it.
        """
        raise NotImplementedError("Subclasses must override this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate area for Rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """Initialize with radius."""
        self.radius = radius

    def area(self):
        """Calculate area for Circle (π * r^2)."""
        return math.pi * (self.radius ** 2)