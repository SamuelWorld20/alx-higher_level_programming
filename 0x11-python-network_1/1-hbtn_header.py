#!/usr/bin/python3
"""
    Takes in a URL sends a request to it
    and displays the value of the X-Request-Id
    variable
"""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as res: 
        headers = res.getheaders()
        print(dict(res.headers).get('X-Request-Id'))
