#!/usr/bin/python3
# -*- coding: utf-8 -*-
# config_app.py
# Settings for world build apps

import os
import sys

# ------- PATHS -------------------------------------------------------
fldr_root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
fldr_data = os.path.join(fldr_root, 'data', 'wb_appdata')
fldr_tools = os.path.join(fldr_root, 'app', 'tools')
fldr_img =  os.path.join(fldr_root, 'app', 'static', 'img')
db_file = os.path.join(fldr_data, 'worldbuild.db')

IMAGE_FOLDER = r'/home/duncan/dev/src/python/worldbuild/worldbuild/samples/alrona/'
THUMBNAIL_FOLDER = r'/home/duncan/dev/src/python/worldbuild/worldbuild/samples/alrona/thumbnails'
THUMBNAIL_SIZE = (192, 192)

sys.path.append(fldr_root)

#sys.path.append(os.path.join(fldr_root, 'src', 'roguelike'))

#import roguelike.dungeon_generator as dg


# ------- Tables -----------------------------------------------------

db_tables = [
'DT_craft_methods',
'DT_craft_recipe',
'DT_craft_recipe_ingredients',
'DT_craft_recipe_steps', 
'DT_Events',
'DT_NPCs',
'DT_Quests',
'ItemList'   
]

# ------- Menu Items -------------------------------------------------


# ------- Tools -------------------------------------------------

tool_list = [ # tool_id,tool_name,py_import,desc,params_with_defaults
    ['example', 'Example Tool', 't_EXAMPLE', 'Example tool for user modification',
     'param1=50, param2=40, param3=-5'],
    ['dungeon', 'Dungeon Generator', 't_gen_dungeon', 'Generates a random dungeon',
     'grid_y=35, grid_x=130, NUM_ROOMS=20, ROOM_SIZE=3, NUM_HORIZ=4, lv_SEED=-1'
     ],
    ['town_gen', 'Town Generator', 't_gen_town', 'Generates a random Town layout',
     'X_pos=1, Y_pos=1, width=10, length=15, sparsness=97'
     ],
    ['world_gen', 'World Generator', 't_gen_world', 'Generates random World',
     'width=80, height=40, num_seeds=5, perc_land=47, perc_sea=50, perc_blocked=0, iterations=3, num_agents=1'
     ],
]


# --------------------------------------------------------------------

if __name__ == '__main__':
    print('config_app.py : fldr_root  = ' + fldr_root)
    print('config_app.py : fldr_data  = ' + fldr_data)
    print('config_app.py : fldr_tools = ' + fldr_tools)
    print('config_app.py : fldr_img   = ' + fldr_img)
    print('config_app.py : DB File    = ' + db_file)



