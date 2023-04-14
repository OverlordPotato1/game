import pygame
import os

import func
from classes.animator import Animator
from classes.movement import Movement
from this_is_kinda_stupid_now import *
from classes.json_handler import JsonFile
from level_loader import level_loader

pygame.init()

screen = pygame.display.set_mode((definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT), pygame.RESIZABLE)
os.environ['SDL_VIDEO_CENTERED'] = '1'  # center the window

world_width = 1000
world_height = 800
world = pygame.Surface((world_width, world_height), pygame.SRCALPHA)  # pygame.SRCALPHA is required to have a transparent background on pngs

player = pygame.Surface((512, 512), pygame.SRCALPHA)  # define the player surface, pygame.SRCALPHA is still required because the surface needs to be transparent

player_height = player_width = 128

rightSwordWalk = func.easy_spritesheet("Images/knight walks/Knight-Walk-Sheet-sword-right.png", (64, 64), (player_width, player_height))

leftSwordWalk = func.easy_spritesheet("Images/knight walks/Knight-Walk-Sheet-sword-left.png", (64, 64), (player_width, player_height))

idle = func.easy_spritesheet("Images/Downloaded/Fantasy Pixel Art Asset Pack/Knight-Idle-Sheet.png", (64, 64), (player_width*0.9, player_height*0.9))


activeAnimationList = rightSwordWalk

playerAnim = Animator(activeAnimationList, 9)  # resize the sprites and pass them to the Animator constructor as a spritesheet
playerWalk = Movement(playerAnim, leftSwordWalk, rightSwordWalk, idle, 3.6)

screen_view = pygame.Surface((definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT), pygame.SRCALPHA)

clock = pygame.time.Clock()

fps = 60

scroll_x = scroll_y = 0

sw, sh = create_base_window_size()

percentOfScreen = 0.15

playerWalk.new_sprites(func.resize_sprites(leftSwordWalk, (sw*percentOfScreen, sw*percentOfScreen)), func.resize_sprites(rightSwordWalk, (sw*percentOfScreen, sw*percentOfScreen)), func.resize_sprites(idle, (sw*percentOfScreen, sw*percentOfScreen)))
playerWalk.move_speed = sh/200
prevSw = sw
prevSh = sh

up, down, left, right = create_movement_objects()

playerScreenCoverage = player_width / sw

screenSizeRatio = definitions.SCREEN_WIDTH / definitions.SCREEN_HEIGHT

font = pygame.font.SysFont(None, 25)

player_collide_group = []

# Create a level_loader instance
lvl_loader = level_loader(screen_view, "levels/", "textures.json", player_collide_group)

# Load a new level
lvl_loader.new_lvl("test.lvl")

frames = 0


doTheThing = True
while doTheThing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doTheThing = False
        # handle window resizes
        sw, sh = func.handle_resize(event, sw, sh)
        if event.type == pygame.WINDOWRESIZED:
            playerWalk.new_sprites(func.resize_sprites(leftSwordWalk, (sw * playerScreenCoverage, sw * playerScreenCoverage)),
                                   func.resize_sprites(rightSwordWalk, (sw * playerScreenCoverage, sw * playerScreenCoverage)),
                                   func.resize_sprites(idle, (sw * playerScreenCoverage, sw * playerScreenCoverage)))
            player_height = player_width = sw*playerScreenCoverage

            playerWalk.move_speed = sh / 200

            widthPercentOffset = scroll_x / prevSw
            heightPercentOffset = scroll_y / prevSh

            scroll_x = sw * widthPercentOffset
            scroll_y = sh * heightPercentOffset

            prevSh = sh
            prevSw = sw

            # sw = screenSizeRatio * sw
            # sh = screenSizeRatio * sh
            # screen.

        # update the states of the up down left right things
        up(event)
        down(event)
        left(event)
        right(event)

    screen.fill((100, 0, 140, 0))
    world.fill((0, 0, 0, 0))

    player.fill((0, 0, 0, 0))
    player.blit(playerAnim(), (0, 0))
    # world.blit(player, (0, 0))

    # Update the scrolling position based on the key flags
    scroll_x, scroll_y = playerWalk(up, down, left, right, scroll_x, scroll_y)

    if up or down or left or right:
        for thing in player_collide_group:
            thing_rect = thing[1]

            # check for collision with player
            player_rect = player.get_rect()
            player_rect.center = (sw / 2, sh / 2)
            if func.pixel_collision(player, player.get_rect(), thing[0], thing[1]):

                # Calculate the overlap size for each direction
                right_overlap = player.get_rect().right - thing_rect.left
                left_overlap = thing_rect.right - player.get_rect().left
                up_overlap = thing_rect.bottom - player.get_rect().top
                down_overlap = player.get_rect().bottom - thing_rect.top

                # Find the smallest overlap
                min_overlap = min(right_overlap, left_overlap, up_overlap, down_overlap)

                # detect right side collision
                if min_overlap == right_overlap:
                    print("hit right")

                # detect left side collision
                elif min_overlap == left_overlap:
                    print("hit left")

                # detect up collision
                elif min_overlap == up_overlap:
                    print("hit up")

                # detect down collision
                elif min_overlap == down_overlap:
                    print("hit down")



        # Draw red boxes around the objects that are collided with
        for thing_rect in player_collide_group:
            thing_screen_pos = ((thing[1].x + scroll_x), (thing[1].y + scroll_y))

            if func.pixel_collision(player, player.get_rect(), thing[0], thing[1]):
                red_box_surface = pygame.Surface((thing_rect.width, thing_rect.height), pygame.SRCALPHA)
                red_box_surface.fill((0, 0, 0, 0))
                pygame.draw.rect(red_box_surface, (255, 0, 0), red_box_surface.get_rect(), 1)
                screen.blit(red_box_surface, thing_screen_pos)
                player_hitbox = pygame.Surface((player_width, player_height), pygame.SRCALPHA)
                player_hitbox.fill((0, 0, 0, 0))
                pygame.draw.rect(player_hitbox, (170, 23, 255), player_hitbox.get_rect(), 2)
                screen.blit(player_hitbox, ((sw/2) - (player_width/2), (sh/2)- (player_height/2)))

    # Draw the level surface
    screen.blit(lvl_loader.surface, (0, 0), (-scroll_x, -scroll_y, sw, sh))

    screen.blit(player, ((sw/2)-(player_width/2), (sh/2)-(player_height/2)), (0, 0, sw, sh))
    try:
        if frames % (int(clock.get_fps()/2)) == 0:
            current_fps = int(clock.get_fps())
    except:
        current_fps = 2147483647

    fps_text = font.render("FPS: {}".format(current_fps), True, pygame.Color('white'))

    screen.blit(fps_text, (10, 10))

    pygame.display.update()
    pygame.display.flip()

    clock.tick(fps)

    frames += 1

pygame.quit()
