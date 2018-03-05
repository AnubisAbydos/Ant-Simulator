import pygame
import random
import Constants as const
import GroundTiles as tiles

# Classes
# Hive Class contains sprite for ant hive
class Hive (pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

    def update(self):
        pass

# Tree Node contains sprite build for Trees on map
class TreeNode (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def update(self):
        pass

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

# UI contains the User Interface elements and updates status bars
class UI (object):
    def __init__(self):
        pass

# Game contains all information for an instance of a game
class Game (object):
    def __init__(self, screen):
        self.screen = screen
        drawUI()
        pass

    def processEvents(self):
        self.handleMouseClicks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            return False

    def handleMouseClicks(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

# Main calls game sets screen and runs game loop
def main():
    pygame.init()
    screen
    game = Game(screen)
    done = False
    while not done:
        game.processEvents()

        game.update()

        game.draw()

    pygame.quit()

# Call main to start game
if __name__ == "__main__":
    main()