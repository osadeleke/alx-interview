#!/usr/bin/python3
"""
prime game
"""


def isWinner(x, nums):
    """
    prime game module
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)

    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False
    for p in range(1, int(max_n**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, max_n + 1, p):
                sieve[i] = False

    prime_count = [0] * (max_n + 1)
    count = 0
    for i in range(2, max_n + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count

    maria = 0
    ben = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
