#!/usr/bin/python3


def pascal_triangle(n):
    if n <= 0:
        return []
    else:
        line = []
        prev = []
        triangles = []
        for i in range(0, n + 1):
            line = [j > 0 and j < i - 1 and i > 2 and prev[j - 1] +
                    prev[j] or 1 for j in range(0, i)]
            prev = line
            triangles += [line]
        return triangles[1:]
