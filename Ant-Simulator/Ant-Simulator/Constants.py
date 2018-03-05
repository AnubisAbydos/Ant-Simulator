# Global Variables
#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#COLORS

#SCREEN AND MAP SIZES
WIDTH = 1100
HEIGHT = 1000
PIXELSIZE = 10
GRIDROWS = WIDTH / PIXELSIZE
GRIDCOLUMNS = HEIGHT / PIXELSIZE
#SCREEN AND MAP SIZES

#GroundTile CONSTS
#used during array construction to determine cells starting state
startAlivePercentage = 38

#variables used during simulation step to change cell states
deathLimit = 3
birthLimit = 4
steps = 4
#GroundTile CONSTS