import pygame
import definitions


class level_loader:
    def __init__ (self, surface: pygame.Surface, textures):
        '''
        Constructor for the level_loader class
        
        Args:
            surface: the surface which all assets will be drawn on
            source_folder: the base folder to search for the .lvl files
            
        Returns:
            None

        Raises:
            None
        '''
        self.surface = surface
        self.textures = textures

    def __load_textures(self):
        with open(self.definitions_pack, "r") as f:
            lines = f.readlines()
        
        table = []
        for line in lines:
            fields = line.strip().split(":")
            table.append(fields)