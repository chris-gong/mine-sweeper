import numpy as np
from random import randint


class MinesweeperGame():
    def __init__(self, length, width, num_mines):
        self.length = length
        self.width = width
        self.num_mines = num_mines
        self.grid = np.zeroes
        self.generate_new_grid()
        
    def get_adjacent_count(self, x, y):
        if not self.in_bounds(x,y):
            #error out of bounds
            pass
        count = 0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if self.grid[i][j]== 9 and not (i == x and j == y):
                    count += 1
        return count
        
    def in_bounds(self, x, y):
        return not ((x < 0 or x >= self.width)
                    or (y < 0 or y >= self.length))
    
    def generate_new_grid(self):
        self.grid = np.zeroes
        #Place the mines
        remaining_mines = self.num_mines
        while remaining_mines >= 0:
            i = randint(0, self.width-1)
            j = randint(0, self.length-1)
            if self.grid[i][j] != 9:
                self.grid[i][j] = 9
                remaining_mines -= 1
        #Set the clues
        for i in range(0, self.width):
            for j in range(0, self.length):
                if self.grid[i][j] != 9:
                    self.grid[i][j] = self.get_adjacent_count(i,j)

    def query_tile(self,x,y):
        return self.grid[x][y]
        