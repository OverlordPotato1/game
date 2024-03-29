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
from classes.switch import switch
import matplotlib.pyplot as plt
import math


import badIdeas
import asyncio

pygame.init()

screen = pygame.display.set_mode((definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT), pygame.SRCALPHA)
os.environ['SDL_VIDEO_CENTERED'] = '1'  # center the window

world = pygame.Surface((1000, 800), pygame.SRCALPHA)  # pygame.SRCALPHA is required to have a transparent background

player_height = player_width = 128

rightSwordWalk = func.easy_spritesheet("Images/knight walks/Knight-Walk-Sheet-sword-right.png", (64, 64), (player_width, player_height))
leftSwordWalk = func.easy_spritesheet("Images/knight walks/Knight-Walk-Sheet-sword-left.png", (64, 64), (player_width, player_height))
attack = func.easy_spritesheet("Images\knight walks\Knight-CLEARED-Attack-Sheet.png", (74,74), (player_width, player_height))

rightSwordWalk = []
for x, img in enumerate(leftSwordWalk):
    rightSwordWalk.append(pygame.transform.flip(img, True, False))

idle = func.easy_spritesheet("Images/Downloaded/Fantasy Pixel Art Asset Pack/Knight-Idle-Sheet.png", (64, 64), (player_width*0.9, player_height*0.9))

playerAnim = Animator(rightSwordWalk, 9)  # resize the sprites and pass them to the Animator constructor as a spritesheet
playerWalk = Movement(playerAnim, leftSwordWalk, rightSwordWalk, idle, 3.6)

screen_view = pygame.Surface((definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT), pygame.SRCALPHA)

clock = pygame.time.Clock()
fps = 60

sw, sh = create_base_window_size()

percentOfScreen = 0.15
playerWalk.new_sprites(func.resize_sprites(leftSwordWalk, (sw*percentOfScreen, sw*percentOfScreen)), func.resize_sprites(rightSwordWalk, (sw*percentOfScreen, sw*percentOfScreen)), func.resize_sprites(idle, (sw*percentOfScreen, sw*percentOfScreen)))
playerWalk.move_speed = sh/200
del percentOfScreen

up, down, left, right = create_movement_objects()
v = Key(pygame.K_v)
k = Key(pygame.K_k)

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
returnFromVoid = True
noClip = False
prevV = False
prevOnGround = False

playerTouching = touching(playerSprite)

lastJump = 0

headHitTime = 0

yHist = []
velyHist = []

bottomFlicker = 0
topFlicker = 0
leftFlicker = 0
rightFlicker = 0

keyL = [up, down, left, right, v, k]

