#!/usr/bin/python3
# -*- coding: utf-8 -*-
# clothes_checker.py
import os
import sys
import pandas as pd

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )

import random

def get_fullname(fname):
    """
    gets full filename of crafting data from this folder
    """
    return os.path.join(root_folder,'data','sanct_game', fname)

def main():
    # setup the main dataset definitions here
    items   = pd.read_csv(get_fullname('ItemList.csv'))
    recipes = pd.read_csv(get_fullname('DT_craft_recipes.csv'))
    clothes = pd.read_csv(get_fullname('Cloth_DB.csv'))


    print(clothes)
    #print(items)
    #print(recipes)
    check_items_clothes(items, clothes)
    create_inv_items_all_clothes(items, clothes)

    print('Done')

def create_inv_items_all_clothes(items, clothes):
    print('generating inventory items for both M & F clothing entries')

    # step 1 - loop through clothes table

    # create an inv item for both M & F skeletal meshes

    # save list to CSV to allow manual importing
    # (OR remove all existing clothes entries and force rebuild - NO, dont do this)



def check_items_clothes(items, clothes):
    print('Checking recipes against clothes....')

    clothes_no_recipes = []

    #marks_list = df['Marks'].tolist()
    clothes_ids = clothes['item_id'].tolist()
    inv_ids = items[items.ID.str.startswith('cloth_')]
    
    for clth in clothes_ids:
        exists_in_inv = 0

        for itm in inv_ids:
            # testing on the Skeletal mesh seeing names are different in Cloth and Inv
            #print('itm = ' + str(itm))
            if 'cloth_' in itm:
                #print('inventory cloth item found = _' + itm + '_ ,  cloth = ' + clth)
                if clth.upper() in itm[4:].upper() :
                
                    exists_in_inv += 1
                    print('Found cloth - ' + clth)
        if exists_in_inv == 0:
            clothes_no_recipes.append(clth)

    print(inv_ids)
    print('clothes_no_recipes = ' + str(len(clothes_no_recipes))) 
    print(clothes_ids)

    print('Total cloths = ' + str(len(inv_ids)))



if __name__ == '__main__':
	main()
