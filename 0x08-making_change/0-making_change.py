#!/usr/bin/python3
"""
    Making Change
    Given a pile of coins of different values,
    determine the fewest number of coins
    needed to meet a given amount total
"""


def makeChange(coins, total):
    """Making Change"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    n = len(coins)
    result = 0
    i = 0
    while i < n and total > 0:
        if total >= coins[i]:
            total -= coins[i]
            result += 1
        else:
            i += 1
    if total != 0:
        return -1
    return result
