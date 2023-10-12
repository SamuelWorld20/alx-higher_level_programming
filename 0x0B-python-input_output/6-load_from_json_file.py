#!/usr/bin/python3

"""
This funct creates an object from a JSON file
"""


import json


def load_from_json_file(filename):
    """Load and parse the JSON data from the file"""
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)
