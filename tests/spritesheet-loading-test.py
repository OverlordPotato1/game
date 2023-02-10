import pygame
from spritesheet import spritesheet


# Initialize Pygame
pygame.init()


# Set up the display
screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)

sprites = spritesheet("D:\game but better\game\Images\Downloaded\Fantasy Pixel Art Asset Pack\Knight-Walk-Sheet.png", (64, 64))
sprites = sprites.returnSprites("list")
print(sprites)

# Start the animation loop
running = True
current_sprite = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255, 255))

    # Draw the current sprite
    screen.blit(sprites[current_sprite], (100, 100))

    # Update the display
    pygame.display.update()

    # Advance to the next sprite
    current_sprite = (current_sprite + 1) % len(sprites)

    # Cap the framerate at 10 FPS
    clock = pygame.time.Clock()
    clock.tick(10)

# Clean up
pygame.quit()




