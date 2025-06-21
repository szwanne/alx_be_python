import math

# Base Class: Shape


class Shape:
    def area(self):
        """
        Abstract method to compute the area.
        Should be overridden by subclasses.
        """
        raise NotImplementedError(
            "Subclasses must implement the area() method.")

# Derived Class: Rectangle


class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Initialize Rectangle with length and width.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Compute the area of the rectangle (length × width).
        """
        return self.length * self.width

# Derived Class: Circle


class Circle(Shape):
    def __init__(self, radius):
        """
        Initialize Circle with a radius.
        """
        self.radius = radius

    def area(self):
        """
        Compute the area of the circle (π × radius²).
        """
        return math.pi * (self.radius ** 2)
