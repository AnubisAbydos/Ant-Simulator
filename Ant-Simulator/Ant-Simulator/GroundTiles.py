import pygame
import Constants as const
from random import *

#Grid variables and 2d array


#Class for holding the cell's shape and state
class cell(object):
    def __init__(self, row, column, isAlive):
        self.rect = pygame.Rect(row * const.PIXELSIZE, column * const.PIXELSIZE, const.PIXELSIZE, const.PIXELSIZE)
        self.oldIsAlive = isAlive
        self.newIsAlive = isAlive
        if isAlive == True:
            self.image = pygame.image.load(const.GRASS)
        else:
            self.image = pygame.image.load(const.SAND)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def changeState(self, newState):
        self.newIsAlive = newState
        if newState == True:
            self.image = pygame.image.load(const.GRASS)
        else:
            self.image = pygame.image.load(const.SAND)

class groundTiles(object):
    def __init__(self, screen):
        self.screen = screen
        self.cells = [[0 for x in range(const.GRIDROWS)] for y in range(const.GRIDCOLUMNS)]
        #Construct cell array Giving random starting state
        for column in xrange(const.GRIDROWS):
            for row in xrange(const.GRIDCOLUMNS):
                if(randint(0, 100) < const.STARTALIVEPERCENTAGE):
                    self.cells[row][column] = cell(row, column, True)
                else:
                    self.cells[row][column] = cell(row, column, False)

        #run simulation step specified number of times
        for i in range(0, const.STEPS):
            self.doSimulationStep()

    #function to count and return number of living neighbors
    def countAliveNeighbors(self, x, y):
        count = 0
        #loop to each neighbor including corners
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbourX = x + i
                neighbourY = y + j
                if (i == 0 and j == 0):
                    pass
                elif (neighbourX < 0 or neighbourY < 0 or neighbourX >= len(self.cells) or neighbourY >= len(self.cells[0])):
                    count = count + 1
                elif (self.cells[neighbourX][neighbourY].oldIsAlive):
                    count = count + 1

        return count

    #loops through every cell in grid calls countAliveNeighbors and then updates state
    def doSimulationStep(self):
        for x in xrange(const.GRIDROWS - 1):
            for y in xrange(const.GRIDCOLUMNS - 1):
                neighborsAlive = self.countAliveNeighbors(x, y)
                if(self.cells[x][y].oldIsAlive):
                    if(neighborsAlive < const.DEATHLIMIT):
                        self.cells[x][y].changeState(False)
                    else:
                        self.cells[x][y].changeState(True)
                else:
                    if(neighborsAlive > const.BIRTHLIMIT):
                        self.cells[x][y].changeState(True)
                    else:
                        self.cells[x][y].changeState(False)
        #resets old state after all new states have been set (to prepare for next simulation)
        for x in xrange(const.GRIDROWS):
            for y in xrange(const.GRIDCOLUMNS):
                self.cells[x][y].oldIsAlive = self.cells[x][y].newIsAlive

    def draw(self):
        for x in xrange(const.GRIDROWS):
            for y in xrange(const.GRIDCOLUMNS):
                self.cells[x][y].draw(self.screen)


