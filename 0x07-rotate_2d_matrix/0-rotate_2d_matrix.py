#!/usr/bin/python3
""" implementation of 2d matrix rotation """


def helper_transpose(matrix):
    """ helper that finds the transpose of a matrix"""
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp


def helper_flip(matrix):
    """ helper function that flips the matrix columns """
    n = len(matrix)

    for i in range(n):
        for j in range(int(n/2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n - j - 1]
            matrix[i][n - j - 1] = temp


def rotate_2d_matrix(matrix):
    """ main function that rotates matrix"""
    helper_transpose(matrix)
    helper_flip(matrix)
