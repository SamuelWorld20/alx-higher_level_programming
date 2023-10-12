#!/usr/bin/python3
import json

"""
This funct turns an object into JSON
representation
"""


def to_json_string(my_obj):
    """convert the object into a JSON formatted string"""
    return json.dumps(my_obj)
