#!/usr/bin/python3
"""Returns the perimeter of an island described in grid
"""


def island_perimeter(grid):
    """returns the perimeter of grid"""
    perimeter = 0
    height = len(grid)
    width = len(grid[0])
    if len(grid) > 100 or len(grid[0]) > 100:
        return

    for row in range(height):
        for col in range(width):
            if grid[row][col] == 0:
                continue
            elif grid[row][col] == 1:
                # check left boundary
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # check right boundary
                if col == width - 1 or grid[row][col + 1] == 0:
                    perimeter += 1
                # check upper boundary
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # check lower boundary
                if row == height - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
    return perimeter