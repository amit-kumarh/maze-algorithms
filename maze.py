import collections
import numpy as np
import random
import collections

class Maze():
    size = (79,49)
    maze = [[True]*size[0]] * size[1]

    def __init__(self):
        # self.grid = Maze.get_random_maze(Maze) 
        self.grid = Maze.recursive_random_maze(False)
        self.start = (0, 0)
        self.end = (Maze.size[0]-1, Maze.size[1]-1)

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

    def recursive_random_maze(prim) -> "list[list[bool]]":
        maze_x: int = int((Maze.size[0]-1)/2)
        maze_y: int = int((Maze.size[1]-1)/2)
        
        grid  = [[1 for _ in range(Maze.size[1])]for _ in range(Maze.size[0])]
        
        
        current = (random.randint(0,maze_x-1), random.randint(0,maze_y-1), "S")
        visited = []
        path = []


        def get_options(current):
            options = []
            if current[1] != 0:
                options.append((current[0], current[1]-1, "N"))
            if current[0] != 0:
                options.append((current[0] - 1, current[1], "W"))
            if current[1] < maze_y-1:
                options.append((current[0], current[1]+1, "S"))
            if current[0] < maze_x-1:
                options.append((current[0]+1, current[1], "E"))

            return options

        def dfs(current, visited):

            loc = (current[0], current[1])
            if loc not in visited:
                visited.append(loc)
                path.append(current)
                options = get_options(current)
                if options == None:
                    return
                random.shuffle(options)
                for option in options:
                    dfs(option, visited)

        dfs(current, visited)

        for x,y,dir in path:
            grid_x = 2*x + 1
            grid_y = 2*y + 1
            if dir == "N":
                grid[grid_x][grid_y] = 0
                grid[grid_x][grid_y+1] = 0
            elif dir == "E":
                grid[grid_x][grid_y] = 0
                grid[grid_x-1][grid_y] = 0
            elif dir == "S":
                grid[grid_x][grid_y] = 0
                grid[grid_x][grid_y-1] = 0
            elif dir == "W":
                grid[grid_x][grid_y] = 0
                grid[grid_x + 1][grid_y] = 0

        grid[0][0] = 0
        grid[1][0] = 0
        grid[Maze.size[0]-1][Maze.size[1]-1] = 0
        grid[Maze.size[0]-2][Maze.size[1]-1] = 0


        return grid

    def new_maze(self, prim=False):
        self.grid = Maze.recursive_random_maze(prim)


    def prim(self):
        TWO_AWAY = [(-2, 0), (2, 0), (0, 2), (0, -2)]
        def get_frontiers(curr):
            frontiers = []
            for dx, dy in TWO_AWAY:
                nx, ny = curr[0] + dx, curr[1] + dy
                if 0 <= nx < Maze.size[0] and 0 <= ny < Maze.size[1]:
                    if grid[nx][ny] == 1:
                        frontiers.append((nx, ny))
            return frontiers

        def get_neighbors(curr):
            neighbors = []
            for dx, dy in TWO_AWAY:
                nx, ny = curr[0] + dx, curr[1] + dy
                if 0 <= nx < Maze.size[0] and 0 <= ny < Maze.size[1]:
                    if grid[nx][ny] == 0:
                        neighbors.append((nx, ny))
            return neighbors

        def midpoint(frontier, neighbor):
            fx, fy = frontier
            nx, ny = neighbor
            return ((fx+nx)//2, (fy+ny)//2)

        def connect(frontier, neighbor):
            mx, my = midpoint(frontier, neighbor)
            grid[mx][my] = 0

        grid  = [[1 for j in range(Maze.size[1])] for i in range(Maze.size[0])]
        curr = (random.randint(1,Maze.size[0]-2), random.randint(1,Maze.size[1]-2))
        grid[curr[0]][curr[1]] = 0
        q = get_frontiers(curr)
        while q:
            curr = q.pop(random.randint(0, len(q)-1))
            if grid[curr[0]][curr[1]] == 1:
                grid[curr[0]][curr[1]] = 0
                neighbors = get_neighbors(curr)
                n = random.choice(neighbors)
                connect(curr, n)
                for f in get_frontiers(curr):
                    q.append(f)

        grid[0][0] = 0
        grid[1][0] = 0
        grid[Maze.size[0]-1][Maze.size[1]-1] = 0
        grid[Maze.size[0]-2][Maze.size[1]-1] = 0
        self.grid = grid
        
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
        

