#!/usr/bin/env python
"""
Script for bubble sort
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

# Shuffling the data
random.shuffle(data)

# Printing the data to sort to screen
print "Sorting the following list:"
for e in data:
    print "\t", e

# Initialisation
firstUnsorted = 0
swap = True

# The algorithm
while firstUnsorted < (len(data) - 1) and swap:
    swap = False
    index = len(data) - 1
    while index > firstUnsorted:
        if data[index] < data[index - 1]:
            # Swapping two elements 'bubbling up'
            data[index], data[index - 1] = data[index - 1], data[index]
            swap = True
        index -= 1
    firstUnsorted += 1

# Printing the results to screen
print "Here is the sorted list:"
for e in data:
    print "\t", e
