def is_safe(board, row, col):
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, 8, 1), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True

def solve_queens(board, col):
    if col >= 8:
        return True
    for i in range(8):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_queens(board, col + 1):
                return True
            board[i][col] = 0
    return False

def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))

if __name__ == "__main__":
    board = [[0] * 8 for _ in range(8)]
    if solve_queens(board, 0):
        print("Solution found:")
        print_board(board)
    else:
        print("No solution found.")
