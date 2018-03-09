import pygame
import Constants as const

# UI contains the User Interface elements and updates status bars
class UI (object):
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, const.WIDTH, const.HEIGHT)
        self.image = pygame.image.load("basic_ui_test.png")

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.image, self.rect)