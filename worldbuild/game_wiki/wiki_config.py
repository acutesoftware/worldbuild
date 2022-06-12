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
op_file_places = os.path.join(op_folder, 'Places.html')
op_file_npcs = os.path.join(op_folder, 'NPC.html')
op_file_items = os.path.join(op_folder, 'Items.html')
op_file_crafting = os.path.join(op_folder, 'Crafting.html')

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
f_recipes = os.path.join(data_folder, 'Crafting_data', 'DT_craft_recipe.csv')
f_recipe_ingred = os.path.join(data_folder, 'Crafting_data', 'DT_craft_recipe_ingredients.csv')
f_builtitem = os.path.join(data_folder, 'Crafting_data', 'DT_BuiltItem.csv')








#####################################################
# Wiki Structure
#####################################################

chapters = [
    #['Players','Players in the world that have high scores, notable achievements, rare discoveries'],
    ['Places', 'places in Alrona'],
    ['NPC', 'Any non player character that can communicate'],
    #['Creatures', 'animals and other creatures in the world'],
    ['Items', 'Items in the world'],
    ['Food', 'Food in the world'],
    ['Plants', 'Plants in the world'],
    ['Animals', 'Animals in the world'],
    ['Fish', 'Fish in the world'],
    ['Clothes', 'Animals in the world'],
    ['Tools', 'Tools to gather and craft'],
    #['MOBs', 'dangerous animals and NPCs in the world'],
    ['Materials', 'stuff for crafting'],
    ['Crafting', 'building and creating things'],
    #['Gathering', 'finding and collecting things']
]
