import pygame, sys, os, random, math
from time import sleep
from Camera import *
import Levels
from Tile import tile
import files
from player import player
tilesize = 50
camera = camera(200, 200, 800, 600, animationSpeed=5, tilesize=tilesize)


def blits():
    pass

# create the screen
screen = pygame.display.set_mode((800, 600))

# set to 60 fps
clock = pygame.time.Clock()

level, lines, texttiles = Levels.loadLevel("maps/1.lvl", tilesize)
tiles = level[0]
entities = level[1]
player = player(0, 0, camera)

lastClick = 0

camera.forceTilesUpdate(tiles)
player.updatePosition(200, 200)


while True:
    # close game when x is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            camera.scroll("down", tiles, entities)
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            camera.scroll("up", tiles, entities)
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            camera.scroll("left", tiles, entities)
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            camera.scroll("right", tiles, entities)
    
    # detect mouse clicks
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            # get the current game tick
            tick = pygame.time.get_ticks()
            if tick - lastClick < 300:
                pass
            else:
                lastClick = tick
                # get the mouse position
                mousePos = pygame.mouse.get_pos()
                try:
                    print("\n------------------")
                    print("Position : " + str(int(mousePos[0]/50)), str(int(mousePos[1]/50)))
                    tempTile, x, y = camera.getTile(mousePos, tiles)
                    print("Displayed : " + tempTile.whoAmI, tempTile.whatsMyRotation)
                    print("File: " + texttiles[y][x])
                    print("Proximity : " + str(Levels.scanNearbyTiles(texttiles, [int(mousePos[0]/50), int(mousePos[1]/50)], ["NULL:VOID"])).replace("[", "").replace("]", "").replace("'", ""))
                    print("------------------")
                except:
                    print("Not a tile")
                    print("------------------")
    
        offset = camera.getCoords()
    # clear the screen
    screen.fill((0, 0, 0))

    for y, line in enumerate(lines):
        for x, current in enumerate(line):
            screen.blit(current.image, current.rect)
    for entity in entities:
        screen.blit(entity.image, entity.rect)

    # blit the player
    screen.blit(player.image, player.rect)

    clock.tick(60)

    pygame.display.flip()
    

screen.close()