#!/usr/bin/python3
""" n-queens solution """

import sys


def create_board(n):
    """ creating empty board"""
    board = []
    for i in range(n):
        board.append([0 for i in range(n)])
    return board


def isSafe(queens, r, c):
    """ Testing if its safe place to place a queen"""
    for q in queens:
        dx = abs(r - q[1])
        dy = abs(c - q[0])
        if dx == 0 or dy == 0 or dy == dx:
            return False
    return True


def solver(board, queens, col):
    """ main implementation """
    if col >= len(board):
        print(queens)

    for i in range(len(board)):
        if isSafe(queens, i, col):
            board[i][col] = 1
            queens.append([col, i])
            if solver(board, queens, col + 1):
                return True
            board[i][col] = 0
            queens.pop()
    return False


def nqueens():
    """ entry point to the implementation """
    n = int(sys.argv[1])
    queens = []
    board = create_board(n)
    solver(board, queens, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not sys.argv[1].isnumeric():
        print("N must be a number")
        exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)
    nqueens()
