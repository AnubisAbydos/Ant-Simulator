import pygame
import Constants as const

# Used by priority queue class for heappush and heappop
import heapq


''' CLASS PRIORITYQUEUE
Used by the pathfinding for A* implementation of f(n) priority
'''
class PriorityQueue(object):
    def __init__(self):
        self.elements = []

    ### Places item in elements based on priority
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    ### Returns top priority item
    def get(self):
        return heapq.heappop(self.elements)[1]

    def empty(self):
        return len(self.elements) == 0


''' CLASS DRAWNTILE
Designed for drawing the ant trail after the path has been found.
Stores image and rect as well as the logic to draw and update animation sequence.
'''
class DrawnTile(object):
    def __init__(self, x, y, state):
        self.rect = pygame.Rect(x, y, const.PIXELSIZE, const.PIXELSIZE)
        self.image = pygame.image.load(const.ANIMATIONPICONE).convert_alpha()
        self.animationState = state

    ### Cycles animation to add dynamic quality
    def update(self, treeReached):
        # Don't update animation while trail moving towards tree (only while at tree and returning)
        if treeReached:
            self.animationState += 1
            self.animationState = self.animationState % 3
            # Update new image state
            self.updateAnimation()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    ### Updates image based on animation state number called once per update
    def updateAnimation(self):
        if self.animationState == 0:
            self.image = pygame.image.load(const.ANIMATIONPICONE).convert_alpha()
        elif self.animationState == 1:
            self.image = pygame.image.load(const.ANIMATIONPICTWO).convert_alpha()
        elif self.animationState == 2:
            self.image = pygame.image.load(const.ANIMATIONPICTHREE).convert_alpha()

''' CLASS TILE
Used as the object in creating the grid in A* pathfinding algrothim.
'''
class Tile(object):
    def __init__(self, x, y, isBlocked):
        self.coords = (x, y)
        self.isBlocked = isBlocked
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0

''' CLASS ANTTRAIL
This class contains all the A* pathfinding logic
This class also creates the tiles for animation and is the main call from Game
Has information regarding the trails current state as well as its calls for draw and update.
'''
class AntTrail(object):
    def __init__(self, screen, treeList):
        self.screen = screen
        self.treeList = treeList
        self.target = None
        self.grid = [[0 for x in range(const.GRIDROWS)] for y in range(const.GRIDCOLUMNS)]
        self.finalPathList = []
        self.createGrid()
        self.treeReached = False
        self.drawingList = []
        self.noDrawList = []
        self.buildingTrail = False
        self.trailActive = False

    ### Creates grid for use in A* algorithm Created on program start
    def createGrid(self):
        for col in xrange(const.GRIDROWS):
            for row in xrange(const.GRIDCOLUMNS):
                x = col * const.PIXELSIZE
                y = row * const.PIXELSIZE
                isBlocked = False
                for tree in self.treeList:
                    # '+ 10' added to point to place collide check in center of grid cell
                    if tree.rect.collidepoint(x + 10, y + 10):
                        isBlocked = True
                self.grid[col][row] = Tile(x, y, isBlocked)

    ### A* pathfinding algorthim takes in the target from game as designated by selected tree
    def findPath(self, target, attempt):
        # If path drawing underway dont start new path
        if self.drawingList:
            pass
        else:
            self.target = target
            openList = PriorityQueue()
            # Start tile is always center of anthill
            start = Tile(740, 740, False)
            openList.put(start, 0)
            closedList = set()
            done = False
            added = 0
            while not done:
                # Get highest priority from open List
                lowestFTile = openList.get()
                # Add to closed
                closedList.add(lowestFTile)
                # Call and examine each neighbor
                neighbors = self.getNeighbors(lowestFTile)
                for neighbor in neighbors:
                    # If the end has been found break loop and build the path
                    if neighbor.coords == target:
                        done = True
                        self.createPath(lowestFTile)
                        del openList
                        del closedList
                        break
                    # If it isnt a tree and hasnt been looked at ie:closed list, add it to open
                    if not neighbor.isBlocked and neighbor not in closedList:
                            added += 1
                            self.updateCell(neighbor, lowestFTile)
                            openList.put(neighbor, neighbor.f)
                # If path isnt found within 1000 tile checks re-run with new target on same tree
                if added > 1000:
                    done = True
                    if attempt == 1:
                        x = target[0] - 20
                        y = target[1]
                        self.findPath((x, y), 2)
                    if attempt == 2:
                        x = target[0]
                        y = target[1] - 20
                        self.findPath((x, y), 3)

    ### Returns a list of a given cells neighbors taken from the grid
    def getNeighbors(self, currentCell):
        cells = []
        currentX = currentCell.coords[0] / 20
        currentY = currentCell.coords[1] / 20
        if currentX + 1 < const.GRIDROWS:
            cells.append(self.grid[currentX + 1][currentY])
        if currentX - 1 >= 0:
            cells.append(self.grid[currentX - 1][currentY])
        if currentY + 1 < const.GRIDROWS:
            cells.append(self.grid[currentX][currentY + 1])
        if currentY - 1 >= 0:
            cells.append(self.grid[currentX][currentY - 1])
        return cells 
    
    ### Updates cell state with given cell's state
    def updateCell(self, neighbor, currentCell):
        # 20 is the arbitrary cost per move between tiles
        neighbor.g = currentCell.g + 20
        neighbor.h = self.setHeuristic(neighbor)
        # Set the parent so that the path can be created later
        neighbor.parent = currentCell
        neighbor.f = neighbor.h + neighbor.g

    ### Sets Hueristic value based on manhattan methodology
    def setHeuristic(self, cell):
        return (abs(cell.coords[0] - self.target[0]) + abs(cell.coords[1] - self.target[1]))

    ### Called after path has been found and is passed the final cell in the path
    ### Works backwards using parents to create the noDrawList
    def createPath(self, endCell):
        addCell = endCell
        while (addCell != None):
            self.finalPathList.append(addCell)
            addCell = addCell.parent
        self.finalPathList.reverse()
        self.noDrawList = []
        state = 0
        for cell in self.finalPathList:
            self.noDrawList.append(DrawnTile(cell.coords[0], cell.coords[1], state))
            # State is rotated for each cell to provide a moving trail effect
            state += 1
            state = state % 3
        self.buildingTrail = True
        self.finalPathList = []

    ### Updates Ant Trail Path
    def update(self):
        # Update only if currently building path
        if self.buildingTrail:
            self.trailActive = True
            # If cells still left in noDrawList add them to drawingList
            if self.noDrawList:
                self.drawingList.append(self.noDrawList.pop(0))
            # If all cells are in drawingList tree has been reached
            else:
                self.treeReached = True
            # Call update on both lists to maintain animation cycles
            for tile in self.noDrawList:
                tile.update(self.treeReached)
            for tile in self.drawingList:
                tile.update(self.treeReached)
        # If trail is Cancelled set not treeReached and remove everything from drawingList to clear screen
        else:
            self.treeReached = False
            if self.drawingList:
                self.drawingList.pop()
            for tile in self.drawingList:
                tile.update(True)
            if not self.drawingList:
                self.trailActive = False

    def draw(self):
        # Draw everything in drawingList
        for tile in self.drawingList:
            tile.draw(self.screen)

