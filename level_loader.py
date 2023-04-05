import pygame
import definitions
from classes.json_handler import JsonFile


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
                  textures
                  ):
        """
        Constructor for the level_loader class

        Args:
            surface: the surface which all assets will be drawn on
            source_folder: the base folder to search for the .lvl files
            textures: the textures dictionary to use

        Returns:
            None

        Raises:
            None
        """
        self.surface = surface
        self.source_folder = source_folder
        self.textures = JsonFile(textures)
        self.texture_dict = {}

    def __load_textures(self):
        self.texture_dict = self.textures.fetch()
        # print(self.textures.fetch())

    def new_lvl(self, file_name):
        self.__load_textures()
        level_data = textLoader(self.source_folder + file_name)

        # Loop through the level data and set the texture of each tile
        for row_idx, row in enumerate(level_data):
            for col_idx, tile in enumerate(row):
                # Get the texture name from the tile value
                texture_path = self.texture_dict[tile]

                # Get the texture surface from the textures dictionary
                texture_surface = pygame.image.load(texture_path)

                # Scale the texture surface to match definitions.tile_size
                texture_surface = pygame.transform.scale(texture_surface,
                                                         (definitions.tile_size, definitions.tile_size))

                # Calculate the position of the tile on the surface
                pos = (col_idx * definitions.tile_size,
                       row_idx * definitions.tile_size)

                # Draw the texture on the surface at the calculated position
                self.surface.blit(texture_surface, pos)

        # Update the display to show the new level
        pygame.display.flip()
