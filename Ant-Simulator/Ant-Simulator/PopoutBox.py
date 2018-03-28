import pygame
import Constants as const
import sys

'''
Used to run Informational Popout boxes Contains a loop to pause the game and wait for click
'''
class PopoutBox (object):
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, const.WIDTH, const.HEIGHT)
        self.exitHighImg = pygame.image.load(const.POPOUTEXITBUTTONHIGH).convert_alpha()

    ### takes an image file name and runs it til the user clicks
    def runGivenPopout(self, image):
        popoutImage = pygame.image.load(image).convert_alpha()
        done = False
        while not done:            
            # Get Cursor Pos every frame
            pos = pygame.mouse.get_pos()
            # If cursor overlaps the button load correct Highlighted Image
            if const.POPOUTEXITBUTTONRECT.collidepoint(pos):
                self.screen.blit(self.exitHighImg, self.rect)
            else:
                self.screen.blit(popoutImage, self.rect)
            # Flip Display
            pygame.display.flip()
            # Get event from pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    pygame.quit()
                    sys.exit()
                # If the mouse is clicked continue game
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    done = True