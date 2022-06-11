#!/usr/bin/python3
# -*- coding: utf-8 -*-
# build_game_wiki.py

import os
import sys
import csv
import wiki_config as cfg


def main():
    print("Generating in game wiki pages in " + cfg.op_folder)
    for chap_num, chapter in enumerate(cfg.chapters):
        print('Chapter ' + str(chap_num+1) + ' : ' + chapter[0])
    
    #check_data_files()
    lvl_list = read_csv_to_list(cfg.f_levels) # ---,level_filename,full_filename,name,desc,image_med,image_icon,is_playable,is_home,is_locked,biome
    waypoint_list = read_csv_to_list(cfg.f_waypoints)  # ---,level_name,location_name,X,Y,Z,biome
    waypoint_spawner = read_csv_to_list(cfg.f_waypoint_spawn_pickups) # ---,level_name,location_name,spawn_id_class_name,radius,min_quant,max_quant



    op = '<H1>Places</H1>'
    for lvl in lvl_list:
        if lvl[7] == 'True':  # is level playable
            lvl_id = lvl[0]
            lvl_waypoints = []
            lvl_spawners = []
    
            op += '<H2>' + lvl[3] + '</H2>' 
            op += '<div>[' + lvl[0] + '] ' + lvl[4] + '</div>'
            for wp in waypoint_list:
                if wp[1] == lvl_id:
                    lvl_waypoints.append(wp)
                    for spwn in waypoint_spawner:
                        if spwn[2] == wp[2]:
                            lvl_spawners.append(spwn)

            op += make_html_level(lvl, lvl_waypoints, lvl_spawners )
       

    with open(cfg.op_file_main, 'w') as fop:
        fop.write(op)


def make_html_level(lvl, lvl_waypoints, lvl_spawners):
    """
    takes the raw data lists and builds it into HTML 
    """
    txt = ''

    print('lvl = ' + str(lvl[0]))
    print('lvl_waypoints = ' + str(lvl_waypoints) + '\n\n')
    print('lvl_spawners = ' + str(lvl_spawners))

    if len(lvl_waypoints) > 0:
        txt += '<B>Waypoints</B><BR>\n' 
        for wp in lvl_waypoints:
            wp_id = wp[2]
            if wp[1] == lvl[0]:
                
                txt += '<H4>' + wp[2] + '</H4>\n'
                txt +='is a <a href=biome.html>' + wp[6] + ' biome</a> at ' + wp[3] + ','+ wp[4] + ','+ wp[5] + '\n'
                
                txt += '<table border=1><tr><td>'
                #op += wp[2] + '[' + wp[6] + '] ' + wp[3] + ','+ wp[4] + ','+ wp[5] + '</td></tr>\n'
                #op += '<TR><TD>'
                txt += '<table border=1>' #<tr><td>spawned item</td><td>radius</td><td>number spawned</td></tr>\n'
                for spwn in lvl_spawners:
                    if spwn[1] == lvl[0]:
                        if spwn[2] == wp_id:
                            txt += '<TR><TD>' + spwn[0] + '</td><TD>' + spwn[1] + '</td><TD>' + spwn[2] + '</td><TD>' + spwn[3] + '</td><td>' + spwn[4] + '</td><td>' +  spwn[5] + '-' +  spwn[6]  + '</td></tr>\n'
                txt += '</table>'
            txt += '</TD></TR></table>'
    return txt


def check_data_files():
    """
    check that all data files are valid before building wiki pages
    (and show some stats)
    """    
    read_file(cfg.f_levels)
    read_file(cfg.f_waypoints)
    read_file(cfg.f_level_pickups)
    read_file(cfg.f_waypoint_spawn_pickups)

    read_file(cfg.f_npcs)
    read_file(cfg.f_fishing_loot)
    read_file(cfg.f_items)


def read_file(fname, show_summary=True):
    rows = 0
    with open(fname, 'r') as fip:
        for row_num, row in enumerate(fip):
            #print(str(row_num) + ' = ' + row)
            rows += 1
    print('File ' + fname + ' has ' + str(rows) + ' records')

def read_csv_to_list(filename):
    """
    reads a CSV file to a list
    """
    import csv

    rows_to_load = []
    with open(filename, 'r', encoding='cp1252') as csvfile: # sort of works with , encoding='cp65001'
        #csvreader = csv.reader(csvfile, delimiter = ',' )

        reader = csv.reader(csvfile)

        rows_to_load = list(reader)
    return rows_to_load

if __name__ == '__main__':
    main()

