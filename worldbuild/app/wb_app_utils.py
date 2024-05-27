#!/usr/bin/python3
# -*- coding: utf-8 -*-
# wb_app_utils.py

import if_sqllite
import config_app as mod_cfg

def show_stats(conn):
    res = if_sqllite.get_data(conn, 'SELECT src_tbl FROM sys_job_steps WHERE src_tbl IS NOT NULL and job_num = "LOAD_CSV"', [])

    for row in res:
        op = row[0].replace('D:\\dev\\src\\worldbuild\\worldbuild\\data\\wb_appdata\\', '')
        print('CSV File loaded : ' + str(op))


# ----- Verify Data ----------------

def verify_data(conn):
    print('Verifying database.....')
    op = []
    for tbl in mod_cfg.db_tables:
        sql = "SELECT count(*) as numrecs FROM " + tbl
        res = if_sqllite.get_data(conn, sql, [])[0][0]
        op.append([tbl, res])

    for line in op:
        print(line[0], line[1])
    



    return




def generate_town(conn):
    print('Generating Town..')
    return

def generate_dungeon(conn):
    print('Generating Dungeon..')
    import roguelike.dungeon_generator as dg
    grid_y = 15
    grid_x = 70
    NUM_ROOMS = 5
    ROOM_SIZE = 4
    NUM_HORIZ = 2
    lv_SEED = -1
    grd, seed = dg.create_dungeon(grid_y, grid_x, NUM_ROOMS, ROOM_SIZE, NUM_HORIZ, lv_SEED)
    #solved = dg.path_find(grd)
    
    print(dg.grid_as_str( grd))
    return

def generate_npc(conn):
    print('Generating NPC..')
    return

def generate_quest(conn):
    print('Generating Quest..')
    return

def generate_item(conn):
    print('Generating Item..')
    return

# ----- Export MOD Files --------------

def export_mod_files(conn):
    print('Exporting mod files ....')
    return