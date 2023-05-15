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
import random

pygame.init()

screen = pygame.display.set_mode((definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT), pygame.SRCALPHA)
os.environ['SDL_VIDEO_CENTERED'] = '1'  # center the window

world_width = 1000
world_height = 800
world = pygame.Surface((world_width, world_height), pygame.SRCALPHA)  # pygame.SRCALPHA is required to have a transparent background

player_height = player_width = 128

rightSwordWalk = func.easy_spritesheet("Images/knight walks/Knight-Walk-Sheet-sword-right.png", (64, 64), (player_width, player_height))

leftSwordWalk = func.easy_spritesheet("Images/knight walks/Knight-Walk-Sheet-sword-left.png", (64, 64), (player_width, player_height))

rightSwordWalk = []
for x, img in enumerate(leftSwordWalk):
    rightSwordWalk.append(pygame.transform.flip(img, True, False))

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

k = Key(pygame.K_k)

playerScreenCoverage = player_width / sw

screenSizeRatio = definitions.SCREEN_WIDTH / definitions.SCREEN_HEIGHT

font = pygame.font.SysFont(None, 25)

player_collide_group = pygame.sprite.Group()

# Create a level_loader instance
lvl_loader = level_loader(screen_view, "levels/", "textures.json", player_collide_group)

# Load a new level
lvl_loader.new_lvl("test.lvl")
prevHash = func.get_file_sha256("levels/test.lvl")

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

yHist = []

prevOnGround = False

start = 0

playerInSprite = False

x_change = 0
y_change = 0

doTheThing = True
while doTheThing:
    player_collide_group = lvl_loader.collide_group

    if prevHash != func.get_file_sha256("levels/test.lvl"):
        lvl_loader.new_lvl("test.lvl")
        prevHash = func.get_file_sha256("levels/test.lvl")
        # scroll_x = 0
        # scroll_y = 580
        # sprite.rect.x += scroll_x
        # sprite.rect.y += scroll_y
        for sprite in player_collide_group:
            sprite.rect.x += scroll_x
            sprite.rect.y += scroll_y

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doTheThing = False

        # Update the states of the up down left right things
        up(event)
        down(event)
        left(event)
        right(event)

        v(event)
        k(event)

    # Clear content from background
    screen.fill((100, 0, 140, 0))
    world.fill((0, 0, 0, 0))

    
    # Update the scrolling position based on the key flags
    noClip, prevV = func.handle_noClip(noClip, v, prevV, playerWalk)

    if k.single():
        vel_y = 50
    
    prevK = bool(k)

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
        x_change += scroll_x - lastX
        y_change += scroll_y - lastY

    lastX = scroll_x
    lastY = scroll_y
    
    hittingHead = False

    debug_surface = pygame.Surface((definitions.SCREEN_HEIGHT, definitions.SCREEN_WIDTH), pygame.SRCALPHA)

    pygame.draw.rect(screen, (40, 0, 0, 20), (0, 0, (scroll_x + definitions.SCREEN_WIDTH/2) - 19, sh))

    screen.blit(lvl_loader.surface, (0, 0), (-scroll_x, -scroll_y, sw, sh))

    if not noClip:
        player_bottom = playerSprite.rect.bottom + 20
        player_top = playerSprite.rect.top + 25
        player_left = playerSprite.rect.left + 45
        player_right = playerSprite.rect.right - 25

        player_height = player_bottom - player_top
        player_width = player_right - player_left

        pygame.draw.rect(debug_surface, (255, 0, 0), (player_left, player_top-15, 1, player_height+30)) # draw the left collision line
        pygame.draw.rect(debug_surface, (0, 255, 0), (player_right, player_top-15, 1, player_height+30)) # draw the right collision line
        pygame.draw.rect(debug_surface, (0, 0, 0), (player_left-15, player_top, player_width+30, 1)) # draw the top collision line
        pygame.draw.rect(debug_surface, (255, 255, 255), (player_left-15, player_bottom, player_width+30, 1)) # draw the bottom collision line
        pygame.draw.rect(debug_surface, (255, 255, 255, 64), (player_left, player_bottom, player_width, 15)) # draw the bottom box
        pygame.draw.rect(debug_surface, (0, 0, 0, 64), (player_left, player_top-15, player_width, 15)) # draw the top box
        pygame.draw.rect(debug_surface, (0, 255, 0, 64), (player_right, player_top, 15, player_height)) # draw the right box
        pygame.draw.rect(debug_surface, (255, 0, 0, 64), (player_left-15, player_top, 15, player_height)) # draw the left box

        for sprite in player_collide_group:
            sprite_bottom = sprite.rect.bottom
            sprite_top = sprite.rect.top
            sprite_left = sprite.rect.left
            sprite_right = sprite.rect.right

            playerRect = [player_bottom, player_top, player_left, player_right]
            spriteRect = [sprite_bottom, sprite_top, sprite_left, sprite_right]

            sprite_width = sprite_right - sprite_left
            sprite_height = sprite_bottom - sprite_top

            pygame.draw.rect(screen, (random.randint(0, 255), 0, 0), (sprite_left, sprite_top, sprite_width, sprite_height))

            if onGround == False:
                if playerTouching.bottom(playerRect, spriteRect) == 2:
                    if vel_y < 0:
                        onGround = True
                        vertical_overlap = sprite_top - player_bottom
                        if abs(vertical_overlap) > 50:
                            # if something fucked up badly ignore it and let it fix itself
                            vertical_overlap = 0
                        if not down and vel_y != 0:
                            scroll_y -= vertical_overlap
                elif playerTouching.bottom(playerRect, spriteRect) == 1:
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
                    # pass
                elif playerTouching.top(sprite) == 1 and vel_y > 0:
                    vel_y *= 2
                    # pass
                # if not playerInSprite:
                #     if playerTouching.right(sprite) == 2:
                #         if vel_x < 0:
                #             vel_x = 0
                #     if playerTouching.left(sprite) == 2:
                #         if vel_x > 0:
                #             vel_x = 0

    justLanded = False

    if onGround and not prevOnGround:
        justLanded = True

    prevOnGround = onGround
    
    playerSprite.image = playerAnim()    
    
    if not noClip:
        if up and onGround and not lastJump > 0:
            # if not nextJumpUpLevel:
            #     lastJump = 30
            #     vel_y = 18
            # else:
            lastJump = 30
            vel_y = 23

            onGround = False

        # if not onGround:
            # print(scroll_y)

        # if down and not cantPhaseThrough:
        #     vel_y = -20
            

        
        lastJump -= 1

        if onGround == False:
            vel_y -= 1
        else:
            if not vel_y > 0:
                vel_y = 0

        headHitTime -= 1

        # if hittingHead and not prevHittingHead:
        #     headHitTime = 5

        # prevHittingHead = hittingHead

        # if headHitTime > 0:
        #     vel_y = 0

        # if hittingHead:
        #     vel_y = 10

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
    

    screen.blit(debug_surface, (0, 0), (0, 0, definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT))

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

    k.x()

pygame.quit()
