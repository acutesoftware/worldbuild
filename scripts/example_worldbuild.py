#!/usr/bin/python3
# -*- coding: utf-8 -*-
# example_worldbuild.py
# Testing worldbuild modules outside of dev environment
# Run the following command to get the package
#      pip3 install --user worldbuild
# Then run this script to test

#import worldbuild.pathfind as pathfind

import worldbuild.dungeon_generator as dg

grid = dg.create_dungeon(grid_y=90, grid_x=150, NUM_ROOMS=90, ROOM_SIZE = 3, NUM_HORIZ = 35)
print(dg.grid_as_str(grid))

# optional - make a path through the grid
print(dg.path_find(grid))

# optional - export as TMX file
dg.convert_grid_to_TileEditor_map('dungeon.tmx', 'samples/ascii_runeset.tsx')
