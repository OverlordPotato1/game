import pygame
import definitions
import os

import func
from classes.spritesheet import Spritesheet
from classes.keys import Key
from classes.animator import Animator
from func import resize_sprites
from classes.movement import Movement
from this_is_kinda_stupid_now import *

pygame.init()

screen = pygame.display.set_mode((definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT), pygame.RESIZABLE)
os.environ['SDL_VIDEO_CENTERED'] = '1'  # center the window

world_width = 1000
world_height = 800
world = pygame.Surface((world_width, world_height), pygame.SRCALPHA)  # pygame.SRCALPHA is required to have a transparent background on pngs

player = pygame.Surface((512, 512), pygame.SRCALPHA)  # define the player surface, pygame.SRCALPHA is still required because the surface needs to be transparent

player_height = player_width = 128

rightSwordWalk = func.easy_spritesheet("Images/Knight-Walk-Sheet-sword-right.png", (64, 64), (player_width, player_height))

leftSwordWalk = func.easy_spritesheet("Images/Knight-Walk-Sheet-sword-left.png", (64, 64), (player_width, player_height))

idle = func.easy_spritesheet("Images/Downloaded/Fantasy Pixel Art Asset Pack/Knight-Idle-Sheet.png", (64, 64), (player_width*0.9, player_height*0.9))


activeAnimationList = rightSwordWalk

playerAnim = Animator(activeAnimationList, 9)  # resize the sprites and pass them to the Animator constructor as a spritesheet
playerWalk = Movement(playerAnim, leftSwordWalk, rightSwordWalk, idle, 3.6)

screen_view = pygame.Surface((definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT))

clock = pygame.time.Clock()

fps = 60

scroll_x = scroll_y = 0

sw, sh = create_base_window_size()

up, down, left, right = create_movement_objects()

doTheThing = True
while doTheThing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doTheThing = False
        # handle window resizes
        sw, sh = func.handle_resize(event, sw, sh)
        if event.type == pygame.WINDOWRESIZED:
            playerWalk.new_sprites(func.resize_sprites(leftSwordWalk, (sw/12, sw/12)), func.resize_sprites(rightSwordWalk, (sw/12, sw/12)), func.resize_sprites(idle, (sw/12, sw/12)))

        # update the states of the up down left right things
        up(event)
        down(event)
        left(event)
        right(event)

    screen.fill((100, 0, 140, 0))
    world.fill((0, 0, 0, 0))

    player.fill((0, 0, 0, 0))
    player.blit(playerAnim(), (0, 0))
    world.blit(player, (0, 0))

    # Update the scrolling position based on the key flags
    scroll_x, scroll_y = playerWalk(up, down, left, right, scroll_x, scroll_y)

    screen_view.blit(world, (0, 0), (scroll_x, scroll_y, sw, sh))

    screen.blit(world, (0, 0), (scroll_x, scroll_y, sw, sh))
    pygame.display.flip()

    clock.tick(fps)

pygame.quit()
