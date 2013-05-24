#!/usr/bin/env python
"""
Script for recursive binary search in a sorted array
"""
from __future__ import division

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

data.sort()

item = "horse"

first = 0
last = len(data) - 1
found = False


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


print binary_search(first, last)
print data.index(item)
