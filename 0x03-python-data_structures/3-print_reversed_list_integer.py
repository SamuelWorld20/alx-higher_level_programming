#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_list = []
    idx = len(my_list) - 1
    while idx >= 0:
        reversed_list.append(my_list[idx])
        idx -= 1
    for element in reversed_list:
        print("{:d}".format(element))
