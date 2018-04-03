import pygame, sys
from random import *
import Constants as const
import GroundTiles as ground

class Enemy(object):
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(200, 200, const.BADBUG1, const.BADBUG1)
        self.animationState = randint(0,4)
        self.isAlive = True

        #self.image = pygame.image.load(const.BBDOWN).convert_alpha()

    def setStateImage(self):
        if self.animationState == 0:
            self.image = pygame.image.load(const.BBDOWN).convert_alpha()
        elif self.animationState == 1 or self.animationState == 4:
            self.image = pygame.image.load(const.BBLEFT).convert_alpha()
        elif self.animationState == 2:
            self.image = pygame.image.load(const.BBUP).convert_alpha()
        elif self.animationState == 3:
            self.image = pygame.image.load(const.BBRIGHT).convert_alpha()

    ### Updates movement (on Random percent) and Animation state 
    def update(self):
        #Working on movement amount.
        if (randint(1,100) < const.MOVEPERCENT):
            if self.animationState == 0:
                self.moveDirection = -20
        self.animationState += randint(4,6)
        self.animationState = self.animationState % 4
        self.setStateImage()
        

    ### Blits bug to Game Window
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    ### Checks for collision given another Rect (in this case another bug)
    def collide(self, givenRect):
        if(self.rect.colliderect(givenRect)):
            return True
        return False

    def isAlive(self):
        return self.isAlive


''' CLASS BUGNODESLIST 
Used to build the list of enemies for use by Game.
'''
class BugNodesList (object):
    def __init__ (self, screen):
        self.screen = screen
        self.newBaddie = None
        self.list = []        
        # Add X number of bad bugs to list ensuring that overlapping does not occur
        for i in xrange(const.NUMBEROFENEMYS):
            # A bug was present previous to the while loop that was adding NoneType objects to the list.
            # The while loop removes this bug.
            while self.newBaddie == None:
                self.newBaddie = self.createNewBaddie()
            # Once valid Baddie is created add to list
            self.list.append(self.newBaddie)
            # reset newBaddie for next find
            self.newBaddie = None

    ### RECURSIVE FUNCTION calls until a valid Bad Bug (not overlapping any others) is returned
    def createNewBaddie(self):
        isCollide = False
        # Calls Enemy __init__ to automatically create a bad bug
        self.newBaddie = Enemy()
        # Checks newBaddie location to each already created bad bug and remakes the bad bug if isCollide
        for badBug in self.list:
            isCollide = badBug.collide(self.newBaddie.rect)
            if isCollide == True:
                self.createNewBaddie()
        if (isCollide == False):
            return self.newBaddie
    
    def checkForCollision(self, pos):
        for badBug in self.list:
            if badBug.rect.collidepoint(pos):
                return badBug
        return None

    ### Calls each bbug's draw function
    def draw(self):
        for baddie in self.list:
            baddie.draw(self.screen)

    ### Calls each bad bug's update function
    def update(self, harvesterNumber):
        for baddie in self.list:
            baddie.update(harvesterNumber)