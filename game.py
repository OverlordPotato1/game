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
world = pygame.Surface((world_width, world_height), pygame.SRCALPHA)

print(world)

player = pygame.Surface((32, 32))
player.fill((255, 0, 0))
world.blit(player, (0, 0))

screen_view = pygame.Surface((definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT))

key_up_pressed = False
key_down_pressed = False
key_left_pressed = False
key_right_pressed = False

clock = pygame.time.Clock()
fps = 180

scroll_x = 0
scroll_y = 0

sw = definitions.SCREEN_WIDTH
sh = definitions.SCREEN_HEIGHT

doTheThing = True
while doTheThing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doTheThing = False
        # if the window is resized, update the definitions
        if event.type == pygame.VIDEORESIZE:
            sw = event.w
            sh = event.h
            print(sw, sh)

        # if wasd or arrow keys are pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                key_up_pressed = True
            elif event.key == pygame.K_DOWN:
                key_down_pressed = True
            elif event.key == pygame.K_LEFT:
                key_left_pressed = True
            elif event.key == pygame.K_RIGHT:
                key_right_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                key_up_pressed = False
            elif event.key == pygame.K_DOWN:
                key_down_pressed = False
            elif event.key == pygame.K_LEFT:
                key_left_pressed = False
            elif event.key == pygame.K_RIGHT:
                key_right_pressed = False

# Update the scrolling position based on the key flags
    if key_up_pressed:
        scroll_y += 1
        if key_left_pressed:
            # run the left walk animation
            pass
        else:
            # run the right walk animation
            pass
    if key_down_pressed:
        scroll_y -= 1
    if key_left_pressed:
        scroll_x += 1
    if key_right_pressed:
        scroll_x -= 1

    # Clear the screen and set the screen background
    # screen.fill((180, 0, 180))

    # # draw a blue circle at position (500, 500) with a radius of 20
    # pygame.draw.circle(screen, definitions.BLUE, (500, 500), 20)

    screen_view.blit(world, (0, 0), (scroll_x, scroll_y, sw, sh))

    screen.blit(world, (0, 0), (scroll_x, scroll_y, sw, sh))
    pygame.display.flip()

    clock.tick(fps)

# Be IDLE friendly
pygame.quit()

