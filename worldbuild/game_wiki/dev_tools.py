#!/usr/bin/python3
# -*- coding: utf-8 -*-
# dev_tools.py

import os
import sys
import csv

from collections import Counter

import wiki_config as cfg

sys.path.append(os.path.join(os.getcwd(), '..'))

import html_utils

def main():
    print("generating list of game exceptions...")
    print(get_stats())
    print(get_progress_log())

def get_progress_log():
    from operator import itemgetter
    txt = '<H3>Progress Log</H3>\n'
    txt += '<table border=0><TR><TD>Date</TD><TD>Area</TD><TD>Type</TD><TD>Details</TD></TR>\n'
    lst_prog = html_utils.read_csv_to_list(cfg.f_about_progress) # .sort(reverse=True)
    for row in sorted(lst_prog, key=itemgetter(1), reverse=True):
        txt += '<TR>'
        for col in row[1:]:
            txt += '<TD>' + col + '</TD>'
        txt += '</TR>'
    txt += '</TABLE>'
    return txt


def get_stats():
    """
    f_levels = os.path.join(data_folder, 'World_data','DT_GameLevels.csv')
    f_waypoints = os.path.join(data_folder, 'World_data','DT_GameWaypoints.csv')  ---,level_name,location_name,X,Y,Z,biome
    f_level_pickups = os.path.join(data_folder, 'World_data','DT_Pickup_Level_Defaults.csv') ---,level_name,spawn_id_class_name,num_items_to_spawn
    f_waypoint_spawn_pickups = os.path.join(data_folder, 'World_data','DT_Pickup_Locations_Spawn_Pickup.csv')
    f_npcs = os.path.join(data_folder, 'NPC_data','DT_NPCs.csv')
    f_fishing_loot = os.path.join(data_folder, 'DT_Fishing_Loot.csv')
    f_recipes = os.path.join(data_folder, 'Crafting_data', 'DT_craft_recipe.csv')
    f_recipe_ingred = os.path.join(data_folder, 'Crafting_data', 'DT_craft_recipe_ingredients.csv')
    f_builtitem = os.path.join(data_folder, 'Crafting_data', 'DT_BuiltItem.csv')
        
    """
    txt = '<H3>Stats</H3>\n'

    txt += get_stats_for_csv('Items', cfg.f_items, 1)
    txt += get_stats_for_csv('Item Types', cfg.f_items, 6)
    txt += get_stats_for_csv('Levels', cfg.f_levels, 0)
    txt += get_stats_for_csv('Level Biomes', cfg.f_levels, 10)
    
    txt += get_stats_for_csv('Waypoints', cfg.f_waypoints, 0)
    txt += get_stats_for_csv('Waypoint - levels', cfg.f_waypoints, 1)
    txt += get_stats_for_csv('Waypoint - Biomes', cfg.f_waypoints, 6)

    txt += get_stats_for_csv('Level Pickups', cfg.f_level_pickups, 0)
    txt += get_stats_for_csv('Level Pickup Levels', cfg.f_level_pickups, 1)
    txt += get_stats_for_csv('Level Pickup Spawners', cfg.f_level_pickups, 2)
    

 



    return txt


def get_stats_for_csv(desc, fname, col_num):
    """
    read a CSV and gets stats (total) as well as distibution sample from col_num
    """
    lst = html_utils.read_csv_to_list(fname)
    tot_recs = len(lst)
    col_list = [x[col_num] for x in lst]
    

    uniq_col = list(set(col_list))
    sample_ids = uniq_col[0] + ',' + uniq_col[len(uniq_col) - 1]

    word_counts = Counter(uniq_col)
    tot_duplicates = 0
    for wrd in uniq_col:
        if word_counts[wrd] > 1:
            #print(wrd + str(word_counts[wrd]))
            tot_duplicates += 1

    return str(tot_recs) + ' ' + desc + ' (' + str(len(uniq_col)) + ' unique) ' + sample_ids + '<BR>\n'
    #return str(tot_recs), str(tot_duplicates), sample_ids


def get_missing_images():
    txt = '<H3>List of Missing Images</H3>\n'
    txt += 'You need to manually export these from UE4 (Possibly get higher res screenshot if in icon format)<BR>'

    # for all image files in Items and Levels - make sure the approp .PNG exists on disk otherwise
    # list the 'expected PNG' file as well as the original texture name in the ItemsList
    list_items = html_utils.read_csv_to_list(cfg.f_items) # 
    txt += '<table border=1><TR><TD>Item</TD><TD>Missing image file</TD></TR>\n'

    for itm in list_items:
        
        img_file = get_img_for_item(itm[1])
        if not os.path.exists(img_file):
            txt += '<TR><TD>' + itm[1] + '</TD><TD><font color=red>' + itm[0] + '.png' + '</font></td></tr>'
    txt += '</table>'


    return txt

def get_img_for_item(item_id):
    """
    gets the icon for an inventory item
    """
    list_inv = html_utils.read_csv_to_list(cfg.f_items) # 
    
    for inv in list_inv:
        if inv[1] == item_id:

            img_file = os.path.join(cfg.op_folder, 'img', 'items',item_id + '.png')
            #print('img file = ' + img_file)
            return img_file
    return ''            


    
 

if __name__ == '__main__':
    main()


