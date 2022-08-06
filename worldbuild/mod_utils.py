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


def verify():
    """
    Self test on initialise to verify all data files
    """
    with open(file_defn_tbls, 'r') as fip:
        print('reading tbls')


def create_npc_line(npc_name):
    """
    creates an NPC record
    """

    return npc_name + ',,,,,\n' 

def create_item_line(itm_name):
    """
    creates an Item record
    """

    return itm_name + ',,,,,\n' 
