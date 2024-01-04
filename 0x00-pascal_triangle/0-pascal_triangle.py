#!/usr/bin/python3
""" implementation of pascal_triangle function """


def pascal_triangle(n):
    """ returns a list of lists of integers representing the Pascal’s triangle of n """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1] + [triangle[i-1][j-1] + triangle[i-1][j] for j in range(1, i)] + [1]
        triangle.append(row)

    return triangle

