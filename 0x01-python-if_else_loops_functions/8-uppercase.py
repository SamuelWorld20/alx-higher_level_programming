#!/usr/bin/python3
def uppercase(str):
    string = ""
    for char in str:
        if 'a' <= char <= 'z':
            uppercase = chr(ord(char) - 32)
            string += uppercase
        else:
            string += char

    print("{}".format(string))
