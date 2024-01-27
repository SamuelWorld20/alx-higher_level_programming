#!/usr/bin/python3
"""
    Takes in a URL sends a request to it
    and displays the value of the X-Request-Id
    variable using requests library
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    response = requests.get(url)
    headers = response.headers
    print(headers.get('X-Request-Id'))
