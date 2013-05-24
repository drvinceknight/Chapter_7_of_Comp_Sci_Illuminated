#!/usr/bin/env python
"""
Script for quick sort
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


def split(splitVal, first, last):
    left = first + 1
    right = last
    while left <= right:
        while left <= right and data[left] <= splitVal:
            left += 1
        while left <= right and data[right] >= splitVal:
            right -= 1
        if left < right:
            data[left], data[right] = data[right], data[left]
    splitPoint = right
    return splitPoint


def quicksort(first, last):
    if first < last:
        splitVal = data[first]
        splitPoint = split(splitVal, first, last)
        quicksort(first, splitPoint - 1)
        #print "---\n", data
        quicksort(splitPoint + 1, last)
        #print "***\n", data


first = 0
last = len(data) - 1


quicksort(first, last)
#print "Split value is:", split(data[0], first, last)
print "Here is the sorted list:"
for e in data:
    print "\t", e
