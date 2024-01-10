#!/usr/bin/python3
"""Defination of a class Square."""


class Square:
    """
        defines a square by size.
    """
    def __init__(self, size=0):
        """
            Args:
                size: the size of the square.
        """
        self.size = size

    def area(self):
        """ returns the current square area """
        return (self.__size ** 2)

    @property
    def size(self):
        """to retrive the size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
