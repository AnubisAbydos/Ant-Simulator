import pygame, sys
from random import *
import Constants as const

''' CLASS Enemy
Contains all information, variables and functions for an instance of a Bad Bug
'''
class Enemy(object):
    def __init__(self, screen, grid, x, y):
        self.screen = screen
        self.grid = grid
        self.rect = pygame.Rect(x, y, const.BADBUG1, const.BADBUG1)
        self.faceDirection = randint(0,3)
        self.isAlive = True
        self.strength = randint(1,6)
        self.image = pygame.image.load(const.BBUP).convert_alpha()
        self.directionTimer = randint(4,8) 
        self.enemyType = randint(0, 4)
        self.moveTimer = 0
        self.setStateImage()

        #timmer to direction move

    #TODO add random skin selector if statement

    def resetImage(self):
        self.image = pygame.image.load(const.BBUP).convert_alpha()
        #if self.enemyType == 0:

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
            if randint(0,100) < 50:
                self.faceDirection += 1
            else: 
                self.faceDirection -= 1
                if self.faceDirection == -1:
                    self.faceDirection = 3
            self.faceDirection = self.faceDirection % 3
            self.setStateImage()
        
            self.moveTimer = 0
            self.directionTimer = randint(4,8)
        #chance to move
        elif (randint(1,100) < const.MOVEPERCENT):
            if self.faceDirection == 0:
                if self.checkCollide(self.rect.x, self.rect.y -20):
                    self.rect.move_ip(0, -20)
            elif self.faceDirection == 1:
                if self.checkCollide(self.rect.x + 20, self.rect.y):
                    self.rect.move_ip(20, 0)
            elif self.faceDirection == 2:
                if self.checkCollide(self.rect.x, self.rect.y +20):
                    self.rect.move_ip(0, 20)
            elif self.faceDirection == 3:
                if self.checkCollide(self.rect.x -20, self.rect.y):
                    self.rect.move_ip(-20, 0)
    
    #TODO check for offscreen     
    def checkCollide(self, x, y):
        return not self.grid[x/20][y/20].isBlocked

    ### Blits bug to Game Window
    def draw(self):
        self.screen.blit(self.image, self.rect)

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
        self.newEnemy = Enemy(self.screen, self.grid, x, y)
        # Checks newBaddie location to each already created bad bug and remakes the bad bug if isCollide
        for enemy in self.list:
            isCollide = enemy.checkCollide(x, y)
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