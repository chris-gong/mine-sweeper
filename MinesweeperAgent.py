from KnowledgeBaseMinesweeper import KnowledgeBase,Predicate

class GameTile:
    def __init__(self):
        pass

class MineSweeperAgent:
    def __init__(self):
        self.playing = False;
        self.kb = None
        
    def new_game(self):
        #Query the user for a width and length
        length = int(input("What is the length of the game board?"))
        width = int(input("What is the width of the game board?"))
        self.kb = KnowledgeBase(length,width)
        self.playing = True;
        
    def play_game(self):
        if not self.playing:
            #tried to play gmae whne not possible
            pass
        #decide on which 
    
if __name__ == '__main__':
    minesweeper = MineSweeper()
    minesweeper.new_game()
    
        