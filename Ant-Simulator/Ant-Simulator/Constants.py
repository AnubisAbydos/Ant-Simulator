# Global Variables
#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#COLORS

#CONSTS FOR Game
TIMEBETWEENUPDATE = 1
#CONSTS FOR Game

#SCREENS AND MAP SIZES START
WIDTH = 1100
HEIGHT = 800
PIXELSIZE = 20
GRIDROWS = (WIDTH - 300) / PIXELSIZE
GRIDCOLUMNS = HEIGHT / PIXELSIZE
LOADINGSCREEN = "loading_screen.png"
#SCREENS AND MAP SIZES END

#GroundTile CONSTS START
#used during array construction to determine cells starting state
STARTALIVEPERCENTAGE = 50

#variables used during simulation step to change cell states
DEATHLIMIT = 3
BIRTHLIMIT = 4
STEPS = 4

#GroundTile pictures
GRASS = "grass.png"
SAND = "dirt.png"
#GroundTile CONSTS END

#AntEater CONSTS START
ANTEATERSIZE = 35
NUMBEROFENEMYS = 5
#ant eater placeholder image
ENEMY1 = "enemy1.png"
#AntEater CONSTS end

#TreeNode CONSTS START
TREEBASESIZE = 40
NUMBEROFTREES = 30
MINLEAVES = 50000
MAXLEAVES = 75000
PERCENTTOCHANGESTATE = 3
#Tree Images
BLACK_S1 = "tree_black_s1.png"
BLACK_S2 = "tree_black_s2.png"
BLACK_S3 = "tree_black_s3.png"
ORANGE_S1 = "tree_orange_s1.png"
ORANGE_S2 = "tree_orange_s2.png"
ORANGE_S3 = "tree_orange_s3.png"
YELLOW_S1 = "tree_yellow_s1.png"
YELLOW_S2 = "tree_yellow_s2.png"
YELLOW_S3 = "tree_yellow_s3.png"
GREEN_S1 = "tree_green_s1.png"
GREEN_S2 = "tree_green_s2.png"
GREEN_S3 = "tree_green_s3.png"
#TreeNode CONSTS END

#UI CONSTS START

#UI CONSTS END
