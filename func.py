import pygame
from classes.spritesheet import Spritesheet as spsh
import hashlib
from math import *


def resize_sprites(spritesheet, dimensions):
    width, height = dimensions
    ss = []
    for pos, image in enumerate(spritesheet):
        image = pygame.transform.scale(image, (width, height))
        ss.append(image)
    return ss


def handle_resize(event, sw, sh):
    if event.type == pygame.VIDEORESIZE:
        sw = event.w
        sh = event.h
        return sw, sh
    else:
        return sw, sh


def easy_spritesheet(file, sprite_dimensions, resize_dimensions):
    sprites = spsh(file, sprite_dimensions)
    sprites.separate_spritesheet()
    sprites.resize_sprites(resize_dimensions)
    return sprites.return_sprites()


def flip_spritesheet(spritesheet):
    sprites = []
    for pos, image in enumerate(spritesheet):
        image = pygame.transform.flip(image, True, False)
        sprites.append(image)
    return sprites


def pixel_collision(surface1, rect1, surface2, rect2):
    # Calculate the overlapping area between the two rects
    overlap_rect = rect1.clip(rect2)

    if overlap_rect.width == 0 or overlap_rect.height == 0:
        return False

    # Calculate the local coordinates of the overlap_rect in both surfaces
    local_overlap_rect1 = pygame.Rect(overlap_rect.x - rect1.x, overlap_rect.y - rect1.y, overlap_rect.width, overlap_rect.height)
    local_overlap_rect2 = pygame.Rect(overlap_rect.x - rect2.x, overlap_rect.y - rect2.y, overlap_rect.width, overlap_rect.height)

    for y in range(local_overlap_rect1.height):
        for x in range(local_overlap_rect1.width):
            # Get the color at the current pixel in both surfaces
            color1 = surface1.get_at((local_overlap_rect1.x + x, local_overlap_rect1.y + y))
            color2 = surface2.get_at((local_overlap_rect2.x + x, local_overlap_rect2.y + y))

            # Check if both pixels have non-transparent colors (alpha > 0)
            if color1[3] > 0 and color2[3] > 0:
                return True

    return False

def handle_noClip(noClip, v, prevV, playerWalk):
    if bool(v) == True and prevV == False:
        noClip = not noClip
        if noClip:
            playerWalk.move_speed = 8
        else:
            playerWalk.move_speed = 4
        
    prevV = bool(v)
    return noClip, prevV

def get_file_sha256(file_path):
    sha256_hash = hashlib.sha256()
    
    with open(file_path, "rb") as file:
        # Read and update hash in chunks to save memory
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)
    
    return sha256_hash.hexdigest()

def horizontally_aligned(playerRect, spriteRect):
    playerBottom = playerRect[0]
    playerTop = playerRect[1]
    playerLeft = playerRect[2]
    playerRight = playerRect[3]
    spriteBottom = spriteRect[0]
    spriteTop = spriteRect[1]
    spriteLeft = spriteRect[2]
    spriteRight = spriteRect[3]

    return spriteLeft <= playerLeft <= spriteRight or spriteLeft <= playerRight <= spriteRight

def vertically_alligned(playerRect, spriteRect):
    playerBottom = playerRect[0]
    playerTop = playerRect[1]
    playerLeft = playerRect[2]
    playerRight = playerRect[3]
    spriteBottom = spriteRect[0]
    spriteTop = spriteRect[1]
    spriteLeft = spriteRect[2]
    spriteRight = spriteRect[3]

    return spriteTop >= playerTop and playerBottom >= spriteTop or spriteBottom >= playerTop and playerBottom >= spriteBottom

def is_bellow(playerRect, spriteRect):
    playerBottom = playerRect[0]
    playerTop = playerRect[1]
    playerLeft = playerRect[2]
    playerRight = playerRect[3]
    spriteBottom = spriteRect[0]
    spriteTop = spriteRect[1]
    spriteLeft = spriteRect[2]
    spriteRight = spriteRect[3]

    return playerBottom < spriteTop and horizontally_aligned(playerRect, spriteRect)

def is_above(playerRect, spriteRect):
    playerBottom = playerRect[0]
    playerTop = playerRect[1]
    playerLeft = playerRect[2]
    playerRight = playerRect[3]
    spriteBottom = spriteRect[0]
    spriteTop = spriteRect[1]
    spriteLeft = spriteRect[2]
    spriteRight = spriteRect[3]

    return playerTop > spriteBottom and horizontally_aligned(playerRect, spriteRect)

def is_left(playerRect, spriteRect):
    playerBottom = playerRect[0]
    playerTop = playerRect[1]
    playerLeft = playerRect[2]
    playerRight = playerRect[3]
    spriteBottom = spriteRect[0]
    spriteTop = spriteRect[1]
    spriteLeft = spriteRect[2]
    spriteRight = spriteRect[3]

    return playerLeft > spriteRight and vertically_alligned(playerRect, spriteRect)
    
def drawCollisionLines(debug_surface, playerRect):
    player_bottom = playerRect[0]
    player_top = playerRect[1]
    player_left = playerRect[2]
    player_right = playerRect[3]
    player_height = player_bottom - player_top
    player_width = player_right - player_left

    pygame.draw.rect(debug_surface, (255, 0, 0), (player_left, player_top-15, 1, player_height+30)) # draw the left collision line
    pygame.draw.rect(debug_surface, (0, 255, 0), (player_right, player_top-15, 1, player_height+30)) # draw the right collision line
    pygame.draw.rect(debug_surface, (0, 0, 0), (player_left-15, player_top, player_width+30, 1)) # draw the top collision line
    pygame.draw.rect(debug_surface, (255, 255, 255), (player_left-15, player_bottom, player_width+30, 1)) # draw the bottom collision line

def debugBox(debug_surface, spriteRect, color, thickness = 2):
    spriteBottom = spriteRect[0]
    spriteTop = spriteRect[1]
    spriteLeft = spriteRect[2]
    spriteRight = spriteRect[3]
    offset = thickness - 1

    pygame.draw.rect(debug_surface, color, (spriteLeft, spriteTop, spriteRight-spriteLeft, thickness))
    pygame.draw.rect(debug_surface, color, (spriteLeft, spriteTop, thickness, spriteBottom-spriteTop))
    pygame.draw.rect(debug_surface, color, (spriteLeft, spriteBottom-offset, spriteRight-spriteLeft, thickness))
    pygame.draw.rect(debug_surface, color, (spriteRight-offset, spriteTop, thickness, spriteBottom-spriteTop))

import pygame

def draw_line_with_collision(screen, start_pos, end_pos, player_collide_group):
    x1 = start_pos[0]
    x2 = end_pos[0]
    y1 = start_pos[1]
    y2 = end_pos[1]
    delta_x = x2 - x1
    delta_y = y2 - y1
    angle_rad = atan2(delta_y, delta_x)
    angle = degrees(angle_rad)
    if angle < 0:
        angle += 360

    dist = sqrt(delta_x**2 + delta_y**2)
    
    dx = cos(radians(angle))
    dy = sin(radians(angle))

    hit = False

    c = 0
    for i in range(0, int(dist), int(dist/35)+1):
        c += 1
        x = start_pos[0] + dx * i
        y = start_pos[1] + dy * i

        for sprite in player_collide_group:
            if sprite.rect.collidepoint(x, y):
                hit = True
                break
        if hit:
            break
        
        if c == 7:
            pygame.draw.rect(screen, (255, 0, 0, 255), (x, y, 7, 7))  
        c += 1
