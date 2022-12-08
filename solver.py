from maze import Maze
import matplotlib.pyplot as plt
import collections
import random


ADJACENT = {'N': (1, 0), 'S': (-1, 0), 'E':(0, 1), 'W':(0, -1)}
def getValidMoves(maze, cell):
    neighbors = {}
    dirs = []
    for d, (i, j) in ADJACENT.items():
        row = cell[0] + i
        col = cell[1] + j
        if row not in range(0, maze.end[0]+1) or col not in range(0, maze.end[1]+1):
            continue

        if maze.grid[row][col] == 0:
            neighbors[d] = (row, col)

    return neighbors

class Solver:

    @staticmethod
    def bfs(maze: Maze) -> "list[tuple(int, int)]":
        visited = {}
        queue = collections.deque()
        queue.append((0,0))

        while queue:
            curr = queue.pop()
            if curr == maze.end:
                print('Reached End')
                break

            moves = getValidMoves(maze, curr)
            for move in moves.values():
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
    def mouse(maze: Maze) -> "list[tuple(int, int)]":
        curr = maze.start
        dir = None
        path = []
        path.append(curr)
        while curr != maze.end:
            neighbors = getValidMoves(maze, curr)
            if dir not in neighbors:
                dir = random.choice(list(neighbors.keys()))
                curr = neighbors[dir]
            else:
                curr = neighbors[dir]

            path.append(curr)
            plt.pcolormesh(maze.grid)

        print(len(path))
        return list(set(path))


        
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
                  ("mouse", mouse.__get__(object)), 
                  ("algo 3", algo_3.__get__(object)),
                  ]
    n_algos = len(algorithms)
