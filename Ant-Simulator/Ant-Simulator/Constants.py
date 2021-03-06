"""
Project Name: Ant Simulator
File Name: Constants.py
Author: Lex Hall, Adam Gehring
Last Updated: August 2nd, 2018
Python Version: 2.7
Pygame Version: 1.9.1.win32-py2.7
"""

import pygame

# Global Variables
# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50,50,50)
RED = (255,0,0)
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
# BACKGROUND IMAGES
GRASS = "grass.png"
SAND = "dirt.png"
# GROUNDTILES CONSTS END



# Enemies CONSTS START
BADBUGSIZE = 20
BADBUG1 = "enemy1.png"
BADBUG2 = "enemy2.png"
BADBUG3 = "enemy3.png"
BADBUG4 = "enemy4.png"
BADBUG5 = "enemy5.png"
NUMBEROFENEMYS = 2
MOVEPERCENT = 50
# Percent chance for a new enemy to spawn each update
NEWSPAWNCHANCE = 1
# Enemies CONSTS end



# TREENODE CONSTS START
TREEBASESIZE = 40
NUMBEROFTREES = 30
MINLEAVES = 500
MAXLEAVES = 1000
PERCENTTOCHANGESTATE = 3
# TREE IMAGES
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



# INFORMATION POPOUTBOX CONSTS START
WORKERPOPOUT = "worker_popout.png"
GATHERPOPOUT = "gather_popout.png"
SOLDIERPOPOUT = "soldier_popout.png"
PRINCESSPOPOUT = "princess_popout.png"
HIVEPOPOUT = "hive_popout.png"
LEAFFUNGUSPOPOUT = "leaf_fungus_popout.png"
POPOUTEXITBUTTONHIGH = "popout_exit_high.png"
# EXIT BUTTON RECT
POPOUTEXITBUTTONRECT = pygame.Rect(640,535, 180,55)
# INFORMATION POPOUTBOX CONSTS END



# UI CONSTS START
# START MENU BUTTON RECTS
STARTBUTTONRECT = pygame.Rect(460,515, 165,50)
TUTORIALBUTTONRECT = pygame.Rect(460,575, 165,50)
EXITBUTTONRECT = pygame.Rect(460,635, 165,50)

#PAUSE MENU BUTTON RECTS
RESUMEPAUSEBUTTONRECT = pygame.Rect(460,450, 165,50)
TUTORIALPAUSEBUTTONRECT = pygame.Rect(460,510, 165,50)
EXITPAUSEBUTTONRECT = pygame.Rect(460,570, 165,50)

# GAME UI BUTTON RECTS
STARTTRAILRECT = pygame.Rect(90,15, 90,30)
ENDTRAILRECT = pygame.Rect(195,15, 90,30)
SPAWNWORKERSBUTTONRECT = pygame.Rect(863,280, 65,20)
SPAWNGATHERBUTTONRECT = pygame.Rect(973,280, 65,20)
SPAWNSOLDIERBUTTONRECT = pygame.Rect(863,445, 65,20)
SPAWNPRINCESSBUTTONRECT = pygame.Rect(973,445, 65,20)
UPGRADEHIVEBUTTONRECT = pygame.Rect(917,610, 65,20)
PAUSEGAMEBUTTONRECT = pygame.Rect(1022,10, 65,20)
DEBUGLOSEGAME = pygame.Rect(0,750, 50,50)

# QUESTION MARK BUTTON RECTS
WORKERQUESTIONMARK = pygame.Rect(850,158, 13,13)
GATHERQUESTIONMARK = pygame.Rect(960,158, 13,13)
SOLDIERQUESTIONMARK = pygame.Rect(850,325, 13,13)
PRINCESSQUESTIONMARK = pygame.Rect(960,325, 13,13)
HIVEQUESTIONMARK = pygame.Rect(850,493, 13,13)
LEAFQUESTIONMARK = pygame.Rect(850,680, 13,13)
FUNGUSQUESTIONMARK = pygame.Rect(950,680, 13,13)

