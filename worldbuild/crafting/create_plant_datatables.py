#!/usr/bin/python3
# -*- coding: utf-8 -*-
# create_plant_datatables.py

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
    using the ItemList.csv, read all plants and make a unique entry for each 
    plant type and make a new data table (CSV here) which has
    - plant base name
    - 1 - 9 SM and textures showing growth stages
    - COMMON name
    - categories (herb, blue, catcus, flower, berry, etc)

    Then, possibly REMOVE the 1-9 plants from inventory and add this entry instead
    otherwise, have a plant lookup data table which is used for crafting (eg any 
    catcus or any thyme plant is good for recipe no matter the plant stage)

    """
    op_file = 'plants.csv'

    print('generating simplified plant database...')
    list_items = html_utils.read_csv_to_list(cfg.f_items) 
    list_plants = html_utils.read_csv_to_list('plant_data_raw.csv') 
    #print(list_plants)
    with open(op_file, 'w') as fop:
        fop.write('invent_id,invent_name,base_name,plant_type,common_name,higher_classification,family,plant_type,plant_height,leaf_size,uses,location,sunlight,water,notes\n')
        for lst in list_items:
            if lst[0].startswith('plant_'):
                fop.write(make_plant_summary_record(lst, list_plants))


def make_plant_summary_record(invent_item, list_plants):
    res = ''
    res += invent_item[1] + ','
    res += invent_item[3] + ','
    res += get_base_name(invent_item[1]) + ','
    res += get_plant_type(invent_item[1]) + ','
    res += lookup_desc(invent_item[1], list_plants)
    res += '\n'
    return res

def get_base_name(nme):
    """
    trims the end of the name to get the base name of a plant 
    to allow grouping
    """
    name_parts = nme.split('_')
    if name_parts[1] in ['flower', 'bush', 'berry']:
        return name_parts[2]
    return nme

def get_plant_type(nme):
    """
    get the plant grouping - probably a lookup table or case statement
    """
    name_parts = nme.split('_')
    if name_parts[1] in ['flower', 'bush', 'berry', 'tree']:
        return name_parts[1]
    return 'misc'


def lookup_desc(itm, list_plants):
    """
    looks up item manually from googling
    """
    txt = ',,,,'
    for plant in list_plants:
        if get_base_name(itm) == plant[0]:
            #print(plant)
            txt = plant[1] + ',' + plant[2] + ',' + plant[3] + ',' + plant[4] + ','
            txt += plant[5] + ',' + plant[6] + ',"' + plant[7] + '",' + plant[8] + ','
            txt += plant[9] + ',' + plant[10] + ',"' + plant[11] + '"'

    return txt




if __name__ == '__main__':
    main()

