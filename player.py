import pygame, sys, os, random, math
# from Camera import camera

class player():
    def __init__(self, x, y, camera):

        
        
        # self.coords = [x, y]
        self.image = pygame.image.load("images/entity/player.png")

        
        self.coords = camera.coords
        self.rect = self.image.get_rect(center=self.coords)
        self.offset = [0,0]
        self.camera = camera

    def getPosition(self):
        return self.coords

    def updatePosition(self, x, y):
        self.coords = [self.coords[0]+x, self.coords[1]+y]

    # def offsetPosition(self, x, y):
        