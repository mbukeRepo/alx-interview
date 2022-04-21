#!/usr/bin/python3
""" 0. Minimum Operations """


def minOperations(n):
    """ Return: total """
    t, m = 0, 2
    while n > 1:
        while not n % m:
            t += m
            n /= m
        m += 1
    return t
