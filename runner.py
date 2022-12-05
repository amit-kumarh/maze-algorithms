from interface import *
from maze import *
from solver import *

class Runner():
    def __init__(self, interface: Interface, maze: Maze, solver: Solver) -> None:
        self.interface = interface
        self.maze = maze

        self.cur_algo = 0
        self.algo_selected = False
        self.solution = None


    def get_updates(self) -> None:
        self.interface.get_updates()

        if self.algo_selected:
            algo = Solver.algorithms[self.cur_algo][1]
            self.solution = algo(self.maze)
            self.algo_selected = False

        for event in self.interface.events:
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.cur_algo+= 1
                elif event.key == K_LEFT:
                    self.cur_algo -= 1
                if event.key == K_RETURN:
                    self.algo_selected = True
            if self.cur_algo > Solver.n_algos-1:
                self.cur_algo = Solver.n_algos-1
            if self.cur_algo < 0:
                self.cur_algo = 0

            
    def push_updates(self) -> None:
        self.interface.push_updates(self.maze, self.solution, self.cur_algo)




        