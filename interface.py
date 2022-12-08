import sys
import pygame
from pygame.locals import *
import numpy as np

from maze import Maze
from solver import Solver

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)
light_grey = (206, 219, 211)
dark_grey = (80, 84, 82)
red = (255, 0, 0)

BLOCK_SIZE = 10

class Interface:
    def __init__(self) -> None:
        pygame.init()

        WINDOW_SIZE = (640, 480)
        self.screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
        pygame.display.set_caption("Maze Algorithms")

        # create internal pygame window
        DISPLAY_SIZE = (BLOCK_SIZE*100, BLOCK_SIZE*75)
        self.display = pygame.Surface(DISPLAY_SIZE)
        
        self.events = pygame.event.get()

    def refresh_window(self):
        """
        Refresh and draw the screen
        """
        self.screen.fill(black)
        new_window_size, center_cords = self.adjust_scale()
        # scale internal display to match window)

        new_disp = pygame.transform.scale(self.display, new_window_size)
        self.screen.blit(new_disp, center_cords)

        pygame.display.update()

    def adjust_scale(self):
        """
        Adjust internal screen for window scaling

        If the window size is changed, scale the game to the maximum amount
        while keeping the same aspect ratio. Also keep the game centered in the
        window.

        Returns:
            display_size::tuple (height, width)
                The updated height and width of the internal game display
            cords::tuple (x_cord, y_cord)
                The cordinates of the upper left corner of the internal game
                display so that when it is blit onto window, it is centered.
        """
        window_size = self.screen.get_size()

        # if window is longer than aspect ratio
        if window_size[0] / window_size[1] >= 1.5:
            display_size = (int(1.5 * window_size[1]), window_size[1])
        # if window is taller than aspect ratio
        else:
            display_size = (window_size[0], int(.75 * window_size[0]))
        # find cords so that display is centered
        cords = ((window_size[0] - display_size[0]) / 2,
                 (window_size[1] - display_size[1]) / 2)

        return display_size, cords

    def get_updates(self) -> None:
        self.events = pygame.event.get()


    def push_updates(self, maze, solution, cur_algo) -> None:
        for event in self.events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        
        self.draw_main(maze, solution, cur_algo)

        self.refresh_window()

    def get_x_center(self) -> int :
        return self.display.get_size()[0]/2


    def draw_maze(self, maze: Maze):
        maze_size = (BLOCK_SIZE*Maze.size[0], BLOCK_SIZE*Maze.size[1])

        border_size = (maze_size[0]+2*BLOCK_SIZE, maze_size[1] +2*BLOCK_SIZE)

        maze_x = float(float(self.display.get_size()[0] - BLOCK_SIZE*Maze.size[0])/2)
        maze_y = 100
        maze_background = pygame.Rect((maze_x,maze_y),maze_size)

        border = pygame.Rect((maze_x - BLOCK_SIZE, maze_y - BLOCK_SIZE), border_size)

        pygame.draw.rect(self.display, dark_grey, border)

        pygame.draw.rect(self.display, light_grey, maze_background)

        # draw lines
        for row_idx, row in enumerate(maze.grid):
            for col_idx, col in enumerate(row):
                if col:
                    # draw square
                    wall_loc = (maze_x + BLOCK_SIZE*row_idx, maze_y + BLOCK_SIZE*col_idx)
                    wall_size = (BLOCK_SIZE, BLOCK_SIZE)
                    wall = pygame.Rect(wall_loc, wall_size)
                    pygame.draw.rect(self.display, black, wall)



    def draw_solution(self, solution) -> None:
        if solution != None:
            grid = solution


        
            thickness = BLOCK_SIZE/1.5

            for row_idx, row in enumerate(grid[0:-1]):
                for col_idx, col in enumerate(row[0:-1]):
                    current_point = grid[row_idx][ col_idx]
                    right_point = grid[row_idx][col_idx+1]
                    down_point = grid[row_idx+1][col_idx]

                    y_offset = 100 + (BLOCK_SIZE-thickness)/2
                    x_offset = ((self.display.get_size()[0] - BLOCK_SIZE*Maze.size[0])/2)+ (BLOCK_SIZE-thickness)/2

                    line_loc = (BLOCK_SIZE*col_idx + x_offset, BLOCK_SIZE*row_idx+ y_offset)
                    # current point is visited
                    if current_point == 1:
                        if right_point == 1:
                            line_size = (BLOCK_SIZE+thickness, thickness)
                            line = pygame.Rect(line_loc, line_size)

                            pygame.draw.rect(self.display, red, line)
                            
                        if down_point == 1:
                            line_size = (thickness, BLOCK_SIZE+thickness)
                            line = pygame.Rect(line_loc, line_size)

                            pygame.draw.rect(self.display, red, line)
                           

                        



        

    def draw_algos(self, cur_algo) -> None:
        n_items = Solver.n_algos
        item_width = BLOCK_SIZE*Maze.size[0]/(n_items+1)
        button_start = (self.display.get_size()[0] - BLOCK_SIZE*Maze.size[0])/2 - BLOCK_SIZE
        item_spacing = (Maze.size[0]*BLOCK_SIZE - n_items*item_width + 2*BLOCK_SIZE)/(n_items+1)
        
        for algo_idx, algo in enumerate(Solver.algorithms):
            button_loc = (algo_idx*(item_width + item_spacing)+button_start + item_spacing, Maze.size[1]*BLOCK_SIZE+150)
            button_size = (item_width, 50)
            button = pygame.Rect(button_loc, button_size)
            pygame.draw.rect(self.display, dark_grey, button)

            label = pygame.font.Font('freesansbold.ttf', 30).render(algo[0], True, white, dark_grey)
            label_rect = label.get_rect()
            label_rect.center = (button_loc[0]+item_width/2, button_loc[1]+25)
            self.display.blit(label, label_rect)
        
        bar_loc = (cur_algo*(item_width + item_spacing)+button_start + item_spacing, Maze.size[1]*BLOCK_SIZE+150+50)
        bar_size = ( BLOCK_SIZE*Maze.size[0]/(n_items+1), BLOCK_SIZE)
        bar = pygame.Rect(bar_loc, bar_size)
        pygame.draw.rect(self.display, black, bar)


    def draw_main(self, maze, solution, cur_algo) -> None:

        self.display.fill(light_grey)

        title = pygame.font.Font('freesansbold.ttf', 30).render('Maze Algorithms', True, black, light_grey)
        title_rect = title.get_rect()
        title_rect.center = (self.get_x_center(), 50)


        self.draw_maze(maze)
        
        self.draw_algos(cur_algo)
        self.draw_solution(solution)
        
       

        self.display.blit(title, title_rect)
        




        

    
