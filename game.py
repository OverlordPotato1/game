import pygame
import os

import func
from classes.animator import Animator
from classes.movement import Movement
from this_is_kinda_stupid_now import *
from classes.json_handler import JsonFile
from level_loader import level_loader
from classes.sprite import Sprite
from classes.touching import touching

pygame.init()

screen = pygame.display.set_mode((definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT))
os.environ['SDL_VIDEO_CENTERED'] = '1'  # center the window

world_width = 1000
world_height = 800
world = pygame.Surface((world_width, world_height), pygame.SRCALPHA)  # pygame.SRCALPHA is required to have a transparent background

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

v = Key(pygame.K_v)

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

scroll_x = 0
scroll_y = 580

lastX = 0
lastY = 0



startVelY = 10
startVelX = -7

vel_y = startVelY
vel_x = startVelX

onGround = False

playerTouching = touching(playerSprite)

lastJump = 0

returnFromVoid = True

noClip = False

prevV = False

prevHittingHead = False

headHitTime = 0

doTheThing = True
while doTheThing:
    player_collide_group = lvl_loader.collide_group

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doTheThing = False

        # Update the states of the up down left right things
        up(event)
        down(event)
        left(event)
        right(event)

        v(event)

    # Clear content from background
    screen.fill((100, 0, 140, 0))
    world.fill((0, 0, 0, 0))

    
    # Update the scrolling position based on the key flags
    noClip, prevV = func.handle_noClip(noClip, v, prevV, playerWalk)
    
    

    if not noClip:
        if not returnFromVoid:
            vel_x, garbage = playerWalk(up, down, left, right, 0, 0)
        onGround = False
    else:
        vel_x, vel_y = playerWalk(up, down, left, right, 0, 0)
        onGround = True

    for sprite in player_collide_group:
        sprite.rect.x += scroll_x - lastX
        sprite.rect.y += scroll_y - lastY

    lastX = scroll_x
    lastY = scroll_y
    
    hittingHead = False

    if not noClip:
        for sprite in player_collide_group:
            player_bottom = playerSprite.rect.bottom + 30
            player_top = playerSprite.rect.top
            sprite_bottom = sprite.rect.bottom
            sprite_top = sprite.rect.top
            
            if onGround == False:
                if playerTouching.bottom(sprite) == 2:
                    onGround = True
                    vertical_overlap = sprite_top - player_bottom
                    if abs(vertical_overlap) > 50:
                        # if something fucked up badly ignore it and let it fix itself
                        vertical_overlap = 0
                    scroll_y -= vertical_overlap + 8
                elif playerTouching.bottom(sprite) == 1:
                    onGround = True
                else:
                    onGround = False
                if playerTouching.top(sprite) == 2:
                    vel_y = 0
                    hittingHead = True
                    vertical_overlap = sprite_bottom - player_top
                    if abs(vertical_overlap) > 50:
                        # if something fucked up badly ignore it and let it fix itself
                        vertical_overlap = 0
                    scroll_y -= vertical_overlap - 32
                elif playerTouching.top(sprite) == 1 and vel_y > 0:
                    vel_y /= 1.5
                if playerTouching.right(sprite) == 2:
                    if vel_x < 0:
                        vel_x = 0
                if playerTouching.left(sprite) == 2:
                    if vel_x > 0:
                        vel_x = 0

        

    
    
    
                    

    playerSprite.image = playerAnim()

    
            
    
    if not noClip:
        if up and onGround and not (lastJump > 0):
            lastJump = 30
            vel_y = 18
            onGround = False
        
        lastJump -= 1

        if onGround == False:
            vel_y -= 1
            # passw
        else:
            if not vel_y > 0:
                vel_y = 0

        headHitTime -= 1

        if hittingHead and not prevHittingHead:
            headHitTime = 5

        prevHittingHead = hittingHead

        if headHitTime > 0:
            vel_y = 0

        scroll_y += vel_y

        if scroll_y < -10000:
            scroll_y = 600
            scroll_x = 0
            vel_y = startVelY
            vel_x = startVelX
            returnFromVoid = True

        if onGround and returnFromVoid:
            returnFromVoid = False

        scroll_x += vel_x
        if scroll_x > 0:
            scroll_x = 0
    else:
        scroll_x += vel_x
        scroll_y += vel_y

    # Draw the level surface
    screen.blit(lvl_loader.surface, (0, 0), (-scroll_x, -scroll_y, sw, sh))

    screen.blit(world, ((sw/2)-(player_width/2), (sh/2)-(player_height/2)), (0, 0, sw, sh))
    
    try:
        if frames % (int(clock.get_fps()/2)) == 0:
            current_fps = int(clock.get_fps())
    except:
        current_fps = 2147483647

    fps_text = font.render("FPS: {}".format(current_fps), True, pygame.Color('white'))

    screen.blit(fps_text, (10, 10))

    playerGroupBecauseIHaveNoClueWhatImDoing.draw(screen)

    pygame.display.update()
    pygame.display.flip()

    clock.tick(fps)

    frames += 1

pygame.quit()
