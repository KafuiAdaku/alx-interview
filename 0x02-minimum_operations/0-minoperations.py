#!/usr/bin/python3
"""
In a text file, there is a single character `H`. Your text editor can execute
only two operations in this file: `Copy All` and `Paste`.
Given a number `n`, write a method that calculates the fewest number of
operations needed to result in exactly `n * H` characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""


def minOperations(n):
    """Returns an integer"""
    if n <= 1:
        return 0

    count = 0
    div = 2

    while div * div <= n:
        while n % div:
            div += 1
        while n % div == 0:
            n //= div
            count += div

    if n > 1:
        count += n

    return count
