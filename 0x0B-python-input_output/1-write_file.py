#!/usr/bin/python3

"""
This funct writes a string to a text file(UTF8)
it returns the number of characters passed in
"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        """return number of characters"""
        return len(text)
