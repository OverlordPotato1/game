import pygame
import math
import definitions

def draw_a_ray(angle, playerSprite, debug_surface, player_collide_group):
    dx = math.cos(math.radians(angle))
    dy = math.sin(math.radians(angle))

    surface = pygame.Surface((definitions.SCREEN_HEIGHT, definitions.SCREEN_WIDTH), pygame.SRCALPHA)

    hit = False

    for i in range(0, 1000, 50):
        x = playerSprite.rect.centerx + dx * i
        y = playerSprite.rect.centery + dy * i
        pygame.draw.rect(debug_surface, (255, 0, 0, 255), (x, y, 2, 2))

        for sprite in player_collide_group:
            if sprite.rect.collidepoint(x, y):
                # sprite.image.set_alpha(128)
                hit = True
                return surface
        if hit:
            return surface
    return surface