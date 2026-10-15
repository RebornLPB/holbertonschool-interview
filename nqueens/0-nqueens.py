#!/usr/bin/python3

import sys


def n_not_valid():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(0, [], n)


def nqueens(row, queens, n):
    if row == n:
        solution = []
        for i in range(n):
            solution.append([i, queens[i]])
        print(solution)
        return

    for col in range(n):
        is_safe = True

        for r in range(len(queens)):
            c = queens[r]

            if c == col:
                is_safe = False

            if abs(c - col) == abs(r - row):
                is_safe = False

        if is_safe:
            queens.append(col)
            nqueens(row + 1, queens, n)
            queens.pop()


if __name__ == "__main__":
    n_not_valid()
