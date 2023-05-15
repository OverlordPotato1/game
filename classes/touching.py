import pygame
import definitions

class touching:
    def __init__(self, entity):
        self.entity = entity

    def top(self, sprite):
        entity_bottom = self.entity.rect.bottom - 30
        entity_top = self.entity.rect.top
        entity_left = self.entity.rect.left + 20
        entity_right = self.entity.rect.right - 20
        sprite_bottom = sprite.rect.bottom - definitions.tile_size
        sprite_top = sprite.rect.top
        sprite_left = sprite.rect.left + 20
        sprite_right = sprite.rect.right - 32

        # check if lined up vertically
        if entity_left < sprite_left and entity_right > sprite_left or entity_left < sprite_right and entity_right > sprite_right:
            if sprite_bottom >= entity_top - 30 and sprite_top <= entity_bottom:
                return 2
            elif sprite_bottom >= entity_top - 35 and sprite_top <= entity_bottom:
                return 1
            else:
                return 0
                
        else:
            return 0

    def bottom(self, playerRect, spriteRect):
        playerBottom = playerRect[0]
        playerTop = playerRect[1]
        playerLeft = playerRect[2]
        playerRight = playerRect[3]
        spriteBottom = spriteRect[0]
        spriteTop = spriteRect[1]
        spriteLeft = spriteRect[2]
        spriteRight = spriteRect[3]
        
        if spriteLeft >= playerLeft and spriteLeft <= playerRight or spriteRight >= playerLeft and spriteRight <= playerRight:
            if spriteTop < playerBottom and spriteBottom > playerBottom:
                return 2
            else:
                return 0

    def left(self, sprite):
        entity_bottom = self.entity.rect.bottom
        entity_top = self.entity.rect.top
        entity_left = self.entity.rect.left - 12
        entity_right = self.entity.rect.right
        sprite_bottom = sprite.rect.bottom - 38
        sprite_top = sprite.rect.top
        sprite_left = sprite.rect.left - definitions.tile_size
        sprite_right = sprite.rect.right - definitions.tile_size

        # check if lined up horizontally
        if entity_top <= sprite_top and entity_bottom >= sprite_top or entity_top <= sprite_bottom and entity_bottom >= sprite_bottom:
            if entity_left <= sprite_right and entity_left >= sprite_left:
                return 2
            # elif sprite_bottom <= entity_top + 30 and sprite_bottom >= entity_top + 15:
            #     return 1
            else:
                return 0
        else:
            return 0


    def right(self, sprite):
        entity_bottom = self.entity.rect.bottom
        entity_top = self.entity.rect.top
        entity_left = self.entity.rect.left
        entity_right = self.entity.rect.right - 26
        sprite_bottom = sprite.rect.bottom - 38
        sprite_top = sprite.rect.top
        sprite_left = sprite.rect.left
        sprite_right = sprite.rect.right

        # check if lined up vertically
        if entity_top <= sprite_top and entity_bottom >= sprite_top or entity_top <= sprite_bottom and entity_bottom >= sprite_bottom:
            if entity_right >= sprite_left and entity_right <= sprite_right:
                return 2
            # elif sprite_bottom <= entity_top + 30 and sprite_bottom >= entity_top + 15:
            #     return 1
            else:
                return 0
        else:
            return 0

