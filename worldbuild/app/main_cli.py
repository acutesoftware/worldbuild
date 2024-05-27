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
import wb_app_utils as mod_wb

db_file = mod_cfg.db_file
fldr_root = mod_cfg.fldr_root

sys.path.append(fldr_root)

from quest_gen import quest     


def main():
    conn = sqlite3.connect(db_file)
    print('Welcome to Worldbuild CLI App')
    print('===========================================================')
    print('Database = ' + db_file)
    menu(conn)


def menu(conn):
    print('\nEnter Command:')
    print('s. Show stats')
    print('g. Generate...')
    print('v. Verify data')
    print('e. Export mod files')
        
    print('h. Help')
    print('q. Quit')
    ans = input('Enter command: ')
    if ans == 's' :
        mod_wb.show_stats(conn)
        press_enter_to_continue()
    if ans == 'g' :
        generate_menu(conn)
        press_enter_to_continue()
    if ans == 'v' :
        mod_wb.verify_data(conn)
        press_enter_to_continue()
    if ans == 'e' :
        mod_wb.export_mod_files(conn)
        press_enter_to_continue()
    if ans == 'h' :
        show_help()
        press_enter_to_continue()
 
    if ans == 'q' or ans == '':
        sys.exit()
    
    print('===========================================================')
    menu(conn)

def generate_menu(conn):
    print('1. Generate Town layout')
    print('2. Generate Dungeon layout')
    print('3. Generate NPC')
    print('4. Generate Quest')
    print('5. Generate Item')

    print('<Enter> Return to main menu')    
    ans = input('What do you want to generate? ')
    if ans == '1':
        mod_wb.generate_town(conn)
    if ans == '2':
        mod_wb.generate_dungeon(conn)
    if ans == '3':
        mod_wb.generate_npc(conn)
    if ans == '4':
        mod_wb.generate_quest(conn)
    if ans == '5':
        mod_wb.generate_item(conn)
    if ans == '':
        return

    return

def show_help():
    print('\nAdd data for your world to the database using SQLite Browser')
    print('Then run the commands below to export the "mod" file')
    return

def press_enter_to_continue():
    input('Press enter to continue...')
    return


main()    
