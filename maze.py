import collections
import numpy as np

class Maze():
    size = (79,49)
    def __init__(self):
        self.grid = Maze.get_maze_from_text("./sample.txt")
        self.start = (0, 0)
        self.end = (Maze.size[0]-1, Maze.size[1]-1)

    @staticmethod
    def get_random_maze(self) -> "list[list[bool]]":
        return np.random.rand(self.size[0],self.size[1])>.5

    def get_maze_from_text(filename: str):
        maze = np.zeros((Maze.size))
        with open(filename) as f:
            for row_idx, row in enumerate(f.readlines()):
                for col_idx, col in enumerate(row):
                    if col == "#":
                        maze[col_idx][row_idx] = 1
                        
        
        return maze

    

if __name__ == '__main__':
    maze = Maze()
    maze.solve()
        

