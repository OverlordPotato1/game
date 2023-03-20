import pygame


class spritesheet:
    def __init__(self, file_name, dimensions):
        """
        Constructor for the spritesheet class

        Args:
            file_name: the path to the spritesheet file
            dimensions: a tuple containing the width and height of each sprite in the spritesheet

        Returns:
            None

        Raises:
            None

        Example:
            spritesheet = spritesheet(definitions.FILE_PATH + "spritesheet.png", (64, 64))
        """
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()
        self.file_width = self.sprite_sheet.get_width()
        self.file_height = self.sprite_sheet.get_height()
        self.sprite_width = dimensions[0]
        self.sprite_height = dimensions[1]
        self.file_name = file_name
        self.dimensions = dimensions
        self.sprite_size = dimensions
        self.sprites = []

    def __load_spritesheet(self):
        """
        Loads a spritesheet into a list of sprites.
        Not intended to be called directly.

        Args:
            None

        Returns:
            None

        Raises:
            None

        Example:
            sprites = spritesheet._load_spritesheet()
        """
        sprite_sheet = self.sprite_sheet
        sprites = []

        for y in range(0, self.file_height, self.sprite_size[1]):
            for x in range(0, self.file_width, self.sprite_size[0]):
                rect = pygame.Rect(x, y, self.sprite_size[0], self.sprite_size[1])
                sprite = sprite_sheet.subsurface(rect)
                sprites.append(sprite)

        self.sprites = sprites

    def returnSprites(self, returnType="list", dictionaryNames=None):
        """
        Returns the spritesheet as a list of sprites or a dictionary of sprites.

        Args:
            returnType: the type of object to return. Can be either "list" or "dict". Is table by default and if
                        spritesheet contains only one row.
            dictionaryNames: a list of names for the sprites. Required if returnType is "dict"

        Returns:
            A list of sprites or a dictionary of sprites.

        Raises:
            None

        Example:
            sprites = spritesheet.returnSprites("list")
            sprites = spritesheet.returnSprites("dict", ["sprite1", "sprite2", "sprite3"])
        """
        self.__load_spritesheet()
        # determine if the spritesheet contains multiple rows and set isMultipleRows accordingly
        if self.sprite_width * len(self.sprites) > self.file_width:
            isMultipleRows = True
        else:
            isMultipleRows = False

        if returnType == "list" or not isMultipleRows:

            # separate sprites into rows if the combined width of the sprites is greater than the width of the spritesheet
            # if isMultipleRows:
            #     self.sprites = [self.sprites[i:i + self.file_width // self.sprite_width] for i in range(0, len(self.sprites), self.file_width // self.sprite_width)]
            return self.sprites
        elif returnType == "dict":
            if dictionaryNames == None:
                raise Exception("dictionaryNames is required if returnType is \"dictionary\"")
            else:
                # separate sprites into rows if the combined width of the sprites is greater than the width of the spritesheet
                if isMultipleRows:
                    self.sprites = [self.sprites[i:i + self.file_width // self.sprite_width] for i in
                                    range(0, len(self.sprites), self.file_width // self.sprite_width)]
                # place each row into a dictionary entry named after the corresponding name in dictionaryNames
                sprites = {}
                for i in range(len(self.sprites)):
                    sprites[dictionaryNames[i]] = self.sprites[i]
                return sprites

        else:
            raise Exception("returnType must be either \"list\" or \"dict\"")
