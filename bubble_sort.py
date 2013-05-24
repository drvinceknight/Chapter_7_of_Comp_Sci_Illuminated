#!/usr/bin/env python
"""
Script for bubble sort
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

firstUnsorted = 0
swap = True
while firstUnsorted < (len(data) - 1) and swap:
    swap = False
    index = len(data) - 1
    while index > firstUnsorted:
        if data[index] < data[index - 1]:
            data[index], data[index - 1] = data[index - 1], data[index]
            swap = True
        index -= 1
    firstUnsorted += 1

print "Here is the sorted list:"
for e in data:
    print "\t", e
