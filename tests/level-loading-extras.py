'''This file is not finished because it is for a top down game.'''



# i have no clue how this works but it does so don't touch it it might explode
class proximityBasedTiles:
    '''This class is used to change the tile texture to a border tile on the fly based on the tiles around it.'''
    def __init__(self):
        '''Before use ensure that all the variables are set.'''
        self.searchFor = []
        self.toReplace = ""
        self.normal = ""
        self.edge = ""
        self.corner = ""
        self.reverseCorner = ""
        self.dualReverseCorner = ""
        self.bridge = ""
        self.point = ""
        self.borderingConditions = []
        self.scan = []

    def _scanNearbyTiles(self, tileslist, coords):
        '''This function is a dependency of the go() function. It scans the tiles around the target and returns all the tiles that match the searchFor table.
        \nThis function is not to be called directly.
        '''
        nearbyTiles = []
        searchFor = self.searchFor
        try:
            if tileslist[coords[1]-1][coords[0]][0] in searchFor:
                nearbyTiles += ["U"]
        except:
            pass
        try:
            if tileslist[coords[1]+1][coords[0]][0] in searchFor:
                nearbyTiles += ["D"]
        except:
            pass
        try:
            if tileslist[coords[1]][coords[0]-1][0] in searchFor:
                nearbyTiles += ["L"]
        except:
            pass
        try:
            if tileslist[coords[1]][coords[0]+1][0] in searchFor:
                nearbyTiles += ["R"]
        except:
            pass
        try:
            if tileslist[coords[1]-1][coords[0]-1][0] in searchFor:
                nearbyTiles += ["UL"]
        except:
            pass
        try:
            if tileslist[coords[1]-1][coords[0]+1][0] in searchFor:
                nearbyTiles += ["UR"]
        except:
            pass
        try:
            if tileslist[coords[1]+1][coords[0]-1][0] in searchFor:
                nearbyTiles += ["DL"]
        except:
            pass
        try:
            if tileslist[coords[1]+1][coords[0]+1][0] in searchFor:
                nearbyTiles += ["DR"]
        except:
            pass
        print (nearbyTiles, coords)
        return nearbyTiles
    
    def go(self, tileslist, coords):
        '''The main function to scan the proximity of the tile and change it to the correct texture.'''
        # ensure that all the self. variables are set
        if self.searchFor == [] or self.toReplace == "" or self.normal == "" or self.edge == "" or self.corner == "" or self.reverseCorner == "" or self.dualReverseCorner == "" or self.bridge == "" or self.point == "" or self.borderingConditions == []:
            # raise an undefined exception
            raise Exception("One or more of the variables are not set. Variables cannot be empty.")
