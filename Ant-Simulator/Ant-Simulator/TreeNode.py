import pygame
import random
import Constants as const

# Tree Node contains sprite build for Trees on map
class TreeNode (object):
    def __init__(self):
        self.rect = pygame.Rect(random.randint(40,700), random.randint(40,700), const.TREEBASESIZE, const.TREEBASESIZE)
        self.treeQuality = random.randint(0,3)
        self.leafQuantity = random.randint(const.MINLEAVES, const.MAXLEAVES)
        self.animationState = random.randint(0,2)
        self.image = None
        self.setStateImage()

    def update(self):
        if (random.randint(1,100) < const.PERCENTTOCHANGESTATE):
            self.treeQuality += 1
            self.treeQuality = self.treeQuality % 4
        self.animationState += 1
        self.animationState = self.animationState % 3
        self.setStateImage()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def collide(self, givenRect):
        if(self.rect.colliderect(givenRect)):
            return True
        return False

    def setStateImage(self):
        if self.treeQuality == 0:
            if self.animationState == 0:
                self.image = pygame.image.load(const.BLACK_S1).convert()
            if self.animationState == 1:
                self.image = pygame.image.load(const.BLACK_S2).convert()
            if self.animationState == 2:
                self.image = pygame.image.load(const.BLACK_S3).convert()
        elif self.treeQuality == 1:
            if self.animationState == 0:
                self.image = pygame.image.load(const.ORANGE_S1).convert()
            if self.animationState == 1:
                self.image = pygame.image.load(const.ORANGE_S2).convert()
            if self.animationState == 2:
                self.image = pygame.image.load(const.ORANGE_S3).convert()
        elif self.treeQuality == 2:
            if self.animationState == 0:
                self.image = pygame.image.load(const.YELLOW_S1).convert()
            if self.animationState == 1:
                self.image = pygame.image.load(const.YELLOW_S2).convert()
            if self.animationState == 2:
                self.image = pygame.image.load(const.YELLOW_S3).convert()
        elif self.treeQuality == 3:
            if self.animationState == 0:
                self.image = pygame.image.load(const.GREEN_S1).convert()
            if self.animationState == 1:
                self.image = pygame.image.load(const.GREEN_S2).convert()
            if self.animationState == 2:
                self.image = pygame.image.load(const.GREEN_S3).convert()

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