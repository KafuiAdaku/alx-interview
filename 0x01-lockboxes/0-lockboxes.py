#!/usr/bin/python3
"""You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

    *Prototype: `def canUnlockAll(boxes)`
    *`boxes` is a list of lists
    *A key with the same number as a box opens that box
    *You can assume all keys will be positive integers
    *There can be keys that do not have boxes
    *The first box `boxes[0]` is unlocked
    *Return True if all boxes can be opened, else return False.
"""


def canUnlockAll(boxes):
    """Returns a True if all boxes can be opened, otherwise False"""
    keys_available = set(boxes[0])
    boxes_unlocked = {0}

    while keys_available:
        key = keys_available.pop()
        if key in range(1, len(boxes)) and key not in boxes_unlocked:
            boxes_unlocked.add(key)
            keys_available.update(boxes[key])

    return len(boxes) == len(boxes_unlocked)
