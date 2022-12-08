from maze import Maze
import matplotlib.pyplot as plt
import collections
import random
import numpy as np


ADJACENT = {'N': (0, -1), 'S': (0, 1), 'E':(1, 0), 'W':(-1, 0)}
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
    def bfs(maze: Maze) -> "list[list[int]]":
        visited = {}
        path = [[0 for i in range(Maze.size[0])]for j in range(Maze.size[1])]
        queue = collections.deque()
        queue.append((0,0))

        while queue:
            curr = queue.pop()
            if curr == maze.end:
                break

            moves = getValidMoves(maze, curr)
            for move in moves.values():
                if move not in visited:
                    queue.append(move)
                    visited[move] = curr

        path[curr[1]][curr[0]] = 1
        while curr != maze.start:
           path[curr[1]][curr[0]] = 1
           curr = visited[curr]

        return path

    @staticmethod
    def mouse(maze: Maze) -> "list[tuple(int, int)]":
        curr = maze.start
        dir = None
        path = []
        path.append(curr)
        while curr != maze.end:
            neighbors = getValidMoves(maze, curr)
            if len(neighbors) > 2 or dir not in neighbors:
                dir = random.choice(list(neighbors.keys()))
                curr = neighbors[dir]
            else:
                curr = neighbors[dir]

            path.append(curr)

        grid = [[0 for i in range(maze.size[0])] for j in range(maze.size[1])]
        for x, y in path:
            grid[y][x] = 1
        print(len(path))
        return grid


        
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
