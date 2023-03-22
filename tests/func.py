import pygame


def resize_sprites(spritesheet, dimensions):
    width, height = dimensions
    for pos, image in enumerate(spritesheet):
        image = pygame.transform.scale(image, (width, height))
        spritesheet[pos] = image
    return spritesheet
