#!/usr/bin/python3
"""
   implements box unlocking
   methods:
     canUnlockAll(bool): unlocks all boxes
"""


def canUnlockAll(boxes):
    """ returns true if all keys are found """
    keys = [0]
    for n in keys:
        for key in boxes[n]:
            if key not in keys and key < len(boxes):
                keys.append(key)
    return len(boxes) == len(keys)
