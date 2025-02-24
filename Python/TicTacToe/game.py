from player import HumanPlayer, RandomComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None 
    
    def print_board(self):
        s = [self.board[i*3 : (i+1) *3] for i in range(3)]
        for i in s:
            print("| " + " | ".join(i) + " |")
    
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3 , (j+1) *3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return " " in self.board
    
    def num_empty_square(self):
        return self.board.count(' ')
        # return len(self.available_moves())
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True 
        return False

    def winner(self, square, letter):
        row_ind = square // 3 
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3 
        col = [self.board[col_ind + i *3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True 

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True 
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        return False

def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()
    
    letter = 'X'

    while game.empty_squares():
        
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
    
        if game.make_move(square, letter):
            if print_game:
                game.print_board()
                print(f"{letter} made the move to {square}")
                print('')

            if game.current_winner:
                if print_game:
                    print(f"{letter} wins!")
                return letter
                
            letter = 'O' if letter == 'X' else 'X'

        time.sleep(0.8)
    if print_game:
        print("It is a Tie!!!")


if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")

    game = TicTacToe()

    play(game, x_player, o_player, print_game=True)
            
