import pygame


class touching:
    def __init__(self, entity):
        self.entity = entity

    def top(self, sprite):
        entity_bottom = self.entity.rect.bottom - 30
        entity_top = self.entity.rect.top - 30
        entity_left = self.entity.rect.left
        entity_right = self.entity.rect.right
        sprite_bottom = sprite.rect.bottom
        sprite_top = sprite.rect.top
        sprite_left = sprite.rect.left
        sprite_right = sprite.rect.right

        # check if lined up vertically
        if entity_top < sprite_bottom and entity_bottom > sprite_bottom or entity_top < sprite_top and entity_bottom > sprite_top:
            if sprite_right >= entity_left and sprite_left <= entity_right:
                return 2
            elif sprite_right >= entity_left + 15 and sprite_left <= entity_right - 15:
                return 1
            else:
                return 0
        else:
            return 0



    def bottom(self, sprite):
        entity_bottom = self.entity.rect.bottom
        entity_top = self.entity.rect.top
        entity_left = self.entity.rect.left + 30
        entity_right = self.entity.rect.right - 30
        sprite_bottom = sprite.rect.bottom
        sprite_top = sprite.rect.top
        sprite_left = sprite.rect.left
        sprite_right = sprite.rect.right

        # +x ------>
        # -y \/

        # check if lined up horizontally
        if entity_left < sprite_left and entity_right > sprite_left or entity_left < sprite_right and entity_right > sprite_right: # it works idk how but it works so dont touch it
            if sprite_top <= entity_bottom + 30 and sprite_top >= entity_bottom - 15:
                return 2
            elif sprite_top <= entity_bottom + 30 and sprite_top >= entity_bottom - 20:
                return 1
            else:
                return 0
        else:
            return 0

    def left(self, sprite):
        entity_bottom = self.entity.rect.bottom
        entity_top = self.entity.rect.top
        entity_left = self.entity.rect.left - 30
        entity_right = self.entity.rect.right - 30
        sprite_bottom = sprite.rect.bottom
        sprite_top = sprite.rect.top
        sprite_left = sprite.rect.left
        sprite_right = sprite.rect.right

        # check if lined up horizontally
        if entity_left < sprite_right and entity_right > sprite_right or entity_left < sprite_left and entity_right > sprite_left:
            if sprite_bottom <= entity_top + 30 and sprite_bottom >= entity_top:
                return 2
            elif sprite_bottom <= entity_top + 30 and sprite_bottom >= entity_top + 15:
                return 1
            else:
                return 0
        else:
            return 0


    def right(self, sprite):
        entity_bottom = self.entity.rect.bottom
        entity_top = self.entity.rect.top
        entity_left = self.entity.rect.left + 30
        entity_right = self.entity.rect.right + 30
        sprite_bottom = sprite.rect.bottom
        sprite_top = sprite.rect.top
        sprite_left = sprite.rect.left
        sprite_right = sprite.rect.right

        # check if lined up horizontally
        if entity_left < sprite_right and entity_right > sprite_right or entity_left < sprite_left and entity_right > sprite_left:
            if sprite_bottom <= entity_top + 30 and sprite_bottom >= entity_top:
                return 2
            elif sprite_bottom <= entity_top + 30 and sprite_bottom >= entity_top + 15:
                return 1
            else:
                return 0
        else:
            return 0
