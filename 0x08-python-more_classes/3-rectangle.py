#!/usr/bin/python3
"""
Module 3-rectangle
Defines a rectangle with private attributes width and height,
public attributes area and perimeter,
and can print the rectangle with # characters.
"""


class Rectangle:
    """Defines a rectangle by the size of its sides."""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle with a width and height.
        The default size is 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle.
        If value is not an integer, a TypeError is raised.
        If value is negative, a ValueError is raised.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
            """Returns the height of the Rectangle."""
            return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle.
        If value is not an integer, a TypeError is raised.
        If value is negative, a ValueError is raised.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the Rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the Rectangle.
        If the Rectangle's width or height is 0, returns an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        """Returns a string representation of the Rectangle
        that can be used to create a new instance of the class.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

