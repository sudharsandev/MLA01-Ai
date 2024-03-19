import math

def minimax(board, depth, maximizing_player):
    if depth == 0 or game_over(board):
        return evaluate(board)

    if maximizing_player:
        max_eval = -math.inf
        for move in get_available_moves(board):
            new_board = make_move(board, move, 'X')
            eval = minimax(new_board, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            new_board = make_move(board, move, 'O')
            eval = minimax(new_board, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

def make_move(board, move, player):
    new_board = board[:]
    new_board[move] = player
    return new_board

def game_over(board):
    return any(board.count(player) >= 3 for player in ['X', 'O'])

def evaluate(board):
    if 'XXX' in ''.join(board):
        return 1
    elif 'OOO' in ''.join(board):
        return -1
    else:
        return 0

def find_best_move(board):
    return max(get_available_moves(board), key=lambda move: minimax(make_move(board, move, 'X'), 4, False))

if __name__ == "__main__":
    board = [' ' for _ in range(9)]
    while not game_over(board) and ' ' in board:
        human_move = int(input("Enter your move (0-8): "))
        if board[human_move] == ' ':
            board[human_move] = 'O'
            if game_over(board):
                break
            ai_move = find_best_move(board)
            board[ai_move] = 'X'
            print("AI makes a move to square", ai_move)
        else:
            print("Invalid move. Try again.")
        for i in range(0, 9, 3):
            print('| ' + ' | '.join(board[i:i+3]) + ' |')
