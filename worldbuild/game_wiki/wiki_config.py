# html_config.py
# update this file manually to determine how HTML files for game wiki is generated

import os 
import sys
#####################################################
# General settings
#####################################################

cur_folder = os.getcwd()
op_folder = os.path.join(cur_folder, "html_op")
data_folder = os.path.join(cur_folder, '..', 'data', 'sanct_game')

op_file_main = os.path.join(op_folder, 'index.html')

#####################################################
# Data Files
#####################################################
f_levels = os.path.join(data_folder, 'World_data','DT_GameLevels.csv')
f_waypoints = os.path.join(data_folder, 'World_data','DT_GameWaypoints.csv')
f_level_pickups = os.path.join(data_folder, 'World_data','DT_Pickup_Level_Defaults.csv')
f_waypoint_spawn_pickups = os.path.join(data_folder, 'World_data','DT_Pickup_Locations_Spawn_Pickup.csv')

f_items = os.path.join(data_folder, 'ItemList.csv')

f_npcs = os.path.join(data_folder, 'NPC_data','DT_NPCs.csv')
f_fishing_loot = os.path.join(data_folder, 'DT_Fishing_Loot.csv')







#####################################################
# Wiki Structure
#####################################################

chapters = [
    #['Players','Players in the world that have high scores, notable achievements, rare discoveries'],
    ['Places', 'places in Alrona'],
    ['NPC', 'Any non player character that can communicate'],
    #['Creatures', 'animals and other creatures in the world'],
    ['Objects', 'Objects in the world'],
    ['Plants', 'Plants in the world'],
    #['MOBs', 'dangerous animals and NPCs in the world'],
    ['Crafting', 'building and creating things'],
    #['Gathering', 'finding and collecting things']
]
