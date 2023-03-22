import pygame
import definitions
import os
from spritesheet import spritesheet
from keys import Key
from animator import Animator
from func import resize_sprites

pygame.init()

screen = pygame.display.set_mode((definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT), pygame.RESIZABLE)
os.environ['SDL_VIDEO_CENTERED'] = '1'  # center the window

world_width = 1000
world_height = 800
world = pygame.Surface((world_width, world_height),
                       pygame.SRCALPHA)  # pygame.SRCALPHA is required to have a transparent background on pngs

player = pygame.Surface((512, 512), pygame.SRCALPHA)  # define the player surface

player_width = 128
player_height = player_width  # set the width and height that the sprites will be expanded to

rightPlayerSprites = spritesheet("Knight-Walk-Sheet-sword-right.png", (64, 64))  # load the spritesheet and divide it into 64 x 64 squares
activeAnimationList = rightPlayerSprites.returnSprites("list")  # return the spritesheet as a list

playerAnim = Animator(
    resize_sprites(activeAnimationList, (player_width, player_height))
    )  # resize the sprites and pass them to the Animator constructor as a spritesheet

screen_view = pygame.Surface((definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT))

clock = pygame.time.Clock()

fps = 180

scroll_x = 0
scroll_y = 0

sw = definitions.SCREEN_WIDTH
sh = definitions.SCREEN_HEIGHT

up = Key([pygame.K_UP, pygame.K_w])
down = Key([pygame.K_DOWN, pygame.K_s])
left = Key([pygame.K_LEFT, pygame.K_a])
right = Key([pygame.K_RIGHT, pygame.K_d])

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
    if up:
        scroll_y += 1
    if down:
        scroll_y -= 1
    if left:
        scroll_x += 1
    if right:
        scroll_x -= 1

    screen_view.blit(world, (0, 0), (scroll_x, scroll_y, sw, sh))

    screen.blit(world, (0, 0), (scroll_x, scroll_y, sw, sh))
    pygame.display.flip()

    clock.tick(fps)

# Be IDLE friendly
pygame.quit()
