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

tool_list = [
    ['dungeon', 'Dungeon Generator', 'dungeon.py', 'Generates a random dungeon'],
    ['town_gen', 'Town Generator', 'town_gen.py', 'Generates a random Town layout'],
    
    ]


# --------------------------------------------------------------------

if __name__ == '__main__':
    print('fldr_root = ' + fldr_root)
    print('fldr_data = ' + fldr_data)
    print('DB File = ' + db_file)
    


