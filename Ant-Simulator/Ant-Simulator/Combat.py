"""
Project Name: Ant Simulator
File Name: Combat.py
Author: Lex Hall
Last Updated: August 1st, 2018
Python Version: 2.7
Pygame Version: 1.9.1.win32-py2.7
"""

import pygame
import Constants as const
from random import *
import sys

'''
Used to run a Combat situation includes information for UI display as well as logic to conclude the combat phase
'''
class CombatController (object):
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, const.WIDTH, const.HEIGHT)
        self.textFont = pygame.font.Font("pixelplay.ttf", 50)
        self.antDice = 1
        self.enemyDice = 1
        self.enemyStrength = -1
        self.enemyHealth = -1
        self.antCount = -1

    ### takes an image file name and runs it til the user clicks
    def runCombatLoop(self, enemyStrength, antCount, antType):
        pygame.mixer.music.pause()
        background = pygame.image.load(const.COMBATWIREFRAME).convert_alpha()
        done = False
        self.antDice = 1
        self.enemyDice = 1
        self.enemyStrength = enemyStrength
        self.enemyHealth = enemyStrength * 100
        self.antCount = antCount
        clock = pygame.time.Clock()
        frameRate = 60
        frameCount = 0
        currentStage = 1
        nextAnimationUpdate = 4
        nextStageUpdate = 60
        while not done:
            # Get event from pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    pygame.quit()
                    sys.exit()

            # Update
            if (frameCount == nextAnimationUpdate and currentStage == 1):
                self.antDice = randint(1,6)
                self.enemyDice = randint(1,6)
                nextAnimationUpdate += 4

            else:
                if self.antCount < 0 or self.enemyHealth < 0:
                    #TODO add animation
                    pygame.time.wait(5000)
                    done = True

            if (frameCount == nextStageUpdate):
                if currentStage == 1:
                    antDice = randint(1,6)
                    enemyDice = randint(1,6)
                    if self.antDice > self.enemyDice:
                        self.enemyHealth -= (antDice * self.antCount)
                    else:
                        self.antCount -= (self.enemyStrength * self.enemyDice)
                currentStage += 1
                if currentStage == 6:
                    currentStage = 1

            # Draw
            self.screen.blit(background, self.rect)
            self.screen.blit(self.textFont.render(str(self.antCount), True, const.BLACK), const.ANTCOUNTBOX)
            self.screen.blit(self.textFont.render(str(self.enemyHealth), True, const.BLACK), const.ENEMYHEALTHBOX)
            if currentStage == 1:
                self.screen.blit(self.textFont.render(str(self.antDice), True, const.BLACK), const.ANTDICEBOX)
                self.screen.blit(self.textFont.render(str(self.enemyDice), True, const.BLACK), const.ENEMYDICEBOX)
            else:
                if self.antDice > self.enemyDice:
                    self.screen.blit(self.textFont.render(str(self.antDice), True, const.RED), const.ANTDICEBOX)
                    self.screen.blit(self.textFont.render(str(self.enemyDice), True, const.BLACK), const.ENEMYDICEBOX)
                else:
                    self.screen.blit(self.textFont.render(str(self.antDice), True, const.BLACK), const.ANTDICEBOX)
                    self.screen.blit(self.textFont.render(str(self.enemyDice), True, const.RED), const.ENEMYDICEBOX)

            # Increment Frames/Ticks
            frameCount += 1

            # Reset frames and seconds every 30 frames to avoid numbers becoming too large
            if (frameCount == 61):
                frameCount = 1
                nextAnimationUpdate = 4

            # Throttle frame rate
            clock.tick(frameRate)

            # Flip Display
            pygame.display.flip()
    
        return self.enemyHealth < 0

    def getAntCountAfterCombat(self):
        return self.antCount

"""
Combat starts
Load image for background
Roll Dice Animation
Calculate 2 "Dice" (Rand 1-6)
make changes to totals
display results for 5 seconds
repeat steps 3-6 until ants are dead or enemy is dead
update deaths with UI
"""