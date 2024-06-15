#!/usr/bin/python3
"""
lock boxes algorithm
"""


def canUnlockAll(boxes):
    """
    lock boxes algo
    """
    n = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        checker = stack.pop()
        visited.add(checker)
        for key in boxes[checker]:
            if key < n and key not in visited:
                stack.append(key)

    if len(visited) == n:
        return True
    else:
        return False
