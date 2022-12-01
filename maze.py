import numpy as np

class Maze():
    size = (80,50)
    def __init__(self):
        
        self.grid = self.get_random_maze()

    def get_random_maze(self) -> "list[list[bool]]":
        return np.random.rand(self.size[0],self.size[1])>.5

        