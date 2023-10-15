#!/usr/bin/python3
"""Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle with width, height, and position.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructs the rectange's attributes

        Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

        Args:
             value(int): value of the rectangle
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the recangle

        Args:
            value(int): value of the rectangle
        """
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The x-coordinate of the top-left corner of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets x value

        Args:
            value(int): value of the rectangle
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The y-coordinate of the top-left corner of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets y value

        Args:
            value(int): value of the rectangle
        """
        if type(value) not in [int]:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
