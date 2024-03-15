#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Prime Game"""
    if not nums or x < 1:
        return None

    n = max(nums)
    primes = [True for _ in range(max(n + 1, 2))]
    primes[0:2] = [False, False]

    for i in range(2, int(n**0.5) + 1):
        if not primes[i]:
            continue
        for j in range(i*i, n + 1, i):
            primes[j] = False

    primes = [i for i, isprime in enumerate(primes) if isprime]

    players = 0
    for n in nums:
        players += sum(1 for p in primes if p <= n)

    if players % 2 == 0:
        return "Ben"
    return "Maria"
