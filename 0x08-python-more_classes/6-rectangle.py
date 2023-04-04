#!/usr/bin/python3
"""
Module 6-rectangle
Defines a Rectangle class with private instance attributes
width and height and public area and perimeter methods.
"""


class Rectangle:
    """
    A Rectangle class with private attributes and public methods
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter for the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        Setter for the height attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Computes the area of this Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes the perimeter of this Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of this Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """
        Returns a string representation of this Rectangle
        """
        return "Rectangle({:d}, {:d
