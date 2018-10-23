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

    def in_bounds(self, x, y):
        return not ((x < 0 or x >= self.width)
                    or (y < 0 or y >= self.length))

    def check_tile_for_conflicts(self, tile):
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
        if count >= tile.adj_mines:
            return True


class Tile():
    def __init__(self, x, y):
        self.visited = False
        self.is_mined = Predicate.undetermined
        self.adj_mines = -1
        self.x = x
        self.y = y


if __name__ == '__main__':
    kb = KnowledgeBase(5, 5)
