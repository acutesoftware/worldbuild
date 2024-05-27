#!/usr/bin/python3
# -*- coding: utf-8 -*-
# config_app.py
# Settings for world build apps

import os
import sys

# ------- PATHS -------------------------------------------------------
fldr_root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
fldr_data = os.path.join(fldr_root, 'data', 'wb_appdata')

db_file = os.path.join(fldr_data, 'worldbuild.db')

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


if __name__ == '__main__':
    print('fldr_root = ' + fldr_root)
    print('fldr_data = ' + fldr_data)
    print('DB File = ' + db_file)
    


