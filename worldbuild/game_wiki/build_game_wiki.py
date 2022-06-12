#!/usr/bin/python3
# -*- coding: utf-8 -*-
# build_game_wiki.py

import os
import sys
import csv
import shutil
import wiki_config as cfg

sys.path.append(os.path.join(os.getcwd(), '..'))

import html_utils

def main():
    print("Generating in game wiki pages in " + cfg.op_folder)
    init_op_folder()
    make_page_index()
    make_page_Places()
    make_page_NPCs()

    #op += make_html_level(lvl, lvl_waypoints, lvl_spawners )
       

    #with open(cfg.op_file_main, 'w') as fop:
    #    fop.write(op)

def get_data_levels(lvl_id):
    #check_data_files()
    waypoint_list = read_csv_to_list(cfg.f_waypoints)  # ---,level_name,location_name,X,Y,Z,biome
    waypoint_spawner = read_csv_to_list(cfg.f_waypoint_spawn_pickups) # ---,level_name,location_name,spawn_id_class_name,radius,min_quant,max_quant

    lvl_waypoints = []
    lvl_spawners = []

    for wp in waypoint_list:
        if wp[1] == lvl_id:
            lvl_waypoints.append(wp)
            for spwn in waypoint_spawner:
                if spwn[2] == wp[2]:
                    lvl_spawners.append(spwn)

    return lvl_waypoints, lvl_spawners
 


def make_page_index():
    # make the main page
    ndx_page = os.path.join(cfg.op_folder, 'index.html')
    with open(ndx_page, 'w') as f:
        f.write(html_utils.get_header('Sanct'))
        f.write(get_world_build_menu('index', 'Welcome to Sanct'))
        
        
        f.write('<div id = content><BR><BR>\n')
        for chap_num, chapter in enumerate(cfg.chapters):
            chap_html = chapter[0] + '.html'
            f.write('<a href="' + chap_html + '">Chapter ' + str(chap_num+1) + ' : ' + chapter[0] + '</a><BR>')

            # add short blurb or list based on each main heading
            if chapter[0] == 'Places':
                f.write('Alrona has the following key locations<BR>')
                lvl_list = read_csv_to_list(cfg.f_levels)
                for lvl in lvl_list:
                    if lvl[7] == 'True':  # is level playable
                        lvl_waypoints, lvl_spawners = get_data_levels(lvl[0])

                        f.write(lvl[3] + ' : ' + lvl[4] + '<BR>')

  


        
        f.write(html_utils.get_footer(''))
     

def init_op_folder():
    """
    sets up the html output folder - wipes all existing content first
    """
    # first create the folder where the wiki files will live
    if not os.path.exists(cfg.op_folder):
        print('Creating output folder ', cfg.op_folder)
        os.makedirs(cfg.op_folder)
    #shutil.copyfile(os.path.join(src_fldr, dat['maps'][0]), os.path.join(cfg.op_folder, 'map_full.jpg'))    
    shutil.copyfile(os.path.join('.', 'game_wiki.css'), os.path.join(cfg.op_folder, 'worldbuild.css'))    # NOTE - renamed for library reuse
    shutil.copyfile(os.path.join('.', 'paper-texture.jpg'), os.path.join(cfg.op_folder, 'paper-texture.jpg'))    
 
    # TODO - copy ALL jpgs to wiki_op shutil.copy(os.path.join(src_fldr, '*.jpg'), op_fldr)    
     


