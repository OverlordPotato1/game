import pygame
import sys
import definitions

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = definitions.SCREEN_WIDTH
screen_height = definitions.SCREEN_HEIGHT
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

# Create the world surface
world_width = screen_width+400
world_height = screen_height+400
world = pygame.Surface((world_width, world_height))

game_element = pygame.Surface((32, 32))
game_element.fill((255, 0, 0))

# Create the visible screen surface
screen_view = pygame.Surface((screen_width, screen_height))

# Main game loop
scroll_x = 0
scroll_y = 0
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            screen_width = event.w
            screen_height = event.h
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            world_width = screen_width+400
            world_height = screen_height+400
            world = pygame.Surface((world_width, world_height))
            screen_view = pygame.Surface((screen_width, screen_height))
            print("Resized to: ", screen_width, screen_height)

    

    # Scroll the world surface
    scroll_x += -1
    scroll_y += -1
    world.scroll(-scroll_x, -scroll_y)

    world.fill((0, 0, 0))

    screen_view.fill((0, 0, 0))
    world.blit(game_element, (0, 0))

    # Blit a portion of the world surface onto the visible screen surface
    screen_view.blit(world, (0, 0), (scroll_x, scroll_y, screen_width, screen_height))

    fps = 60
    clock = pygame.time.Clock()
    clock.tick(fps)

    # Update the display
    screen.blit(screen_view, (0, 0))
    pygame.display.flip()
