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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
