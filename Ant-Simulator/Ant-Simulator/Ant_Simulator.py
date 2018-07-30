"""
Project Name: Ant Simulator
File Name: Ant_Simulator.py
Author: Lex Hall
Last Updated: July 30th, 2018
Python Version: 2.7
Pygame Version: 1.9.1.win32-py2.7
"""

import pygame
import Constants as const
import GroundTiles as ground
import TreeNode as tree
import UI as ui
import AntTrail as trail
import PopoutBox as popout
import Enemy as enemy
import sys

''' CLASS GAME
Contains all information, variables and functions for an instance of a game
'''
class Game (object):
    def __init__(self, screen):
        self.screen = screen

        # init UI
        self.UI = ui.UI(screen)

        # Calls UI loadingScreen to display loading screen while the game finishes __init__
        self.UI.loadingScreen()

        # init all classes building game
        self.groundTiles = ground.groundTiles(screen)
        self.trees = tree.TreeNodesList(screen)
        self.antTrail = trail.AntTrail(screen, self.trees.list)
        self.popoutLoader = popout.PopoutBox(screen)
        self.enemy = enemy.EnemyList(screen, self.antTrail.grid, self.UI)

        # Background Music
        pygame.mixer.music.load("background_music.mp3")

        # Variables set up for use in the AntTrail and Leaf Collection Logic
        self.isTrailSelected = False
        self.trailTree = None

        # Mouse Cursor setup
        self.mouseCursor = pygame.image.load("mouse_cursor.png").convert_alpha()

        # Calls Start Screen loop after all assests are loaded
        self.UI.startScreen()
        pygame.mixer.music.set_volume(.3)
       
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
        # Has the user clicked a Tree?
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

        # Has user clicked Pause?
        elif const.PAUSEGAMEBUTTONRECT.collidepoint(pos):
            self.isTrailSelected = False
            pygame.mixer.music.pause()
            self.UI.pauseGame()
            pygame.mixer.music.unpause()

        # Has user clicked Worker Question Mark?
        elif const.WORKERQUESTIONMARK.collidepoint(pos):
            self.isTrailSelected = False
            pygame.mixer.music.pause()
            self.popoutLoader.runGivenPopout(const.WORKERPOPOUT)
            pygame.mixer.music.unpause()

        # Has user clicked Gather Question Mark?
        elif const.GATHERQUESTIONMARK.collidepoint(pos):
            self.isTrailSelected = False
            pygame.mixer.music.pause()
            self.popoutLoader.runGivenPopout(const.GATHERPOPOUT)
            pygame.mixer.music.unpause()

        # Has user clicked Soldier Question Mark?
        elif const.SOLDIERQUESTIONMARK.collidepoint(pos):
            self.isTrailSelected = False
            pygame.mixer.music.pause()
            self.popoutLoader.runGivenPopout(const.SOLDIERPOPOUT)
            pygame.mixer.music.unpause()

        # Has user clicked Princess Question Mark?
        elif const.PRINCESSQUESTIONMARK.collidepoint(pos):
            self.isTrailSelected = False
            pygame.mixer.music.pause()
            self.popoutLoader.runGivenPopout(const.PRINCESSPOPOUT)
            pygame.mixer.music.unpause()

        # Has user clicked Hive Question Mark?
        elif const.HIVEQUESTIONMARK.collidepoint(pos):
            self.isTrailSelected = False
            pygame.mixer.music.pause()
            self.popoutLoader.runGivenPopout(const.HIVEPOPOUT)
            pygame.mixer.music.unpause()

        # Has user clicked Leaf Question Mark?
        elif const.LEAFQUESTIONMARK.collidepoint(pos):
            self.isTrailSelected = False
            pygame.mixer.music.pause()
            self.popoutLoader.runGivenPopout(const.LEAFFUNGUSPOPOUT)
            pygame.mixer.music.unpause()

        # Has user clicked Fungus Question Mark?
        elif const.FUNGUSQUESTIONMARK.collidepoint(pos):
            self.isTrailSelected = False
            pygame.mixer.music.pause()
            self.popoutLoader.runGivenPopout(const.LEAFFUNGUSPOPOUT)
            pygame.mixer.music.unpause()
        elif const.DEBUGLOSEGAME.collidepoint(pos):
            pygame.mixer.music.pause()
            self.UI.gameOver(False)
            pygame.mixer.music.unpause()
        else:
            self.isTrailSelected = False

    ### One Second Update Calls
    def update1Second(self):
        # If there is a tree get its quality and leaf count
        if self.antTrail.treeReached and self.trailTree != None:
            treeQuality = self.trailTree.getTreeQuality()
            leafQuantity = self.trailTree.getLeafQuantity()
            self.trailTree.isBeingHarvested = True
        else:
            treeQuality = 0
            leafQuantity = -1
        self.trees.update(self.UI.antGatherCount)
                
        # Pass Game State variables to UI for updating
        self.UI.update(self.antTrail.treeReached, leafQuantity > 0, treeQuality)

    ### Fifteen frame/tick Update Calls
    def update15Tick(self):
        self.antTrail.update()
        self.enemy.update()
        
    ### Draw Calls
    def draw(self):
        self.groundTiles.draw()
        self.trees.draw()
        self.antTrail.draw()
        self.UI.draw()
        self.enemy.draw()

        # Change cursor to flag when trail button is selected
        if self.isTrailSelected:
            pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
            self.screen.blit(self.mouseCursor, pygame.mouse.get_pos())

        # Return Cursor to orginal Design
        else:
            pygame.mouse.set_cursor((16, 19), (0, 0), (128, 0, 192, 0, 160, 0, 144, 0, 136, 0, 132, 0, 130, 0, 129, 0, 128, 128, 128, 64, 128, 32, 128, 16, 129, 240, 137, 0, 148, 128, 164, 128, 194, 64, 2, 64, 1, 128), (128, 0, 192, 0, 224, 0, 240, 0, 248, 0, 252, 0, 254, 0, 255, 0, 255, 128, 255, 192, 255, 224, 255, 240, 255, 240, 255, 0, 247, 128, 231, 128, 195, 192, 3, 192, 1, 128))

### Main calls game sets screen and runs game loop
def main():
    pygame.init()

    # Build and set window Icon and Title
    icon = pygame.image.load("icon.jpg")
    iconSurface = pygame.Surface((32,32))
    iconRect = pygame.Rect(0,0, 32,32)
    iconSurface.fill(const.GREY)
    iconSurface.blit(icon, iconRect)
    pygame.display.set_icon(iconSurface)
    pygame.display.set_caption('Ant-Simulator')

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
    nextTickUpdate = 15

    # Loop Start
    while not done:
        # Used in One Second Update Interval
        totalSeconds = frameCount // frameRate

        # Calls Process events for user input
        done = game.processEvents()

        # Update roughly once every second
        if (totalSeconds == nextSecondUpdate):
            game.update1Second()

        # Update every 15 frames/ticks
        if (frameCount == nextTickUpdate):
            game.update15Tick()
            nextTickUpdate += 15

        # Draw the screen
        game.draw()

        # Increment Frames/Ticks
        frameCount += 1

        # Reset frames and seconds every 60 frames to avoid numbers becoming too large
        if (frameCount == 61):
            frameCount = 1
            nextTickUpdate = 15
            totalSeconds = 0

        # Throttle frame rate
        clock.tick(frameRate)
        
        # UnComment below line to display FPS in console
        #print(clock.get_fps())

        # Flip to user
        pygame.display.flip()

    #Loop End
    pygame.quit()
    sys.exit()

# Call main to start game
if __name__ == "__main__":
    main()