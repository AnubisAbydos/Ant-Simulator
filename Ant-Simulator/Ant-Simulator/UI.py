"""
Project Name: Ant Simulator
File Name: UI.py
Author: Lex Hall
Last Updated: July 30th, 2018
Python Version: 2.7
Pygame Version: 1.9.1.win32-py2.7
"""

import pygame
import Constants as const

# Sys is used to exit python when exit button is clicked
import sys

''' CLASS UI
Contains the User Interface elements and updates status bars
'''
class UI (object):
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, const.WIDTH, const.HEIGHT)
        self.uiOverlay = pygame.image.load(const.UITEMPLATE).convert_alpha()
        self.questionMarkOverlay = pygame.image.load(const.QUESTIONMARKOVERLAY).convert_alpha()
        self.hiveRect = pygame.Rect(700,700,100,100)

        # Variables used for state of game
        self.antWorkerCount = 12345
        self.antGatherCount = 235
        self.antSoldierCount = 1235
        self.hiveLeafCount = 123456
        self.hiveFungusCount = 678954
        self.hiveLevel = 5
        self.spawnCount = 10
        self.hiveUpgradeTime = 10
        self.hiveUpgradeCost = 1000
        # Variables used for spawn buttons
        self.spawnWorkerStatus = -1
        self.spawnWorkerBarImg = pygame.image.load(const.SPAWNWORKERBARFULL).convert_alpha()
        self.spawnGatherStatus = -1
        self.spawnGatherBarImg = pygame.image.load(const.SPAWNGATHERBARFULL).convert_alpha()
        self.spawnSoldierStatus = -1
        self.spawnSoldierBarImg = pygame.image.load(const.SPAWNSOLDIERBARFULL).convert_alpha()
        self.spawnPrincessStatus = -1
        self.spawnPrincessBarImg = pygame.image.load(const.SPAWNPRINCESSBARFULL).convert_alpha()
        self.upgradeHiveStatus = -1
        self.hiveUpgrading = False
        self.hiveImage = pygame.image.load(const.HIVEL1).convert_alpha()
        self.hiveSideImg = pygame.image.load(const.HIVESIDE1).convert_alpha()
        self.spawnWorkerTile = pygame.image.load(const.SPAWNWORKERTILE).convert_alpha()
        self.spawnGatherTile = pygame.image.load(const.SPAWNGATHERTILE).convert_alpha()
        self.spawnSoldierTile = pygame.image.load(const.SPAWNSOLDIERTILE).convert_alpha()
        self.spawnPrincessTile = pygame.image.load(const.SPAWNPRINCESSTILE).convert_alpha()
        # Font
        self.textFont = pygame.font.Font("pixelplay.ttf", 23)
        self.costTextFont = pygame.font.Font("pixelplay.ttf", 10)
        # Sounds
        self.spawnSound = pygame.mixer.Sound("spawn_sound.wav")
        self.hiveUpgradeSound = pygame.mixer.Sound("hive_upgrade_sound.wav")
        # Highlighted button variables
        self.blittingButtonHigh = False
        self.setDestButtonHigh = pygame.image.load(const.SETDESTBUTTONHIGH).convert_alpha()
        self.setDestButtonHighBlitting = False
        self.backToHiveButtonHigh = pygame.image.load(const.BACKTOHIVEBUTTONHIGH).convert_alpha()
        self.backToHiveButtonHighBlitting = False
        self.workerButtonHigh = pygame.image.load(const.WORKERBUTTONHIGH).convert_alpha()
        self.workerButtonHighBlitting = False
        self.gatherButtonHigh = pygame.image.load(const.GATHERBUTTONHIGH).convert_alpha()
        self.gatherButtonHighBlitting = False
        self.soldierButtonHigh = pygame.image.load(const.SOLDIERBUTTONHIGH).convert_alpha()
        self.soldierButtonHighBlitting = False
        self.princessButtonHigh = pygame.image.load(const.PRINCESSBUTTONHIGH).convert_alpha()
        self.princessButtonHighBlitting = False
        self.upgradeHiveButton = pygame.image.load(const.UPGRADEHIVEHIGH).convert_alpha()
        self.upgradeHiveButtonBlitting = False
        self.pauseButtonHigh = pygame.image.load(const.PAUSEHIGH).convert_alpha()
        self.pauseButtonHighBlitting = False
        # Image Preloading
        self.spawnWorkerBarEmpty = pygame.image.load(const.SPAWNWORKERBAREMPTY).convert_alpha()
        self.spawnWorkerBar1Q = pygame.image.load(const.SPAWNWORKERBAR1Q).convert_alpha()
        self.spawnWorkerBarHalf = pygame.image.load(const.SPAWNWORKERBARHALF).convert_alpha()
        self.spawnWorkerBar3Q = pygame.image.load(const.SPAWNWORKERBAR3Q).convert_alpha()
        self.spawnWorkerBarFull = pygame.image.load(const.SPAWNWORKERBARFULL).convert_alpha()
        self.spawnGatherBarEmpty = pygame.image.load(const.SPAWNGATHERBAREMPTY).convert_alpha()
        self.spawnGatherBar1Q = pygame.image.load(const.SPAWNGATHERBAR1Q).convert_alpha()
        self.spawnGatherBarHalf = pygame.image.load(const.SPAWNGATHERBARHALF).convert_alpha()
        self.spawnGatherBar3Q = pygame.image.load(const.SPAWNGATHERBAR3Q).convert_alpha()
        self.spawnGatherBarFull = pygame.image.load(const.SPAWNGATHERBARFULL).convert_alpha()
        self.spawnSoldierBarEmpty = pygame.image.load(const.SPAWNSOLDIERBAREMPTY).convert_alpha()
        self.spawnSoldierBar1Q = pygame.image.load(const.SPAWNSOLDIERBAR1Q).convert_alpha()
        self.spawnSoldierBarHalf = pygame.image.load(const.SPAWNSOLDIERBARHALF).convert_alpha()
        self.spawnSoldierBar3Q = pygame.image.load(const.SPAWNSOLDIERBAR3Q).convert_alpha()
        self.spawnSoldierBarFull = pygame.image.load(const.SPAWNSOLDIERBARFULL).convert_alpha()
        self.spawnPrincessBarEmpty = pygame.image.load(const.SPAWNPRINCESSBAREMPTY).convert_alpha()
        self.spawnPrincessBar1Q = pygame.image.load(const.SPAWNPRINCESSBAR1Q).convert_alpha()
        self.spawnPrincessBarHalf = pygame.image.load(const.SPAWNPRINCESSBARHALF).convert_alpha()
        self.spawnPrincessBar3Q = pygame.image.load(const.SPAWNPRINCESSBAR3Q).convert_alpha()
        self.spawnPrincessBarFull = pygame.image.load(const.SPAWNPRINCESSBARFULL).convert_alpha()
        self.hiveSideConstruction = pygame.image.load(const.HIVESIDECONSTRUCTION).convert_alpha()
        self.hiveL2 = pygame.image.load(const.HIVEL2)
        self.hiveL3 = pygame.image.load(const.HIVEL3)
        self.hiveL4 = pygame.image.load(const.HIVEL4)
        self.hiveL5 = pygame.image.load(const.HIVEL5)
        self.hiveL6 = pygame.image.load(const.HIVEL6)
        self.hiveL7 = pygame.image.load(const.HIVEL7)
        self.hiveL8 = pygame.image.load(const.HIVEL8)
        self.hiveL9 = pygame.image.load(const.HIVEL9)
        self.hiveL10 = pygame.image.load(const.HIVEL10)
        self.hiveSide2 = pygame.image.load(const.HIVESIDE2)
        self.hiveSide3 = pygame.image.load(const.HIVESIDE3)
        self.hiveSide4 = pygame.image.load(const.HIVESIDE4)
        self.hiveSide5 = pygame.image.load(const.HIVESIDE5)
        self.hiveSide6 = pygame.image.load(const.HIVESIDE6)
        self.hiveSide7 = pygame.image.load(const.HIVESIDE7)
        self.hiveSide8 = pygame.image.load(const.HIVESIDE8)
        self.hiveSide9 = pygame.image.load(const.HIVESIDE9)
        self.hiveSide10 = pygame.image.load(const.HIVESIDE10)
        

        self.setHiveImgs()

    ### Takes in all state variables from Game to determine updates
    def update(self, treeReached, treeFull, treeQuality):
        self.hiveFungusCount += (self.hiveLevel * 10)
        if treeReached and treeFull:
            self.hiveLeafCount += self.antGatherCount * treeQuality
        # Call spawn functions passing false for not button call
        self.spawnWorker(False)
        self.spawnGather(False)
        self.spawnSoldier(False)
        self.spawnPrincess(False)
        self.upgradeHive(False)

    ### Process mouse pos passed from Game set blitting correct highlighted button image based on pos
    def processMousePos(self, pos):
        if const.STARTTRAILRECT.collidepoint(pos):
            self.blittingButtonHigh = True
            self.setDestButtonHighBlitting = True
            self.backToHiveButtonHighBlitting = False
        elif const.ENDTRAILRECT.collidepoint(pos):
            self.blittingButtonHigh = True
            self.backToHiveButtonHighBlitting = True
            self.setDestButtonHighBlitting = False
        elif const.SPAWNWORKERSBUTTONRECT.collidepoint(pos):
            self.blittingButtonHigh = True
            self.workerButtonHighBlitting = True
        elif const.SPAWNGATHERBUTTONRECT.collidepoint(pos):
            self.blittingButtonHigh = True
            self.gatherButtonHighBlitting = True
        elif const.SPAWNSOLDIERBUTTONRECT.collidepoint(pos):
            self.blittingButtonHigh = True
            self.soldierButtonHighBlitting = True
        elif const.SPAWNPRINCESSBUTTONRECT.collidepoint(pos):
            self.blittingButtonHigh = True
            self.princessButtonHighBlitting = True
        elif const.UPGRADEHIVEBUTTONRECT.collidepoint(pos):
            self.blittingButtonHigh = True
            self.upgradeHiveButtonBlitting = True
        elif const.PAUSEGAMEBUTTONRECT.collidepoint(pos):
            self.blittingButtonHigh = True
            self.pauseButtonHighBlitting = True
        # If pos is not over button reset bools
        else:
            self.blittingButtonHigh = False
            self.setDestButtonHighBlitting = False
            self.backToHiveButtonHighBlitting = False
            self.workerButtonHighBlitting = False
            self.gatherButtonHighBlitting = False
            self.soldierButtonHighBlitting = False
            self.princessButtonHighBlitting = False
            self.upgradeHiveButtonBlitting = False
            self.pauseButtonHighBlitting = False

    ### Handles all drawing required by the UI
    def draw(self):
        self.screen.blit(self.uiOverlay, self.rect)
        # Hive image drawing
        self.screen.blit(self.hiveImage, self.hiveRect)
        self.screen.blit(self.hiveSideImg, self.rect)
        # Load white ant tile if they meet spawn cost requirement
        if(self.hiveFungusCount > const.SPAWNWORKERCOST):
            self.screen.blit(self.spawnWorkerTile, self.rect)
        if(self.hiveFungusCount > const.SPAWNGATHERCOST):
            self.screen.blit(self.spawnGatherTile, self.rect)
        if(self.hiveFungusCount > const.SPAWNSOLDIERCOST):
            self.screen.blit(self.spawnSoldierTile, self.rect)
        if(self.hiveFungusCount > const.SPANWPRINCESSCOST):
            self.screen.blit(self.spawnPrincessTile, self.rect)
        self.screen.blit(self.spawnWorkerBarImg, self.rect)
        self.screen.blit(self.spawnGatherBarImg, self.rect)
        self.screen.blit(self.spawnSoldierBarImg, self.rect)
        self.screen.blit(self.spawnPrincessBarImg, self.rect)
        self.screen.blit(self.questionMarkOverlay, self.rect)
        # Highlighted button blitting 
        if self.blittingButtonHigh:
            if self.setDestButtonHighBlitting:
                self.screen.blit(self.setDestButtonHigh, self.rect)
            elif self.backToHiveButtonHighBlitting:
                self.screen.blit(self.backToHiveButtonHigh, self.rect)
            elif self.workerButtonHighBlitting:
                self.screen.blit(self.workerButtonHigh, self.rect)
            elif self.gatherButtonHighBlitting:
                self.screen.blit(self.gatherButtonHigh, self.rect)
            elif self.soldierButtonHighBlitting:
                self.screen.blit(self.soldierButtonHigh, self.rect)
            elif self.princessButtonHighBlitting:
                self.screen.blit(self.princessButtonHigh, self.rect)
            elif self.upgradeHiveButtonBlitting:
                self.screen.blit(self.upgradeHiveButton, self.rect)
            elif self.pauseButtonHighBlitting:
                self.screen.blit(self.pauseButtonHigh, self.rect)
        # Number Text Rendering
        self.screen.blit(self.textFont.render(str(self.antWorkerCount), True, const.WHITE), const.WORKERTEXTBOX)
        self.screen.blit(self.textFont.render(str(self.antGatherCount), True, const.WHITE), const.GATHERTEXTBOX)
        self.screen.blit(self.textFont.render(str(self.antSoldierCount), True, const.WHITE), const.SOLDIERTEXTBOX)
        self.screen.blit(self.textFont.render(str('{:06d}'.format(self.hiveFungusCount)), True, const.WHITE), const.FUNGUSTEXTBOX)
        self.screen.blit(self.textFont.render(str('{:06d}'.format(self.hiveLeafCount)), True, const.WHITE), const.LEAFTEXTBOX)
        self.screen.blit(self.costTextFont.render(str(const.SPAWNWORKERCOST), True, const.BLACK), const.WORKERFUNGUSCOSTBOX)
        self.screen.blit(self.costTextFont.render(str(const.SPAWNGATHERCOST), True, const.BLACK), const.GATHERFUNGUSCOSTBOX)
        self.screen.blit(self.costTextFont.render(str(const.SPAWNSOLDIERCOST), True, const.BLACK), const.SOLDIERFUNGUSCOSTBOX)
        self.screen.blit(self.costTextFont.render(str(const.SPANWPRINCESSCOST), True, const.BLACK), const.PRINCESSFUNGUSCOSTBOX)
        if self.hiveLevel !=  10:
            self.screen.blit(self.costTextFont.render("Leaf Cost --- " + str(self.hiveUpgradeCost), True, const.BLACK), const.UPGRADEHIVELEAFCOSTBOX)
        # If the hive is being upgraded display the timer til completion
        if self.hiveUpgrading:
            time = self.upgradeHiveStatus
            sec = time % 60
            min = time / 60
            self.screen.blit(self.textFont.render(str('%02d:%02d' % (min, sec)), True, const.WHITE), const.HIVEUPGRADETIMEBOX)

    ### Handles logic and timer for Worker Spawn takes Bool whether the call came from a button click
    def spawnWorker(self, workerButton):
        # If the call comes from button and is not running timer and fungus count is above cost start timer
        if workerButton and self.spawnWorkerStatus == -1 and self.hiveFungusCount > const.SPAWNWORKERCOST:
            self.spawnWorkerStatus = const.SPAWNWORKERTIME
            self.hiveFungusCount -= const.SPAWNWORKERCOST
            self.spawnWorkerBarImg = self.spawnWorkerBarEmpty
        # If timer is started and is not finished and this is not a button call decrement timer and update status bar
        elif self.spawnWorkerStatus != -1 and self.spawnWorkerStatus != 0 and not workerButton:
            self.spawnWorkerStatus -= 1
            percentCompleteWorker = abs((float(self.spawnWorkerStatus) / float(const.SPAWNWORKERTIME)) - 1)
            if percentCompleteWorker < .25:
                pass
            elif percentCompleteWorker >= .25 and percentCompleteWorker < .50:
                self.spawnWorkerBarImg = self.spawnWorkerBar1Q
            elif percentCompleteWorker >= .50 and percentCompleteWorker < .75:
                self.spawnWorkerBarImg = self.spawnWorkerBarHalf
            elif percentCompleteWorker >= .75 and percentCompleteWorker < .99:
                self.spawnWorkerBarImg = self.spawnWorkerBar3Q
            else:
                self.spawnWorkerBarImg = self.spawnWorkerBarFull
        # If timer complete and this is not a button call complete action and reset timer
        elif self.spawnWorkerStatus == 0 and not workerButton:
            self.spawnSound.play()
            self.spawnWorkerStatus = -1
            self.spawnWorkerBarImg = self.spawnWorkerBarFull
            self.antWorkerCount += self.spawnCount

    ### Handles logic and timer for Gather Spawn takes Bool whether the call came from a button click
    def spawnGather(self, gatherButton):
        # If the call comes from button and is not running timer and fungus count is above cost start timer
        if gatherButton and self.spawnGatherStatus == -1 and self.hiveFungusCount > const.SPAWNGATHERCOST:
            self.spawnGatherStatus = const.SPAWNGATHERTIME
            self.hiveFungusCount -= const.SPAWNGATHERCOST
            self.spawnGatherBarImg = self.spawnGatherBarEmpty
        # If timer is started and is not finished and this is not a button call decrement timer and update status bar
        elif self.spawnGatherStatus != -1 and self.spawnGatherStatus != 0 and not gatherButton:
            self.spawnGatherStatus -= 1
            percentCompleteGather = abs((float(self.spawnGatherStatus) / float(const.SPAWNGATHERTIME)) - 1)
            if percentCompleteGather < .25:
                pass
            elif percentCompleteGather >= .25 and percentCompleteGather < .50:
                self.spawnGatherBarImg = self.spawnGatherBar1Q
            elif percentCompleteGather >= .50 and percentCompleteGather < .75:
                self.spawnGatherBarImg = self.spawnGatherBarHalf
            elif percentCompleteGather >= .75 and percentCompleteGather < .99:
                self.spawnGatherBarImg = self.spawnGatherBar3Q
            else:
                self.spawnGatherBarImg = self.spawnGatherBarFull
        # If timer complete and this is not a button call complete action and reset timer
        elif self.spawnGatherStatus == 0 and not gatherButton:
            self.spawnSound.play()
            self.spawnGatherStatus = -1
            self.spawnGatherBarImg = self.spawnGatherBarFull
            self.antGatherCount += self.spawnCount

    ### Handles logic and timer for Soldier Spawn takes Bool whether the call came from a button click
    def spawnSoldier(self, soldierButton):
        # If the call comes from button and is not running timer and fungus count is above cost start timer
        if soldierButton and self.spawnSoldierStatus == -1 and self.hiveFungusCount > const.SPAWNSOLDIERCOST:
            self.spawnSoldierStatus = const.SPAWNSOLDIERTIME
            self.hiveFungusCount -= const.SPAWNSOLDIERCOST
            self.spawnSoldierBarImg = self.spawnSoldierBarEmpty
        # If timer is started and is not finished and this is not a button call decrement timer and update status bar
        elif self.spawnSoldierStatus != -1 and self.spawnSoldierStatus != 0 and not soldierButton:
            self.spawnSoldierStatus -= 1
            percentCompleteSoldier = abs((float(self.spawnSoldierStatus) / float(const.SPAWNSOLDIERTIME)) - 1)
            if percentCompleteSoldier < .25:
                pass
            elif percentCompleteSoldier >= .25 and percentCompleteSoldier < .50:
                self.spawnSoldierBarImg = self.spawnSoldierBar1Q
            elif percentCompleteSoldier >= .50 and percentCompleteSoldier < .75:
                self.spawnSoldierBarImg = self.spawnSoldierBarHalf
            elif percentCompleteSoldier >= .75 and percentCompleteSoldier < .99:
                self.spawnSoldierBarImg = self.spawnSoldierBar3Q
            else:
                self.spawnSoldierBarImg = self.spawnSoldierBarFull
        # If timer complete and this is not a button call complete action and reset timer
        elif self.spawnSoldierStatus == 0 and not soldierButton:
            self.spawnSound.play()
            self.spawnSoldierStatus = -1
            self.spawnSoldierBarImg = self.spawnSoldierBarFull
            self.antSoldierCount += self.spawnCount

    ### Handles logic and timer for Princess Spawn takes Bool whether the call came from a button click
    def spawnPrincess(self, princessButton):
        # If the call comes from button and is not running timer and fungus count is above cost start timer
        if princessButton and self.spawnPrincessStatus == -1 and self.hiveFungusCount > const.SPANWPRINCESSCOST:
            self.spawnPrincessStatus = const.SPAWNPRINCESSTIME
            self.hiveFungusCount -= const.SPANWPRINCESSCOST
            self.spawnPrincessBarImg = self.spawnPrincessBarEmpty
        # If timer is started and is not finished and this is not a button call decrement timer and update status bar
        elif self.spawnPrincessStatus != -1 and self.spawnPrincessStatus != 0 and not princessButton:
            self.spawnPrincessStatus -= 1
            percentCompletePrincess = abs((float(self.spawnPrincessStatus) / float(const.SPAWNPRINCESSTIME)) - 1)
            if percentCompletePrincess < .25:
                pass
            elif percentCompletePrincess >= .25 and percentCompletePrincess < .50:
                self.spawnPrincessBarImg = self.spawnPrincessBar1Q
            elif percentCompletePrincess >= .50 and percentCompletePrincess < .75:
                self.spawnPrincessBarImg = self.spawnPrincessBarHalf
            elif percentCompletePrincess >= .75 and percentCompletePrincess < .99:
                self.spawnPrincessBarImg = self.spawnPrincessBar3Q
            else:
                self.spawnPrincessBarImg = self.spawnPrincessBarFull
        # If timer complete and this is not a button call complete action and reset timer
        elif self.spawnPrincessStatus == 0 and not princessButton:
            self.spawnPrincessStatus = -1
            self.gameOver(True)

    ### Handles logic and timer for Upgrade Hive takes Bool whether the call came from a button click
    def upgradeHive(self, upgradeHiveButton):
        # If the call comes from button and is not running timer and leaf count is above cost and if not at max hive level start timer
        if upgradeHiveButton and self.upgradeHiveStatus == -1 and self.hiveLeafCount > self.hiveUpgradeCost and self.hiveLevel != 10:
            self.upgradeHiveStatus = self.hiveUpgradeTime - self.antWorkerCount
            if self.upgradeHiveStatus < 10:
                self.upgradeHiveStatus = 5
            self.hiveLeafCount -= self.hiveUpgradeCost
            self.hiveSideImg = self.hiveSideConstruction
            self.hiveUpgrading = True
        # If timer is started and is not finished and this is not a button call decrement timer
        elif self.upgradeHiveStatus != -1 and self.upgradeHiveStatus != 0 and not upgradeHiveButton:
            self.upgradeHiveStatus -= 1
        # If timer complete and this is not a button call complete action and reset timer
        elif self.upgradeHiveStatus == 0 and not upgradeHiveButton:
            self.hiveUpgradeSound.play()
            self.upgradeHiveStatus = -1
            self.hiveLevel += 1
            self.hiveUpgradeCost += 1000
            self.hiveUpgradeTime += 120
            self.spawnCount += 10
            self.hiveUpgrading = False
            self.setHiveImgs()

    ### Sets side view and top down view of hive images based on current hive level
    def setHiveImgs(self):
        if self.hiveLevel == 2:
            self.hiveImage = self.hiveL2
            self.hiveSideImg = self.hiveSide2
        elif self.hiveLevel == 3:
            self.hiveImage = self.hiveL3
            self.hiveSideImg = self.hiveSide3
        elif self.hiveLevel == 4:
            self.hiveImage = self.hiveL4
            self.hiveSideImg = self.hiveSide4
        elif self.hiveLevel == 5:
            self.hiveImage = self.hiveL5
            self.hiveSideImg = self.hiveSide5
        elif self.hiveLevel == 6:
            self.hiveImage = self.hiveL6
            self.hiveSideImg = self.hiveSide6
        elif self.hiveLevel == 7:
            self.hiveImage = self.hiveL7
            self.hiveSideImg = self.hiveSide7
        elif self.hiveLevel == 8:
            self.hiveImage = self.hiveL8
            self.hiveSideImg = self.hiveSide8
        elif self.hiveLevel == 9:
            self.hiveImage = self.hiveL9
            self.hiveSideImg = self.hiveSide9
        elif self.hiveLevel == 10:
            self.hiveImage = self.hiveL10
            self.hiveSideImg = self.hiveSide10

    ### Controls and resolves combat between enemies and ants
    def combatScreen(self, enemyStrength):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    done = True
            # TODO Remove and replace
            loadImage = pygame.image.load(const.LOADINGSCREEN).convert()
            self.screen.blit(loadImage, self.rect)
            pygame.display.flip()
                    
        return False

        
    
    ### Loading Screen is blit and flipped to display while game assests load
    def loadingScreen(self):
        loadImage = pygame.image.load(const.LOADINGSCREEN).convert()
        self.screen.blit(loadImage, self.rect)
        pygame.display.flip()

    ### StartScreen controls the while loop for the entire Start Screen
    def startScreen(self):
        startImage = pygame.image.load(const.STARTSCREEN).convert()
        startImageStartHigh = pygame.image.load(const.STARTSCREENSTARTHIGH).convert()
        startImageTutorialHigh = pygame.image.load(const.STARTSCREENTUTORIALHIGH).convert()
        startImageExitHigh = pygame.image.load(const.STARTSCREENEXITHIGH).convert()
        done = False
        pygame.mixer.music.play(-1)
        # Main Menu Loop takes in mouse clicks for the buttons
        while not done:            
            # Get Cursor Pos every frame
            pos = pygame.mouse.get_pos()
            # If cursor overlaps a button load correct Highlighted Image
            if const.STARTBUTTONRECT.collidepoint(pos):
                self.screen.blit(startImageStartHigh, self.rect)
            elif const.TUTORIALBUTTONRECT.collidepoint(pos):
                self.screen.blit(startImageTutorialHigh, self.rect)
            elif const.EXITBUTTONRECT.collidepoint(pos):
                self.screen.blit(startImageExitHigh, self.rect)
            else:
                self.screen.blit(startImage, self.rect)
            # Flip Display
            pygame.display.flip()
            # Get event from pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    pygame.quit()
                    sys.exit()
                # If the mouse is clicked check if it was on a button and execute commands if true
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if const.STARTBUTTONRECT.collidepoint(pos):
                        done = True
                    elif const.TUTORIALBUTTONRECT.collidepoint(pos):
                        self.startTutorial()
                        pygame.mixer.music.set_volume(1)
                    elif const.EXITBUTTONRECT.collidepoint(pos):
                        done = True
                        pygame.quit()
                        sys.exit()

    ### Called when user clicks pause in main game 
    def pauseGame(self):
        pauseImage = pygame.image.load(const.PAUSESCREEN).convert_alpha()
        pauseImageResumeHigh = pygame.image.load(const.PAUSESCREENRESUMEHIGH).convert_alpha()
        pauseImageTutorialHigh = pygame.image.load(const.PAUSESCREENTUTORIALHIGH).convert_alpha()
        pauseImageExitHigh = pygame.image.load(const.PAUSESCREENEXITHIGH).convert_alpha()
        done = False
        while not done:            
            # Get Cursor Pos every frame
            pos = pygame.mouse.get_pos()
            # If cursor overlaps a button load correct Highlighted Image
            if const.RESUMEPAUSEBUTTONRECT.collidepoint(pos):
                self.screen.blit(pauseImageResumeHigh, self.rect)
            elif const.TUTORIALPAUSEBUTTONRECT.collidepoint(pos):
                self.screen.blit(pauseImageTutorialHigh, self.rect)
            elif const.EXITPAUSEBUTTONRECT.collidepoint(pos):
                self.screen.blit(pauseImageExitHigh, self.rect)
            else:
                self.screen.blit(pauseImage, self.rect)
            # Flip Display
            pygame.display.flip()
            # Get event from pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    pygame.quit()
                    sys.exit()
                # If the mouse is clicked check if it was on a button and execute commands if true
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if const.RESUMEPAUSEBUTTONRECT.collidepoint(pos):
                        done = True
                    elif const.TUTORIALPAUSEBUTTONRECT.collidepoint(pos):
                        pygame.mixer.music.unpause()
                        self.startTutorial()
                        done = True
                    elif const.EXITPAUSEBUTTONRECT.collidepoint(pos):
                        done = True
                        pygame.quit()
                        sys.exit()
    
    ### Runs the tutorial screens progressing through them on click
    def startTutorial(self):
        pygame.mixer.music.set_volume(.3)
        tutorialScreenOne = pygame.image.load(const.TUTORIALONE).convert()
        tutorialScreenTwo = pygame.image.load(const.TUTORIALTWO).convert()
        tutorialScreenThree = pygame.image.load(const.TUTORIALTHREE).convert()
        tutorialScreenFour = pygame.image.load(const.TUTORIALFOUR).convert()
        tutorialScreenFive = pygame.image.load(const.TUTORIALFIVE).convert()
        tutorialScreenSix = pygame.image.load(const.TUTORIALSIX).convert()
        tutorialScreenSeven = pygame.image.load(const.TUTORIALSEVEN).convert()
        done = False
        stage = 1
        while not done:
            if stage == 7:
                self.screen.blit(tutorialScreenSeven, self.rect)
            elif stage == 6:
                self.screen.blit(tutorialScreenSix, self.rect)
            elif stage == 5:
                self.screen.blit(tutorialScreenFive, self.rect)
            elif stage == 4:
                self.screen.blit(tutorialScreenFour, self.rect)
            elif stage == 3:
                self.screen.blit(tutorialScreenThree, self.rect)
            elif stage == 2:
                self.screen.blit(tutorialScreenTwo, self.rect)
            else:
                self.screen.blit(tutorialScreenOne, self.rect)
            # Flip Display
            pygame.display.flip()
            # Get event from pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    pygame.quit()
                    sys.exit()
                # If the mouse is clicked continue game
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if stage != 7:
                        stage += 1
                    else:
                        done = True
    
    ### Loads and controls Gameover windows Both Win and Lose
    def gameOver(self, isWon):
        done = False
        if isWon:
            wonBackground = pygame.image.load("win_background.png").convert()
            wonStageZero = pygame.image.load("win_zero.png").convert_alpha()
            wonStageOne = pygame.image.load("win_one.png").convert_alpha()
            wonStageTwo = pygame.image.load("win_two.png").convert_alpha()
            wonStageThree = pygame.image.load("win_three.png").convert_alpha()
            wonStageFour = pygame.image.load("win_four.png").convert_alpha()
            wonStageFive = pygame.image.load("win_five.png").convert_alpha()
            wonStageSix = pygame.image.load("win_six.png").convert_alpha()
            wonStageSeven = pygame.image.load("win_seven.png").convert_alpha()
            wonStageEight = pygame.image.load("win_eight.png").convert_alpha()
            wonStageNine = pygame.image.load("win_nine.png").convert_alpha()
            wonStageTen = pygame.image.load("win_ten.png").convert_alpha()
            wonStageEleven = pygame.image.load("win_eleven.png").convert_alpha()
            stage = 0
            clock = pygame.time.Clock()
            frameRate = 30
            frameCount = 0
            nextTickUpdate = 5
            musicTick = 120
            pygame.mixer.music.pause()
            winSound = pygame.mixer.Sound("game_over_win_sound.ogg")
            winSound.play()
            while not done:
                # Get event from pygame
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                        pygame.quit()
                        sys.exit()
                    # If the mouse is clicked continue game
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        done = True
                
                # Update
                if (frameCount == nextTickUpdate):
                    stage += 1
                    stage = stage % 12
                    nextTickUpdate += 5

                if (frameCount == musicTick):
                    winSound.play()
                
                # Draw
                if stage == 11:
                    self.screen.blit(wonBackground, self.rect)
                    self.screen.blit(wonStageEleven, self.rect)
                elif stage == 10:
                    self.screen.blit(wonBackground, self.rect)
                    self.screen.blit(wonStageTen, self.rect)
                elif stage == 9:
                    self.screen.blit(wonBackground, self.rect)
                    self.screen.blit(wonStageNine, self.rect)
                elif stage == 8:
                    self.screen.blit(wonBackground, self.rect)
                    self.screen.blit(wonStageEight, self.rect)
                elif stage == 7:
                    self.screen.blit(wonBackground, self.rect)
                    self.screen.blit(wonStageSeven, self.rect)
                elif stage == 6:
                    self.screen.blit(wonBackground, self.rect)
                    self.screen.blit(wonStageSix, self.rect)
                elif stage == 5:
                    self.screen.blit(wonBackground, self.rect)
                    self.screen.blit(wonStageFive, self.rect)
                elif stage == 4:
                    self.screen.blit(wonBackground, self.rect)
                    self.screen.blit(wonStageFour, self.rect)
                elif stage == 3:
                    self.screen.blit(wonBackground, self.rect)
                    self.screen.blit(wonStageThree, self.rect)
                elif stage == 2:
                    self.screen.blit(wonBackground, self.rect)
                    self.screen.blit(wonStageTwo, self.rect)
                elif stage == 1:
                    self.screen.blit(wonBackground, self.rect)
                    self.screen.blit(wonStageOne, self.rect)
                else:
                    self.screen.blit(wonBackground, self.rect)
                    self.screen.blit(wonStageZero, self.rect)

                # Increment Frames/Ticks
                frameCount += 1
                # Reset frames and seconds every 30 frames to avoid numbers becoming too large
                if (frameCount == 121):
                    frameCount = 1
                    nextTickUpdate = 5
                # Throttle frame rate
                clock.tick(frameRate)
                # Flip Display
                pygame.display.flip()

        else:
            loseBackground = pygame.image.load("lose_background.png").convert()
            loseStageZero = pygame.image.load("lose_zero.png").convert_alpha()
            loseStageOne = pygame.image.load("lose_one.png").convert_alpha()
            loseStageTwo = pygame.image.load("lose_two.png").convert_alpha()
            loseStageThree = pygame.image.load("lose_three.png").convert_alpha()
            loseStageFour = pygame.image.load("lose_four.png").convert_alpha()
            stage = 0
            clock = pygame.time.Clock()
            frameRate = 30
            frameCount = 0
            nextTickUpdate = 10
            musicTick = 120
            pygame.mixer.music.pause()
            loseSound = pygame.mixer.Sound("lose_sound.wav")
            loseSound.play()
            while not done:
                # Get event from pygame
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                        pygame.quit()
                        sys.exit()
                    # If the mouse is clicked continue game
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        done = True
                
                # Update
                if (frameCount == nextTickUpdate):
                    stage += 1
                    stage = stage % 6
                    nextTickUpdate += 10

                if (frameCount == musicTick):
                    loseSound.play()
                
                # Draw
                if stage == 5:
                    self.screen.blit(loseBackground, self.rect)
                elif stage == 4:
                    self.screen.blit(loseBackground, self.rect)
                    self.screen.blit(loseStageFour, self.rect)
                elif stage == 3:
                    self.screen.blit(loseBackground, self.rect)
                    self.screen.blit(loseStageThree, self.rect)
                elif stage == 2:
                    self.screen.blit(loseBackground, self.rect)
                    self.screen.blit(loseStageTwo, self.rect)
                elif stage == 1:
                    self.screen.blit(loseBackground, self.rect)
                    self.screen.blit(loseStageOne, self.rect)
                else:
                    self.screen.blit(loseBackground, self.rect)
                    self.screen.blit(loseStageZero, self.rect)

                # Increment Frames/Ticks
                frameCount += 1
                # Reset frames and seconds every 30 frames to avoid numbers becoming too large
                if (frameCount == 121):
                    frameCount = 1
                    nextTickUpdate = 10
                # Throttle frame rate
                clock.tick(frameRate)
                # Flip Display
                pygame.display.flip()

        # Load Credits
        pygame.mixer.music.unpause()
        pygame.mixer.music.set_volume(.3)
        creditScreenOne = pygame.image.load("credit_one.png").convert()
        creditScreenTwo = pygame.image.load("credit_two.png").convert()
        creditScreenThree = pygame.image.load("credit_three.png").convert()
        done = False
        stage = 1
        while not done:
            if stage == 3:
                self.screen.blit(creditScreenThree, self.rect)
            elif stage == 2:
                self.screen.blit(creditScreenTwo, self.rect)
            else:
                self.screen.blit(creditScreenOne, self.rect)
            # Flip Display
            pygame.display.flip()
            # Get event from pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    pygame.quit()
                    sys.exit()
                # If the mouse is clicked continue game
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if stage != 3:
                        stage += 1
                    else:
                        done = True