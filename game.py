import pygame
import random
import math
import definitions
import os
import subprocess

pygame.init()

# get the screen size
definitions.REAL_SCREEN_WIDTH = pygame.display.Info().current_w
definitions.REAL_SCREEN_HEIGHT = pygame.display.Info().current_h


# open the window in borderless fullscreen
screen = pygame.display.set_mode((definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT), pygame.RESIZABLE)
# center the window
os.environ['SDL_VIDEO_CENTERED'] = '1'

world_width = 1000
world_height = 800
world = pygame.Surface((world_width, world_height))

print(world)

game_element = pygame.Surface((32, 32))
game_element.fill((255, 0, 0))
world.blit(game_element, (0, 0))

screen_view = pygame.Surface((definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT))

scroll_x = 0
scroll_y = 0
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break            
    # if the winow is resized, update the definitions
    if event.type == pygame.VIDEORESIZE:
        definitions.SCREEN_WIDTH = event.w
        definitions.SCREEN_HEIGHT = event.h

    scroll_x += 1
    scroll_y += 1
    world.scroll(-scroll_x, -scroll_y)

    

    # if wasd or arrow keys are pressed
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            pass
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            pass
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            pass
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            pass

    # Clear the screen and set the screen background
    screen.fill(definitions.BLACK)

    # draw a blue circle at position (500, 500) with a radius of 20
    pygame.draw.circle(screen, definitions.BLUE, (500, 500), 20)

    screen_view.blit(world, (0, 0), (scroll_x, scroll_y, definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT))

    screen.blit(screen_view, (0, 0))
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()

