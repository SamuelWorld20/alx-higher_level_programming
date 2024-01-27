#!/usr/bin/python3
"""
   Takes in a URL and a email
   sends a post request to the URL with the email as param
   displays the body of the response in utf-8
"""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')

    request = urllib.request.Request(url, data=encoded_data)
    with urllib.request.urlopen(request) as res:
        print(res.read().decode('utf-8'))
