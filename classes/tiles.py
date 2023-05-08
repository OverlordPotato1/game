# i didn't want to write this file but here i am and i hate it
import base64

import pygame
import base64

class tiles:
    # class that will hold the image, position and all other information for a tile
    def __init__(self, identity, relative_position, textures):
        self.identity = identity
        self.textures = textures
        self.__getSelfInDict()


    def __getSelfInDict(self):
        self.texture_dict = self.textures.fetch()[self.identity]
        self.image = self.texture_dict['path']
        self.collidable = self.texture_dict['collidable']
        self.name = self.texture_dict['name']
        self.id = int.from_bytes(
            base64.b64decode(
                base64.b64encode(
                    self.name.encode("utf-8")
                ).decode("utf-8")
            )
        )
        # its inefficient
        # i dont care
        # it works
