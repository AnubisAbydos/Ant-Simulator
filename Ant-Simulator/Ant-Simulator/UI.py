import pygame
import time
import Constants as const

# UI contains the User Interface elements and updates status bars
class UI (object):
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, const.WIDTH, const.HEIGHT)
        self.image = pygame.image.load("basic_ui_test.png").convert_alpha()
        self.hiveImage = pygame.image.load("hive_10.png").convert_alpha()
        self.hiveRect = pygame.Rect(700,700,100,100)
        self.loadImage = pygame.image.load(const.LOADINGSCREEN).convert()
        #self.startImage = pygame.image.load("start_screen.png").convert()

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.hiveImage, self.hiveRect)

    def loadingScreen(self):
        self.screen.blit(self.loadImage, self.rect)

    def startScreen(self):
        #TODO add while loop to take in commands
        pygame.mixer.music.load("start_menu_tune.wav")
        pygame.mixer.music.play()
        #self.screen.blit(self.startImage, self.rect)
        pygame.display.flip()
        time.sleep(10)
        pygame.mixer.music.stop()