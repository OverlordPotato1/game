import pygame
import definitions

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, size):
        super().__init__()
        self.image = pygame.image.load(image)
        # self.rect = self.image.get_rect() im incompetentent 
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
    
    def changeImage(self, new_honda_accord):
        self.image = new_honda_accord
        self.rect = self.image.get_rect()
