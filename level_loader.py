import pygame
import definitions


class level_loader:
    def __init__ (self, surface: pygame.Surface, source_folder: str, definitions_pack: str = None):
        '''
        Constructor for the level_loader class
        
        Args:
            surface: the surface which all assets will be drawn on
            source_folder: the base folder to search for the .lvl files
            definitions_pack: pack that defines what images each key will load (Leave empty to use specified pack in each .lvl file)
            
        Returns:
            None

        Raises:
            None
        '''
        self.surface = surface
        self.source = source_folder
        self.definitions_pack = definitions_pack
        if (definitions_pack == None):
            self.dynmaic_def_pack = False
        else:
            self.dynamic_def_pack = True 

    def __load_def_pack(self):
        with open(self.definitions_pack, "r") as f:
            lines = f.readlines()
        
        table = []
        for line in lines:
            fields = line.strip().split(":")
            table.append(fields)