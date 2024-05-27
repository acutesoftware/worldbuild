#!/usr/bin/python3
# -*- coding: utf-8 -*-
# main_cli.py
"""
===========================================================
THINGS TO DO
Use this to check the SQLite database for issues with missing data
make a structure of quest lines and generate ALL quests and NPCs
===========================================================
Go to the Start in lvl_grassland and get me a part for my work in Tool Crafter
Go to the town in lvl_grassland and get me a part for my work in Clothes Design
Go to the Highlands in lvl_quarry and get me a part for my work in Weaponsmth
Go to the town in lvl_grassland and get me a part for my work in Baking
Go to the farm_orchid in lvl_doctade and get me a part for my work in Diving
Go to the Highlands in lvl_quarry and get me a part for my work in Stir Fry
Go to the Shed in lvl_quarry and get me a part for my work in Fishing
PS C:\C_DATA\dev\src\PROCGEN\src\genCode\alrona> 
"""

import os
import sys
import time
import random
import sqlite3
import if_sqllite
import config_app as mod_cfg

db_file = mod_cfg.db_file
fldr_root = mod_cfg.fldr_root

sys.path.append(fldr_root)

from quest_gen import quest     


def main():
    conn = sqlite3.connect(db_file)
    print('Welcome to Worldbuild')
    menu()

    show_stats(conn)


def menu():
    print('===========================================================')
    print('THINGS TO DO')
    print('Use this to check the SQLite database for issues with missing data')
    print('make a structure of quest lines and generate ALL quests and NPCs')
    print('===========================================================')


def show_stats(conn):
    res = if_sqllite.get_data(conn, 'SELECT src_tbl FROM sys_job_steps WHERE src_tbl IS NOT NULL and job_num = "LOAD_CSV"', [])

    for row in res:
        op = row[0].replace('D:\\dev\\src\\worldbuild\\worldbuild\\data\\wb_appdata\\', '')
        print('CSV File loaded : ' + str(op))

main()    
