import pygame
import definitions
from func import *

class touching:
    def __init__(self, entity):
        self.entity = entity

    def top(self, playerRect, spriteRect, vel_y):
        playerBottom = playerRect[0]
        playerTop = playerRect[1]
        playerLeft = playerRect[2]
        playerRight = playerRect[3]
        spriteBottom = spriteRect[0]
        spriteTop = spriteRect[1]
        spriteLeft = spriteRect[2]
        spriteRight = spriteRect[3]
        half = (spriteTop+spriteBottom)/2

        if horizontally_aligned(playerRect, spriteRect):
            if spriteBottom > playerTop and half < playerTop:
                return 3
            elif is_above(playerRect, spriteRect) and playerTop + -vel_y*2 < spriteBottom:
                return 2
            elif spriteBottom <= playerTop and playerTop <= spriteBottom+2:
                return 1
            else:
                return 0

    def bottom(self, playerRect, spriteRect, vel_y):
        playerBottom = playerRect[0]
        playerTop = playerRect[1]
        playerLeft = playerRect[2]
        playerRight = playerRect[3]
        spriteBottom = spriteRect[0]
        spriteTop = spriteRect[1]
        spriteLeft = spriteRect[2]
        spriteRight = spriteRect[3]
        fourth = (spriteTop+spriteBottom)/2
        
        if horizontally_aligned(playerRect, spriteRect):
            if spriteTop < playerBottom and fourth > playerBottom:
                return 3
            elif is_bellow(playerRect, spriteRect) and playerBottom + -vel_y*2 > spriteTop:
                return 2
            elif playerBottom <= spriteTop and spriteTop <= playerBottom+2:
                return 1
            else:
                return 0

    def left(self, playerRect, spriteRect, vel_x):
        playerRect[0] -= 10
        playerRect[1] += 10
        playerBottom = playerRect[0]
        playerTop = playerRect[1]
        playerLeft = playerRect[2]
        playerRight = playerRect[3]
        spriteBottom = spriteRect[0]
        spriteTop = spriteRect[1]
        spriteLeft = spriteRect[2]
        spriteRight = spriteRect[3]

        if vertically_alligned(playerRect, spriteRect):
            if spriteRight >= playerLeft and playerRight >= spriteRight:
                return 2
            elif spriteRight >= playerLeft - 5 and playerRight - 5 >= spriteRight:
                return 1
            else:
                return 0


    def right(self, playerRect, spriteRect, vel_x):
        playerRect[0] -= 10
        playerRect[1] += 10
        playerBottom = playerRect[0]
        playerTop = playerRect[1]
        playerLeft = playerRect[2]
        playerRight = playerRect[3]
        spriteBottom = spriteRect[0]
        spriteTop = spriteRect[1]
        spriteLeft = spriteRect[2]
        spriteRight = spriteRect[3]

        if vertically_alligned(playerRect, spriteRect):
            if spriteLeft <= playerRight and playerLeft <= spriteLeft:
                return 2
            elif spriteLeft <= playerRight + 5 and playerLeft - 5 <= spriteLeft:
                return 1
            else:
                return 0

