import pygame
import definitions
from classes.json_handler import JsonFile
from classes.sprite import Sprite


def textLoader(file):
    with open(file) as file:
        # Read the file and split each line by newline character "\n"
        lines = file.readlines()

        # Split each line by space " " to create a list of elements
        elements = [line.strip().split(" ") for line in lines]

        # Print the resulting list of lists
        return elements


class level_loader:
    def __init__ (self,
                  surface: pygame.Surface,
                  source_folder,
                  textures,
                  collide_group
                  ):
        """
        Constructor for the level_loader class

        Args:
            surface: the surface which all assets will be drawn on
            source_folder: the base folder to search for the .lvl files
            textures: the textures dictionary to
            collide_group: the collide group

        Returns:
            None

        Raises:
            None
        """
        self.surface = surface
        self.source_folder = source_folder
        self.textures = JsonFile(textures)
        self.texture_dict = {}
        self.collide_group = collide_group
        self.all_sprites = pygame.sprite.Group()

    def __load_textures(self):
        self.texture_dict = self.textures.fetch()

    def new_lvl(self, file_name):
        self.__load_textures()
        level_data = textLoader(self.source_folder + file_name)

        # Calculate the size of the level in pixels
        level_width = len(level_data[0]) * definitions.tile_size
        level_height = len(level_data) * definitions.tile_size

        # Create a new surface to hold the level
        self.surface = pygame.Surface((level_width, level_height), pygame.SRCALPHA)

        # Loop through the level data and set the texture of each tile
        for row_idx, row in enumerate(level_data):
            for col_idx, tile in enumerate(row):
                pos = (col_idx * definitions.tile_size, row_idx * definitions.tile_size)

                try:
                    tile_data = self.texture_dict[tile]
                except KeyError:
                    tile_data = self.texture_dict["null"]
                texture_path = tile_data["path"]

                # Create a new Sprite object with the texture image
                sprite = Sprite(texture_path, (definitions.tile_size, definitions.tile_size))

                # Set the position of the sprite on the level surface
                sprite.rect.topleft = pos

                # Check if the tile is collidable and add it to the player_collide_group
                if tile_data.get("collidable", False):
                    self.collide_group.add(sprite)

                # Add the sprite to the all_sprites group
                self.all_sprites.add(sprite)

        # Update the display to show the new level
        self.all_sprites.draw(self.surface)

        pygame.display.flip()
