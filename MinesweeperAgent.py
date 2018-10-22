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
        # Query the user for a width and length
        length = int(input("What is the length of the game board?"))
        width = int(input("What is the width of the game board?"))
        num_mines = int(input("How many mines do you want the generated\
                              map to have?"))
        self.kb = KnowledgeBase(length,width)
        self.game = MinesweeperGame(length,width,num_mines)
        self.game_type = "CPU"
        
    def new_human_game(self):
        # Query the user for a width and length
        length = int(input("What is the length of the game board?"))
        width = int(input("What is the width of the game board?"))
        self.kb = KnowledgeBase(length,width)
        self.game_type = "HUMAN"
        
    def play_game(self):
        if self.gameType is not None:
            #tried to play game when not possible
            pass
        # decide on which tile to query
        # perform PBC if nothing to safely visit
        # guess if there is nothing clear and PBC on every viable option

    def proof_by_contradiction(self, x, y):
        # Returns a predicate on if the arg tile is mined
        predicates = self.kb.mine_predicates_arr
        if predicates[x][y] is not Predicate.undetermined:
            # Error no need to do PBC on an already known tile
            return
            
        def try_to_satisfy(x, y):
            kb = self.kb
            result = False
            # TODO
            '''
            1. Check if the current setup conflicts
            2. Add mines to try and satisfy
            3. If not possible
            '''
            return result
            pass

        # Add p to KB and try to satisfy
        predicates[x][y] = Predicate.true
        p1 = try_to_satisfy(x,y)
        # Add not p to KB and try to satisfy
        predicates[x][y] = Predicate.false
        p2 = try_to_satisfy(x,y)

        if p1 and p2:
            predicates[x][y] = Predicate.undetermined
        elif p1 and not p2:
            predicates[x][y] = Predicate.true
        elif not p1 and p2:
            predicates[x][y] = Predicate.false
        else:
            # Error 
            return
        return


if __name__ == '__main__':
    agent = MineSweeperAgent()
    agent.new_cpu_game()
    
        