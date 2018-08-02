"""
Project Name: Ant Simulator
File Name: GroundTiles.py
Author: Lex Hall
Last Updated: August 2nd, 2018
Python Version: 2.7
Pygame Version: 1.9.1.win32-py2.7
"""

import pygame
import Constants as const
from random import *

''' CLASS CELL
Holds the cell's rect, image and state information for Celluar Automata generation
'''
class cell(object):
    def __init__(self, row, column, isAlive):
        self.rect = pygame.Rect(row * const.PIXELSIZE, column * const.PIXELSIZE, const.PIXELSIZE, const.PIXELSIZE)
        self.oldIsAlive = isAlive
        self.newIsAlive = isAlive
        self.grassImg = pygame.image.load(const.GRASS).convert()
        self.sandImg = pygame.image.load(const.SAND).convert()
        if isAlive == True:
            self.image = self.grassImg
        else:
            self.image = self.sandImg

    ### Blits the cell to the given surface called screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    ### Assigns new image and state to cell (For use by simulation step)
    def changeState(self, newState):
        self.newIsAlive = newState
        if newState == True:
            self.image = self.grassImg
        else:
            self.image = self.sandImg

''' CLASS GROUNDTILES
Builds a background tile surface from the Celluar Automata Algorithm to blit to the screen
'''
class groundTiles(object):
    def __init__(self, screen):
        # This is the game window stored for use by draw function
        self.screen = screen

        # Surface created to hold background tiles
        self.background = pygame.Surface((800, 800))

        # 2D array for use by Celluar Automata
        self.cells = [[0 for x in range(const.GRIDROWS)] for y in range(const.GRIDCOLUMNS)]

        # Construct cell array Giving random starting state
        for column in xrange(const.GRIDROWS):
            for row in xrange(const.GRIDCOLUMNS):
                if(randint(0, 100) < const.STARTALIVEPERCENTAGE):
                    self.cells[row][column] = cell(row, column, True)
                else:
                    self.cells[row][column] = cell(row, column, False)

        ### Run simulation step specified number of times
        for i in range(0, const.STEPS):
            self.doSimulationStep()

        # After Simulation is complete blit all Background tile cells to the background surface
        self.drawToSurface()

    ### Function to count and return number of a cell's living neighbors (Used by doSimulationStep)
    def countAliveNeighbors(self, x, y):
        count = 0

        # Loop to each neighbor including corners
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

    ### Loops through every cell in grid calls countAliveNeighbors and then updates state
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

        # Resets old state after all new states have been set (to prepare for next simulation)
        for x in xrange(const.GRIDROWS):
            for y in xrange(const.GRIDCOLUMNS):
                self.cells[x][y].oldIsAlive = self.cells[x][y].newIsAlive
    
    ### Blit all cells to the Background surface
    def drawToSurface(self):
        for x in xrange(const.GRIDROWS):
            for y in xrange(const.GRIDCOLUMNS):
                self.cells[x][y].draw(self.background)
        del self.cells

    ### Blits Background surface to game window
    def draw(self):
        self.screen.blit(self.background, pygame.Rect((0,0),(800,800)))