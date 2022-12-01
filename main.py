from display import *
from maze import *
from solver import *
from runner import *


def main():
    display = Interface()
    maze = Maze()
    solver = Solver()
    runner = Runner(display, maze, solver)
    
    while runner.still_running():
        runner.get_updates()
        runner.push_updates()

if __name__ == "__main__":
    main()



