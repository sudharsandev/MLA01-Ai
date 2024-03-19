from collections import deque

def get_neighbors(board):
    neighbors = []
    empty_row, empty_col = next((i, j) for i, row in enumerate(board) for j, val in enumerate(row) if val == 0)
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_board = [row[:] for row in board]
            new_board[empty_row][empty_col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[empty_row][empty_col]
            neighbors.append(new_board)
    return neighbors

def bfs(board):
    visited = set()
    queue = deque([(board, 0)])
    while queue:
        current_board, moves = queue.popleft()
        if current_board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            return moves
        visited.add(str(current_board))
        for neighbor in get_neighbors(current_board):
            if str(neighbor) not in visited:
                queue.append((neighbor, moves + 1))
    return -1

# Execution
initial_board = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
print("Minimum number of moves required:", bfs(initial_board))
