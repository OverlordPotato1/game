import os, pygame, sys, random, math
from Tile import tile
import files
from Camera import camera

def scanNearbyTiles(tileslist, coords, searchFor):
    nearbyTiles = []
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

def like80BuggyNestedIfStatments(lines, toReplace, borderingConditions, normal, edge, corner, reverseCorner, dualReverseCorner, bridge, point):
    for y, line in enumerate(lines):
        for x, current in enumerate(line):
            tempTile = current
            print(current)
            try:
                if current[0] == toReplace:
                    tempTile = [normal[0], normal[1], True, 0, normal[2]]
                    scan = scanNearbyTiles(lines, [x,y], borderingConditions)
                    if "R" in scan:
                        tempTile = [edge[0], edge[1], False, 180, edge[2]]
                        if "U" in scan:
                            tempTile = [corner[0], corner[1], False, -90, corner[2]]
                            if "L" in scan:
                                tempTile = [point[0], point[1], False, 0, point[2]]
                            elif "D" in scan:
                                tempTile = [point[0], point[1], False, -90, point[2]]
                        elif "D" in scan:
                            tempTile = [corner[0], corner[1], False, 180, corner[2]]
                            if "L" in scan:
                                tempTile = [point[0], point[1], False, 180, point[2]]
                        elif "L" in scan:
                            tempTile = [bridge[0], bridge[1], False, 0, bridge[2]]
                    

                    elif "L" in scan:
                        tempTile = [edge[0], edge[1], False, 0, edge[2]]
                        if "U" in scan:
                            tempTile = [corner[0], corner[1], False, 0, corner[2]]
                        elif "D" in scan:
                            tempTile = [corner[0], corner[1], False, 90, corner[2]]
                    

                    elif "U" in scan:
                        tempTile = [edge[0], edge[1], False, -90, edge[2]]
                        if "D" in scan:
                            tempTile = [bridge[0], bridge[1], False, -90, bridge[2]]


                    elif "D" in scan:
                        tempTile = [edge[0], edge[1], False, 90, edge[2]]


                    elif "UL" in scan:
                        tempTile = [reverseCorner[0], reverseCorner[1], False, 0, reverseCorner[2]]
                        if "UR" in scan:
                            tempTile = [dualReverseCorner[0], dualReverseCorner[1], False, 0, dualReverseCorner[2]]
                        elif "DR" in scan:
                            tempTile = [dualReverseCorner[0], dualReverseCorner[1], False, 270, dualReverseCorner[2]]
                        elif "DL" in scan:
                            tempTile = [dualReverseCorner[0], dualReverseCorner[1], False, 90, dualReverseCorner[2]]


                    elif "UR" in scan:
                        tempTile = [reverseCorner[0], reverseCorner[1], False, -90, reverseCorner[2]]
                        if "DR" in scan:
                            tempTile = [dualReverseCorner[0], dualReverseCorner[1], False, -90, dualReverseCorner[2]]


                    elif "DL" in scan:
                        print("DL", scan, x,y)
                        tempTile = [reverseCorner[0], reverseCorner[1], False, 180, reverseCorner[2]]
                        if "DR" in scan:
                            print("DR", scan, x,y)
                            tempTile = [dualReverseCorner[0], dualReverseCorner[1], False, 180, dualReverseCorner[2]]


                    elif "DR" in scan:
                        print("DR", scan, x,y)
                        tempTile = [reverseCorner[0], reverseCorner[1], False, 270, reverseCorner[2]]
                        if "DL" in scan:
                            print("DL", scan, x,y)
                            tempTile = [dualReverseCorner[0], dualReverseCorner[1], False, 0, dualReverseCorner[2]]

                                    
                    lines[y][x] = tempTile
            except:
                lines[y][x] = ["NULL:VOID", "void.png", False, 0, "VOID"]
    return lines



def loadLevel(level, tilesize):
    f = open(level, "r")
    lines = f.readlines()
    f.close()

    size = tilesize
    offset = size/2
    tiles = []
    entities = []
    player = []




    #separate spaces
    for y, line in enumerate(lines):
        tempLine = line.split(" ")
        for x, current in enumerate(tempLine):
            tempLine[x] = current.replace("\n", "")
        lines[y] = tempLine

    waterlist = []
    for y, line in enumerate(lines):
        for x, current in enumerate(line):
            tempTile = []
            if current == "0" or current == "v" or current == "":
                tempTile = ["NULL:VOID", "void.png", False, 0, "VOID"]
            elif current == "g" or current == "1":
                tempTile = ["GROUND:GRASS", "grass.png", True, 0, "GRASS"]
            elif current == "w":
                waterlist.append([x,y])
                tempTile = ["NULL:WATER", "water.png", False, 0, "WATER"]
            lines[y][x] = tempTile
    LINES = lines
    tiles = like80BuggyNestedIfStatments(lines, "GROUND:GRASS", ["NULL:VOID"], ["GROUND:GRASS", "grass.png", "GRASS"], ["GROUND:GRASS", "grass_edge.png", "GRASS_EDGE"], ["GROUND:GRASS", "grass_corner.png", "GRASS_CORNER"], ["GROUND:GRASS", "grass_reverse_corner.png", "GRASS_CORNER"], ["GROUND:GRASS", "grass_dual_reverse_corner.png", "GRASS_CORNER"], ["GROUND:GRASS", "grass_bridge.png", "GRASS_BRIDGE"], ["GROUND:GRASS", "grass_point.png", "GRASS_POINT"])
    

    TEXTTILES = tiles
    for y, line in enumerate(tiles):
        for x, current in enumerate(line):
            tiles[y][x] = tile([x*size+offset, y*size+offset],current[1], current[0], current[2], current[3], current[4], tilesize)         
    
    
    allData = [tiles, entities, player]
    return allData, LINES, TEXTTILES
