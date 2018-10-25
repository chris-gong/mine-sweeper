from KnowledgeBaseMinesweeper import KnowledgeBase, Predicate
from MinesweeperGame import MinesweeperGame
from copy import deepcopy
import random

class GameTile:
    def __init__(self):
        pass


class MineSweeperAgent:
    def __init__(self):
        self.gameType = None
        self.kb = None
        self.gameover = False
        self.won = False

    def new_cpu_game(self):
        # Query the user for a width and length
        '''
        length = int(input("What is the length of the game board?"))
        width = int(input("What is the width of the game board?"))
        num_mines = int(input("How many mines do you want the generated"
                              "map to have?"))
        '''
        length,width,num_mines = (10,10,20)

        self.length = length
        self.width = width
        self.kb = KnowledgeBase(length, width)
        self.game = MinesweeperGame(length, width, num_mines)
        self.game_type = "CPU"
        self.gameover = False
        self.won = False

    def new_human_game(self):
        # Query the user for a width and length
        length = int(input("What is the length of the game board?"))
        width = int(input("What is the width of the game board?"))
        self.kb = KnowledgeBase(length, width)
        self.game_type = "HUMAN"
        self.gameover = False
        self.won = False

    def play_game(self):
        if self.gameType is not None:
            # tried to play game when not possible
            pass
        # decide on which tile to query
        # perform PBC if nothing to safely visit
        # guess if there is nothing clear and PBC on every viable option
        # First guess is middle of game
        unvisited_cleared_tiles = set()
        fringe = set() # unknown tiles that are adjacent to discovered nodes

        first_tile = self.query_tile(int(self.length/2), int(self.width/2))
        adj_unvisited = self.kb.get_unvisited_neighbors(first_tile)
        for tile in adj_unvisited:
            fringe.add(tile)
        while not self.gameover:
            if len(unvisited_cleared_tiles) != 0:
                # If there are any safe nodes to go to make those moves
                print("clearing cleared_tiles:"+str(len(unvisited_cleared_tiles)))
                while len(unvisited_cleared_tiles) != 0:
                    tile = unvisited_cleared_tiles.pop()
                    self.query_tile(tile.x,tile.y)
                    adj_unvisited = self.kb.get_unvisited_neighbors(tile)
                    for tile in adj_unvisited:
                        fringe.add(tile)
                continue
            if len(fringe) != 0:
                # Nowhere safe rn to go to so search fringe for safe node
                print("querying fringe")
                tiles_to_remove = []
                for tile in fringe:
                    is_tile_mined = self.proof_by_contradiction(tile.x,tile.y)
                    if is_tile_mined is Predicate.true:
                        self.kb.flag_mine(tile)
                        tiles_to_remove.append(tile)
                    elif is_tile_mined is Predicate.false:
                        tile.is_mined = Predicate.false
                        unvisited_cleared_tiles.add(tile)
                        tiles_to_remove.append(tile)
                    else:
                        continue
                for tile in tiles_to_remove:
                    fringe.remove(tile)
                if len(unvisited_cleared_tiles) == 0:
                    # Have to guess because we only have undetermined tiles left,
                    # no cleared tiles (predicate false or true)
                    print("guess - nowhere safe to go")
                    guess_tile = fringe.pop()
                    print("guessing: "+str(guess_tile.x)+','+str(guess_tile.y))
                    unvisited_cleared_tiles.add(guess_tile)
                    # self.kb.print_kb()
                    # return

                # TODO queries concluded nothing
            else:
                # TODO If the fringe is empty that means all adjacent
                # undiscovered nodes are mines so pick random undertermined mine
                print("guess -surroundded by mines")
                # guess randomly on a unvisited tile because
                # no adjacent tiles to visit (for e.g. remaining
                # tiles are surrounded by mines
                candidates = []
                for i in range(len(self.kb.tile_arr)):
                    for j in range(len(self.kb.tile_arr[i])):
                        if(self.kb.tile_arr[i][j].is_mined is Predicate.undetermined):
                            candidates.append(self.kb.tile_arr[i][j])
                if len(candidates) == 0:
                    self.gameover = True
                    self.won = True
                    break
                # TODO PERFORM HEURISTIC ON THE CANDIDATES
                rand_index = random.randint(0, len(candidates) - 1)
                unvisited_cleared_tiles.add(candidates[rand_index])
                #self.kb.print_kb()
                #return

        if self.won:
            print("WINNER WINNER CHICKEN DINNER")
        else:
            print("GAMEOVER")
        self.kb.print_kb()
        return

    def process_query(self, num, cur_tile):
        if num == 9:
            print("gameover x = " + str(cur_tile.x))
            print("gameover y = " + str(cur_tile.y))
            self.gameover = True
            self.won = False
            return
        elif num >= 0 and num <= 8:
            self.kb.visit_tile(cur_tile, num)
        else:
            # Error invalid num
            return

    def query_tile(self, x, y):
        if self.gameType is "HUMAN":
            return self.query_tile_human(x, y)
        else:
            return self.query_tile_cpu(x, y)

    def query_tile_human(self, x, y):
        # returns 0-8 for num of adj mines or 9 if the tile is mined
        querystring = "What is in space ({},{})", (x, y)
        num = int(input(querystring))
        cur_tile = self.kb.tile_arr[x][y]
        self.process_query(num, cur_tile)
        return cur_tile

    def query_tile_cpu(self, x, y):
        # returns 0-8 for num of adj mines or 9 if the tile is mined
        num = int(self.game.grid[x][y])
        cur_tile = self.kb.tile_arr[x][y]
        self.process_query(num, cur_tile)
        return cur_tile

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
        #test_kb.unflag_mine(cur_tile)
        cur_tile.is_mined = Predicate.false;
        p2 = test_kb.try_to_satisfy()
        # print("p1: " + str(p1))
        # print("p2: " + str(p2))

        if p1 and p2:
            return Predicate.undetermined
        elif p1 and not p2:
            return Predicate.true
        elif not p1 and p2:
            return Predicate.false
        else:
            # Error
            print("Error: Inconsistent kb")
            return
        return




if __name__ == '__main__':
    '''
    kb = KnowledgeBase(5, 5)
    tile = kb.tile_arr[3][4]
    kb.visit_tile(tile, 0)
    tile = kb.tile_arr[2][4]
    kb.visit_tile(tile, 2)
    tile = kb.tile_arr[1][2]
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

    result = agent.proof_by_contradiction(3,3)
    print("proof " + str(result))
    '''
    agent = MineSweeperAgent()

    agent = MineSweeperAgent()
    agent.new_cpu_game()
    agent.play_game()
    agent.game.render_grid()
