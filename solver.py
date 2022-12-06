from maze import Maze
import collections


ADJACENT = ((1, 0), (-1, 0), (0, 1), (0, -1))
def getValidMoves(maze, cell):
    neighbors = []
    for i, j in ADJACENT:
        row = cell[0] + i
        col = cell[1] + j
        if row not in range(0, maze.end[0]+1) or col not in range(0, maze.end[1]+1):
            continue

        if maze.grid[row][col] == 0:
            neighbors.append((row, col))

    return neighbors

class Solver:
    def bfs(self, maze: Maze) -> "list[tuple(int, int)]":
        visited = {}
        queue = collections.deque()
        queue.append((0,0))

        while queue:
            curr = queue.pop()
            if curr == maze.end:
                break

            moves = getValidMoves(maze, curr)
            for move in moves:
                if move not in visited:
                    queue.append(move)
                    visited[move] = curr

        path = []
        path.append(visited[curr])
        while curr != maze.start:
            path.append(curr := visited[curr])

        path = list(reversed(path))
        return path

    @staticmethod
    def algo_2(maze: Maze) -> "list[tuple(int, int)]":
        path = []

        for x in range(maze.size[0]-1):
            path.append((x,0))

        for y in range(maze.size[1]-1):
            path.append((maze.size[0]-2,y))


        # fill in function here

        
        return path
        
    @staticmethod
    def algo_3(maze: Maze) -> "list[tuple(int, int)]":
        path = []

        for y in range(maze.size[1]-1):
            path.append((0,y))

        for x in range(maze.size[0]-1):
            path.append((x,maze.size[1]-1))

        

        return path
    
    algorithms = [
                  ("bfs", bfs.__get__(object)), 
                  ("algo 2", algo_2.__get__(object)), 
                  ("algo 3", algo_3.__get__(object)),
                  ]

    n_algos = len(algorithms)
