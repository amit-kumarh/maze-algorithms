from interface import *
from maze import *
from solver import *

import sys
import pygame
from pygame.locals import *

class Runner():
    def __init__(self, interface: Interface, maze: Maze, solver: Solver) -> None:
        self.interface = interface
        self.maze = maze
        self.solver = solver

    def get_updates(self) -> None:
        self.interface.get_updates()

        for event in self.interface.events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    
    def push_updates(self) -> None:
        self.interface.refresh_window



        