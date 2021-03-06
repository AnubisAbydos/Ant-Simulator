"""
Project Name: Ant Simulator
File Name: setup.py
Author: Lex Hall
Last Updated: August 2nd, 2018
Python Version: 2.7
Pygame Version: 1.9.1.win32-py2.7
cx_Freeze Version: 5.0.2
"""

import cx_Freeze

executables = [cx_Freeze.Executable("Ant_Simulator.py")]

cx_Freeze.setup(
    name = "Ant Simulator",
    options = {"build_exe":  {"packages":["pygame", "sys"],
                              "include_files":["AntTrail.py", "Combat.py", "Constants.py",
                                               "Enemy.py", "GroundTiles.py", "PopoutBox.py",
                                               "TreeNode.py", "UI.py", "back_to_hive_button_high.png",
                                               "background_music.mp3", "blank_img.png", "combat_wireframe.png",
                                               "credit_one.png", "credit_two.png", "credit_three.png",
                                               "default_ui.png", "dirt.png", "enemy1.png",
                                               "enemy2.png", "enemy3.png", "enemy4.png",
                                               "enemy5.png", "game_over_win_sound.ogg", "gather_button_high.png",
                                               "gather_popout.png", "gather_progress_1q.png", "gather_progress_3q.png",
                                               "gather_progress_empty.png", "gather_progress_full.png", "gather_progress_half.png",
                                               "grass.png", "hive_1.png", "hive_2.png",
                                               "hive_3.png", "hive_4.png", "hive_5.png",
                                               "hive_6.png", "hive_7.png", "hive_8.png",
                                               "hive_9.png", "hive_10.png", "hive_popout.png",
                                               "hive_side_1.png", "hive_side_2.png", "hive_side_3.png",
                                               "hive_side_4.png", "hive_side_5.png", "hive_side_6.png",
                                               "hive_side_7.png", "hive_side_8.png", "hive_side_9.png",
                                               "hive_side_10.png", "hive_side_construction.png", "hive_upgrade_sound.wav",
                                               "icon.jpg", "leaf_fungus_popout.png", "loading_screen.png",
                                               "lose_background.png", "lose_four.png", "lose_one.png",
                                               "lose_sound.wav", "lose_three.png", "lose_two.png",
                                               "lose_zero.png", "mouse_cursor.png", "pause_game_high.png",
                                               "pause_screen.png", "pause_screen_exit_high.png", "pause_screen_resume_high.png",
                                               "pause_screen_tutorial_high.png", "pixelplay.ttf", "popout_exit_high.png",
                                               "princess_button_high.png", "princess_popout.png", "princess_progress_1q.png",
                                               "princess_progress_3q.png", "princess_progress_empty.png", "princess_progress_full.png",
                                               "princess_progress_half.png", "question_marks_and_menu_overlay.png",
                                               "set_destination_button_high.png", "soldier_button_high.png", "soldier_popout.png",
                                               "soldier_progress_1q.png", "soldier_progress_3q.png", "soldier_progress_empty.png",
                                               "soldier_progress_full.png", "soldier_progress_half.png", "spawn_gather_tile.png",
                                               "spawn_princess_tile.png", "spawn_soldier_tile.png", "spawn_sound.wav",
                                               "spawn_worker_tile.png", "start_screen_exit_high.png", "start_screen_not_high.png",
                                               "start_screen_start_high.png", "start_screen_tutorial_high.png", "trail_one.png",
                                               "trail_three.png", "trail_two.png", "tree_black_s1.png",
                                               "tree_black_s2.png", "tree_black_s3.png", "tree_green_s1.png",
                                               "tree_green_s2.png", "tree_green_s3.png", "tree_orange_s1.png",
                                               "tree_orange_s2.png", "tree_orange_s3.png", "tree_reach_sound.wav",
                                               "tree_yellow_s1.png", "tree_yellow_s2.png", "tree_yellow_s3.png",
                                               "tutorial_five.png", "tutorial_four.png", "tutorial_one.png",
                                               "tutorial_seven.png", "tutorial_six.png", "tutorial_three.png",
                                               "tutorial_two.png", "upgrade_hive_button_high.png", "win_background.png",
                                               "win_eight.png", "win_eleven.png", "win_five.png",
                                               "win_four.png", "win_nine.png", "win_one.png",
                                               "win_seven.png", "win_six.png", "win_ten.png",
                                               "win_three.png", "win_two.png", "win_zero.png",
                                               "worker_button_high.png", "worker_popout.png", "worker_progress_1q.png",
                                               "worker_progress_3q.png", "worker_progress_empty.png", "worker_progress_full.png",
                                               "worker_progress_half.png",]}},
    executables = executables
    )