#!/usr/bin/python3

"""
This funct appends a string at the end of a text file (UTF8)
It returns the number of characters passed in
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        """return number of characters"""
        return len(text)
