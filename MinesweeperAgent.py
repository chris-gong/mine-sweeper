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
        '''
        length = int(input("What is the length of the game board?"))
        width = int(input("What is the width of the game board?"))
        num_mines = int(input("How many mines do you want the generated"
                              "map to have?"))
        '''
        length,width,num_mines = (5,5,5)

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
            self.kb.visit_tile(cur_tile, num)
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
        test_kb = deepcopy(self.kb)
        cur_tile = test_kb.tile_arr[x][y]
        # Returns a predicate on if the arg tile is mined
        if cur_tile.is_mined is not Predicate.undetermined:
            # Error no need to do PBC on an already known tile
            return
        # Add p to KB and try to satisfy
        test_kb.flag_mine(cur_tile)
        if test_kb.check_local_sat(cur_tile) >= 1:
            p1 = False
        else:
            p1 = test_kb.try_to_satisfy()

        # Add not p to KB and try to satisfy
        test_kb = deepcopy(self.kb)
        cur_tile = test_kb.tile_arr[x][y]
        test_kb.unflag_mine(cur_tile)
        p2 = test_kb.try_to_satisfy()
        print("p1: " + str(p1))
        print("p2: " + str(p2))

        if p1 and p2:
            pass
        elif p1 and not p2:
            cur_tile.is_mined = Predicate.true
            return True
        elif not p1 and p2:
            cur_tile.is_mined = Predicate.false
            return False
        else:
            # Error
            print("Error: Inconsistent kb")
            return
        return




if __name__ == '__main__':

    kb = KnowledgeBase(5, 5)
    tile = kb.tile_arr[3][4]
    kb.visit_tile(tile, 1)
    tile = kb.tile_arr[2][4]
    kb.visit_tile(tile, 2)
    tile = kb.tile_arr[1][4]
    kb.visit_tile(tile, 1)
    tile = kb.tile_arr[1][1]
    kb.flag_mine(tile)
    tile = kb.tile_arr[3][1]
    kb.flag_mine(tile)
    kb2 = deepcopy(kb)
    # print(kb2.check_local_sat(kb.tile_arr[3][3]))
    # print(kb2.try_to_satisfy())

    agent = MineSweeperAgent()
    agent.kb = kb

    kb.print_kb()
    result = agent.proof_by_contradiction(0,3)
    print("proof " + str(result))

    agent = MineSweeperAgent()
    agent.new_cpu_game()
    print("HEY")



