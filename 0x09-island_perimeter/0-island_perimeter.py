#!/usr/bin/python3
""" this file contains implementation of calculation of island perimeter"""


def dfs(i, j, grid, visit):
    """helper function that implements perimeter calculation"""
    print("it is called")
    if i >= len(grid) or j >= len(grid[0]) or \
       i < 0 or j < 0 or grid[i][j] == 0:
        return 1
    if (i, j) in visit:
        return 0
    visit.add((i, j))
    perim = dfs(i, j + 1, grid, visit)
    perim += dfs(i + 1, j, grid, visit)
    perim += dfs(i, j - 1, grid, visit)
    perim += dfs(i - 1, j, grid, visit)

    return perim


def island_perimeter(grid):
    """calculates island perimeter"""
    visit = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i, j, grid, visit)
    return 0
