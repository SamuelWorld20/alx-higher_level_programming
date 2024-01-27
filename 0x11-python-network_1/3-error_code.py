#!/usr/bin/python3
"""
   Sends a request to a URL and displays
   the body of the response in utf-8
   with HTTPError handled
"""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
