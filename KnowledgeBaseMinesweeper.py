import numpy as np
import matplotlib.pyplot as plt
from enum import Enum

class Predicate(Enum):
    true = 1
    false = 2
    undetermined = 3


class KnowledgeBase():
    def __init__(self, length, width):
        self.mine_predicates_arr = [[Predicate.undetermined for y in range(length)] for x in range(width)]
        self.tile_arr= [[Tile(False) for y in range(length)] for x in range(width)]

class Tile():
    def __init__(self, discovered):
        self.discovered = discovered
        self.adj_mines = -1
        self.satisfied = True


if __name__ == '__main__':
    kb = KnowledgeBase(5, 5)
