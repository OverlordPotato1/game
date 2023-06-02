import pygame
import definitions

class Entity:
    def __init__(self, agroDistance, canPenetrate=False):
        self.ad = agroDistance
        self.penetrate = canPenetrate

    def __call__(self, player, debug_surface):
        #i dont know what to do
        pass