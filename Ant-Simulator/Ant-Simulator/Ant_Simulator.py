import pygame
import Constants as const
import GroundTiles as ground
import TreeNode as tree
import UI as ui

# Enemy contains sprite for any enemy that could attack the ants
class Enemy (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def update(self):
        pass

# Ant Trail contains logic and drawing for foraging ant trail
class AntTrail (object):
    def __init__(self):
        pass

# Popout Box contains logic and drawing for pop out informational boxes
class PopoutBox (object):
    def __init__(self):
        pass

# Game contains all information for an instance of a game
class Game (object):
    def __init__(self, screen):
        self.screen = screen
        self.UI = ui.UI(screen)
        #Calls UI loadingScreen to display loading screen while the game finishes __init__
        self.UI.loadingScreen()
        self.groundTiles = ground.groundTiles(screen)
        self.trees = tree.TreeNodesList(screen)
        #calls Start Screen loop after all assests are loaded
        self.UI.startScreen()
       
        
    def processEvents(self):
        self.handleMouseClicks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            return False

    def handleMouseClicks(self):
        pass

    def update(self):
        self.trees.update()

    def draw(self):
        self.groundTiles.draw()
        self.UI.draw()        
        self.trees.draw()

# Main calls game sets screen and runs game loop
def main():
    pygame.init()
    screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
    game = Game(screen)
    done = False
    clock = pygame.time.Clock()
    frameRate = 60
    frameCount = 0
    nextUpdateCount = 1
    # Loop Start
    while not done:
        totalSeconds = frameCount // frameRate
        done = game.processEvents()

        if (totalSeconds == nextUpdateCount):
            game.update()
            nextUpdateCount += const.TIMEBETWEENUPDATE

        game.draw()
        frameCount += 1
        clock.tick(frameRate)
        pygame.display.flip()

    #Loop End
    pygame.quit()

# Call main to start game
if __name__ == "__main__":
    main()