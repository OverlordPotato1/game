from . import functions
import pygame


class Movement:
    def __init__(self, animation_class, left_walk, right_walk, idle, move_speed):
        self.animation_class = animation_class
        self.leftWalk = left_walk
        self.rightWalk = right_walk
        self.idle = idle
        self.last_direction = 0
        self.move_speed = move_speed
        self.flippedIdle = functions.flip_spritesheet(idle)

    def __call__(self, up, down, left, right, scroll_x, scroll_y):
        succeed = 0
        ms = self.move_speed
        if up and not down:
            scroll_y += ms
            succeed += 1
            if self.last_direction == -2:
                self.animation_class.switch_sheet(self.leftWalk)
                self.last_direction = 1
            elif self.last_direction == -1:
                self.animation_class.switch_sheet(self.rightWalk)
                self.last_direction = 0
        if down and not up:
            scroll_y -= ms
            succeed += 1
            if self.last_direction == -2:
                self.animation_class.switch_sheet(self.leftWalk)
                self.last_direction = 1
            elif self.last_direction == -1:
                self.animation_class.switch_sheet(self.rightWalk)
                self.last_direction = 0
        if left and not right:
            scroll_x += ms
            if self.last_direction != 1:
                self.animation_class.switch_sheet(self.leftWalk)
                self.last_direction = 1
            succeed += 1
        if right and not left:
            scroll_x -= ms
            if self.last_direction != 0:
                self.animation_class.switch_sheet(self.rightWalk)
                self.last_direction = 0
            succeed += 1
        if succeed == 0:
            if self.last_direction == 1:
                self.animation_class.switch_sheet(self.idle)
                self.last_direction = -2
            elif self.last_direction == 0:
                self.animation_class.switch_sheet(self.flippedIdle)
                self.last_direction = -1

        return scroll_x, scroll_y

    def new_sprites(self, left_walk, right_walk, idle):
        self.leftWalk = left_walk
        self.rightWalk = right_walk
        self.idle = idle
        self.flippedIdle = functions.flip_spritesheet(idle)
        if self.last_direction == 1:
            self.animation_class.switch_sheet(self.idle)
            self.last_direction = -2
        elif self.last_direction == 0:
            self.animation_class.switch_sheet(self.flippedIdle)
            self.last_direction = -1
        elif self.last_direction == -1:
            self.animation_class.switch_sheet(self.flippedIdle)
        elif self.last_direction == -2:
            self.animation_class.switch_sheet(self.idle)
