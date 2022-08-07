#!/usr/bin/python3
# -*- coding: utf-8 -*-
# mod_gen_simple.py

import os
import sys
import csv
import mod_utils as md

op_folder = os.path.join(md.fldr_op_mod_root, 'simple' )

op_file_npc = os.path.join(op_folder,'mod_simple_npc.csv')
op_file_item = os.path.join(op_folder,'mod_simple_item.csv')
op_file_level = os.path.join(op_folder,'mod_simple_level.csv')

npcs = [
    'frank','jane','alex','simon','mary'
]

items = ['key','plank']


def main():
    print("generates simple mods from a list in a simplified config file")
    md.verify()
    make_sample_level()
    make_file_npc()
    make_file_items()

def make_sample_level():
    """
    env_level_template,env,file,file of the template used for the map
    env_level_biome,env,biome,"default biome of the level (decides spawner types ONLY, not paint layers)"
    env_level_image,env,image,small screenshot of the level to show on selection screen
    env_level_image_map,env,image,top view showing map of the level
    env_level_pos_X_start,env,location,starting X pos of level - used to add blocking volume for map edges
    env_level_pos_X_end,env,location,end X pos of level - used to add blocking volume for map edges
    env_level_pos_Y_start,env,location,starting Y pos of level - used to add blocking volume for map edges
    env_level_pos_Y_end,env,location,end Y pos of level - used to add blocking volume for map edges
    """

    dat = md.create_level_line('user_map_01','Sample Map','template','forest','img_lvl_sample1.PNG','img_lvl_sample1.PNG',0,20000,0,20000)
    
    with open(op_file_level, 'w') as fop:
        fop.write(md.create_level_header())
        fop.write(dat)





def make_file_npc():
    npc_txt = ''
    for npc in npcs:
        npc_txt += md.create_npc_line(npc)

    with open(op_file_npc, 'w') as fop:
        fop.write(npc_txt)

def make_file_items():
    itm_txt = ''
    for itm in items:
        itm_txt += md.create_item_line(itm)

    with open(op_file_item, 'w') as fop:
        fop.write(itm_txt)


main()
    