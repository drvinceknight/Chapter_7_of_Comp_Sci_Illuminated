#!/usr/bin/env python
"""
Script for a recursive factorial
"""
from __future__ import division
from sys import argv


def factorial(N):
    if N == 0:
        return 1
    return N * factorial(N - 1)

if len(argv) != 2:
    print "Single number as argument"
else:
    N = eval(argv[1])
    print N, factorial(N)
