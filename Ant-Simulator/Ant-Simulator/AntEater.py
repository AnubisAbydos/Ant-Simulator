import pygame
import random
import math
import Constants as const


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
 
 
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load(const.ENEMY1).convert_alpha()
        
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 
        # Instance variables that control the edges of where we bounce
        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0
 
        # Instance variables for our current speed and direction
        self.change_x = 0
        self.change_y = 0
 
    def update(self):
        """ Called each frame. """
        self.rect.x += self.change_x
        self.rect.y += self.change_y
 
        if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
            self.change_x *= -1
 
        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1
 
 

 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
antEaterList = pygame.sprite.Group()
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    # This represents a block
    block = Block(BLACK, 20, 15)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
 
    block.change_x = random.randrange(-3, 4)
    block.change_y = random.randrange(-3, 4)
    block.left_boundary = 0
    block.top_boundary = 0
    block.right_boundary = screen_width
    block.bottom_boundary = screen_height
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a red player block
player = Player(RED, 20, 15)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Clear the screen
    screen.fill(WHITE)
 
    # Calls update() method on every sprite in the list
    all_sprites_list.update()
 
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
 
    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        print(score)
 
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
#Main enemy class object
class AntEater(pygame.sprite.Sprite):

    def __init__(self):
        self.rect = pygame.Rect(random.randrange(60,700,20), random.randrange(60,700,20), const.ANTEATERSIZE, const.ANTEATERSIZE)
        self.image = None
        self.setStateImage()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def setStateImage(self):
        pass

class AntEaterList (object):
    def __init__ (self, screen):
        self.newEater = None
        self.list = []
        self.screen = screen
        for i in xrange(const.NUMBEROFENEMYS):
            #A bug was present previous to the while loop that was adding NoneType objects to the list.
            #The while loop removes this bug.
            while self.newEater == None:
                self.newEater = self.createNewEater()
            self.list.append(self.newEater)
            self.newEater = None

    def createNewEater(self):
        isCollide = False
        self.newEater = AntEater()
        for eater in self.list:
            isCollide = eater.collide(self.newEater.rect)
            if isCollide == True:
                self.createNewEater()
        if (isCollide == False):
            return self.newEater
    
    def draw(self):
        for eater in self.list:
            eater.draw(self.screen)

    def update(self):
        for eater in self.list:
            eater.update()
        