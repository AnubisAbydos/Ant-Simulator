import pygame
from random import *
import Constants as const

''' CLASS TREENODE
Contains sprite build data for Trees.
'''
class TreeNode (object):
    def __init__(self):
        # Randomize start location
        self.rect = pygame.Rect(randrange(60,700,20), randrange(60,700,20), const.TREEBASESIZE, const.TREEBASESIZE)
        # Tree Quality determines the multiplier for leaf gathering/color of tree
        self.treeQuality = randint(0,3)
        self.leafQuantity = randint(const.MINLEAVES, const.MAXLEAVES)
        self.isBeingHarvested = False
        # Used to track and progress animation cycle called in update (Randomized to have even start states)
        self.animationState = randint(0,3)
        # Image is loaded by setStateImage() but declared here
        self.image = None
        self.setStateImage()

    ### Sets Tree image based on Quality and Animation State
    def setStateImage(self):
        if self.treeQuality == 0:
            if self.animationState == 0:
                self.image = pygame.image.load(const.BLACK_S1).convert_alpha()
            elif self.animationState == 1 or self.animationState == 3:
                self.image = pygame.image.load(const.BLACK_S2).convert_alpha()
            elif self.animationState == 2:
                self.image = pygame.image.load(const.BLACK_S3).convert_alpha()
        elif self.treeQuality == 1:
            if self.animationState == 0:
                self.image = pygame.image.load(const.ORANGE_S1).convert_alpha()
            elif self.animationState == 1 or self.animationState == 3:
                self.image = pygame.image.load(const.ORANGE_S2).convert_alpha()
            elif self.animationState == 2:
                self.image = pygame.image.load(const.ORANGE_S3).convert_alpha()
        elif self.treeQuality == 2:
            if self.animationState == 0:
                self.image = pygame.image.load(const.YELLOW_S1).convert_alpha()
            elif self.animationState == 1 or self.animationState == 3:
                self.image = pygame.image.load(const.YELLOW_S2).convert_alpha()
            elif self.animationState == 2:
                self.image = pygame.image.load(const.YELLOW_S3).convert_alpha()
        elif self.treeQuality == 3:
            if self.animationState == 0:
                self.image = pygame.image.load(const.GREEN_S1).convert_alpha()
            elif self.animationState == 1 or self.animationState == 3:
                self.image = pygame.image.load(const.GREEN_S2).convert_alpha()
            elif self.animationState == 2:
                self.image = pygame.image.load(const.GREEN_S3).convert_alpha()

    ### Updates Quality (on Random percent), Animation state and leaf count
    def update(self, harvesterNumber):
        if (randint(1,100) < const.PERCENTTOCHANGESTATE):
            self.treeQuality += 1
            self.treeQuality = self.treeQuality % 4
            if self.leafQuantity <= 0:
                self.leafQuantity += randint(const.MINLEAVES, const.MAXLEAVES)
        self.animationState += 1
        self.animationState = self.animationState % 4
        self.setStateImage()
        if self.isBeingHarvested:
            self.leafQuantity -= harvesterNumber

    ### Blits tree to Game Window
    def draw(self, screen):
        if self.leafQuantity > 0:
            screen.blit(self.image, self.rect)

    ### Checks for collision given another Rect (in this case another tree)
    def collide(self, givenRect):
        if(self.rect.colliderect(givenRect)):
            return True
        return False

    def getTreeQuality(self):
        return self.treeQuality

    def getLeafQuantity(self):
        return self.leafQuantity

''' CLASS TREENODESLIST 
Used to build the list of Trees for use by Game.
'''
class TreeNodesList (object):
    def __init__ (self, screen):
        self.screen = screen
        self.newTree = None
        self.list = []
        # Add X number of trees to list ensuring that overlapping does not occur
        for i in xrange(const.NUMBEROFTREES):
            # A bug was present previous to the while loop that was adding NoneType objects to the list.
            # The while loop removes this bug.
            while self.newTree == None:
                self.newTree = self.createNewTree()
            # Once valid tree is created add to list
            self.list.append(self.newTree)
            # reset newTree for next find
            self.newTree = None

    ### RECURSIVE FUNCTION calls until a valid tree (not overlapping any others) is returned
    def createNewTree(self):
        isCollide = False
        # Calls TreeNode __init__ to automatically create a tree
        self.newTree = TreeNode()
        # Checks newTrees location to each already created tree and remakes the tree if isCollide
        for tree in self.list:
            isCollide = tree.collide(self.newTree.rect)
            if isCollide == True:
                self.createNewTree()
        if (isCollide == False):
            return self.newTree
    
    def checkForCollision(self, pos):
        for tree in self.list:
            if tree.rect.collidepoint(pos):
                return tree
        return None

    ### Calls each tree's draw function
    def draw(self):
        for tree in self.list:
            tree.draw(self.screen)

    ### Calls each tree's update function
    def update(self, harvesterNumber):
        for tree in self.list:
            tree.update(harvesterNumber)