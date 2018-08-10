"""
Project Name: Ant Simulator
File Name: Enemy.py
Author: Lex Hall, Adam Gehring
Last Updated: August 2nd, 2018
Python Version: 2.7
Pygame Version: 1.9.1.win32-py2.7
"""

import sys
import pygame
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
        self.image = None
        self.directionTimer = randint(4,8) 
        self.enemyType = randint(0, 4)
        self.moveTimer = 0
        self.badBug1 = pygame.image.load(const.BADBUG1).convert_alpha()
        self.badBug2 = pygame.image.load(const.BADBUG2).convert_alpha()
        self.badBug3 = pygame.image.load(const.BADBUG3).convert_alpha()
        self.badBug4 = pygame.image.load(const.BADBUG4).convert_alpha()
        self.badBug5 = pygame.image.load(const.BADBUG5).convert_alpha()
        self.setStateImage()


    ### Random skin selector if statement
    def resetImage(self):
        if self.enemyType == 0:
            self.image = self.badBug1
        if self.enemyType == 1:
            self.image = self.badBug2
        if self.enemyType == 2:
            self.image = self.badBug3
        if self.enemyType == 3:
            self.image = self.badBug4
        if self.enemyType == 4:
            self.image = self.badBug5
        

    ### Sets enemy image rotation based on faceDirection
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


    ### Updates movement (on Random percent) and Animation state Returns Bool to signify if combat should begin
    def update(self):
        # Check if combat needs to be intiated 
        if self.checkCombatCollision(self.rect.x, self.rect.y):
            return True

        # If not Combat continue update
        else:
            # Increment timer til next direction rotate
            self.moveTimer += 1
            if self.moveTimer == self.directionTimer:
                # 50/50 chance to turn left or right
                if randint(1,100) < 50:
                    self.faceDirection += 1
                else: 
                    self.faceDirection -= 1
                    if self.faceDirection == -1:
                        self.faceDirection = 3
                self.faceDirection = self.faceDirection % 4
                self.setStateImage()
                # Reset Timer
                self.moveTimer = 0
                self.directionTimer = randint(4,8)
                return False

            # Chance to move each update
            elif (randint(1,100) < const.MOVEPERCENT):
                # Check next space if valid move rect to next square (based on direction facing)
                if self.faceDirection == 0:
                    if self.checkCollide(self.rect.x, self.rect.y -20):
                        self.rect.move_ip(0, -20)
                        return False
                elif self.faceDirection == 1:
                    if self.checkCollide(self.rect.x - 20, self.rect.y):
                        self.rect.move_ip(-20, 0)
                        return False
                elif self.faceDirection == 2:
                    if self.checkCollide(self.rect.x, self.rect.y +20):
                        self.rect.move_ip(0, 20)
                        return False
                elif self.faceDirection == 3:
                    if self.checkCollide(self.rect.x + 20, self.rect.y):
                        self.rect.move_ip(20, 0)
                        return False
    

    ### Checks for collision on grid     
    def checkCollide(self, x, y):
        if x > 798 or x < 2 or y > 798 or y < 57:
            return False
        else:
            return not self.grid[x/20][y/20].isBlocked


    ### Checks for Combat collosion by checking where ant trail or hive is compared to bug location
    def checkCombatCollision(self, x, y):
        if self.grid[x/20][y/20].isTrail or (x > 700 and y > 700):
            return True
        else:
            return False


    ### Blits bug to Game Window
    def draw(self):
        self.screen.blit(self.image, self.rect)



''' CLASS BUGNODESLIST 
Used to build the list of enemies for use by Game.
'''
class EnemyList (object):
    def __init__ (self, screen, grid, UI):
        self.screen = screen
        self.grid = grid
        self.UI = UI
        self.newEnemy = None
        self.list = []        
        # Add X number of bad bugs to list ensuring that overlapping does not occur
        for i in xrange(const.NUMBEROFENEMYS):
            while self.newEnemy == None:
                self.newEnemy = self.createNewEnemy()
            # Once valid Enemy is created add to list
            self.list.append(self.newEnemy)
            # reset newEnemy for next find
            self.newEnemy = None


    ### RECURSIVE FUNCTION calls until a valid enemy (not overlapping any trees) is returned
    def createNewEnemy(self):
        isCollide = False
        # Calls Enemy __init__ to automatically create a bad bug
        self.newEnemy = Enemy(self.screen, self.grid)
        # Checks Enemy location to each checkCollide location Remakes if there is a collision
        for enemy in self.list:
            isCollide = not enemy.checkCollide(self.newEnemy.x, self.newEnemy.y)
            if isCollide == True:
                self.createNewEnemy()
        if isCollide == False:
            return self.newEnemy


    ### Calls each Enemy's draw function
    def draw(self):
        for enemy in self.list:
            if enemy.isAlive:
                enemy.draw()


    ### Calls each Enemy's update function
    def update(self):
        # 2% chance each update to create a new enemy
        if (randint(1,100) < const.NEWSPAWNCHANCE + 1):
            self.list.append(self.createNewEnemy())

        # Update all alive Enemy
        for enemy in self.list:
            if not enemy.isAlive:
                del enemy
            else:
                # Calls update on enemy; bool returned: True = enemy is colliding with trail or anthill
                if enemy.update():
                    enemy.isAlive = self.UI.intiateCombat(enemy.strength, enemy.rect.x, enemy.rect.y)