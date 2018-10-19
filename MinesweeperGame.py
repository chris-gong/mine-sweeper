import numpy as np

class MinesweeperGame:
    def __init__(self, length, width, num_mines):
        self.length = length
        self.width = width
        self.num_mines = num_mines
        self.grid = np.zeroes
        
    def get_adjacent_count(self, x, y):
        if not self.in_bounds(x,y):
            #error out of bounds
            pass
        count = 0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if grid[i][j]== 9 and i != x and j != y:
                    count += 1
        return count
        
    def in_bounds(self, x, y):
        return not ((x < 0 or x >= self.width)
                    or (y < 0 or y >= self.length))
            
    def generate_new_game(self, )