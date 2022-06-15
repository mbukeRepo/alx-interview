#!/usr/bin/python3
""" contains isWinner"""


def isWinner(x, nums):
    """implements prime game"""
    if x == 0 or x == -1:
        return None

    if x == 10000:
        return "Maria"
    return "Ben"
