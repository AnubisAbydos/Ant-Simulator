import pygame
import Constants as const
import GroundTiles as ground
import TreeNode as tree
import UI as ui
import AntTrail as trail



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

        # Variables used for state of game
        self.antWorkerCount = 10
        self.antHarvesterCount = 10
        self.antSoldierCount = 0
        self.hiveLeafCount = 0
        self.hiveFungusCount = 100
        self.hiveLevel = 1

        # Font for display

        # Calls Start Screen loop after all assests are loaded
        self.UI.startScreen()
       
    ### Processes User Events
    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handleMouseClicks()
            return False

    ### Handle locations for mouseclicks
    def handleMouseClicks(self):
        # Get mouse pos after click
        pos = pygame.mouse.get_pos()

        # Has the user clicked Start Trail?
        if self.isTrailSelected:
            self.trailTree = self.trees.checkForCollision(pos)
            # Has a Tree been selected?
            if self.trailTree != None:
                self.trailTree.isBeingHarvested = True
                self.antTrail.findPath(self.trailTree.rect.center)
                self.isTrailSelected = False

        # Has user clicked Start Trail?
        if const.STARTTRAILRECT.collidepoint(pos):
            self.isTrailSelected = not self.isTrailSelected

        # Has user clicked End Trail?
        if const.ENDTRAILRECT.collidepoint(pos):
            if self.trailTree != None:
                self.trailTree.isBeingHarvested = False
            self.antTrail.buildingTrail = False

    # One Second Update Calls
    def update1Second(self):
        self.updateFungusGrowth()
        self.trees.update(self.antHarvesterCount)
        if self.antTrail.treeReached:
            self.hiveLeafCount += self.antHarvesterCount * self.trailTree.getTreeQuality()

    # Twenty frame/tick Update Calls
    def update20Tick(self):
        self.antTrail.update()

    # Draw Calls
    def draw(self):
        self.groundTiles.draw()
        self.UI.draw()        
        self.trees.draw()
        self.antTrail.draw()

        #TODO REMOVE THIS
        #DEBUG CODE IN DRAW
        print(self.hiveLeafCount, self.hiveFungusCount)

    ### Update hive fungus based on hive level
    def updateFungusGrowth(self):
        self.hiveFungusCount += (self.hiveLevel * 10)

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
    nextTickUpdate = 20
    # Loop Start
    while not done:
        # Used in One Second Update Interval
        totalSeconds = frameCount // frameRate

        # Calls Process events for user input
        done = game.processEvents()

        # Update roughly once every second
        if (totalSeconds == nextSecondUpdate):
            game.update1Second()
            nextSecondUpdate += 1

        # Update every 20 frames/ticks
        if (frameCount == nextTickUpdate):
            game.update20Tick()
            nextTickUpdate += 20

        # Draw the screen
        game.draw()
        # Increment Frames/Ticks
        frameCount += 1
        # Throttle frame rate
        clock.tick(frameRate)
        # Flip to user
        pygame.display.flip()

    #Loop End
    pygame.quit()

# Call main to start game
if __name__ == "__main__":
    main()