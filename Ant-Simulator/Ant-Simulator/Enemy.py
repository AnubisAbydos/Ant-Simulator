import pygame, sys
from random import *
import Constants as const

''' CLASS Enemy
Contains all information, variables and functions for an instance of a Bad Bug
'''
class Enemy(object):
    def __init__(self, screen, grid):
        self.screen = screen
        self.grid = grid
        self.x = randrange(60,700,20)
        self.y = randrange(60,700,20)
        self.rect = pygame.Rect(self.x, self.y, const.BADBUGSIZE, const.BADBUGSIZE)
        self.faceDirection = randint(0,3)
        self.isAlive = True
        self.strength = randint(1,6)
        self.image = pygame.image.load(const.BADBUG1).convert_alpha()
        self.directionTimer = randint(4,8) 
        self.enemyType = randint(0, 4)
        self.moveTimer = 0
        self.setStateImage()

        #timmer to direction move


    #Random skin selector if statement
    def resetImage(self):
        if self.enemyType == 0:
            self.image = pygame.image.load(const.BADBUG1).convert_alpha()
        if self.enemyType == 1:
            self.image = pygame.image.load(const.BADBUG2).convert_alpha()
        if self.enemyType == 2:
            self.image = pygame.image.load(const.BADBUG3).convert_alpha()
        if self.enemyType == 3:
            self.image = pygame.image.load(const.BADBUG4).convert_alpha()
        if self.enemyType == 4:
            self.image = pygame.image.load(const.BADBUG5).convert_alpha()
        
        #right now there is only one type of bad bug.
    def setStateImage(self):
        self.resetImage()
        if self.faceDirection == 0:
            pass
        elif self.faceDirection == 1:
            self.image = pygame.transform.rotate(self.image, 90)
        elif self.faceDirection == 2:
            self.image = pygame.transform.rotate(self.image, 180)
        elif self.faceDirection == 3:
            self.image = pygame.transform.rotate(self.image, 270)

    ### Updates movement (on Random percent) and Animation state 
    def update(self):
        self.moveTimer += 1

        if self.moveTimer == self.directionTimer:
            if randint(1,100) < 50:
                self.faceDirection += 1
            else: 
                self.faceDirection -= 1
                if self.faceDirection == -1:
                    self.faceDirection = 3
            self.faceDirection = self.faceDirection % 4
            self.setStateImage()
        
            self.moveTimer = 0
            self.directionTimer = randint(4,8)
        #chance to move
        elif (randint(1,100) < const.MOVEPERCENT):
            if self.faceDirection == 0:
                if self.checkCollide(self.rect.x, self.rect.y -20):
                    self.rect.move_ip(0, -20)
            elif self.faceDirection == 1:
                if self.checkCollide(self.rect.x - 20, self.rect.y):
                    self.rect.move_ip(-20, 0)
            elif self.faceDirection == 2:
                if self.checkCollide(self.rect.x, self.rect.y +20):
                    self.rect.move_ip(0, 20)
            elif self.faceDirection == 3:
                if self.checkCollide(self.rect.x + 20, self.rect.y):
                    self.rect.move_ip(20, 0)
    
    #### Checks for collision given another Rect (in this case another bug)     
    def checkCollide(self, x, y):
    #TODO check for offscreen (x 0 - 800) (y 60 - 800)
        if x > 798 or x < 2 or y > 798 or y < 57:
            return False
        else:
            return not self.grid[x/20][y/20].isBlocked

    ### Blits bug to Game Window
    def draw(self):
        self.screen.blit(self.image, self.rect)

    def isAlive(self):
        return self.isAlive


''' CLASS BUGNODESLIST 
Used to build the list of enemies for use by Game.
'''
class EnemyList (object):
    def __init__ (self, screen, grid):
        self.screen = screen
        self.grid = grid
        self.newEnemy = None
        self.list = []        
        # Add X number of bad bugs to list ensuring that overlapping does not occur
        for i in xrange(const.NUMBEROFENEMYS):
            # A bug was present previous to the while loop that was adding NoneType objects to the list.
            # The while loop removes this bug.
            while self.newEnemy == None:
                self.newEnemy = self.createNewEnemy()
            # Once valid Baddie is created add to list
            self.list.append(self.newEnemy)
            # reset newBaddie for next find
            self.newEnemy = None

    ### RECURSIVE FUNCTION calls until a valid Bad Bug (not overlapping any others) is returned
        #TODO set random location spawning (x 0 - 800) (y 60 - 800)
    def createNewEnemy(self):
        isCollide = False
        # Calls Enemy __init__ to automatically create a bad bug
        self.newEnemy = Enemy(self.screen, self.grid)
        # Checks newBaddie location to each already created bad bug and remakes the bad bug if isCollide
        for enemy in self.list:
            isCollide = not enemy.checkCollide(self.newEnemy.x, self.newEnemy.y)
            if isCollide == True:
                self.createNewEnemy()
        if isCollide == False:
            return self.newEnemy

    ### Calls each bbug's draw function
    def draw(self):
        for enemy in self.list:
            if enemy.isAlive:
                enemy.draw()

    ### Calls each bad bug's update function
    def update(self):
        for enemy in self.list:
            if not enemy.isAlive:
                del enemy
            else:
                enemy.update()