"""
File containing all definitions for the game that are used in multiple files
"""
import pygame
import os

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
BROWN = (165, 42, 42)
PINK = (255, 192, 203)
GREY = (128, 128, 128)
DARK_GREY = (64, 64, 64)
LIGHT_GREY = (192, 192, 192)
DARK_GREEN = (0, 100, 0)
DARK_BLUE = (0, 0, 128)
DARK_RED = (128, 0, 0)
DARK_YELLOW = (128, 128, 0)
DARK_ORANGE = (255, 140, 0)
DARK_PURPLE = (128, 0, 128)
DARK_CYAN = (0, 128, 128)
DARK_BROWN = (128, 64, 0)
DARK_PINK = (255, 20, 147)
LIGHT_GREEN = (0, 255, 0)
LIGHT_BLUE = (0, 0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

TILE_SIZE = 32

FILEPATH = str(os.path.dirname(os.path.abspath(__file__)))

LIST = "list"
DICT = "dict"

UP_KEYS = [pygame.K_UP, pygame.K_w]
DOWN_KEYS = [pygame.K_DOWN, pygame.K_s]
LEFT_KEYS = [pygame.K_LEFT, pygame.K_a]
RIGHT_KEYS = [pygame.K_RIGHT, pygame.K_d]

tile_size = 64
