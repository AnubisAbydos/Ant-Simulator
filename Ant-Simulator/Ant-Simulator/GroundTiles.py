self.tiles = [[0 for x in range(WIDTH / 10)] for y in range(HEIGHT / 10)]
drawMapTiles()


# Class containing Ground Tile
class GroundTile(object):
    def __init__(self, row, column, isAlive, cellPixelSize):
        self.cellRect = pygame.Rect(row * cellPixelSize, column * cellPixelSize, cellPixelSize, cellPixelSize)
        self.oldIsAlive = isAlive
        self.newIsAlive = isAlive
    def setTile(self, newIsAlive):
        self.newIsAlive = newIsAlive
        if self.newIsAlive == True:
            self.image = pygame.image.load()
        else:
            self.image = pygame.image.load()

    
    def drawMapTiles(self):
        tilePixelSize = 10

        #used during array construction to determine tiles starting state
        startAlivePercentage = 38
        steps = 2

        #Construct cell array Giving random starting state
        for column in xrange(WIDTH):
            for row in xrange(HEIGHT):
                if(randint(0, 100) < startAlivePercentage):
                    self.tiles[row][column] = GroundTile(row, column, True, tilePixelSize)
                else:
                    self.tiles[row][column] = GroundTile(row, column, False, tilePixelSize)

        #run simulation step specified number of times
        for i in range(0, steps):
            doSimulationStep()

    def countAliveNeighbors(self, x, y):
        count = 0
        #loop to each neighbor including corners
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbourX = x + i
                neighbourY = y + j
                if (i == 0 and j == 0):
                    pass
                elif (neighbourX < 0 or neighbourY < 0 or neighbourX >= len(self.tiles) or neighbourY >= len(self.tiles[0])):
                    count = count + 1
                elif (self.tiles[neighbourX][neighbourY].oldIsAlive):
                    count = count + 1
        return count

    #loops through every cell in grid calls countAliveNeighbors and then updates state
    def doSimulationStep(self):
        #variables used during simulation step to change cell states
        deathLimit = 3
        birthLimit = 4
        
        for x in range(0, WIDTH):
            for y in range(0, HEIGHT):
                neighborsAlive = countAliveNeighbors(x, y)
                if(self.tiles[x][y].oldIsAlive):
                    if(neighborsAlive < deathLimit):
                        self.tiles[x][y].setTile(False)
                    else:
                        self.tiles[x][y].setTile(True)
                else:
                    if(neighborsAlive > birthLimit):
                        self.tiles[x][y].setTile(True)
                    else:
                        self.tiles[x][y].setTile(False)
        #resets old state after all new states have been set (to prepare for next simulation)
        for x in range(0, r):
            for y in range(0, c):
                self.tiles[x][y].oldIsAlive = self.tiles[x][y].newIsAlive
