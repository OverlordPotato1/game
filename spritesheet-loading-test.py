import pygame

def load_spritesheet(file_name, sprite_size):
    sprite_sheet = pygame.image.load(file_name).convert_alpha()
    sprites = []

    for y in range(0, sprite_sheet.get_height(), sprite_size[1]):
        for x in range(0, sprite_sheet.get_width(), sprite_size[0]):
            rect = pygame.Rect(x, y, sprite_size[0], sprite_size[1])
            sprite = sprite_sheet.subsurface(rect)
            sprites.append(sprite)

    return sprites

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)

# Load the sprite sheet
sprites = load_spritesheet("D:\game but better\game\Images\Downloaded\Fantasy Pixel Art Asset Pack\Knight-Idle-Sheet.png", (64, 64))

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

    # Cap the framerate at 20 FPS
    clock = pygame.time.Clock()
    clock.tick(20)

# Clean up
pygame.quit()




