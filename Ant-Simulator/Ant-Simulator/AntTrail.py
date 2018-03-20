import pygame
import Constants as const

class Tile(object):
    def __init__(self, x, y, isBlocked):
        self.coords = (x, y)
        self.isBlocked = isBlocked
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0

class AntTrail(object):
    def __init__(self, screen, treeList):
        self.screen = screen
        self.treeList = treeList
        self.grid = [[0 for x in range(const.GRIDROWS)] for y in range(const.GRIDCOLUMNS)]
        self.createGrid()

    def findPath(self, target):
        openList = []
        start = Tile((740,740), target)
        openList.append(start)
        closedList = []
        done = False
        while not done:
            lowestFTile = openList[0]
            for tile in openList:
                if tile.f < lowestFTile.f:
                    lowestFTile = tile
            openList.remove(lowestFTile)
            closedList.append(lowestFTile)
            if lowestFTile.coords == target:
                done = True
    
    def updateCell(self, neighbor, currentCell):
        pass

    def getNeighbors(self, currentCell):
        cells = []
        currentX = currentCell.coords[0] / 20
        currentY = currentCell.coords[1] / 20
        if currentX + 1 < const.GRIDROWS:
            cells.append(grid[currentX + 1][currentY])
        if currentX - 1 >= 0:
            cells.append(grid[currentX - 1][currentY])
        if currentY + 1 < const.GRIDROWS:
            cells.append(grid[currentX][currentY + 1])
        if currentY - 1 >= 0:
            cells.append(grid[currentX][currentY - 1])
        return cells

    def createGrid(self):
        for col in xrange(const.GRIDROWS):
            for row in xrange(const.GRIDCOLUMNS):
                x = col * const.PIXELSIZE
                y = row * const.PIXELSIZE
                isBlocked = False
                for tree in self.treeList:
                    # + 10 added to point to place collide check in center of grid
                    if tree.rect.collidepoint(x + 10, y + 10):
                        isBlocked = True
                self.grid[col][row] = Tile(x, y, isBlocked)
