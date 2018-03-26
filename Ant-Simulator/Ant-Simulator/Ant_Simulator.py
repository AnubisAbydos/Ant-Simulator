import pygame
import Constants as const
import GroundTiles as ground
import TreeNode as tree
import UI as ui
import AntTrail as trail
import sys



''' CLASS GAME
Contains all information, variables and functions for an instance of a game
'''
class Game (object):
    def __init__(self, screen):
        self.screen = screen
        self.UI = ui.UI(screen)
        # Calls UI loadingScreen to display loading screen while the game finishes __init__
        self.UI.loadingScreen()
        self.groundTiles = ground.groundTiles(screen)
        self.trees = tree.TreeNodesList(screen)
        self.antTrail = trail.AntTrail(screen, self.trees.list)

        # Variables set up for use in the AntTrail and Leaf Collection Logic
        self.isTrailSelected = False
        self.trailTree = None
        self.mouseCursor = pygame.image.load("mouse_cursor.png").convert_alpha()

        # Calls Start Screen loop after all assests are loaded
        self.UI.startScreen()
       
    ### Processes User Events
    def processEvents(self):
        pos = pygame.mouse.get_pos()
        self.UI.processMousePos(pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handleMouseClicks(pos)
            return False

    ### Handle locations for mouseclicks
    def handleMouseClicks(self, pos):
        # Has the user clicked Start Trail?
        if self.isTrailSelected and self.trailTree == None and not self.antTrail.trailActive:
            self.trailTree = self.trees.checkForCollision(pos)
            self.isTrailSelected = False
            # Has a Tree been selected?
            if self.trailTree != None:
                self.antTrail.findPath(self.trailTree.rect.center, 1)
                
        # Has user clicked Start Trail?
        elif const.STARTTRAILRECT.collidepoint(pos):
            self.isTrailSelected = not self.isTrailSelected
        # Has user clicked End Trail?
        elif const.ENDTRAILRECT.collidepoint(pos):
            if self.trailTree != None:
                self.trailTree.isBeingHarvested = False
            self.antTrail.buildingTrail = False
            self.trailTree = None
            self.isTrailSelected = False
        # Has user clicked Spawn Worker?
        elif const.SPAWNWORKERSBUTTONRECT.collidepoint(pos):
            self.UI.spawnWorker(True)
            self.isTrailSelected = False
        # Has user clicked Spawn Gatherer?
        elif const.SPAWNGATHERBUTTONRECT.collidepoint(pos):
            self.UI.spawnGather(True)
            self.isTrailSelected = False
        # Has user clicked Spawn Soldier?
        elif const.SPAWNSOLDIERBUTTONRECT.collidepoint(pos):
            self.UI.spawnSoldier(True)
            self.isTrailSelected = False
        # Has user clicked Spawn Princess?
        elif const.SPAWNPRINCESSBUTTONRECT.collidepoint(pos):
            self.UI.spawnPrincess(True)
            self.isTrailSelected = False
        # Has user clicked Upgrade Hive?
        elif const.UPGRADEHIVEBUTTONRECT.collidepoint(pos):
            self.UI.upgradeHive(True)
            self.isTrailSelected = False
        else:
            self.isTrailSelected = False

    ### One Second Update Calls
    def update1Second(self):
        # If there is a tree get its quality
        if self.antTrail.treeReached and self.trailTree != None:
            treeQuality = self.trailTree.getTreeQuality()
            leafQuantity = self.trailTree.getLeafQuantity()
            self.trailTree.isBeingHarvested = True
        else:
            treeQuality = 0
            leafQuantity = -1
        self.trees.update(self.UI.getHarvesterCount())        
        # Pass Game State variables to UI for updating
        self.UI.update(self.antTrail.treeReached, leafQuantity > 0, treeQuality)
        # Reset Button Statues
        self.workerButtonPressed = False
        self.gatherButtonPressed = False
        self.soldierButtonPressed = False
        self.princessButtonPressed = False
        self.upgradeHiveButtonPressed = False


    ### Twenty frame/tick Update Calls
    def update10Tick(self):
        self.antTrail.update()

    ### Draw Calls
    def draw(self):
        self.groundTiles.draw()
        self.trees.draw()
        self.antTrail.draw()
        self.UI.draw()
        if self.isTrailSelected:
            pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
            self.screen.blit(self.mouseCursor, pygame.mouse.get_pos())
        else:
            pygame.mouse.set_cursor((16, 19), (0, 0), (128, 0, 192, 0, 160, 0, 144, 0, 136, 0, 132, 0, 130, 0, 129, 0, 128, 128, 128, 64, 128, 32, 128, 16, 129, 240, 137, 0, 148, 128, 164, 128, 194, 64, 2, 64, 1, 128), (128, 0, 192, 0, 224, 0, 240, 0, 248, 0, 252, 0, 254, 0, 255, 0, 255, 128, 255, 192, 255, 224, 255, 240, 255, 240, 255, 0, 247, 128, 231, 128, 195, 192, 3, 192, 1, 128))

### Main calls game sets screen and runs game loop
def main():
    pygame.init()
    # Build the screen
    screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
    # Build the game and pass it the screen
    game = Game(screen)
    done = False
    # Start the clock
    clock = pygame.time.Clock()
    frameRate = 60
    frameCount = 0
    nextSecondUpdate = 1
    nextTickUpdate = 10
    # Loop Start
    while not done:
        # Used in One Second Update Interval
        totalSeconds = frameCount // frameRate

        # Calls Process events for user input
        done = game.processEvents()

        # Update roughly once every second
        if (totalSeconds == nextSecondUpdate):
            game.update1Second()

        # Update every 10 frames/ticks
        if (frameCount == nextTickUpdate):
            game.update10Tick()
            nextTickUpdate += 10

        # Draw the screen
        game.draw()
        # Increment Frames/Ticks
        frameCount += 1
        #Reset frames and seconds every 60 frames to avoid numbers becoming too large
        if (frameCount == 61):
            frameCount = 1
            nextTickUpdate = 10
            totalSeconds = 0
        # Throttle frame rate
        clock.tick(frameRate)
        # Flip to user
        pygame.display.flip()

    #Loop End
    pygame.quit()
    sys.exit()

# Call main to start game
if __name__ == "__main__":
    main()