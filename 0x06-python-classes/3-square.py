#!/usr/bin/python3
"""class Square that defines a square by:
    Private instance attribute: size
    Instantiation with optional size
    size must be an integer, otherwise raise a TypeError
    exception with the message size must be an integer
    if size is less than 0, raise a ValueError exception
    with the message size must be >= 0
    Public instance method: def area(self): that returns
    the current square area
"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Private instance attribute size instantiated with size"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        elif type(size) is int and size >= 0:
            self.__size = size

    def area(self):
        """Calculates area of the square
        Returns:
            the area of the square
        """
        return self.__size ** 2
