import numpy as np
import random

class Maze():
    size = (80,50)
    maze = [[True]*size[0]] * size[1]

    def __init__(self):
        
        self.grid = self.get_random_maze()

    def get_random_maze(self) -> "list[list[bool]]":
        
        x = random.randrange(self.size[0])
        y = random.randrange(self.size[1])
        
        random_cell = self.maze[int(x),int(y)] 
        random_cell = False
        frontier_cells = [[x-2,y], [x+2,y], [x,y-2], [x, y+2]]

        
        #return maze

        return np.random.rand(self.size[0],self.size[1])>.5

        """ Pick a random Cell, set it to state Passage and Compute its frontier cells. A frontier cell of a Cell 
        is a cell with distance 2 in state Blocked and within the grid.
        While the list of frontier cells is not empty:
        Pick a random frontier cell from the list of frontier cells.
        Let neighbors(frontierCell) = All cells in distance 2 in state Passage. Pick a random neighbor and connect 
        the frontier cell with the neighbor by setting the cell in-between to state Passage. Compute the frontier 
        cells of the chosen frontier cell and add them to the frontier list. Remove the chosen frontier cell from the
        list of frontier cells. """



        