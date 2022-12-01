import sys
import pygame
from pygame.locals import *

class Interface:
    def __init__(self) -> None:
        pygame.init()

        WINDOW_SIZE = (640, 480)
        self.screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
        pygame.display.set_caption("Maze Algorithms")

        # create internal pygame window
        DISPLAY_SIZE = (640, 480)
        self.display = pygame.Surface(DISPLAY_SIZE)
        
        self.events = pygame.event.get()

    def refresh_window(self):
        """
        Refresh and draw the screen
        """
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
