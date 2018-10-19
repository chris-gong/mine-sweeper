import numpy as np


class MinesweeperGame:
    def __init__(self, length, width, num_mines):
        self.length = length
        self.width = width
        self.num_mines = num_mines
        self.grid = np.zeroes
        
    def get_adjacent_count(self, x, y):
        if 
        
    def in_bounds(self, x, y):
        return not ((x < 0 or x >= self.width)
                    or (y < 0 or y >= self.length)):
            
    def generate_new_game