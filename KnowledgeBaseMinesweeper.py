from enum import Enum


class Predicate(Enum):
    true = 1
    false = 2
    undetermined = 3


class KnowledgeBase():
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.tile_arr = [[Tile(x, y) for y in range(length)]
                         for x in range(width)]
        self.unsatisfied_tiles = []

    def visit_tile(self, tile, num):
            tile.discovered = True
            tile.adj_mines = num
            tile.is_mined = Predicate.falsenum
            i = self.cmp_tile_to_adj(tile)
            if i >= 0:
                # Error conflict when discovering new node
                return
            elif i == 0:
                pass
            else:
                self.unsatisfied_tile.append(tile)

    def in_bounds(self, x, y):
        return not ((x < 0 or x >= self.width)
                    or (y < 0 or y >= self.length))

    def cmp_tile_to_adj(self, tile):
        count = 0
        x = tile.x
        y = tile.y
        # Count adjacent mines
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if (self.in_bounds(i, j) and
                        self.tile_arr[i][j] == Predicate.true
                        and not (i == x and j == y)):
                    count += 1
        return count - tile.adj_mines

    def try_to_satisfy(self):
        # TODO
        possible_mines = []
        for unsat_tile in self.unsatisfied_tiles:
            x = unsat_tile.x
            y = unsat_tile.y
            # Count adjacent mines
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if (self.in_bounds(i, j)
                            and self.tile_arr[i][j].is_mined is
                            Predicate.undetermined):
                        possible_mines.append(self.tile_arr[i][j])
        last_mine_stack = []
        subset_end = -1
        while True:
            if subset_end+1 is len(possible_mines):
                global_sat = check_global_sat
                if global_sat is true:
                    return true
                else:
                    if len(last_mine_stack) is 0:
                        return false
                    subset_end = last_mine_stack.pop()
                    possible_mines[subset_end].is_mined = Predicate.false
            # Add Mine
            subset_end += 1
            possible_mines[subset_end].is_mined = Predicate.true
            last_mine_stack.push(subset_end)
            # Local sat
            local_sat = check_local_sat(possible_mines[subset_end])
            if local_sat <= 0:
                continue
            elif local_sat == 0 and check_global_sat:
                return True
            elif local_sat >= 0:
                last_mine_stack.pop()
                possible_mines[subset_end].is_mined = Predicate.false

    def check_global_sat(self):
        pass

    def check_local_sat(self,tile):
        pass

class Tile():
    def __init__(self, x, y):
        self.visited = False
        self.is_mined = Predicate.undetermined
        self.adj_mines = -1
        self.x = x
        self.y = y


if __name__ == '__main__':
    kb = KnowledgeBase(5, 5)
