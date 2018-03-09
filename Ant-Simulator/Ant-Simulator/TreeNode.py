import pygame
import random
import Constants as const

# Tree Node contains sprite build for Trees on map
class TreeNode (object):
    def __init__(self):
        self.image = pygame.image.load("tree.png")
        self.rect = pygame.Rect(random.randint(40,700), random.randint(40,700), const.PIXELSIZE * 4, const.PIXELSIZE * 4)
        self.treeQuality = random.randint(0,3)

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def collide(self, givenRect):
        if(self.rect.colliderect(givenRect)):
            return True
        return False

class TreeNodesList (object):
    def __init__ (self, screen):
        self.newTree = TreeNode()
        self.list = []
        self.screen = screen
        for i in xrange(30):
            self.list.append(self.createNewTree())

    def createNewTree(self):
        isCollide = False
        self.newTree = TreeNode()
        for tree in self.list:
            isCollide = tree.collide(self.newTree.rect)
            if isCollide == True:
                self.createNewTree()
        if isCollide == False:
            return self.newTree
    
    def draw(self):
        for tree in self.list:
            tree.draw(self.screen)

    def update(self):
        pass