doTheThing = True
while doTheThing:
    
    player_collide_group = lvl_loader.collide_group

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doTheThing = False
        for key in keyL:
            key(event)

    screen.fill((100, 0, 140, 0))
    world.fill((0, 0, 0, 0))
    noClip, prevV = func.handle_noClip(noClip, v, prevV, playerWalk) # comment this out to prevent noclip
    # noClip = False # uncomment this to prevent noclip

    if k.single(): # big boy jump
        vel_y = 50
    prevK = bool(k)

    if not noClip:
        if not returnFromVoid:
            vel_x, garbage = playerWalk(up, down, left, right, 0, 0)
            del garbage # i just dont want to screw with the movement class
        onGround = False
    else:
        vel_x, vel_y = playerWalk(up, down, left, right, 0, 0)
        onGround = True

    # move the sprites to the scrolls
    for sprite in player_collide_group:
        sprite.rect.x += -scroll_x - lastX
        sprite.rect.y += scroll_y - lastY
    """
    for entity in sprite_group:
        entity.rect.x += -scroll_x - lastX
        entity.rect.y += scroll_y - lastY
    """

    lastX = -scroll_x
    lastY = scroll_y

    debug_surface = pygame.Surface((definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT), pygame.SRCALPHA)

    thisIsStupid = []
    for sprite in player_collide_group:
        thisIsStupid.append(sprite)
        func.draw_line_with_collision(debug_surface, playerSprite.rect.center, sprite.rect.center, player_collide_group)
    # print(thisIsStupid[0].rect.center)
    
    screen.blit(lvl_loader.surface, (0, 0), (scroll_x, -scroll_y, sw, sh))
    surfaceThatIsCurrentlyBeingSmashedInto = []

    player_bottom = playerSprite.rect.bottom + 20
    player_top = playerSprite.rect.top + 25
    player_left = playerSprite.rect.left + 45
    player_right = playerSprite.rect.right - 25

    player_height = player_bottom - player_top
    player_width = player_right - player_left

    func.drawCollisionLines(debug_surface, [player_bottom, player_top, player_left, player_right])

    alreadyHit = False   
    alreadyHitX = []

    # Do not touch any of this shit because i have no idea how it works but it is the best collision system i have managed to do
    for sprite in player_collide_group:
        
        sprite_bottom = sprite.rect.bottom
        sprite_top = sprite.rect.top
        sprite_left = sprite.rect.left
        sprite_right = sprite.rect.right
        sprite_width = sprite_right - sprite_left
        sprite_height = sprite_bottom - sprite_top
        playerRect = [player_bottom, player_top, player_left, player_right]
        spriteRect = [sprite_bottom, sprite_top, sprite_left, sprite_right]
        
        if bottomFlicker > 0:
            pygame.draw.rect(debug_surface, (255, 255, 255, 200), (player_left, player_bottom, player_width, 15)) # draw the bottom box
            if vel_y < 0:
                vel_y = 0
            bottomFlicker -= 1
        else:
            pygame.draw.rect(debug_surface, (255, 255, 255, 64), (player_left, player_bottom, player_width, 15)) # draw the bottom box

        if leftFlicker > 0:
            pygame.draw.rect(debug_surface, (255, 0, 0, 200), (player_left-15, player_top, 15, player_height)) # draw the left box
            leftFlicker -= 1
        else:
            pygame.draw.rect(debug_surface, (255, 0, 0, 64), (player_left-15, player_top, 15, player_height)) # draw the left box

        if rightFlicker > 0:
            pygame.draw.rect(debug_surface, (0, 255, 0, 200), (player_right, player_top, 15, player_height)) # draw the left box
            rightFlicker -= 1
        else:
            pygame.draw.rect(debug_surface, (0, 255, 0, 64), (player_right, player_top, 15, player_height)) # draw the left box

        if topFlicker > 0:
            pygame.draw.rect(debug_surface, (0, 0, 0, 200), (player_left, player_top-15, player_width, 15)) # draw the bottom box
            topFlicker -= 1
        else:
            pygame.draw.rect(debug_surface, (0, 0, 0, 64), (player_left, player_top-15, player_width, 15)) # draw the bottom box

        if func.is_bellow([player_bottom - 1, player_top, player_left, player_right], spriteRect) and not ((sprite_left + scroll_x) in alreadyHitX):
            distanceOffScreen = (player_bottom+sprite_top)/2 - definitions.SCREEN_HEIGHT
            x = ((player_left + player_right)/2 + (sprite_left + sprite_right)/2)/2
            pygame.draw.rect(debug_surface, (255,255,255), (x, player_bottom, 1, sprite_top-player_bottom))
            distance = sprite_top-player_bottom
            dist = font.render("{} px".format(distance), True, pygame.Color('white'))
            if distanceOffScreen > 0:
                debug_surface.blit(dist, (x + 5, definitions.SCREEN_HEIGHT - 15))
            else:
                debug_surface.blit(dist, (x + 5, (player_bottom+sprite_top)/2))

            alreadyHit = True
            alreadyHitX.append(sprite_left + scroll_x)
            func.debugBox(debug_surface, spriteRect, (255, 0, 0), 5)
            
        if not onGround and not noClip:
            c = switch(playerTouching.bottom(playerRect, spriteRect, vel_y-1))
            if c(3):
                if not noClip:
                    if vel_y < 0:
                        vel_y = 0
                    onGround = True
                    vertical_overlap = sprite_top - player_bottom
                    scroll_y -= vertical_overlap
                bottomFlicker = 100
            elif c(2):
                if not noClip:
                    if vel_y < 0:
                        vel_y = 0
                    vertical_overlap = sprite_top - player_bottom
                    scroll_y -= vertical_overlap
                    onGround = True
                bottomFlicker = 100
            elif c(1):
                if not noClip:
                    if vel_y < 0:
                        vel_y = 0
                    onGround = True
                bottomFlicker = 100
            elif c(0):
                if not noClip:
                    onGround = False
            c = switch(playerTouching.top(playerRect, spriteRect, vel_y))
            if c(3):
                surfaceThatIsCurrentlyBeingSmashedInto.append(spriteRect)
                if vel_y > 0:
                    vel_y = 0
                vertical_overlap = sprite_bottom - player_top
                scroll_y -= vertical_overlap
                topFlicker = 100
            elif c(2):
                surfaceThatIsCurrentlyBeingSmashedInto.append(spriteRect)
                if vel_y > 0:
                    vel_y = 0

                topFlicker = 100
        if surfaceThatIsCurrentlyBeingSmashedInto:
            for tile in surfaceThatIsCurrentlyBeingSmashedInto:
                func.debugBox(debug_surface, tile, (255,255,255))

        if not (surfaceThatIsCurrentlyBeingSmashedInto in spriteRect) and not noClip:
            c = switch(playerTouching.left(playerRect, spriteRect, vel_x))
            if c(2):
                scroll_x += 5
                if vel_x > 0:
                    vel_x = 0
                leftFlicker = 100
            if c(1):
                if vel_x > 0:
                    vel_x = 0
                # overlap = player_left - sprite_right
                # vel_x= overlap
                leftFlicker = 100
            c = switch(playerTouching.right(playerRect, spriteRect, vel_x))
            if c(2):
                scroll_x -= 5
                # if vel_x < 0:
                #     vel_x = 0
                rightFlicker = 100
            elif c(1):
                if vel_x < 0:
                    vel_x = 0
                rightFlicker = 100

    # for angle in range(-90+(playerWalk.facing*180), 90+(playerWalk.facing*180), 10):
    #     dx = math.cos(math.radians(angle))
    #     dy = math.sin(math.radians(angle))

    #     hit = False

    #     c = 0
    #     for i in range(50, 500, 50):
    #         c += 1
    #         x = playerSprite.rect.centerx + dx * i
    #         y = playerSprite.rect.centery + dy * i

    #         for sprite in player_collide_group:
    #             if sprite.rect.collidepoint(x, y):
    #                 hit = True
    #                 break
    #         if hit:
    #             break
            
    #         pygame.draw.rect(debug_surface, (255, 0, 0, 255), (x, y, 2, 2))       

    if not noClip:
        idk = 0
        if vel_y > 0:
            idk = vel_y**1.3
        else:
            idk = -(player_bottom - player_top)
        pygame.draw.rect(debug_surface, (221, 224, 16), ((player_left+player_right)/2, player_top-idk, 3, abs(vel_y)**1.3))
    
    justLanded = False
    if onGround and not prevOnGround:
        justLanded = True
    prevOnGround = onGround
    playerSprite.image = playerAnim()    
    
    # touch this if statement and you die ↓
    if not noClip:
        if up and onGround and not lastJump > 0:
            lastJump = 30
            vel_y = 23
            onGround = False
        
        lastJump -= 1

        if not onGround:
            vel_y -= 1
        else:
            if not vel_y > 0:
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

        scroll_x -= vel_x
        if scroll_x < 0:
            scroll_x = 0
    else:
        scroll_x -= vel_x
        scroll_y += vel_y

    # pygame.draw.rect(debug_surface, (40, 0, 0, 80), (0, 0, (-scroll_x + definitions.SCREEN_WIDTH/2) - 19, sh)) # the box that shows where you cant walk

    try:
        if frames % (int(clock.get_fps()/2)) == 0:
            current_fps = int(clock.get_fps())
    except:
        current_fps = -1
    fps_text = font.render(f"FPS: {current_fps}     Scroll_x {scroll_x}     Scroll_y {scroll_y}     Vel_x {vel_x}     Vel_y {vel_y}", True, pygame.Color('white'))
    debug_surface.blit(fps_text, (10, 10))

    screen.blit(debug_surface, (0, 0), (0, 0, definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT))
    screen.blit(world, ((sw/2)-(player_width/2), (sh/2)-(player_height/2)), (0, 0, sw, sh))
    playerGroupBecauseIHaveNoClueWhatImDoing.draw(screen)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(fps)
    k.x()
    frames += 1

pygame.quit()
