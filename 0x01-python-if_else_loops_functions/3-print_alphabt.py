#!/usr/bin/python3
letter = 'a'
alphabet = ""
while letter <= 'z':
    if letter == 'q' and letter == 'e':
        alphabet += letter
        letter = chr(ord(letter) + 1)

print("{}".format(alphabet), end='')
