import pygame
import time
import Constants as const

#sys is used to exit python when exit button is clicked
import sys


# UI contains the User Interface elements and updates status bars
class UI (object):
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, const.WIDTH, const.HEIGHT)
        self.image = pygame.image.load(const.UITEMPLATE).convert_alpha()
        self.hiveImage = pygame.image.load(const.HIVEL10).convert_alpha()
        #TODO Update Hive PNGs to be full screen right corner at 0,0 then remove hiveRect
        self.hiveRect = pygame.Rect(700,700,100,100)

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.hiveImage, self.hiveRect)

    #Loading Screen is blit and flipped to display while game assests load
    def loadingScreen(self):
        loadImage = pygame.image.load(const.LOADINGSCREEN).convert()
        self.screen.blit(loadImage, self.rect)
        pygame.display.flip()

    #startScreen controls the while loop for the entire Start Screen
    def startScreen(self):
        startImage = pygame.image.load(const.STARTSCREEN).convert()
        startImageStartHigh = pygame.image.load(const.STARTSCREENSTARTHIGH).convert()
        startImageTutorialHigh = pygame.image.load(const.STARTSCREENTUTORIALHIGH).convert()
        startImageExitHigh = pygame.image.load(const.STARTSCREENEXITHIGH).convert()
        done = False
        pygame.mixer.music.load("start_menu_tune.wav")
        pygame.mixer.music.play(-1)
        #Main Menu Loop takes in mouse clicks for the buttons
        while not done:            
            #Get Cursor Pos every frame
            pos = pygame.mouse.get_pos()
            #If cursor overlaps a button load correct Highlighted Image
            if const.STARTBUTTONRECT.collidepoint(pos):
                self.screen.blit(startImageStartHigh, self.rect)
            elif const.TUTORIALBUTTONRECT.collidepoint(pos):
                self.screen.blit(startImageTutorialHigh, self.rect)
            elif const.EXITBUTTONRECT.collidepoint(pos):
                self.screen.blit(startImageExitHigh, self.rect)
            else:
                self.screen.blit(startImage, self.rect)
            #Flip Display
            pygame.display.flip()
            #Get event from pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    pygame.quit()
                    sys.exit()
                #If the mouse is clicked check if it was on a button and execute commands if true
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if const.STARTBUTTONRECT.collidepoint(pos):
                        done = True
                        pygame.mixer.music.stop()
                    elif const.TUTORIALBUTTONRECT.collidepoint(pos):
                        done = True
                        self.startTutorial()
                    elif const.EXITBUTTONRECT.collidepoint(pos):
                        done = True
                        pygame.quit()
                        sys.exit()

    #TODO Build tutorial loop with pictures
    def startTutorial(self):
        pass
