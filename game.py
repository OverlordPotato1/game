import pygame
import definitions
import os

import func
from classes.spritesheet import spritesheet
from classes.keys import Key
from classes.animator import Animator
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

rightPlayerSprites = spritesheet("Images/Knight-Walk-Sheet-sword-right.png", (64, 64))  # load the spritesheet and divide it into 64 x 64 squares
rightPlayerSprites.separate_spritesheet()
rightPlayerSprites.resize_sprites((player_width, player_height))
rightSwordWalk = rightPlayerSprites.returnSprites("list")  # return the spritesheet as a list

leftPlayerSprites = spritesheet("Images/Knight-Walk-Sheet-sword-left.png", (64, 64))
leftPlayerSprites.separate_spritesheet()
leftPlayerSprites.resize_sprites((player_width, player_height))
leftSwordWalk = leftPlayerSprites.returnSprites("list")

activeAnimationList = rightSwordWalk

playerAnim = Animator(activeAnimationList)  # resize the sprites and pass them to the Animator constructor as a spritesheet

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

lastDirection = 0

doTheThing = True
while doTheThing:
    succeed = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doTheThing = False
        # handle window resizes
        sw, sh = func.handle_resize(event, sw, sh)

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
    if up and not down:
        scroll_y += 1
        succeed += 1
    if down and not up:
        scroll_y -= 1
        succeed += 1
    if left and not right:
        scroll_x += 1
        if lastDirection == 0:
            playerAnim.switch_sheet(leftSwordWalk)
            lastDirection = 1
        succeed += 1
    if right and not left:
        scroll_x -= 1
        if lastDirection == 1:
            playerAnim.switch_sheet(rightSwordWalk)
            lastDirection = 0
        succeed += 1
    if succeed == 0:
        playerAnim.ticks_since = 0

    screen_view.blit(world, (0, 0), (scroll_x, scroll_y, sw, sh))

    screen.blit(world, (0, 0), (scroll_x, scroll_y, sw, sh))
    pygame.display.flip()

    clock.tick(fps)

pygame.quit()
