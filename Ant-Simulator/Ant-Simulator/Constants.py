# Global Variables
#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#COLORS

#SCREEN AND MAP SIZES START
WIDTH = 1100
HEIGHT = 800
PIXELSIZE = 10
GRIDROWS = (WIDTH - 300) / PIXELSIZE
GRIDCOLUMNS = HEIGHT / PIXELSIZE
#SCREEN AND MAP SIZES END

#GroundTile CONSTS START
#used during array construction to determine cells starting state
STARTALIVEPERCENTAGE = 50

#variables used during simulation step to change cell states
DEATHLIMIT = 3
BIRTHLIMIT = 4
STEPS = 4

#GroundTile pictures
GRASS = "grass.jpg"
SAND = "sand.jpg"
#GroundTile CONSTS END

#TreeNode CONSTS START
TREEBASESIZE = 20
NUMBEROFTREES = 50
#TreeNode CONSTS END

#UI CONSTS START

#UI CONSTS END
