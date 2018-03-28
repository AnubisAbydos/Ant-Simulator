import pygame
import Constants as const
import GroundTiles as ground
import TreeNode as tree
import UI as ui
import AntTrail as trail

class Enemy(object):
    def __init__(self, screen):
        self.rect = pygame.Rect(200, 200, const.BADBUG1, const.BADBUG1)
        self.image = pygame.image.load(const.BB1IMAGE).convert_alpha()
    def draw(self):
    #Draw everything in drawingList    