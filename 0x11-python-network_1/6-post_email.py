#!/usr/bin/python3
"""
   Takes in a URL and a email
   sends a post request to the URL with the email as param
   displays the body of the response in utf-8
   using requests library
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}

    response = requests.post(url, data)
    content = response.text
    print(content)
