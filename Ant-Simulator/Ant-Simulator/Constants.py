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
MINLEAVES = 1000
MAXLEAVES = 2000
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
UITEMPLATE = "default_ui.png"
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
HIVESIDE1 = "hive_side_1.png"
HIVESIDE2 = "hive_side_2.png"
HIVESIDE3 = "hive_side_3.png"
HIVESIDE4 = "hive_side_4.png"
HIVESIDE5 = "hive_side_5.png"
HIVESIDE6 = "hive_side_6.png"
HIVESIDE7 = "hive_side_7.png"
HIVESIDE8 = "hive_side_8.png"
HIVESIDE9 = "hive_side_9.png"
HIVESIDE10 = "hive_side_10.png"
SPAWNWORKERBARFULL = "worker_progress_full.png"
SPAWNWORKERBAR3Q = "worker_progress_3q.png"
SPAWNWORKERBARHALF = "worker_progress_half.png"
SPAWNWORKERBAR1Q = "worker_progress_1q.png"
SPAWNWORKERBAREMPTY = "worker_progress_empty.png"
SPAWNGATHERBARFULL = "gather_progress_full.png"
SPAWNGATHERBAR3Q = "gather_progress_3q.png"
SPAWNGATHERBARHALF = "gather_progress_half.png"
SPAWNGATHERBAR1Q = "gather_progress_1q.png"
SPAWNGATHERBAREMPTY = "gather_progress_empty.png"
SPAWNSOLDIERBARFULL = "soldier_progress_full.png"
SPAWNSOLDIERBAR3Q = "soldier_progress_3q.png"
SPAWNSOLDIERBARHALF = "soldier_progress_half.png"
SPAWNSOLDIERBAR1Q = "soldier_progress_1q.png"
SPAWNSOLDIERBAREMPTY = "soldier_progress_empty.png"
SPAWNPRINCESSBARFULL = "princess_progress_full.png"
SPAWNPRINCESSBAR3Q = "princess_progress_3q.png"
SPAWNPRINCESSBARHALF = "princess_progress_half.png"
SPAWNPRINCESSBAR1Q = "princess_progress_1q.png"
SPAWNPRINCESSBAREMPTY = "princess_progress_empty.png"
SPAWNWORKERTILE = "spawn_worker_tile.png"
SPAWNGATHERTILE = "spawn_gather_tile.png"
SPAWNSOLDIERTILE = "spawn_soldier_tile.png"
SPAWNPRINCESSTILE = "spawn_princess_tile.png"
SETDESTBUTTONHIGH = "set_destination_button_high.png"
BACKTOHIVEBUTTONHIGH = "back_to_hive_button_high.png"
WORKERBUTTONHIGH = "worker_button_high.png"
GATHERBUTTONHIGH = "gather_button_high.png"
SOLDIERBUTTONHIGH = "soldier_button_high.png"
PRINCESSBUTTONHIGH = "princess_button_high.png"
UPGRADEHIVEHIGH = "upgrade_hive_button_high.png"
BLANKIMG = "blank_img.png"

# SPAWNING COSTS AND TIMES
SPAWNWORKERTIME = 10
SPAWNWORKERCOST = 100
SPAWNGATHERTIME = 10
SPAWNGATHERCOST = 300
SPAWNSOLDIERTIME = 15
SPAWNSOLDIERCOST = 1000
SPAWNPRINCESSTIME = 60
SPANWPRINCESSCOST = 100000

# TEXT RENDER BOXES
WORKERTEXTBOX = pygame.Rect(415,13, 65,24)
GATHERTEXTBOX = pygame.Rect(560,13, 65,24)
SOLDIERTEXTBOX = pygame.Rect(710,13, 65,24)
FUNGUSTEXTBOX = pygame.Rect(865,755, 60,20)
LEAFTEXTBOX = pygame.Rect(975,755, 60,20)
# UI CONSTS END

# ANTTRAIL CONSTS START
ANIMATIONPICONE = "trail_one.png"
ANIMATIONPICTWO = "trail_two.png"
ANIMATIONPICTHREE = "trail_three.png"
# ANTTRAIL CONSTS END
