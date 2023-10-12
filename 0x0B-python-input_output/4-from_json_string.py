#!/usr/bin/python3
import json

"""
This funct returns an object represented by a JSON string
"""


def from_json_string(my_str):
    """Convert the JSON string to a Python data structure"""
    return json.loads(my_str)
