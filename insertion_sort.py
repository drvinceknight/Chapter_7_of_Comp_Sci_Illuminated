#!/usr/bin/env python
"""
Script for insertion sort (a modification of the bubble sort algorithm)
"""
from __future__ import division
import random

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

# Shuffling the data to make sure we have something to sort
random.shuffle(data)

# Print to screen
print "Sorting the following list:"
for e in data:
    print "\t", e

# Initialisation
current = 1

# The algorithm
while current < len(data):
    index = current
    placeFound = False
    while index > 0 and not placeFound:
        if data[index] < data[index - 1]:
            # Swapping elements 'remnants of the bubbling algorithm'
            data[index], data[index - 1] = data[index - 1], data[index]
            index -= 1
        else:
            placeFound = True
    current += 1

# Printing sorted data to screen
print "Here is the sorted list:"
for e in data:
    print "\t", e
