from KnowledgeBaseMinesweeper import KnowledgeBase,Predicate
from MinesweeperGame import MinesweeperGame
class GameTile:
    def __init__(self):
        pass

class MineSweeperAgent:
    def __init__(self):
        self.gameType = None
        self.kb = None
        
    def new_cpu_game(self):
        #Query the user for a width and length
        length = int(input("What is the length of the game board?"))
        width = int(input("What is the width of the game board?"))
        num_mines = int(input("How many mines do you want the generated\
                              map to have?"))
        self.kb = KnowledgeBase(length,width)
        self.game = MinesweeperGame(length,width,num_mines)
        self.game_type = "CPU"
        
    def new_human_game(self):
        #Query the user for a width and length
        length = int(input("What is the length of the game board?"))
        width = int(input("What is the width of the game board?"))
        self.kb = KnowledgeBase(length,width)
        self.game_type = "HUMAN"
        
    def play_game(self):
        if not self.playing:
            #tried to play gmae whne not possible
            pass
        #decide on which 
    
if __name__ == '__main__':
    agent = MineSweeperAgent()
    agent.new_cpu_game()
    
        