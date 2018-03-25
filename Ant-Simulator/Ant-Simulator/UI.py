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
        self.hiveSideImg = pygame.image.load(const.HIVESIDE1).convert_alpha()
        self.upgradeHiveTime = 120
        self.spawnWorkerTile = pygame.image.load(const.SPAWNWORKERTILE).convert_alpha()
        self.spawnGatherTile = pygame.image.load(const.SPAWNGATHERTILE).convert_alpha()
        self.spawnSoldierTile = pygame.image.load(const.SPAWNSOLDIERTILE).convert_alpha()
        self.spawnPrincessTile = pygame.image.load(const.SPAWNPRINCESSTILE).convert_alpha()
        self.highlightedButtonImg = pygame.image.load(const.BLANKIMG).convert_alpha()
        # Font
        self.topBarTextFont = pygame.font.Font("pixelplay.ttf", 23)
        self.bottomRightTextFont = pygame.font.Font("pixelplay.ttf", 21)

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
        self.screen.blit(self.topBarTextFont.render(str(self.antWorkerCount), True, const.WHITE), const.WORKERTEXTBOX)
        self.screen.blit(self.topBarTextFont.render(str(self.antGatherCount), True, const.WHITE), const.GATHERTEXTBOX)
        self.screen.blit(self.topBarTextFont.render(str(self.antSoldierCount), True, const.WHITE), const.SOLDIERTEXTBOX)
        self.screen.blit(self.topBarTextFont.render(str('{:06d}'.format(self.hiveFungusCount)), True, const.WHITE), const.FUNGUSTEXTBOX)
        self.screen.blit(self.topBarTextFont.render(str('{:06d}'.format(self.hiveLeafCount)), True, const.WHITE), const.LEAFTEXTBOX)

    def getHarvesterCount(self):
        return self.antGatherCount

    def spawnWorker(self, workerButton):
        if workerButton and self.spawnWorkerStatus == -1 and self.hiveFungusCount > const.SPAWNWORKERCOST:
            self.spawnWorkerStatus = const.SPAWNWORKERTIME
            self.hiveFungusCount -= const.SPAWNWORKERCOST
            self.spawnWorkerBarImg = pygame.image.load(const.SPAWNWORKERBAREMPTY).convert_alpha()
        elif self.spawnWorkerStatus != -1 and self.spawnWorkerStatus != 0:
            self.spawnWorkerStatus -= 1
            percentComplete = abs((float(self.spawnWorkerStatus) / float(const.SPAWNWORKERTIME)) - 1)
            if percentComplete < .25:
                pass
            elif percentComplete >= .25 and percentComplete < .50:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNWORKERBAR1Q).convert_alpha()
            elif percentComplete >= .50 and percentComplete < .75:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNWORKERBARHALF).convert_alpha()
            elif percentComplete >= .75 and percentComplete < .99:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNWORKERBAR3Q).convert_alpha()
            else:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNWORKERBARFULL).convert_alpha()
        elif self.spawnWorkerStatus == 0:
            self.spawnWorkerStatus = -1
            self.spawnWorkerBarImg = pygame.image.load(const.SPAWNWORKERBARFULL).convert_alpha()
            self.antWorkerCount += self.spawnCount

    def spawnGather(self, gatherButton):
        if gatherButton and self.spawnGatherStatus == -1 and self.hiveFungusCount > const.SPAWNGATHERCOST:
            self.spawnGatherStatus = const.SPAWNGATHERTIME
            self.hiveFungusCount -= const.SPAWNGATHERCOST
            self.spawnGatherBarImg = pygame.image.load(const.SPAWNGATHERBAREMPTY).convert_alpha()
        elif self.spawnGatherStatus != -1 and self.spawnGatherStatus != 0:
            self.spawnGatherStatus -= 1
            percentComplete = abs((float(self.spawnGatherStatus) / float(const.SPAWNGATHERTIME)) - 1)
            if percentComplete < .25:
                pass
            elif percentComplete >= .25 and percentComplete < .50:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNGATHERBAR1Q).convert_alpha()
            elif percentComplete >= .50 and percentComplete < .75:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNGATHERBARHALF).convert_alpha()
            elif percentComplete >= .75 and percentComplete < .99:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNGATHERBAR3Q).convert_alpha()
            else:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNGATHERBARFULL).convert_alpha()
        elif self.spawnGatherStatus == 0:
            self.spawnGatherStatus = -1
            self.spawnGatherBarImg = pygame.image.load(const.SPAWNGATHERBARFULL).convert_alpha()
            self.antGatherCount += self.spawnCount

    def spawnSoldier(self, soldierButton):
        if soldierButton and self.spawnSoldierStatus == -1 and self.hiveFungusCount > const.SPAWNSOLDIERCOST:
            self.spawnSoldierStatus = const.SPAWNSOLDIERTIME
            self.hiveFungusCount -= const.SPAWNSOLDIERCOST
            self.spawnSoldierBarImg = pygame.image.load(const.SPAWNSOLDIERBAREMPTY).convert_alpha()
        elif self.spawnSoldierStatus != -1 and self.spawnSoldierStatus != 0:
            self.spawnSoldierStatus -= 1
            percentComplete = abs((float(self.spawnSoldierStatus) / float(const.SPAWNSOLDIERTIME)) - 1)
            if percentComplete < .25:
                pass
            elif percentComplete >= .25 and percentComplete < .50:
                self.spawnSoldierBarImg = pygame.image.load(const.SPAWNSOLDIERBAR1Q).convert_alpha()
            elif percentComplete >= .50 and percentComplete < .75:
                self.spawnSoldierBarImg = pygame.image.load(const.SPAWNSOLDIERBARHALF).convert_alpha()
            elif percentComplete >= .75 and percentComplete < .99:
                self.spawnSoldierBarImg = pygame.image.load(const.SPAWNSOLDIERBAR3Q).convert_alpha()
            else:
                self.spawnSoldierBarImg = pygame.image.load(const.SPAWNSOLDIERBARFULL).convert_alpha()
        elif self.spawnSoldierStatus == 0:
            self.spawnSoldierStatus = -1
            self.spawnSoldierBarImg = pygame.image.load(const.SPAWNSOLDIERBARFULL).convert_alpha()
            self.antSoldierCount += self.spawnCount

    def spawnPrincess(self, princessButton):
        if princessButton and self.spawnPrincessStatus == -1 and self.hiveFungusCount > const.SPANWPRINCESSCOST:
            self.spawnPrincessStatus = const.SPAWNPRINCESSTIME
            self.hiveFungusCount -= const.SPANWPRINCESSCOST
            self.spawnPrincessBarImg = pygame.image.load(const.SPAWNPRINCESSBAREMPTY).convert_alpha()
        elif self.spawnPrincessStatus != -1 and self.spawnPrincessStatus != 0:
            self.spawnPrincessStatus -= 1
            percentComplete = abs((float(self.spawnPrincessStatus) / float(const.SPAWNPRINCESSTIME)) - 1)
            if percentComplete < .25:
                pass
            elif percentComplete >= .25 and percentComplete < .50:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNPRINCESSBAR1Q).convert_alpha()
            elif percentComplete >= .50 and percentComplete < .75:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNPRINCESSBARHALF).convert_alpha()
            elif percentComplete >= .75 and percentComplete < .99:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNPRINCESSBAR3Q).convert_alpha()
            else:
                self.spawnWorkerBarImg = pygame.image.load(const.SPAWNPRINCESSBARFULL).convert_alpha()
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
