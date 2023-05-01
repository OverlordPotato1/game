import pygame


class Animator:
    def __init__(self, spritesheet, cycles_per_frame = 20):
        if isinstance(spritesheet, str):
            raise TypeError
        self.sprites = spritesheet
        self.cpf = cycles_per_frame
        self.frame = 0
        self.ticks_since = 0
        self.last_sheet = spritesheet
        self.last_frame = 0

    def switch_sheet(self, new_sheet):
        if isinstance(new_sheet, str):
            raise TypeError
        self.last_sheet = self.sprites
        self.last_frame = self.frame
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
        try:
            return self.sprites[self.frame]
        except:
            self.frame -= 1
            return self.sprites[self.frame]

    def undoChange(self):
        # self.frame = self.last_frame
        self.sprites = self.last_sheet
