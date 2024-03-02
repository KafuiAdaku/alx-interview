#!/usr/bin/python3
"""N queens puzzle"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)


def can_place(board, row, col):
    """Check if a queen can be placed on board[row][col]"""
    for i in range(col):
        if board[i] == row or \
            board[i] - i == row - col or \
                board[i] + i == row + col:
            return False
    return True


def place_queens(board, col):
    """Place queens on the board"""
    if col == N:
        print([[i, board[i]] for i in range(N)])
    else:
        for i in range(N):
            if can_place(board, i, col):
                board[col] = i
                place_queens(board, col + 1)


place_queens([0]*N, 0)
