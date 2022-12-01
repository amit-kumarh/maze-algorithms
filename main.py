from interface import *
from maze import *
from solver import *
from runner import *

import sys
import pygame
from pygame.locals import *


def main():
    display = Interface()
    maze = Maze()
    solver = Solver()
    runner = Runner(display, maze, solver)

    clock = pygame.time.Clock()
    
    while True:
        clock.tick(60)
        runner.get_updates()
        runner.push_updates()

if __name__ == "__main__":
    main()



