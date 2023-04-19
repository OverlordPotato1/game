import pygame
import definitions

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, size):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, size)
