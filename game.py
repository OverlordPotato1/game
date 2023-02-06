import pygame
import random
import math
import definitions
import os
import subprocess
import simple_pid

pygame.init()

# get the screen size
definitions.REAL_SCREEN_WIDTH = pygame.display.Info().current_w
definitions.REAL_SCREEN_HEIGHT = pygame.display.Info().current_h


# open the window in borderless fullscreen
screen = pygame.display.set_mode((definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT), pygame.RESIZABLE)
# center the window
os.environ['SDL_VIDEO_CENTERED'] = '1'


while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break            
    # if the winow is resized, update the definitions
    if event.type == pygame.VIDEORESIZE:
        definitions.SCREEN_WIDTH = event.w
        definitions.SCREEN_HEIGHT = event.h

    # Clear the screen and set the screen background
    screen.fill(definitions.BLACK)

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, definitions.BLUE, (definitions.SCREEN_WIDTH // 2, definitions.SCREEN_HEIGHT // 2), 20)


    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()

