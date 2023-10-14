#!/usr/bin/python3
"""
Base class
"""


class Base:
    """Represent the class Base
    This is used as a foundation for other classes
    to manage the id attribute consistently and
    avoid duplicating code for generating unique IDs
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Creates an instance of the 'id' class.

        Parameters:
        id (int): An integer representing the class identifier.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
