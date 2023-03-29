import pygame


def flip_spritesheet(sheet):
    new_sheet = []
    for pos, image in enumerate(sheet):
        image = pygame.transform.flip(image, True, False)
        new_sheet.append(image)
    return new_sheet
