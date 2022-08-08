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


lvl_id = 'user_level_sample01'
items = ['key','plank']


def main():
    print("generates simple mods from a list in a simplified config file")
    md.verify()
    make_sample_level()
    make_file_npc()
    make_file_items()

####################################################################################################

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

    dat = md.create_level_line(lvl_id,'Sample Map','template','forest','img_lvl_sample1.PNG','img_lvl_sample1.PNG',0,20000,0,20000)
    
    with open(op_file_level, 'w') as fop:
        fop.write(md.create_level_header())
        fop.write(dat)



####################################################################################################

def make_file_npc():

    with open(op_file_npc, 'w') as fop:
        fop.write(md.create_npc_header())
        fop.write(md.create_npc_line('npc_01_sandra','Sandra','Female_Brunette_A', lvl_id, 500,500,1000))
        fop.write(md.create_npc_line('npc_02_george','George','Male_Glasses', lvl_id, 500,2500,1000))
        fop.write(md.create_npc_line('npc_03_dindra','Dindra','Female_Blonde_C', lvl_id, 2500,500,1000))
        fop.write(md.create_npc_line('npc_04_zoltan','Zoltan','Male_Viking', lvl_id, 1500,1500,1000))
        





####################################################################################################



def make_file_items():

    with open(op_file_item, 'w') as fop:
        fop.write(md.create_item_header())
        fop.write(md.create_item_line('wood_frame_stud','Wood Stud for framing','wood_plank_pine', 'mat_wood_rough', 90,35,2400))
        fop.write(md.create_item_line('wood_frame_plate','Wood Plate for framing','wood_plank_pine', 'mat_wood_rough', 90,35,4800))
        fop.write(md.create_item_line('wood_frame_noggin','Wood Noggin for framing','wood_plank_pine', 'mat_wood_rough', 90,35,565))
        fop.write(md.create_item_line('wood_frame_lintel','Wood Lintel for framing','wood_plank_pine', 'mat_wood_rough', 190,35,1800))
        fop.write(md.create_item_line('golden_key','Golden Key','loot_key_base', 'mat_gold', 1,1,1))


main()
    