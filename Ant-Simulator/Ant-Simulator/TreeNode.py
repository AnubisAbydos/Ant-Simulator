import pygame
import random
import Constants as const

# Tree Node contains sprite build for Trees on map
class TreeNode (object):
    def __init__(self):
        self.image = pygame.image.load("tree.png").convert()
        self.rect = pygame.Rect(random.randint(40,700), random.randint(40,700), const.PIXELSIZE * 4, const.PIXELSIZE * 4)
        self.treeQuality = random.randint(0,3)
        self.leafQuantity = random.randint(const.MINLEAVES, const.MAXLEAVES)

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
        self.newTree = None
        self.list = []
        self.screen = screen
        for i in xrange(const.NUMBEROFTREES):
            #A bug was present previous to the while loop that was adding NoneType objects to the list.
            #The while loop removes this bug.
            while self.newTree == None:
                self.newTree = self.createNewTree()
            self.list.append(self.newTree)
            self.newTree = None

    def createNewTree(self):
        isCollide = False
        self.newTree = TreeNode()
        for tree in self.list:
            isCollide = tree.collide(self.newTree.rect)
            if isCollide == True:
                self.createNewTree()
        if (isCollide == False):
            return self.newTree
    
    def draw(self):
        for tree in self.list:
            tree.draw(self.screen)

    def update(self):
        for tree in self.list:
            tree.update()