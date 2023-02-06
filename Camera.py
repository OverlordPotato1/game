import pygame, sys, os
from Tile import tile


class camera():
    def __init__(self, startx, starty, width, height, animationSpeed = 25, tilesize = 50):
        self.coords = [startx, starty]
        self.windowSize = [width, height]
        self.dimensions = [width/tilesize, height/tilesize]

        self.animationSpeed = animationSpeed
        self.tilesize = tilesize
        self.startTile = [int(startx/tilesize), int(starty/tilesize)]
        self.coordsOpposite = [startx, starty]

        

    def getWindowSize(self):
        return self.windowSize

    def getCoords(self):
        return self.coords

    def scroll(self, direction, tiles, entities): 
        print(self.coordsOpposite[0], self.coordsOpposite[1])
        til, x, y = self.getTile(self.coords, tiles)
        print (til)
        if direction == "up":
            # get the tile the player will be moving to
            targetTile, x, y = self.getTile([self.coordsOpposite[0]/self.tilesize, self.coordsOpposite[1]/self.tilesize], tiles)
            # if the tile is walkable, move the camera
            if targetTile.walkable:
                self.coords[1] += self.animationSpeed
                self.coordsOpposite[1] -= self.animationSpeed
                for y in tiles:
                    for x in y:
                        x.updateOffset(self.coords[0], self.coords[1])
                        x.updatePosition()
                for entity in entities:
                    entity[entity].updateOffset(0, -1)
        if direction == "down":
            targetTile, x, y = self.getTile([self.coordsOpposite[0]/self.tilesize, self.coordsOpposite[1]/self.tilesize], tiles)
            if targetTile.walkable:
                self.coords[1] -= self.animationSpeed
                self.coordsOpposite[1] += self.animationSpeed
                for y in tiles:
                    for x in y:
                        x.updateOffset(self.coords[0], self.coords[1])
                        x.updatePosition()
                for entity in entities:
                    entity[entity].updateOffset(0, 1)
        if direction == "left":
            targetTile, x, y = self.getTile([self.coordsOpposite[0]/self.tilesize, self.coordsOpposite[1]/self.tilesize], tiles)
            print(targetTile.walkable)
            if targetTile.walkable:
                self.coords[0] += self.animationSpeed
                self.coordsOpposite[0] -= self.animationSpeed
                for y in tiles:
                    for x in y:
                        x.updateOffset(self.coords[0], self.coords[1])
                        x.updatePosition()
                for entity in entities:
                    entity[entity].updateOffset(-1, 0)
        if direction == "right":
            targetTile, x, y = self.getTile([self.coordsOpposite[1]/self.tilesize, self.coordsOpposite[0]/self.tilesize], tiles)
            if targetTile.walkable:
                self.coords[0] -= self.animationSpeed
                self.coordsOpposite[0] += self.animationSpeed
                for y in tiles:
                    for x in y:
                        x.updateOffset(self.coords[0], self.coords[1])
                        x.updatePosition()
                for entity in entities:
                    entity[entity].updateOffset(1, 0)

    def getTile(self, targetPosition, tiles):
        for y, line in enumerate(tiles):
            for x, tile in enumerate(line):
                if tile.rect.collidepoint(targetPosition):
                    return tile, x, y

    def forceTilesUpdate(self, tiles):
        for y in tiles:
            for x in y:
                x.updateOffset(self.coords[0], self.coords[1])
                x.updatePosition()



