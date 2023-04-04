#!/usr/bin/python3
# -*- coding: utf-8 -*-

def add_integer(a, b=98):
    """Adds two integers

    Args:
        a (int/float): The first number to be added
        b (int/float): The second number to be added (default is 98)

    Returns:
        int: The sum of a and b

    Raises:
        TypeError: If either a or b is not an int or a float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
