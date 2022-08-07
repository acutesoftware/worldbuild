#!/usr/bin/python3
# -*- coding: utf-8 -*-
# mod_utils.py
#
# Core utilies to generate mods for sanct game.
# Contains standard lists and data structures from the game to be used
# to generate new levels and mods.

import os
import sys
import csv

# Source Data for definitions and game IDs
file_defn_tbls = os.path.join(os.getcwd(), 'data','_defn_mapping_tables.csv')
file_defn_cols = os.path.join(os.getcwd(), 'data','_defn_mapping_columns.csv')
file_defn_func = os.path.join(os.getcwd(), 'data','_defn_mapping_function.csv')


# Output Files for Mods
fldr_op_mod_root = os.path.join(os.getcwd(), 'samples','sanct_mods')

# delim and formatting
delim = ','
newline = '\n'

def verify():
    """
    Self test on initialise to verify all data files
    """
    with open(file_defn_tbls, 'r') as fip:
        print('reading tbls')


def create_level_header():
    """
    creates a Level header record
    id,name,template,biome,image,image_map,pos_X_start,X_end,Y_start,Y_end
    """
    op  = 'id' + delim
    op += 'name' + delim
    op += 'template' + delim
    op += 'biome' + delim
    op += 'image' + delim
    op += 'image_map' + delim
    op += 'X_start' + delim
    op += 'X_end' + delim
    op += 'Y_start' + delim
    op += 'Y_end' 

    return op + newline


def create_level_line(id,name,template,biome,image,image_map,X_start,X_end,Y_start,Y_end):
    """
    creates a Level record
    """
    op = id + delim
    op += name + delim
    op += template + delim
    op += biome + delim
    op += image + delim
    op += image_map + delim
    op += str(X_start) + delim
    op += str(X_end) + delim
    op += str(Y_start) + delim
    op += str(Y_end) 

    return op + newline


def create_npc_line(npc_name):
    """
    creates an NPC record
    char_id
char_name
char_image_icon
char_image_full

    """

    return npc_name + ',,,,,\n' 

def create_item_line(itm_name):
    """
    creates an Item record
    """

    return itm_name + ',,,,,\n' 
