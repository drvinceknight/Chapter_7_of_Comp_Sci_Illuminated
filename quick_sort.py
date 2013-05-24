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


def quicksort(first, last):
    if first < last:
        splitVal = data[first]
        splitPoint = split(splitVal, first, last)
        quicksort(first, splitPoint - 1)
        quicksort(splitPoint + 1, last)


def split(splitVal, first, last):
    left = first
    right = last
    while left <= right:
        while data[left] <= splitVal and left <= right:
            print data[left]
            left += 1
        while data[right] >= splitVal and left <= right:
            right -= 1
        if left < right:
            print data[left], data[right]
            data[left], data[right] = data[right], data[left]
        print data
    splitPoint = right
    return splitPoint

first = 0
last = len(data) - 1


#quicksort(first, last)
split(data[0], first, last)
print "Here is the sorted list:"
for e in data:
    print "\t", e
