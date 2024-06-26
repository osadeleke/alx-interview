#!/usr/bin/python3
"""
lock boxes algorithm
"""


def canUnlockAll(boxes):
    """
    lock boxes algo
    """
    n = len(boxes)
    visited = [False] * n
    stack = [0]
    holder = []

    while stack:
        checker = stack.pop()
        holder.append(checker)
        visited[checker] = True
        for key in boxes[checker]:
            if key < n and key not in stack and key not in holder:
                stack.append(key)
    return all(visited)
