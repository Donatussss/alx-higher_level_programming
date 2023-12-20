#!/usr/bin/python3
"""class Square that defines a square by:
Private instance attribute: size
property def size(self): to retrieve it
property setter def size(self, value): to set it:
    size must be an integer, otherwise raise a TypeError
    exception with the message size must be an integer
    if size is less than 0, raise a ValueError exception
    with the message size must be >= 0
Instantiation with optional size
Public instance method:
    def area(self): that returns the current square area
"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Private instance attribute size instantiated with size"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        elif type(value) is int and value >= 0:
            self.__size = value

    def area(self):
        """Calculates area of the square
        Returns:
            the area of the square
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
