import pygame


class Animator:
    def __init__(self, spritesheet, cycles_per_frame=20):
        self.pause = False
        if isinstance(spritesheet, str):
            raise TypeError
        self.sprites = spritesheet
        self.cpf = cycles_per_frame
        self.frame = 0
        self.ticks_since = 0

    def switch_sheet(self, new_sheet):
        del self.sprites
        self.sprites = new_sheet
        self.frame = 0
        self.ticks_since = 0

    def __progress(self):
        self.ticks_since += 1
        if self.ticks_since >= self.cpf:
            self.ticks_since = 0
            self.frame += 1
            if self.frame > len(self.sprites) - 1:
                self.frame = 0

    def __call__(self):
        self.__progress()
        return self.sprites[self.frame]
