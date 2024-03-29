#!/usr/bin/python3
"""This module contains a function called `pascal_triangle`"""


memory = {}


def combination(n, r):
    """computes the combinatorics of two integers"""
    if r == 0 or n == r:
        return 1

    if (n, r) in memory:
        return memory[(n, r)]

    result = combination(n - 1, r - 1) + combination(n - 1, r)
    memory[(n, r)] = result

    return result


def pascal_triangle(n):
    """
    Returns a list of integers represent Pascal's triangle

    Args:
    n: integer

    return: list of integers
    """
    matrix = []

    if n <= 0:
        return matrix

    for row in range(0, n):
        mat_row = []
        for col in range(0, row + 1):
            mat_row.append(combination(row, col))
        matrix.append(mat_row)

    return matrix
