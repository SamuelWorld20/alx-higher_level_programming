#!/usr/bin/python3
""" funct to find peak of unsorted integers """
def find_peak(list_of_integers):
    n = len(list_of_integers)

    # check if list is empty
    if n == 0:
        return None

    # Check if the first or last element is a peak
    if n == 1 or list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[n - 1] >= list_of_integers[n - 2]:
        return list_of_integers[n - 1]

    # Iterate through the list to find a peak
    for i in range (1, n - 1):
        if list_of_integers[i] >= list_of_integers[i - 1] and list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]

    return None
