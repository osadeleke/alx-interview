#!/usr/bin/python3
"""
making change module
"""


def makeChange(coins, total):
    """
    making change module
    """
    if total <= 0:
        return 0

    lval = [float('inf')] * (total + 1)
    lval[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if lval[i - coin] != float('inf'):
                lval[i] = min(lval[i], lval[i - coin] + 1)

    return lval[total] if lval[total] != float('inf') else -1
