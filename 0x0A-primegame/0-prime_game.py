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

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        turn = sum(1 for p in primes if p <= n)
        if turn % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
