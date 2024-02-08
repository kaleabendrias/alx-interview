#!/usr/bin/python3
def is_valid(board, row, col, N):
    # Check if placing a queen at (row, col) is valid
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def print_solution(board):
    # Convert the board to a list of coordinates and print it
    solution = [[i, board[i]] for i in range(len(board))]
    print(solution)


def solve_nqueens(board, row, N):
    if row == N:
        # All queens are placed, print the solution
        print_solution(board)
        return

    for col in range(N):
        if is_valid(board, row, col, N):
            # Place a queen at (row, col) and move on to the next row
            board[row] = col
            solve_nqueens(board, row + 1, N)
            # Backtrack: undo the placement and try the next column
            board[row] = -1


def nqueens(N):
    # Initialize the chessboard with -1 indicating an empty square
    board = [-1] * N
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: ./script.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)
