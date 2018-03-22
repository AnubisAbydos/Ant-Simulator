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
MINLEAVES = 100
MAXLEAVES = 200
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
SPAWNWORKERSBUTTONRECT = pygame.Rect(863,280, 65,20)
SPAWNGATHERBUTTONRECT = pygame.Rect(973,280, 65,20)
SPAWNSOLDIERBUTTONRECT = pygame.Rect(863,445, 65,20)
SPAWNPRINCESSBUTTONRECT = pygame.Rect(973,445, 65,20)
UPGRADEHIVEBUTTONRECT = pygame.Rect(917,610, 65,20)

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
SPAWNWORKERBARFULL = "basic_ui_test.png"
SPAWNWORKERBAR3Q = "basic_ui_test.png"
SPAWNWORKERBARHALF = "basic_ui_test.png"
SPAWNWORKERBAR1Q = "basic_ui_test.png"
SPAWNWORKERBAREMPTY = "basic_ui_test.png"
SPAWNGATHERBARFULL = "basic_ui_test.png"
SPAWNGATHERBAR3Q = "basic_ui_test.png"
SPAWNGATHERBARHALF = "basic_ui_test.png"
SPAWNGATHERBAR1Q = "basic_ui_test.png"
SPAWNGATHERBAREMPTY = "basic_ui_test.png"
SPAWNSOLDIERBARFULL = "basic_ui_test.png"
SPAWNSOLDIERBAR3Q = "basic_ui_test.png"
SPAWNSOLDIERBARHALF = "basic_ui_test.png"
SPAWNSOLDIERBAR1Q = "basic_ui_test.png"
SPAWNSOLDIERBAREMPTY = "basic_ui_test.png"
SPAWNPRINCESSBARFULL = "basic_ui_test.png"
SPAWNPRINCESSBAR3Q = "basic_ui_test.png"
SPAWNPRINCESSBARHALF = "basic_ui_test.png"
SPAWNPRINCESSBAR1Q = "basic_ui_test.png"
SPAWNPRINCESSBAREMPTY = "basic_ui_test.png"

# SPAWNING COSTS AND TIMES
SPAWNWORKERTIME = 10
SPAWNWORKERCOST = 100
SPAWNGATHERTIME = 10
SPAWNGATHERCOST = 300
SPAWNSOLDIERTIME = 15
SPAWNSOLDIERCOST = 1000
SPAWNPRINCESSTIME = 60
SPANWPRINCESSCOST = 100000
# UI CONSTS END

# ANTTRAIL CONSTS START
ANIMATIONPICONE = "trail_one.png"
ANIMATIONPICTWO = "trail_two.png"
ANIMATIONPICTHREE = "trail_three.png"
ANIMATIONPICFOUR = "trail_four.png"
# ANTTRAIL CONSTS END
