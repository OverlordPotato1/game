import os, pygame, sys, random, math

class tile():
    def __init__(self, position, image, typeAndName, randomRotation = True, rotation = 0, whoAmI = "", tilesize = 50):
        image = "images/tile/"+image
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (tilesize, tilesize))

        if randomRotation:
            self.image = pygame.transform.rotate(self.image, random.randint(0, 4)*90)
        else:
            self.image = pygame.transform.rotate(self.image, rotation)
        self.offset = [0,0]
        self.coords = position

        self.whoAmI = whoAmI
        # the type of the tile is before the : in typeAndName
        self.type = typeAndName.split(":")[0]
        self.whatsMyRotation = rotation
        
        self.rect = self.image.get_rect(center=position)

        if self.type == "NULL":
            self.walkable = False
        else:
            self.walkable = True

    def updatePosition(self):
        newCoords = [self.coords[0]+self.offset[0], self.coords[1]+self.offset[1]]
        self.rect = self.image.get_rect(center=newCoords)

    def updateOffset(self, x, y):
        self.offset[0] = x
        self.offset[1] = y
    
    def lookingAt(self, targetPosition):
        if self.rect.collidepoint(targetPosition):
            return True
        else:
            return False


