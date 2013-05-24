#!/usr/bin/env python
"""
Script for the Square root algorithm of Chapter 7
"""
from __future__ import division
from sys import argv

if len(argv) != 2:
    print "Single number as argument"
else:
    square = eval(argv[1])
    guess = square / 4
    epsilon = 1
    while epsilon > .001:
        guess = (guess + square / guess) / 2
        epsilon = abs(square - guess ** 2)
        print square, guess
