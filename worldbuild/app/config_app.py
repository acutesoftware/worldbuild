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
     'grid_y=30, grid_x=80, NUM_ROOMS=10, ROOM_SIZE=4, NUM_HORIZ=6, lv_SEED=-1'
     ],
    ['town_gen', 'Town Generator', 't_gen_town', 'Generates a random Town layout',
     'X_pos=1, Y_pos=1, width=22, length=10, sparsness=95'],
    
    ]


# --------------------------------------------------------------------

if __name__ == '__main__':
    print('fldr_root = ' + fldr_root)
    print('fldr_data = ' + fldr_data)
    print('DB File = ' + db_file)
    


