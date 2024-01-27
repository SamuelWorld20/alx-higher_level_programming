#!/usr/bin/python3
"""
   Takes in username and password
   and displays user's id using GitHub API
"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    auth = HTTPBasicAuth(username, password)
    res = requests.get(url, auth=auth)
    user_data = res.json()
    print(user_data.get('id'))
