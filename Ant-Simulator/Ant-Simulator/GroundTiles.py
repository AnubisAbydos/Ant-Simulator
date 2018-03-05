import pygame
import Constants as const
from random import *

#Grid variables and 2d array
cells = [[0 for x in range(const.GRIDROWS)] for y in range(const.GRIDCOLUMNS)]

#Class for holding the cell's shape and state
class cell(object):
    def __init__(self, row, column, isAlive):
        self.cellRect = pygame.Rect(row * cellPixelSize, column * cellPixelSize, cellPixelSize, cellPixelSize)
        self.oldIsAlive = isAlive
        self.newIsAlive = isAlive
        if isAlive == True:
            self.image = pygame.image.load()
        else:
            self.image = pygame.image.load()

#function to count and return number of living neighbors
def countAliveNeighbors(x, y):
    count = 0
    #loop to each neighbor including corners
    for i in range(-1, 2):
        for j in range(-1, 2):
            neighbourX = x + i
            neighbourY = y + j
            if (i == 0 and j == 0):
                pass
            elif (neighbourX < 0 or neighbourY < 0 or neighbourX >= len(cells) or neighbourY >= len(cells[0])):
                count = count + 1
            elif (cells[neighbourX][neighbourY].oldIsAlive):
                count = count + 1
    return count

#loops through every cell in grid calls countAliveNeighbors and then updates state
def doSimulationStep():
    for x in range(0, r):
        for y in range(0, c):
            neighborsAlive = countAliveNeighbors(x, y)
            if(cells[x][y].oldIsAlive):
                if(neighborsAlive < deathLimit):
                    cells[x][y].newIsAlive = False
                else:
                    cells[x][y].newIsAlive = True
            else:
                if(neighborsAlive > birthLimit):
                    cells[x][y].newIsAlive = True
                else:
                    cells[x][y].newIsAlive = False
    #resets old state after all new states have been set (to prepare for next simulation)
    for x in range(0, r):
        for y in range(0, c):
            cells[x][y].oldIsAlive = cells[x][y].newIsAlive

#Construct cell array Giving random starting state
for column in xrange(r):
    for row in xrange(c):
        if(randint(0, 100) < startAlivePercentage):
            cells[row][column] = cell(row, column, True)
        else:
            cells[row][column] = cell(row, column, False)

#run simulation step specified number of times
for i in range(0, steps):
    doSimulationStep()

#Pygame variable setup

pygame.display.init()
#Screen size is set based on number of cells in grid multiplied by each rect size to make perfect screen size
screen = pygame.display.set_mode((r * cellPixelSize, c * cellPixelSize))
run = True

#Game loop start
while (run):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    for x in range(0, r):
        for y in range(0, c):
            #Draw only dead cells to create the open passable area
            if (cells[x][y].oldIsAlive == False):
                pygame.draw.rect(screen, white, cells[x][y].cellRect, 0)
    pygame.display.flip()

pygame.display.quit()
