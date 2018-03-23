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
        self.image = pygame.image.load(const.UITEMPLATE).convert_alpha()
        # TODO Update Hive PNGs to be full screen right corner at 0,0 then remove hiveRect
        self.hiveRect = pygame.Rect(700,700,100,100)
        # Variables used for state of game
        self.antWorkerCount = 10
        self.antGatherCount = 10
        self.antSoldierCount = 0
        self.hiveLeafCount = 0
        self.hiveFungusCount = 100
        self.hiveLevel = 1
        self.spawnCount = 10
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
        self.hiveImage = pygame.image.load(const.HIVEL1).convert_alpha()

    ### Takes in all state variables from Game to determine updates
    def update(self, treeReached, treeFull, treeQuality, workerButton,
              gatherButton, soldierButton, princessButton, upgradeHiveButton):
        self.hiveFungusCount += (self.hiveLevel * 10)
        if treeReached and treeFull:
            self.hiveLeafCount += self.antGatherCount * treeQuality
        self.spawnWorker(workerButton)
        self.spawnGather(gatherButton)
        self.spawnSoldier(soldierButton)
        self.spawnPrincess(princessButton)
        self.upgradeHive(upgradeHiveButton)

    def draw(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.hiveImage, self.hiveRect)
        self.screen.blit(self.spawnWorkerBarImg, self.rect)
        self.screen.blit(self.spawnGatherBarImg, self.rect)
        self.screen.blit(self.spawnSoldierBarImg, self.rect)
        self.screen.blit(self.spawnPrincessBarImg, self.rect)
        
        #TODO REMOVE THIS
        #DEBUG CODE
        print(self.hiveLeafCount, self.hiveFungusCount, self.antGatherCount, self.antSoldierCount, self.antWorkerCount)

    def getHarvesterCount(self):
        return self.antGatherCount

    def spawnWorker(self, workerButton):
        if workerButton and self.spawnWorkerStatus == -1 and self.hiveFungusCount > const.SPAWNWORKERCOST:
            self.spawnWorkerStatus = const.SPAWNWORKERTIME
            self.hiveFungusCount -= const.SPAWNWORKERCOST
            self.spawnWorkerBarImg = pygame.image.load(const.SPAWNWORKERBAREMPTY)
        elif self.spawnWorkerStatus != -1 and self.spawnWorkerStatus != 0:
            self.spawnWorkerStatus -= 1
            percentComplete = abs((self.spawnWorkerStatus / const.SPAWNWORKERTIME) - 1)
            if percentComplete < .25:
                pass
            elif percentComplete >= .25 and percentComplete < .50:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNWORKERBAR1Q)
            elif percentComplete >= .50 and percentComplete < .75:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNWORKERBARHALF)
            elif percentComplete >= .75 and percentComplete < .99:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNWORKERBAR3Q)
            else:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNWORKERBARFULL)
        elif self.spawnWorkerStatus == 0:
            self.spawnWorkerStatus = -1
            self.spawnWorkerBarImg = pygame.image.load(const.SPAWNWORKERBARFULL)
            self.antWorkerCount += self.spawnCount

    def spawnGather(self, gatherButton):
        if gatherButton and self.spawnGatherStatus == -1 and self.hiveFungusCount > const.SPAWNGATHERCOST:
            self.spawnGatherStatus = const.SPAWNGATHERTIME
            self.hiveFungusCount -= const.SPAWNGATHERCOST
            self.spawnGatherBarImg = pygame.image.load(const.SPAWNGATHERBAREMPTY)
        elif self.spawnGatherStatus != -1 and self.spawnGatherStatus != 0:
            self.spawnGatherStatus -= 1
            percentComplete = abs((self.spawnGatherStatus / const.SPAWNGATHERTIME) - 1)
            if percentComplete < .25:
                pass
            elif percentComplete >= .25 and percentComplete < .50:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNGATHERBAR1Q)
            elif percentComplete >= .50 and percentComplete < .75:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNGATHERBARHALF)
            elif percentComplete >= .75 and percentComplete < .99:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNGATHERBAR3Q)
            else:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNGATHERBARFULL)
        elif self.spawnGatherStatus == 0:
            self.spawnGatherStatus = -1
            self.spawnGatherBarImg = pygame.image.load(const.SPAWNGATHERBARFULL)
            self.antGatherCount += self.spawnCount

    def spawnSoldier(self, soldierButton):
        if soldierButton and self.spawnSoldierStatus == -1 and self.hiveFungusCount > const.SPAWNSOLDIERCOST:
            self.spawnSoldierStatus = const.SPAWNSOLDIERTIME
            self.hiveFungusCount -= const.SPAWNSOLDIERCOST
            self.spawnSoldierBarImg = pygame.image.load(const.SPAWNSOLDIERBAREMPTY)
        elif self.spawnSoldierStatus != -1 and self.spawnSoldierStatus != 0:
            self.spawnSoldierStatus -= 1
            percentComplete = abs((self.spawnSoldierStatus / const.SPAWNSOLDIERTIME) - 1)
            if percentComplete < .25:
                pass
            elif percentComplete >= .25 and percentComplete < .50:
                self.spawnSoldierBarImg = pygame.image.load(const.SPAWNSOLDIERBAR1Q)
            elif percentComplete >= .50 and percentComplete < .75:
                self.spawnSoldierBarImg = pygame.image.load(const.SPAWNSOLDIERBARHALF)
            elif percentComplete >= .75 and percentComplete < .99:
                self.spawnSoldierBarImg = pygame.image.load(const.SPAWNSOLDIERBAR3Q)
            else:
                self.spawnSoldierBarImg = pygame.image.load(const.SPAWNSOLDIERBARFULL)
        elif self.spawnSoldierStatus == 0:
            self.spawnSoldierStatus = -1
            self.spawnSoldierBarImg = pygame.image.load(const.SPAWNSOLDIERBARFULL)
            self.antSoldierCount += self.spawnCount

    def spawnPrincess(self, princessButton):
        if princessButton and self.spawnPrincessStatus == -1 and self.hiveFungusCount > const.SPANWPRINCESSCOST:
            self.spawnPrincessStatus = const.SPAWNPRINCESSTIME
            self.hiveFungusCount -= const.SPANWPRINCESSCOST
            self.spawnPrincessBarImg = pygame.image.load(const.SPAWNPRINCESSBAREMPTY)
        elif self.spawnPrincessStatus != -1 and self.spawnPrincessStatus != 0:
            self.spawnPrincessStatus -= 1
            percentComplete = abs((self.spawnPrincessStatus / const.SPAWNPRINCESSTIME) - 1)
            if percentComplete < .25:
                pass
            elif percentComplete >= .25 and percentComplete < .50:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNPRINCESSBAR1Q)
            elif percentComplete >= .50 and percentComplete < .75:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNPRINCESSBARHALF)
            elif percentComplete >= .75 and percentComplete < .99:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNPRINCESSBAR3Q)
            else:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNPRINCESSBARFULL)
        elif self.spawnWorkerStatus == 0:
            # TODO Add win game code
            pass

    def upgradeHive(self, upgradeHiveButton):
        # TODO Add the Upgrade Functionality
        pass
    
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
        pygame.mixer.music.load("start_menu_tune.wav")
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
            buttonClick = pygame.mixer.Sound("grass1.ogg")
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
                        pygame.mixer.music.stop()
                    elif const.TUTORIALBUTTONRECT.collidepoint(pos):
                        buttonClick.play()
                        #done = True
                        #self.startTutorial()
                    elif const.EXITBUTTONRECT.collidepoint(pos):
                        done = True
                        pygame.quit()
                        sys.exit()

    # TODO Build tutorial loop with pictures
    def startTutorial(self):
        pass
