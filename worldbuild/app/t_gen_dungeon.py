#!/usr/bin/python3
# -*- coding: utf-8 -*-
# t_dungeon.py
"""
python files with t_*.py are for use in the Tools menu of worldbuild.
You need to make sure your python tool has the following functions
res = run_tool(params) returns HTML_output showing the result of the tool
(NO - this is in mod_wb) html = build_form(params, param_defaults)
(NOT NEEDED) param_values = get_form_results(params)

"""

import os
import sys
import time

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".."  )
pth = os.path.join(root_folder, 'worldbuild', 'roguelike')
print ('WORLDBUILD PATH = ' + pth)
sys.path.append(pth)


import dungeon_generator as dg

def run_tool(params):
    grid_y = params[0]
    grid_x = params[1]
    NUM_ROOMS = params[2]
    ROOM_SIZE = params[3]
    NUM_HORIZ = params[4]
    lv_SEED = params[5]

    grid, seed = dg.create_dungeon(grid_y, grid_x, NUM_ROOMS, ROOM_SIZE, NUM_HORIZ, lv_SEED)
    #print(dg.grid_as_str(grid))

    # optional - make a path through the grid
    solved = dg.path_find(grid)
    #print(solved)

    # optional - export as TMX file
    # dg.convert_grid_to_TileEditor_map('dungeon.tmx', 'samples/ascii_runeset.tsx')
    if solved == 'no path found':
        return '<h3>No path found</h3>' + dg.grid_as_html(grid, seed), seed
    else:
        return dg.solved_grid_as_html(solved, seed), seed
