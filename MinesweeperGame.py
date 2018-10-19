import numpy as np
from random import randint
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class MinesweeperGame:
    def __init__(self, length, width, num_mines):
        self.length = length
        self.width = width
        self.num_mines = num_mines
        self.grid = np.zeros((width, length))
        self.generate_new_grid()

    def get_adjacent_count(self, x, y):
        if not self.in_bounds(x, y):
            # Error out of bounds
            pass
        count = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if (self.in_bounds(i, j) and
                        self.grid[i][j] == 9
                        and not (i == x and j == y)):
                    count += 1
        return count

    def in_bounds(self, x, y):
        return not ((x < 0 or x >= self.width)
                    or (y < 0 or y >= self.length))

    def generate_new_grid(self):
        self.grid = np.zeros((self.width, self.length))
        # Place the mines
        remaining_mines = self.num_mines
        while remaining_mines > 0:
            i = randint(0, self.width-1)
            j = randint(0, self.length-1)
            if self.grid[i][j] != 9:
                self.grid[i][j] = 9
                remaining_mines -= 1
        # Set the clues
        for i in range(0, self.width):
            for j in range(0, self.length):
                if self.grid[i][j] != 9:
                    self.grid[i][j] = self.get_adjacent_count(i, j)

    def query_tile(self, x, y):
        return self.grid[x][y]

    def render_grid(self):
        # cmap = colors.ListedColormap(['white', 'red', 'red', 'red', 'blue'])
        colors0 = plt.cm.binary(np.linspace(0, 1, 1))
        colors1 = plt.cm.Reds(np.linspace(.2, .8, 8))
        # colors1 = np.flip(colors1,0)
        colors2 = plt.cm.binary(np.linspace(1, 1, 1))

        # combine them and build a new colormap
        colors = np.vstack((colors0, colors1, colors2))
        mymap = mcolors.LinearSegmentedColormap.from_list('my_colormap', colors)
        '''
        bounds = [0, .5, 1.5, 2.5, 8, 10]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        fig, ax = plt.subplots()
        ax.imshow(self.grid, cmap=cmap, norm=norm)
        '''
        plt.pcolor(self.grid, cmap=mymap)
        plt.colorbar()
        plt.show()
        '''
        # draw gridlines
        ax.grid(which='major', axis='both',
                linestyle='-', color='k', linewidth=2)
        ax.set_xticks(np.arange(-.5, 10, 1))
        ax.set_yticks(np.arange(-.5, 10, 1))
        plt.show()
        '''


if __name__ == '__main__':
    ms_game = MinesweeperGame(10, 10, 25)
    ms_game.render_grid()
