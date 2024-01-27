#!/usr/bin/python3
"""
   Takes in a letter and sends a POST
   request to a URL with the letter as a parameter
"""
import requests
import sys

if __name__ == '__main__':
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = 'http://0.0.0.0:5000/search_user'

    res = requests.post(url, data={'q': q})

    try:
        response = res.json()
        if response == {}:
            print("No result")

        else:
            print("[{}] {}".format(response.get('id'), response.get('name')))

    except ValueError:
        print("Not a valid JSON")