def make_page_Places():
    """
    takes the raw data lists and builds it into HTML 
    """
    txt = html_utils.get_header('Sanct')
    txt += '<H1>Places</H1><div id = content><BR><BR>'
    txt += get_world_build_menu('Places', 'Sanct Places')
    lvl_list = read_csv_to_list(cfg.f_levels) # ---,level_filename,full_filename,name,desc,image_med,image_icon,is_playable,is_home,is_locked,biome
    for lvl in lvl_list:
        if lvl[7] == 'True':  # is level playable
            lvl_waypoints, lvl_spawners = get_data_levels(lvl[0])
            cur_level_file = os.path.join(cfg.op_folder, 'Places_' + lvl[0] + '.html')
            
            txt += '<H2><a href=' + cur_level_file + '>' + lvl[3] + '<a/></H2>' 
            txt += '<div>[' + lvl[0] + '] ' + lvl[4] + '</div>'


            # make a page for each level
            with open(cur_level_file, 'w') as f_cur:
                f_cur.write(html_utils.get_header('Sanct'))
                f_cur.write(get_world_build_menu('Places', 'Place - ' + lvl[3]))
                f_cur.write('<div id = content>\n')
                f_cur.write('<div>[' + lvl[0] + '] ' + lvl[4] + '</div>')
                cur_txt = ''

                if len(lvl_waypoints) > 0:
                    cur_txt += '<B>Waypoints</B><BR>\n' 
                    for wp in lvl_waypoints:
                        wp_id = wp[2]
                        if wp[1] == lvl[0]:
                            
                            cur_txt += '<H4>' + wp[2] + '</H4>\n'
                            cur_txt +='is a <a href=biome.html>' + wp[6] + ' biome</a> at ' + wp[3] + ','+ wp[4] + ','+ wp[5] + '\n'
                            
                            cur_txt += '<table border=1><tr><td>'
                            #op += wp[2] + '[' + wp[6] + '] ' + wp[3] + ','+ wp[4] + ','+ wp[5] + '</td></tr>\n'
                            #op += '<TR><TD>'
                            cur_txt += '<table border=1>' #<tr><td>spawned item</td><td>radius</td><td>number spawned</td></tr>\n'
                            for spwn in lvl_spawners:
                                if spwn[1] == lvl[0]:
                                    if spwn[2] == wp_id:
                                        cur_txt += '<TR><TD>' + spwn[0] + '</td><TD>' + spwn[1] + '</td><TD>' + spwn[2] + '</td><TD>' + spwn[3] + '</td><td>' + spwn[4] + '</td><td>' +  spwn[5] + '-' +  spwn[6]  + '</td></tr>\n'
                            cur_txt += '</table>'
                        cur_txt += '</TD></TR></table>'
                f_cur.write(cur_txt)
                f_cur.write(html_utils.get_footer(''))
            #txt += cur_txt
    txt += html_utils.get_footer('')
    with open(cfg.op_file_places, 'w') as fop:
        fop.write(txt)
    #    return txt



def make_page_NPCs():
    """
    build the main NPC page and sub pages if needed 
    ---,NPC_ID,Name,UCS_Preset,Clothes,SpawnLand,SpawnLocation,spawn_direction_Z,is_active,is_shop,shop_filter_include,shop_filter_exclude,sound_welcome,sound_bye,text_welcome,text_bye,animNormal,animSeqBaseWelcome
    """
    txt = html_utils.get_header('Sanct')
    txt += '<H1>NPCs</H1><div id = content><BR>NPCs in game<BR>'

    txt += get_world_build_menu('NPC', 'Sanct NPCs')
    list_npc = read_csv_to_list(cfg.f_npcs) # ---,level_filename,full_filename,name,desc,image_med,image_icon,is_playable,is_home,is_locked,biome
    for npc in list_npc:
        txt += '<H2>' + npc[2] + '</H2>'
        txt += '<div>' + npc[0] + ' lives in <a href="Places_' + npc[5] + '.html">' + npc[5] + '</a> and usually spawns at ' + npc[6] + '</div>\n'
        if npc[9] == 'True':
            txt += 'They sell the following items:<BR>'
            if npc[10] == '':
                txt += '[ALL ITEMS]<BR>'
            else:
                txt +=  npc[10] + '<BR>'
            if npc[11] == '':
                txt += '(no exclusions)<BR>'
            else:
                txt +=  'Except : ' + npc[11] + '<BR>'
        

    txt += html_utils.get_footer('')
    with open(cfg.op_file_npcs, 'w') as fop:
        fop.write(txt)

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

def get_world_build_menu(cur_chap, heading_str):
    lf = chr(13) + chr(10)
    txt = ''
    txt += '<H1>' + heading_str + '</H1>'
    txt += '<div id = "mainMenu"><UL>\n'
    # home page
    if heading_str[0:11] == 'Welcome to ':
        txt += '<DIV ID=mainMenuItem-sel><LI><a href=index.html>Home</a></LI></DIV>'
    else:
        txt += '<DIV ID=mainMenuItem><LI><a href=index.html>Home</a></LI></DIV>'
    
    for chap in cfg.chapters:
        #print('heading_str = ',heading_str , 'chap = ', chap)
        if cur_chap == chap[0]:
        
            txt += '<DIV ID=mainMenuItem-sel><LI><a href=' + chap[0] + '.html>' + chap[0] + '</a></LI></DIV>' + lf
        else:
            txt += '<DIV ID=mainMenuItem><LI><a href=' + chap[0] + '.html>' + chap[0] + '</a></LI></DIV>' + lf
    txt += '</UL></div>\n'
    
    return txt

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
    return rows_to_load[1:]

if __name__ == '__main__':
    main()

