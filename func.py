import pygame
from classes.spritesheet import Spritesheet as spsh


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
