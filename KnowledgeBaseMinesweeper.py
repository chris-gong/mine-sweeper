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
        while len(self.unsa >= 0):
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
