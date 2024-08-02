#!/usr/bin/python3
""" N Queens placement on NxN chessboard """

import sys

def solve_nqueens(n):
    """
    Solves the N queens problem and returns all possible solutions
    Args:
        n (int): The size of the board and number of queens
    Returns:
        List[List[int]]: A list of solutions, each solution is a list of queen positions
    """
    def is_safe(board, row, col):
        """ Check if it's safe to place a queen at board[row][col] """
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        """ Solve the problem using backtracking """
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * n
    solve(board, 0)

    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(n)]
        print(formatted_solution)

if __name__ == '__main__':
    solve_nqueens(int(sys.argv[1]))
