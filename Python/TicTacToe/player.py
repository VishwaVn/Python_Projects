import math 
import random 
class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter
    
    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False 
        val = None 
        while not valid_square:
            square = input(f"{self.letter}'s turn, Input move (0-8)")
            try:
                val = int(square) 
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid Square, try again')
        return val 

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square 