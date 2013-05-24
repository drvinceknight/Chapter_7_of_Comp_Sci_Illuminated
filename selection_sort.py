#!/usr/bin/env python
"""
Script for selection sort
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

# Shuffling the data so that we have something to sort:
random.shuffle(data)

# Printing the data to screen
print "Sorting the following list:"
for e in data:
    print "\t", e

# Initialisation
firstUnsorted = 0

# The algorithm
while firstUnsorted < len(data) - 1:
    # Find smallest unsorted item
    indexOfSmallest = firstUnsorted
    index = firstUnsorted + 1
    while index <= len(data) - 1:
        if data[index] < data[indexOfSmallest]:
            indexOfSmallest = index
        index += 1
    # Swap firstUnsorted with smallest
    data[firstUnsorted], data[indexOfSmallest] = data[indexOfSmallest], data[firstUnsorted]
    firstUnsorted += 1

# Printing sorted data to screen
print "Here is the sorted list:"
for e in data:
    print "\t", e
