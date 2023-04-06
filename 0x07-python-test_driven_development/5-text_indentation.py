#!/usr/bin/python3

def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): the size length of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
