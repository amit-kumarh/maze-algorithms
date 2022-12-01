import numpy as np

class Maze():
    def __init__(self):
        self.size = (80,50)
        self.grid = self.get_random_maze()

    def get_random_maze(self) -> "list[list[bool]]":
        return np.random.rand(self.size[0],self.size[1])>.5

        