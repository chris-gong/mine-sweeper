from KnowledgeBaseMinesweeper import KnowledgeBase, Predicate
from MinesweeperGame import MinesweeperGame
from copy import deepcopy

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
        num_mines = int(input("How many mines do you want the generated"
                              "map to have?"))

        self.length = length
        self.width = width
        self.kb = KnowledgeBase(length, width)
        self.game = MinesweeperGame(length, width, num_mines)
        self.game_type = "CPU"

    def new_human_game(self):
        # Query the user for a width and length
        length = int(input("What is the length of the game board?"))
        width = int(input("What is the width of the game board?"))
        self.kb = KnowledgeBase(length, width)
        self.game_type = "HUMAN"
#
    def play_game(self):
        if self.gameType is not None:
            # tried to play game when not possible
            pass
        # decide on which tile to query
        # perform PBC if nothing to safely visit
        # guess if there is nothing clear and PBC on every viable option

    def process_query(self, num, cur_tile):
        if num is 9:
            # TODO gameover
            return
        elif num >= 0 and num <= 8:
            cur_tile.discovered = True
            cur_tile.adj_mines = num
            cur_tile.is_mined = Predicate.false
        else:
            # Error invalid num
            return

    def query_tile_human(self, x, y):
        # returns 0-8 for num of adj mines or 9 if the tile is mined
        querystring = "What is in space ({},{})", (x, y)
        num = int(input(querystring))
        cur_tile = self.kb.tile_arr[x][y]
        self.process_query(num, cur_tile)

    def query_tile_cpu(self, x, y):
        # returns 0-8 for num of adj mines or 9 if the tile is mined
        num = self.game.grid[x][y]
        cur_tile = self.kb.tile_arr[x][y]
        self.process_query(num, cur_tile)

    def proof_by_contradiction(self, x, y):
        cur_tile = self.kb.tile_arr[x][y]
        # Returns a predicate on if the arg tile is mined
        if cur_tile.is_mined is not Predicate.undetermined:
            # Error no need to do PBC on an already known tile
            return4

        # Add p to KB and try to satisfy
        cur_tile.is_mined = Predicate.true
        p1 = self.try_to_satisfy(x, y)
        # Add not p to KB and try to satisfy
        cur_tile.is_mined = Predicate.false
        p2 = self.try_to_satisfy(x, y)

        if p1 and p2:
            pass
        elif p1 and not p2:
            cur_tile.is_mined = Predicate.true
        elif not p1 and p2:
            cur_tile.is_mined = Predicate.false
        else:
            # Error
            return
        return

    def try_to_satisfy(self, x, y):
        test_kb = deepcopy(self.kb)

        result = False
        # TODO
        '''
        1. Check if the current setup conflicts
        2. Add mines to try and satisfy
        3. If not possible
        '''
        del(test_kb)
        return result


if __name__ == '__main__':
    agent = MineSweeperAgent()
    agent.new_cpu_game()
