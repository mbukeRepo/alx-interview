#!/usr/bin/python3
"""
   implements box unlocking
   methods:
     new_keys(int[]): returns array of new keys
     canUnlockAll(bool): unlocks all boxes
"""


def new_keys(T, R):
    """ returns array of keys """
    res = []
    for k in R:
        res += T[k]
    return res


def canUnlockAll(boxes):
    """ returns true if all keys are found """
    index = 0
    total = list(set(boxes[0]) | {0})
    added = True
    while added:
        added = False
        for j in new_keys(boxes, total[index:]):
            if j not in total:
                total.append(j)
                index += 1
                added = True
    return len(boxes) == len(total)
