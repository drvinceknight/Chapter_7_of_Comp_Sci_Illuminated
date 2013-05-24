#!/usr/bin/env python
"""
Script for binary search in a sorted array
"""
from __future__ import division

# An array:
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

# Making sure the array is sorted (binary search needs a sorted array)
data.sort()

# The item we are going to search for:
item = "horse"

# Some basic initialisation
first = 0
last = len(data) - 1
found = False

# The algorithm
while first <= last and not found:
    middle = int((first + last) / 2)
    if item == data[middle]:
        found = True
    elif item < data[middle]:
        last = middle - 1
    else:
        first = middle + 1

print middle
