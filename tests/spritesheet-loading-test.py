import pygame
from spritesheet import spritesheet
import definitions


# Initialize Pygame
pygame.init()


# Set up the display
screen = pygame.display.set_mode((definitions.SCREEN_WIDTH, definitions.SCREEN_HEIGHT), pygame.RESIZABLE)
scr_width = definitions.SCREEN_WIDTH
scr_height = definitions.SCREEN_HEIGHT

sprites = spritesheet("D:\game but better\game\Images\Downloaded\Fantasy Pixel Art Asset Pack\Knight-Walk-Sheet.png", (64, 64))
sprites = sprites.returnSprites("list")
# double the size of the sprites
for i in range(len(sprites)):
    sprites[i] = pygame.transform.scale(sprites[i], (128, 128))
print(sprites)

# Start the animation loop
running = True
current_sprite = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if the winow is resized, update the definitions
        if event.type == pygame.VIDEORESIZE:
            print("resize")
            scr_width = event.w
            scr_height = event.h
            print(scr_width, scr_height)

    # Clear the screen
    screen.fill((255, 255, 255, 255))

    # Draw the current sprite and animate it in a circle
    screen.blit(sprites[current_sprite], ((scr_width / 2)-64, (scr_height / 2)-64))


    # Update the display
    pygame.display.update()

    # Advance to the next sprite
    current_sprite = (current_sprite + 1) % len(sprites)

    # Cap the framerate at 10 FPS
    clock = pygame.time.Clock()
    clock.tick(10)

# Clean up
pygame.quit()




