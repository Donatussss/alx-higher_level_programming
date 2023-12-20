#!/usr/bin/python3
"""class Square that defines a square by:
Private instance attribute:
    size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it:
            size must be an integer, otherwise raise a TypeError
            exception with the message size must be an integer
            if size is less than 0, raise a ValueError exception
            with the message size must be >= 0
    position:
        property def position(self): to retrieve it
        property setter def position(self, value): to set it:
            position must be a tuple of 2 positive integers,
            otherwise raise a TypeError exception with the
            message position must be a tuple of 2 positive integers
Instantiation with optional size
Public instance method:
    def area(self): that returns the current square area
    def my_print(self):
        that prints in stdout the square with the character #
        if size is equal to 0, print an empty line
"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Private instance attribute size instantiated with size"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple\
                or (type(value) is tuple and len(value) != 2):
            raise TypeError('position must be a tuple of 2\
 positive integers')
        else:
            for i in value:
                if type(i) is not int or i < 0:
                    raise TypeError('position must be a\
 tuple of 2 positive integers')
            self.__position = value

    def area(self):
        """Calculates area of the square
        Returns:
            the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using #"""
        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print("")
