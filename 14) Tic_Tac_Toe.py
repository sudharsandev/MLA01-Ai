class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for i in range(0, 9, 3):
            print('| ' + ' | '.join(self.board[i:i+3]) + ' |')

    def print_board_nums(self):
        for i in range(0, 9, 3):
            print('| ' + ' | '.join(str(num) for num in range(i, i+3)) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        if all([spot == letter for spot in self.board[row_ind*3:(row_ind+1)*3]]):
            return True
        col_ind = square % 3
        if all([self.board[col_ind+i*3] == letter for i in range(3)]):
            return True
        if square % 2 == 0:
            if all([self.board[i] == letter for i in [0, 4, 8]]) or all([self.board[i] == letter for i in [2, 4, 6]]):
                return True
        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + ' makes a move to square', square)
                game.print_board()
                print('')
                
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print('It\'s a tie!')

class HumanPlayer:
    def get_move(self, game):
        while True:
            move = input("Enter your move (0-8): ")
            if move.isdigit():
                move = int(move)
                if 0 <= move <= 8 and game.board[move] == ' ':
                    return move
            print("Invalid move. Try again.")

if __name__ == "__main__":
    x_player = HumanPlayer()
    o_player = HumanPlayer()
    t = TicTacToe()
    play(t, x_player, o_player)
