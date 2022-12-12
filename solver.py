from maze import Maze
import matplotlib.pyplot as plt
import collections
import random
import numpy as np
from time import perf_counter


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
        start = perf_counter()
        visited = {}
        grid = [[0 for i in range(Maze.size[0])]for j in range(Maze.size[1])]
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

        grid[curr[1]][curr[0]] = 1
        while curr != maze.start:
           grid[curr[1]][curr[0]] = 1
           curr = visited[curr]

        duration = (perf_counter() - start)*1000
        return grid, duration

    @staticmethod
    def mouse(maze: Maze) -> "list[tuple(int, int)]":
        start = perf_counter()
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
        duration = (perf_counter() - start)*1000
        return grid, duration

    @staticmethod
    def wall_follow(maze: Maze) -> "list[tuple(int, int)]":
        start = perf_counter()
        path = [[0 for i in range(Maze.size[0])]for j in range(Maze.size[1])]

        curr = maze.start

        direction = "S"

        while curr != maze.end:

            print(curr)
            print(direction)
            print(getValidMoves(maze, curr).values())


            if direction == "S":

                front_cell = (curr[0],curr[1]-1)
                right_cell = (curr[0]-1, curr[1])
                if right_cell in getValidMoves(maze, curr).values():
                    direction = "W"
                elif front_cell in getValidMoves(maze, curr).values():
                    curr = front_cell
                else:
                    direction = "E"
                continue
            if direction == "E":
                front_cell = (curr[0]+1, curr[1])
                right_cell = (curr[0], curr[1]-1)
                if right_cell in getValidMoves(maze, curr).values():
                    direction = "S"
                elif front_cell in getValidMoves(maze, curr).values():
                    curr = front_cell
                else:
                    direction = "N"
                continue
            if direction == "N":
                front_cell = (curr[0], curr[1]+1)
                right_cell = (curr[0]+1, curr[1])
                if right_cell in getValidMoves(maze, curr).values():
                    direction = "E"
                elif front_cell in getValidMoves(maze, curr).values():
                    curr = front_cell
                else:
                    direction = "W"
                continue
            if direction == "W":
                front_cell = (curr[0]-1, curr[1])
                right_cell = (curr[0], curr[1]+1)
                if right_cell in getValidMoves(maze, curr).values():
                    direction = "N"
                elif front_cell in getValidMoves(maze, curr).values():
                    curr = front_cell
                else:
                    direction = "S"
                continue
            print()


        duration = (perf_counter() - start)*1000
        return path, duration

    
    algorithms = [
                  ("bfs", bfs.__get__(object)), 
                  ("mouse", mouse.__get__(object)), 
                  ("wall follow", wall_follow.__get__(object)),
                  ]
    n_algos = len(algorithms)
