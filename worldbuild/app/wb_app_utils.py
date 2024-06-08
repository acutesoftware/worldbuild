#!/usr/bin/python3
# -*- coding: utf-8 -*-
# wb_app_utils.py

import if_sqllite
import config_app as mod_cfg



def show_logs(conn):
    res = if_sqllite.get_data(conn, 'SELECT src_tbl FROM sys_job_steps WHERE src_tbl IS NOT NULL and job_num = "LOAD_CSV"', [])

    for row in res:
        op = row[0].replace('D:\\dev\\src\\worldbuild\\worldbuild\\data\\wb_appdata\\', '')
        print('CSV File loaded : ' + str(op))

# ----- Find Str ----------------

def find_str(conn):
    f = input('Enter string to find :')
    num_found = 0
    print('Searching for ' + f + ' ...')
    tbl_list = if_sqllite.get_data(conn, 'SELECT * FROM App_menu WHERE "table" is not NULL', [])
    op = []
    for tbl in tbl_list:
        tbl_data = if_sqllite.get_data(conn, 'SELECT * FROM ' + tbl[3] , [])
        if tbl_data:
            for row in tbl_data:
                if f.upper() in str(row).upper():
                    num_found += 1
                    op.append(tbl[3] + ':' + str(row))
                    print(tbl[3] + ':' + str(row))

                    
    print(str(len(op)) + ' results')
    return
        

# ----- Verify Data ----------------

def verify_data(conn):
    tbl_list = if_sqllite.get_data(conn, "SELECT menu,submenu,table_name,col_list_view FROM App_menu", [])
    op = []
    tot_cols = 0
    tot_rows = 0
    for tbl in tbl_list:
        v_tbl = tbl[2]
        v_cols = tbl[3]
        if v_tbl is not None:
            sql = "SELECT " + v_cols + " FROM " + v_tbl
            print('Checking : ' + sql)
            res = if_sqllite.get_data(conn, sql, [])
            tot_rows += len(res)
    print ('All good - read ' + str(tot_rows) + ' rows from ' + str(len(tbl_list)) + ' tables')

    
    return

# ----- Show Stats  ----------------

def show_stats(conn):
    print('Database Stats...')

    tbl_list = if_sqllite.get_data(conn, "SELECT * FROM App_menu", [])
    op = []
    for tbl in tbl_list:
        if tbl[3] is not None:
            v_tbl = tbl[3]
            sql = "SELECT count(*) as numrecs FROM " + v_tbl
            #print('sql = ' + sql)
            res = if_sqllite.get_data(conn, sql, [])
            #print('res = ' + str(res))
            if res is None:
                op.append([tbl[0], tbl[1], tbl[2],  v_tbl, res])
            else:
                op.append([tbl[0], tbl[1], tbl[2],  v_tbl, res[0][0]])
        else:
            res = [['-1']]
            v_tbl = 'no table specified'
            op.append([tbl[0], tbl[1], tbl[2],  'no table specified', '0'])

    for line in op:
        print(str(line))
 
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
