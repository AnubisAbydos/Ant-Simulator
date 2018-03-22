import pygame

# Global Variables
# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# COLORS

# SCREENS AND MAP SIZES START
WIDTH = 1100
HEIGHT = 800
PIXELSIZE = 20
GRIDROWS = (WIDTH - 300) / PIXELSIZE
GRIDCOLUMNS = HEIGHT / PIXELSIZE
# SCREENS AND MAP SIZES END

# GROUNDTILES CONSTS START
# Used during array construction to determine cells starting state
STARTALIVEPERCENTAGE = 50
# Variables used during simulation step to change cell states
DEATHLIMIT = 3
BIRTHLIMIT = 4
STEPS = 4
# GroundTile pictures
GRASS = "grass.png"
SAND = "dirt.png"
# GROUNDTILES CONSTS END

# AntEater CONSTS START
ANTEATERSIZE = 35
NUMBEROFENEMYS = 5
# Ant eater placeholder image
ENEMY1 = "enemy1.png"
# AntEater CONSTS end

# TREENODE CONSTS START
TREEBASESIZE = 40
NUMBEROFTREES = 30
MINLEAVES = 50000
MAXLEAVES = 75000
PERCENTTOCHANGESTATE = 3
# Tree Images
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
# TREENODE CONSTS END

# UI CONSTS START
# START MENU BUTTON RECTS
STARTBUTTONRECT = pygame.Rect(460,515, 165,50)
TUTORIALBUTTONRECT = pygame.Rect(460,575, 165,50)
EXITBUTTONRECT = pygame.Rect(460,635, 165,50)

# GAME UI BUTTON RECTS
STARTTRAILRECT = pygame.Rect(90,15, 90,30)
ENDTRAILRECT = pygame.Rect(195,15, 90,30)

# UI SCREEN PNGs
LOADINGSCREEN = "loading_screen.png"
STARTSCREEN = "start_screen_not_high.png"
STARTSCREENSTARTHIGH = "start_screen_start_high.png"
STARTSCREENTUTORIALHIGH = "start_screen_tutorial_high.png"
STARTSCREENEXITHIGH = "start_screen_exit_high.png"

# IN-GAME UI PNG ELEMENTS
UITEMPLATE = "basic_ui_test.png"
HIVEL1 = "hive_1.png"
HIVEL2 = "hive_2.png"
HIVEL3 = "hive_3.png"
HIVEL4 = "hive_4.png"
HIVEL5 = "hive_5.png"
HIVEL6 = "hive_6.png"
HIVEL7 = "hive_7.png"
HIVEL8 = "hive_8.png"
HIVEL9 = "hive_9.png"
HIVEL10 = "hive_10.png"
# UI CONSTS END

# ANTTRAIL CONSTS START
ANIMATIONPICONE = "trail_one.png"
ANIMATIONPICTWO = "trail_two.png"
ANIMATIONPICTHREE = "trail_three.png"
# ANTTRAIL CONSTS END
