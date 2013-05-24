#!/usr/bin/env python
"""
Script for binary search in a sorted array
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

while first <= last and not found:
    middle = int((first + last) / 2)
    if item == data[middle]:
        found = True
    elif item < data[middle]:
        last = middle - 1
    else:
        first = middle + 1

print middle
print data.index(item)
