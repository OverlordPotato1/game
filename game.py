import pygame
import os

import func
from classes.animator import Animator
from classes.movement import Movement
from this_is_kinda_stupid_now import *
from classes.json_handler import JsonFile
from level_loader import level_loader
from classes.sprite import Sprite

pygame.init()

screen = pygame.display.set_mode((definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT), pygame.RESIZABLE)
os.environ['SDL_VIDEO_CENTERED'] = '1'  # center the window

world_width = 1000
world_height = 800
world = pygame.Surface((world_width, world_height), pygame.SRCALPHA)  # pygame.SRCALPHA is required to have a transparent background on pngs

# player = pygame.Surface((512, 512), pygame.SRCALPHA)  # define the player surface, pygame.SRCALPHA is still required because the surface needs to be transparent
# playerSprite = Sprite("Images/Null.png", (player_width, player_height))

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

player_collide_group = pygame.sprite.Group()

# Create a level_loader instance
lvl_loader = level_loader(screen_view, "levels/", "textures.json", player_collide_group)

# Load a new level
lvl_loader.new_lvl("test.lvl")

frames = 0

playerGroupBecauseIHaveNoClueWhatImDoing = pygame.sprite.Group()

playerSprite = Sprite("Images/Null.png", (player_width, player_height))

playerSprite.rect.x = (definitions.SCREEN_WIDTH / 2) - (player_width / 2)
playerSprite.rect.y = (definitions.SCREEN_HEIGHT / 2) - (player_height / 2)

playerGroupBecauseIHaveNoClueWhatImDoing.add(playerSprite)

scroll_x = 300
scroll_y = 600

lastX = 0
lastY = 0

vel_y = 0
vel_x = 0

onGround = False


# playerSprite.rect.y 

doTheThing = True
while doTheThing:
    player_collide_group = lvl_loader.collide_group

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

    # player.fill((0, 0, 0, 0))
    # player.blit(playerAnim(), (0, 0))

    playerSprite.image = playerAnim()
    # world.blit(playerSprite.image, (playerSprite.rect.x - scroll_x, playerSprite.rect.y - scroll_y))
    # world.blit(player, (0, 0))

    # Update the scrolling position based on the key flags
    scroll_x, scroll_y = playerWalk(up, down, left, right, scroll_x, scroll_y)

    if up or down or left or right:
        pass

    for sprite in player_collide_group:
        sprite.rect.x += scroll_x - lastX
        sprite.rect.y += scroll_y - lastY

    lastX = scroll_x
    lastY = scroll_y

    

    # collision = pygame.sprite.spritecollide(playerSprite, player_collide_group, False)
    # if collision:
    #     print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")



    for sprite in player_collide_group:
        # if playerSprite.rect.colliderect(sprite.rect):
        player_bottom = playerSprite.rect.bottom
        player_top = playerSprite.rect.top
        sprite_bottom = sprite.rect.bottom
        sprite_top = sprite.rect.top
        vertical_overlap = sprite_top - player_bottom
        print(sprite_top, player_bottom, sprite_bottom, player_top)
        if sprite_top <= player_bottom + 20 and sprite_top >= player_bottom - 40:
            print("fall")
            vel_y = 1
            onGround = True
            throughGround = True

    if onGround == False:
        vel_y -= 1
    scroll_y += vel_y
    


    # Draw the level surface
    screen.blit(lvl_loader.surface, (0, 0), (-scroll_x, -scroll_y, sw, sh))

    for sprite in player_collide_group:
        pygame.draw.rect(screen, (255, 0, 0), sprite.rect, 2)

    pygame.draw.rect(screen, (0, 255, 0), playerSprite.rect, 2)

    # screen.blit(player, ((sw/2)-(player_width/2), (sh/2)-(player_height/2)), (0, 0, sw, sh))
    screen.blit(world, ((sw/2)-(player_width/2), (sh/2)-(player_height/2)), (0, 0, sw, sh))
    try:
        if frames % (int(clock.get_fps()/2)) == 0:
            current_fps = int(clock.get_fps())
    except:
        current_fps = 2147483647

    fps_text = font.render("FPS: {}".format(current_fps), True, pygame.Color('white'))

    screen.blit(fps_text, (10, 10))

    playerGroupBecauseIHaveNoClueWhatImDoing.draw(screen)

    # lvl_loader.all_sprites.draw(screen)

    pygame.display.update()
    pygame.display.flip()

    clock.tick(fps)

    frames += 1

pygame.quit()
