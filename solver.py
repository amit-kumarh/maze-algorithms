from maze import Maze


class Solver:

    @staticmethod
    def algo_1(maze: Maze) -> "list[tuple(int, int)]":
        path = []

        for x in range(maze.size[0]-1):
            path.append((x,0))

        for y in range(maze.size[1]-1):
            path.append((maze.size[0]-2,y))


        # fill in function here

        
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
                  ("algo 1", algo_1.__get__(object)), 
                  ("algo 2", algo_2.__get__(object)), 
                  ("algo 3", algo_3.__get__(object)),
                  ]

    n_algos = len(algorithms)
