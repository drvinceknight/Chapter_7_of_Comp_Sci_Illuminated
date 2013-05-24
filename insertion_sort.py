#!/usr/bin/env python
"""
Script for insertion sort (a modification of the bubble sort algorithm)
"""
from __future__ import division
import random

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

random.shuffle(data)
print "Sorting the following list:"
for e in data:
    print "\t", e

current = 1
while current < len(data):
    index = current
    placeFound = False
    while index > 0 and not placeFound:
        if data[index] < data[index - 1]:
            data[index], data[index - 1] = data[index - 1], data[index]
            index -= 1
        else:
            placeFound = True
    current += 1

print "Here is the sorted list:"
for e in data:
    print "\t", e
