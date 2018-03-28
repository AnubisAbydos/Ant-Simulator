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
        self.hiveRect = pygame.Rect(700,700,100,100)

        # Variables used for state of game
        self.antWorkerCount = 10
        self.antGatherCount = 10
        self.antSoldierCount = 0
        self.hiveLeafCount = 100000
        self.hiveFungusCount = 100
        self.hiveLevel = 1
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
        self.highlightedButtonImg = pygame.image.load(const.BLANKIMG).convert_alpha()
        # Font
        self.textFont = pygame.font.Font("pixelplay.ttf", 23)

    ### Takes in all state variables from Game to determine updates
    def update(self, treeReached, treeFull, treeQuality):
        self.hiveFungusCount += (self.hiveLevel * 10)
        if treeReached and treeFull:
            self.hiveLeafCount += self.antGatherCount * treeQuality
        self.spawnWorker(False)
        self.spawnGather(False)
        self.spawnSoldier(False)
        self.spawnPrincess(False)
        self.upgradeHive(False)

    def processMousePos(self, pos):
        if const.STARTTRAILRECT.collidepoint(pos):
            self.highlightedButtonImg = pygame.image.load(const.SETDESTBUTTONHIGH).convert_alpha()
        elif const.ENDTRAILRECT.collidepoint(pos):
            self.highlightedButtonImg = pygame.image.load(const.BACKTOHIVEBUTTONHIGH).convert_alpha()
        elif const.SPAWNWORKERSBUTTONRECT.collidepoint(pos):
            self.highlightedButtonImg = pygame.image.load(const.WORKERBUTTONHIGH).convert_alpha()
        elif const.SPAWNGATHERBUTTONRECT.collidepoint(pos):
            self.highlightedButtonImg = pygame.image.load(const.GATHERBUTTONHIGH).convert_alpha()
        elif const.SPAWNSOLDIERBUTTONRECT.collidepoint(pos):
            self.highlightedButtonImg = pygame.image.load(const.SOLDIERBUTTONHIGH).convert_alpha()
        elif const.SPAWNPRINCESSBUTTONRECT.collidepoint(pos):
            self.highlightedButtonImg = pygame.image.load(const.PRINCESSBUTTONHIGH).convert_alpha()
        elif const.UPGRADEHIVEBUTTONRECT.collidepoint(pos):
            self.highlightedButtonImg = pygame.image.load(const.UPGRADEHIVEHIGH).convert_alpha()
        else:
            self.highlightedButtonImg = pygame.image.load(const.BLANKIMG).convert_alpha()

    def draw(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.hiveImage, self.hiveRect)
        self.screen.blit(self.hiveSideImg, self.rect)
        self.screen.blit(self.highlightedButtonImg, self.rect)
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
        self.screen.blit(self.textFont.render(str(self.antWorkerCount), True, const.WHITE), const.WORKERTEXTBOX)
        self.screen.blit(self.textFont.render(str(self.antGatherCount), True, const.WHITE), const.GATHERTEXTBOX)
        self.screen.blit(self.textFont.render(str(self.antSoldierCount), True, const.WHITE), const.SOLDIERTEXTBOX)
        self.screen.blit(self.textFont.render(str('{:06d}'.format(self.hiveFungusCount)), True, const.WHITE), const.FUNGUSTEXTBOX)
        self.screen.blit(self.textFont.render(str('{:06d}'.format(self.hiveLeafCount)), True, const.WHITE), const.LEAFTEXTBOX)
        if self.hiveUpgrading:
            time = self.upgradeHiveStatus
            sec = time % 60
            min = time / 60
            self.screen.blit(self.textFont.render(str('%02d:%02d' % (min, sec)), True, const.BLACK), const.HIVEUPGRADETIMEBOX)

    def getHarvesterCount(self):
        return self.antGatherCount

    def spawnWorker(self, workerButton):
        if workerButton and self.spawnWorkerStatus == -1 and self.hiveFungusCount > const.SPAWNWORKERCOST:
            self.spawnWorkerStatus = const.SPAWNWORKERTIME
            self.hiveFungusCount -= const.SPAWNWORKERCOST
            self.spawnWorkerBarImg = pygame.image.load(const.SPAWNWORKERBAREMPTY).convert_alpha()
        elif self.spawnWorkerStatus != -1 and self.spawnWorkerStatus != 0 and not workerButton:
            self.spawnWorkerStatus -= 1
            percentCompleteWorker = abs((float(self.spawnWorkerStatus) / float(const.SPAWNWORKERTIME)) - 1)
            if percentCompleteWorker < .25:
                pass
            elif percentCompleteWorker >= .25 and percentCompleteWorker < .50:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNWORKERBAR1Q).convert_alpha()
            elif percentCompleteWorker >= .50 and percentCompleteWorker < .75:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNWORKERBARHALF).convert_alpha()
            elif percentCompleteWorker >= .75 and percentCompleteWorker < .99:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNWORKERBAR3Q).convert_alpha()
            else:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNWORKERBARFULL).convert_alpha()
        elif self.spawnWorkerStatus == 0 and not workerButton:
            self.spawnWorkerStatus = -1
            self.spawnWorkerBarImg = pygame.image.load(const.SPAWNWORKERBARFULL).convert_alpha()
            self.antWorkerCount += self.spawnCount

    def spawnGather(self, gatherButton):
        if gatherButton and self.spawnGatherStatus == -1 and self.hiveFungusCount > const.SPAWNGATHERCOST:
            self.spawnGatherStatus = const.SPAWNGATHERTIME
            self.hiveFungusCount -= const.SPAWNGATHERCOST
            self.spawnGatherBarImg = pygame.image.load(const.SPAWNGATHERBAREMPTY).convert_alpha()
        elif self.spawnGatherStatus != -1 and self.spawnGatherStatus != 0 and not gatherButton:
            self.spawnGatherStatus -= 1
            percentCompleteGather = abs((float(self.spawnGatherStatus) / float(const.SPAWNGATHERTIME)) - 1)
            if percentCompleteGather < .25:
                pass
            elif percentCompleteGather >= .25 and percentCompleteGather < .50:
                self.spawnGatherBarImg = pygame.image.load(const.SPAWNGATHERBAR1Q).convert_alpha()
            elif percentCompleteGather >= .50 and percentCompleteGather < .75:
                self.spawnGatherBarImg = pygame.image.load(const.SPAWNGATHERBARHALF).convert_alpha()
            elif percentCompleteGather >= .75 and percentCompleteGather < .99:
                self.spawnGatherBarImg = pygame.image.load(const.SPAWNGATHERBAR3Q).convert_alpha()
            else:
                self.spawnGatherBarImg = pygame.image.load(const.SPAWNGATHERBARFULL).convert_alpha()
        elif self.spawnGatherStatus == 0 and not gatherButton:
            self.spawnGatherStatus = -1
            self.spawnGatherBarImg = pygame.image.load(const.SPAWNGATHERBARFULL).convert_alpha()
            self.antGatherCount += self.spawnCount

    def spawnSoldier(self, soldierButton):
        if soldierButton and self.spawnSoldierStatus == -1 and self.hiveFungusCount > const.SPAWNSOLDIERCOST:
            self.spawnSoldierStatus = const.SPAWNSOLDIERTIME
            self.hiveFungusCount -= const.SPAWNSOLDIERCOST
            self.spawnSoldierBarImg = pygame.image.load(const.SPAWNSOLDIERBAREMPTY).convert_alpha()
        elif self.spawnSoldierStatus != -1 and self.spawnSoldierStatus != 0 and not soldierButton:
            self.spawnSoldierStatus -= 1
            percentCompleteSoldier = abs((float(self.spawnSoldierStatus) / float(const.SPAWNSOLDIERTIME)) - 1)
            if percentCompleteSoldier < .25:
                pass
            elif percentCompleteSoldier >= .25 and percentCompleteSoldier < .50:
                self.spawnSoldierBarImg = pygame.image.load(const.SPAWNSOLDIERBAR1Q).convert_alpha()
            elif percentCompleteSoldier >= .50 and percentCompleteSoldier < .75:
                self.spawnSoldierBarImg = pygame.image.load(const.SPAWNSOLDIERBARHALF).convert_alpha()
            elif percentCompleteSoldier >= .75 and percentCompleteSoldier < .99:
                self.spawnSoldierBarImg = pygame.image.load(const.SPAWNSOLDIERBAR3Q).convert_alpha()
            else:
                self.spawnSoldierBarImg = pygame.image.load(const.SPAWNSOLDIERBARFULL).convert_alpha()
        elif self.spawnSoldierStatus == 0 and not soldierButton:
            self.spawnSoldierStatus = -1
            self.spawnSoldierBarImg = pygame.image.load(const.SPAWNSOLDIERBARFULL).convert_alpha()
            self.antSoldierCount += self.spawnCount

    def spawnPrincess(self, princessButton):
        if princessButton and self.spawnPrincessStatus == -1 and self.hiveFungusCount > const.SPANWPRINCESSCOST:
            self.spawnPrincessStatus = const.SPAWNPRINCESSTIME
            self.hiveFungusCount -= const.SPANWPRINCESSCOST
            self.spawnPrincessBarImg = pygame.image.load(const.SPAWNPRINCESSBAREMPTY).convert_alpha()
        elif self.spawnPrincessStatus != -1 and self.spawnPrincessStatus != 0 and not princessButton:
            self.spawnPrincessStatus -= 1
            percentCompletePrincess = abs((float(self.spawnPrincessStatus) / float(const.SPAWNPRINCESSTIME)) - 1)
            if percentCompletePrincess < .25:
                pass
            elif percentCompletePrincess >= .25 and percentCompletePrincess < .50:
                self.spawnPrincessBarImg = pygame.image.load(const.SPAWNPRINCESSBAR1Q).convert_alpha()
            elif percentCompletePrincess >= .50 and percentCompletePrincess < .75:
                self.spawnPrincessBarImg = pygame.image.load(const.SPAWNPRINCESSBARHALF).convert_alpha()
            elif percentCompletePrincess >= .75 and percentCompletePrincess < .99:
                self.spawnPrincessBarImg = pygame.image.load(const.SPAWNPRINCESSBAR3Q).convert_alpha()
            else:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNPRINCESSBARFULL).convert_alpha()
        elif self.spawnPrincessStatus == 0 and not princessButton:
            # TODO Add win game code
            pass

    def upgradeHive(self, upgradeHiveButton):
        if upgradeHiveButton and self.upgradeHiveStatus == -1 and self.hiveLeafCount > self.hiveUpgradeCost and self.hiveLevel != 10:
            self.upgradeHiveStatus = self.hiveUpgradeTime - self.antWorkerCount
            if self.upgradeHiveStatus < 10:
                self.upgradeHiveStatus = 10
            self.hiveLeafCount -= self.hiveUpgradeCost
            self.hiveSideImg = pygame.image.load(const.HIVESIDECONSTRUCTION).convert_alpha()
            self.hiveUpgrading = True
        elif self.upgradeHiveStatus != -1 and self.upgradeHiveStatus != 0 and not upgradeHiveButton:
            self.upgradeHiveStatus -= 1
        elif self.upgradeHiveStatus == 0 and not upgradeHiveButton:
            self.upgradeHiveStatus = -1
            self.hiveLevel += 1
            self.hiveUpgradeCost += 1000
            self.hiveUpgradeTime += 120
            self.spawnCount += 10
            self.hiveUpgrading = False
            self.setHiveImgs()

    def setHiveImgs(self):
        if self.hiveLevel == 2:
            self.hiveImage = pygame.image.load(const.HIVEL2)
            self.hiveSideImg = pygame.image.load(const.HIVESIDE2)
        elif self.hiveLevel == 3:
            self.hiveImage = pygame.image.load(const.HIVEL3)
            self.hiveSideImg = pygame.image.load(const.HIVESIDE3)
        elif self.hiveLevel == 4:
            self.hiveImage = pygame.image.load(const.HIVEL4)
            self.hiveSideImg = pygame.image.load(const.HIVESIDE4)
        elif self.hiveLevel == 5:
            self.hiveImage = pygame.image.load(const.HIVEL5)
            self.hiveSideImg = pygame.image.load(const.HIVESIDE5)
        elif self.hiveLevel == 6:
            self.hiveImage = pygame.image.load(const.HIVEL6)
            self.hiveSideImg = pygame.image.load(const.HIVESIDE6)
        elif self.hiveLevel == 7:
            self.hiveImage = pygame.image.load(const.HIVEL7)
            self.hiveSideImg = pygame.image.load(const.HIVESIDE7)
        elif self.hiveLevel == 8:
            self.hiveImage = pygame.image.load(const.HIVEL8)
            self.hiveSideImg = pygame.image.load(const.HIVESIDE8)
        elif self.hiveLevel == 9:
            self.hiveImage = pygame.image.load(const.HIVEL9)
            self.hiveSideImg = pygame.image.load(const.HIVESIDE9)
        elif self.hiveLevel == 10:
            self.hiveImage = pygame.image.load(const.HIVEL10)
            self.hiveSideImg = pygame.image.load(const.HIVESIDE10)

    
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
