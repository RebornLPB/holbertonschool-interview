#!/usr/bin/python3
"""
Module 0-lockboxes
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes in a given list can be opened.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    opened = set([0])
    keys = [0]

    while keys:
        current_box = keys.pop(0)

        for key in boxes[current_box]:
            if key < len(boxes) and key not in opened:
                opened.add(key)
                keys.append(key)

    return len(opened) == len(boxes)
