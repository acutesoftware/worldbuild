# html_config.py
# update this file manually to determine how HTML files for game wiki is generated

import os 
import sys
#####################################################
# General settings
#####################################################

cur_folder = os.getcwd()
op_folder = os.path.join(cur_folder, '..', '..', '..', 'divitie', 'website')
data_folder = os.path.join(cur_folder, '..', 'data', 'sanct_game')

op_file_main = os.path.join(op_folder, 'index.html')
op_file_places = os.path.join(op_folder, 'Places.html')
op_file_npcs = os.path.join(op_folder, 'NPC.html')
op_file_items = os.path.join(op_folder, 'Items.html')
op_file_crafting = os.path.join(op_folder, 'Crafting.html')
op_file_dev = os.path.join(op_folder, 'Dev.html')
op_file_game_help = os.path.join(op_folder, 'Game.html')

#####################################################
# Data Files
#####################################################
f_levels = os.path.join(data_folder, 'World_data','DT_GameLevels.csv')
f_waypoints = os.path.join(data_folder, 'World_data','DT_GameWaypoints.csv')
f_level_pickups = os.path.join(data_folder, 'World_data','DT_Pickup_Level_Defaults.csv')
f_waypoint_spawn_pickups = os.path.join(data_folder, 'World_data','DT_Pickup_Locations_Spawn_Pickup.csv')

f_tree_spawner_types = os.path.join(data_folder, 'World_data','DT_Tree_Spawner_Types.csv')

f_fishing_loot = os.path.join(data_folder, 'DT_Fishing_Loot.csv')
f_crops = os.path.join(data_folder, 'DT_Crops.csv')
f_plants_harvestable = os.path.join(data_folder, 'DT_Plants_Harvestable.csv')
f_plants = os.path.join(data_folder, 'World_data', 'DT_plants_combined.csv')



f_quests = os.path.join(data_folder, 'DT_Quests.csv')
f_achievements = os.path.join(data_folder, 'DT_Achievements.csv')
f_emotes = os.path.join(data_folder, 'DT_djm_emotes.csv')

f_tool_type = os.path.join(data_folder, 'DT_Tool_Type.csv')
f_object_type = os.path.join(data_folder, 'DT_Object_Type.csv')
f_object_actions = os.path.join(data_folder, 'DT_Object_Actions.csv')

f_npcs = os.path.join(data_folder, 'DT_NPCs.csv')


f_items = os.path.join(data_folder, 'ItemList.csv')

f_npcs = os.path.join(data_folder, 'NPC_data','DT_NPCs.csv')
f_fishing_loot = os.path.join(data_folder, 'DT_Fishing_Loot.csv')
f_recipes = os.path.join(data_folder, 'Crafting_data', 'DT_craft_recipe.csv')
f_recipe_ingred = os.path.join(data_folder, 'Crafting_data', 'DT_craft_recipe_ingredients.csv')
f_builtitem = os.path.join(data_folder, 'Crafting_data', 'DT_BuiltItem.csv')
f_builtitem_parts = os.path.join(data_folder, 'Crafting_data', 'DT_BuiltItem_Parts.csv')

f_learn_skills = os.path.join(data_folder, 'Learning_data', 'DT_Learn_Skills.csv')
f_learn_professions = os.path.join(data_folder, 'Learning_data', 'DT_Learn_Professions.csv')
f_learn_profession_skills = os.path.join(data_folder, 'Learning_data', 'DT_Learn_Profession_Skills.csv')
f_events = os.path.join(data_folder, 'World_data', 'DT_Events.csv')

f_sounds = os.path.join(data_folder, 'World_data', 'DT_Sounds.csv')
f_sounds_game_level = os.path.join(data_folder, 'World_data', 'DT_Sounds_Game_Level.csv')

f_about_progress = os.path.join(data_folder,  'DT_about_dev_log.csv')
f_game_help =  os.path.join(data_folder, 'misc', 'sanct_help.csv')







#####################################################
# Wiki Structure
#####################################################

chapters = [
    #['Players','Players in the world that have high scores, notable achievements, rare discoveries'],
    ['Game', 'Game play and general help'],
    ['Places', 'places in Alrona'],
    ['NPC', 'Any non player character that can communicate'],
    #['Creatures', 'animals and other creatures in the world'],
    ['Items', 'Items in the world'],
    ['Food', 'Food in the world'],
    ['Plants', 'Plants in the world'],
    ['Animals', 'Animals in the world'],
    ['Fish', 'Fish in the world'],
    ['Clothes', 'Craftable clothes worn by players and NPCs'],
    ['Tools', 'Tools to gather and craft'],
    #['MOBs', 'dangerous animals and NPCs in the world'],
    ['Materials', 'stuff for crafting'],
    ['Crafting', 'building and creating things. Details of Recipes and buildable items'],
    ['Dev', 'DevLog and works in progress'],
    #['Gathering', 'finding and collecting things']
]