# SECONDARY SCREENS PNGs
LOADINGSCREEN = "loading_screen.png"
STARTSCREEN = "start_screen_not_high.png"
STARTSCREENSTARTHIGH = "start_screen_start_high.png"
STARTSCREENTUTORIALHIGH = "start_screen_tutorial_high.png"
STARTSCREENEXITHIGH = "start_screen_exit_high.png"
PAUSESCREEN = "pause_screen.png"
PAUSESCREENRESUMEHIGH = "pause_screen_resume_high.png"
PAUSESCREENTUTORIALHIGH = "pause_screen_tutorial_high.png"
PAUSESCREENEXITHIGH = "pause_screen_exit_high.png"
# TUTORIAL SCREENS
TUTORIALONE = "tutorial_one.png"
TUTORIALTWO = "tutorial_two.png"
TUTORIALTHREE = "tutorial_three.png"
TUTORIALFOUR = "tutorial_four.png"
TUTORIALFIVE = "tutorial_five.png"
TUTORIALSIX = "tutorial_six.png"
TUTORIALSEVEN = "tutorial_seven.png"

# IN-GAME UI PNG ELEMENTS
UITEMPLATE = "default_ui.png"
QUESTIONMARKOVERLAY = "question_marks_and_menu_overlay.png"
# HIVE IMAGES BOTH SIDE AND TOP DOWN VIEWS
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
HIVESIDECONSTRUCTION = "hive_side_construction.png"
# PROGRESS BARS
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
# SPAWN TILE IMAGES
SPAWNWORKERTILE = "spawn_worker_tile.png"
SPAWNGATHERTILE = "spawn_gather_tile.png"
SPAWNSOLDIERTILE = "spawn_soldier_tile.png"
SPAWNPRINCESSTILE = "spawn_princess_tile.png"
# BUTTON HIGHLIGHTED VERSIONS
SETDESTBUTTONHIGH = "set_destination_button_high.png"
BACKTOHIVEBUTTONHIGH = "back_to_hive_button_high.png"
WORKERBUTTONHIGH = "worker_button_high.png"
GATHERBUTTONHIGH = "gather_button_high.png"
SOLDIERBUTTONHIGH = "soldier_button_high.png"
PRINCESSBUTTONHIGH = "princess_button_high.png"
UPGRADEHIVEHIGH = "upgrade_hive_button_high.png"
PAUSEHIGH = "pause_game_high.png"
# BLANK IMAGE
BLANKIMG = "blank_img.png"


# SPAWNING COSTS AND TIMES
SPAWNWORKERTIME = 10
SPAWNWORKERCOST = 100
SPAWNGATHERTIME = 10
SPAWNGATHERCOST = 300
SPAWNSOLDIERTIME = 15
SPAWNSOLDIERCOST = 1000
SPAWNPRINCESSTIME = 100
SPANWPRINCESSCOST = 100000

# GAME START VARAIBLES
STARTWORKERCOUNT = 30
STARTGATHERCOUNT = 20
STARTSOLDIERCOUNT = 10
STARTLEAFCOUNT = 0
STARTFUNGUSCOUNT = 0
STARTSPAWNCOUNT = 10
STARTHIVEUPGRADETIME = 10
STARTHIVEUPGRADECOST = 1000

# TEXT RENDER BOXES
WORKERTEXTBOX = pygame.Rect(415,13, 65,24)
GATHERTEXTBOX = pygame.Rect(560,13, 65,24)
SOLDIERTEXTBOX = pygame.Rect(710,13, 65,24)
FUNGUSTEXTBOX = pygame.Rect(865,755, 60,20)
LEAFTEXTBOX = pygame.Rect(975,755, 60,20)
HIVEUPGRADETIMEBOX = pygame.Rect(990,525, 60,20)
WORKERFUNGUSCOSTBOX = pygame.Rect(870,240, 40,15)
GATHERFUNGUSCOSTBOX = pygame.Rect(985,240, 40,15)
SOLDIERFUNGUSCOSTBOX = pygame.Rect(870,410, 40,15)
PRINCESSFUNGUSCOSTBOX = pygame.Rect(985,410, 40,15)
UPGRADEHIVELEAFCOSTBOX = pygame.Rect(913,635, 100,15)
# UI CONSTS END



# COMBAT CONSTS START
COMBATWIREFRAME = "combat_wireframe.png"
ANTDICEBOX = pygame.Rect(150,640, 100,100)
ENEMYDICEBOX = pygame.Rect(750,640, 100,100)
ANTCOUNTBOX = pygame.Rect(95,500, 300,50)
ENEMYHEALTHBOX = pygame.Rect(670,500, 300,50)
# COMBAT CONSTS END



# ANTTRAIL CONSTS START
ANIMATIONPICONE = "trail_one.png"
ANIMATIONPICTWO = "trail_two.png"
ANIMATIONPICTHREE = "trail_three.png"
# ANTTRAIL CONSTS END