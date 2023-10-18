#!/usr/bin/python3
"""Student class module
"""


class Student:
    """initialising attributes"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
                attrs = self.__dict__.keys() 

        json_rep = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_rep[attr] = getattr(self, attr)

        return json_rep
