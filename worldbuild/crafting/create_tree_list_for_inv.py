#!/usr/bin/python3
# -*- coding: utf-8 -*-
# create_tree_list_for_inv.py

import os
import sys
import csv
import shutil
sys.path.append(os.path.join(os.getcwd(), '..', 'game_wiki'))

import wiki_config as cfg
import dev_tools as mod_dev
sys.path.append(os.path.join(os.getcwd(), '..'))

import html_utils

def main():
    """
    using the tree spawner data table, read all tree meshes and make 
    inventory list for appending
    ---,tree_type,name,spawn_in_biomes,grow_chance_at_stage,SM_tree_mesh_at_stage
    """

    op_file = os.path.join(os.getcwd(), '..', 'data', 'sanct_game','World_data','trees_raw.csv')

    print('generating tree list...')
    list_items = html_utils.read_csv_to_list(cfg.f_items) 
    list_trees = html_utils.read_csv_to_list(cfg.f_tree_spawner_types) 
    #print(list_trees)
    tot = 0
    with open(op_file, 'w') as fop:
        fop.write('---,ID,Name,Description,Quality,Icon,ItemType,Amount,IsStackable,MaxStackSize,IsDroppable,WorldMesh,Health,Duration,WeaponActorClass,EquipmentMesh,EquipmentType,EquipmentSlot,Damage,Armor,Strength,Dexterity,Intelligence\n')
        for lst in list_trees:
            cur_tree_meshes = lst[5].split(',StaticMesh')
            #print(cur_tree_meshes)
            for mesh_num, mesh in enumerate(cur_tree_meshes):
                id = 'plant_tree_' + lst[1] + '_' + str(mesh_num+1)
                nme = 'Tree ' + lst[2] + ' ' + str(mesh_num+1)
                msh = mesh.strip(')').strip('")"').strip('\'').strip('"').strip("'").strip("(StaticMesh'\"") 
                tot += 1
                fop.write(id + ',' + nme + ',"(StaticMesh''""' + msh + '""'')\n')

    print('saved ' + str(tot) + ' tree records to ' + op_file)



if __name__ == '__main__':
    main()

