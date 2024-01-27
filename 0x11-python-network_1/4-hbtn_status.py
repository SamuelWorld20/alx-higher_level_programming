#!/usr/bin/python3
""" fetches a given URL status """
import requests

if __name__ == '__main__':
    response = requests.get('https://alx-intranet.hbtn.io/status')
    content = response.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
