#!/usr/bin/python3
"""This module contains a function called `pascal_triangle`"""


def factorial(n):
    """returns the factorial of an interger"""
    fact = 1
    if n < 1:
        return 1

    while n > 1:
        fact = fact * n
        n -= 1
    return fact


def combination(n, r):
    """computes the combinatorics of two integers"""
    num = factorial(n)
    denum = factorial(n - r) * factorial(r)

    return int(num / denum)


def pascal_triangle(n):
    """
    Returns a list of integers represent Pascal's triangle

    Args:
    n: integer

    return: list of integers
    """
    matrix = []
    if n <= 0:
        return []

    for row in range(0, n):
        mat_row = []
        for col in range(0, row + 1):
            mat_row.append(combination(row, col))
        matrix.append(mat_row)

    return matrix
#
#
#def main():
#    print(pascal_triangle(10))
#
#
#if __name__ == "__main__":
#    main()
