#!/usr/bin/python3
letter = 'a'
while letter <= 'z':
    print(letter, end='')
    letter = chr(ord(letter) + 1)
