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
    
    def push_updates(self) -> None:
        self.interface.refresh_window()



        