#!/usr/bin/env python
"""
Script for recursive binary search in a sorted array
"""
from __future__ import division

# Some data
data = [
    "ant",
    "cat",
    "chicken",
    "cow",
    "deer",
    "dog",
    "fish",
    "goat",
    "horse",
    "rat",
    "snake"
]

# Making sure the data is sorted so that binary search will work
data.sort()

# The element we are searching for
item = "horse"

# Some initialisation
first = 0
last = len(data) - 1
found = False


# A function for binary search (which is needed for recursion)
def binary_search(first, last):
    if first > last:
        return False
    middle = int((first + last) / 2)
    if item == data[middle]:
        return middle
    if item < data[middle]:
        return binary_search(first, middle - 1)
    else:
        return binary_search(middle + 1, last)

# Print the binary search
print binary_search(first, last)
