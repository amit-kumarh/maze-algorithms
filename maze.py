import collections
import numpy as np

class Maze():
    size = (80,50)
    def __init__(self):
        self.grid = self.get_random_maze()
        self.start = (0, 0)
        self.end = (Maze.size[0]-1, Maze.size[1]-1)

    def get_random_maze(self) -> "list[list[bool]]":
        return np.random.rand(self.size[0],self.size[1])>.5

if __name__ == '__main__':
    maze = Maze()
    maze.solve()
        

