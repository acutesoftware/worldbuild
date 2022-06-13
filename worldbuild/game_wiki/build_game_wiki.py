#!/usr/bin/python3
# -*- coding: utf-8 -*-
# build_game_wiki.py

import os
import sys
import csv
import shutil
import wiki_config as cfg
import dev_tools as mod_dev
sys.path.append(os.path.join(os.getcwd(), '..'))

import html_utils

def main():
    print("Generating in game wiki pages in " + cfg.op_folder)
    init_op_folder()
    make_page_index()
    make_page_Places()
    make_page_NPCs()
    make_page_Items()
    make_page_Item_list_filtered('Food', 'food_')
    make_page_Item_list_filtered('Plants', 'plant_')
    make_page_Item_list_filtered('Fish', 'fish_')
    make_page_Item_list_filtered('Animals', 'animal_')
    make_page_Item_list_filtered('Clothes', 'cloth_')
    make_page_Item_list_filtered('Tools', 'tool_')
    make_page_Item_list_filtered('Materials', 'build_')

    make_page_crafting()
    #op += make_html_level(lvl, lvl_waypoints, lvl_spawners )
       
    make_page_DevLog()

    #with open(cfg.op_file_main, 'w') as fop:
    #    fop.write(op)

def get_data_levels(lvl_id):
    #check_data_files()
    waypoint_list = html_utils.read_csv_to_list(cfg.f_waypoints)  # ---,level_name,location_name,X,Y,Z,biome
    waypoint_spawner = html_utils.read_csv_to_list(cfg.f_waypoint_spawn_pickups) # ---,level_name,location_name,spawn_id_class_name,radius,min_quant,max_quant

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
                lvl_list = html_utils.read_csv_to_list(cfg.f_levels)
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
    lvl_list = html_utils.read_csv_to_list(cfg.f_levels) # ---,level_filename,full_filename,name,desc,image_med,image_icon,is_playable,is_home,is_locked,biome
    for lvl in lvl_list:
        if lvl[7] == 'True':  # is level playable
            lvl_waypoints, lvl_spawners = get_data_levels(lvl[0])
            #cur_level_file = os.path.join(cfg.op_folder, 'Places_' + lvl[0] + '.html')
            #img_file = os.path.join(cfg.op_folder, 'img', 'places',lvl[0] + '.png')
            cur_level_file = 'Places_' + lvl[0] + '.html'
            img_file = 'img' + os.sep + 'places' + os.sep + lvl[0] + '.png'
            
            txt += '<a href=' + cur_level_file + '><img align=center Title="' + lvl[4] + '" alt= ' + lvl[4] + ' height=240px width=320px src="' + img_file + '"><a/>'
                


            # make a page for each level
            with open(cur_level_file, 'w') as f_cur:
                f_cur.write(html_utils.get_header('Sanct'))
                f_cur.write(get_world_build_menu('Places', 'Place - ' + lvl[3]))
                f_cur.write('<div id = content>\n')
                f_cur.write('<div>[' + lvl[0] + '] ' + lvl[4] + '</div>')
                cur_txt = ''
                
                f_cur.write('<img align=center  width = 800px src="' + img_file + '"><BR>')  #  align=left width = 250px src="' + 'map_' + entry['name'] + '.jpg">'
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


    txt += '<H2>Biomes</H2>'            
    txt += 'The following biomes are in the game<BR>\n'


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
    list_npc = html_utils.read_csv_to_list(cfg.f_npcs) # ---,level_filename,full_filename,name,desc,image_med,image_icon,is_playable,is_home,is_locked,biome
    for npc in list_npc:
        txt += '<H2>' + npc[2] + '</H2>'
        txt += '<div>' + npc[0] + ' lives in <a href="Places_' + npc[5] + '.html">' + npc[5] + '</a> and usually spawns at ' + get_short_coord(npc[6]) + '</div>\n'
        if npc[9] == 'True':
            txt += 'They sell the following items:<BR>'
            if npc[10] == '':
                if npc[11] == '':
                    txt += '[ALL ITEMS]<BR>'
                else:
                    txt +=  'Evertything except for : ' + npc[11] + '<BR>'
            else:
                txt +=  npc[10] + '<BR>'
       

    txt += html_utils.get_footer('')
    with open(cfg.op_file_npcs, 'w') as fop:
        fop.write(txt)


def make_page_Items():
    """
    build the main Object page and sub pages if needed 
    ---,ID,Name,Description,Quality,Icon,ItemType,Amount,IsStackable,MaxStackSize,IsDroppable,WorldMesh,Health,Duration,WeaponActorClass,EquipmentMesh,EquipmentType,EquipmentSlot,Damage,Armor,Strength,Dexterity,Intelligence

    """
    txt = html_utils.get_header('Sanct')
    txt += '<H1>Items</H1><div id = content><BR>Details of in game items<BR>'

    txt += get_world_build_menu('Items', 'Items in the game')
    list_items = html_utils.read_csv_to_list(cfg.f_items) # 
    for itm in list_items:
        itm_id = itm[1].lower()
        #txt += '<H2>' + itm[2] + '</H2>'

        # NOTE - we need to exclude items in the other lists below
        show_this_here = 1
        if 'food_' in itm_id:
            show_this_here = 0
        if 'plant_' in itm_id:
            show_this_here = 0
        if 'fish_' in itm_id:
            show_this_here = 0
        if 'animal_' in itm_id:
            show_this_here = 0
        if 'cloth_' in itm_id:
            show_this_here = 0
        if 'tool_' in itm_id:
            show_this_here = 0
        if 'build_' in itm_id:
            show_this_here = 0

        if show_this_here == 1:
            txt += '<div><a href="Item_' + itm[1] + '.html">' + itm[2] + '</a> = ' + itm[3] + '</div>\n'


    txt += html_utils.get_footer('')
    with open(cfg.op_file_items, 'w') as fop:
        fop.write(txt)

def make_page_Item_list_filtered(filter_list_desc, filter_string):
    """
    build a filtered list of items, but do NOT create pages (aalready done by 'make_page_Items')
    ---,ID,Name,Description,Quality,Icon,ItemType,Amount,IsStackable,MaxStackSize,IsDroppable,WorldMesh,Health,Duration,WeaponActorClass,EquipmentMesh,EquipmentType,EquipmentSlot,Damage,Armor,Strength,Dexterity,Intelligence

    """
    opfile = os.path.join(cfg.op_folder, '' + filter_list_desc + '.html' )
    txt = html_utils.get_header('Sanct')
    txt += '<H1>Items : ' + filter_list_desc + '</H1><div id = content><BR>'

    txt += get_world_build_menu(filter_list_desc, filter_list_desc + ' in the game')
    list_items = html_utils.read_csv_to_list(cfg.f_items) # 
    txt += '<table border=1><TR><TD>Item</TD><TD>Details</TD></TR>\n'

    for itm in list_items:
        #txt += '<H2>' + itm[2] + '</H2>'
        if filter_string.lower() in itm[0].lower():
            txt += '<TR><TD>'
            txt += '<img align=left  width = 50px src="' + get_img_for_item(itm[1]) + '">'
                    
            txt += '<div><a href="Item_' + itm[1] + '.html">' + itm[2] + '</a>'
            txt += '</td><TD>'
            txt +=  itm[3] 
            txt += '</TD></TR>\n'
    txt += '</table>\n'

    txt += html_utils.get_footer('')
    with open(opfile, 'w') as fop:
        fop.write(txt)

def make_page_crafting(view_type='ICON'):
    """
    crafting page with recipes AND built items
    recipe data = ---,recipe_id,recipe_name,base_time_to_build,base_cost_to_build,num_produced_per_craft,tools_or_workbench_required
    recipe ingred data = ---,recipe_id,item_id,quantity,crafting_method_id
    builtitem data = ---,built_item_id,Built Item Name,level_required,icon,floorplan_img,SM_foundation_for_placing,building_size

    """
    opfile = cfg.op_file_crafting
    txt = html_utils.get_header('Sanct')
    txt += '<H1>Recipes and Built Items</H1><div id = content><BR>'

    txt += '<BR><div id = content><BR>'

    txt += get_world_build_menu('Crafting', 'Crafting recipes')
    list_items = html_utils.read_csv_to_list(cfg.f_recipes) # 
    list_item_ingred = html_utils.read_csv_to_list(cfg.f_recipe_ingred) # 
    txt += '<table border=1><TR><TD>Recipe</TD><TD>Ingredients</TD><TD>Workstation</TD></TR>\n'
    for itm in list_items:
        txt += '<TR><TD valign=top>\n'
        
        # get icon for main recipe
        txt += '<img align=left  width = 50px src="' + get_img_for_item(itm[1]) + '">'
        txt += '<div><a href="Item_' + itm[1] + '.html">' + itm[2] + '</a>'
        txt += '</TD><TD valign=top>'
        for ingr in list_item_ingred:
            if ingr[1] == itm[1]:
                if view_type != 'ICON':
                    # DETAIL VIEW
                    txt += ingr[3] + 'x ' + ingr[2]
                    if ingr[4] != 'None':
                        txt += ' (' + ingr[4] + ')'
                    txt += '<BR>'
                else:
                    # ICON VIEW (which everyone likes)
                    alt_text = ingr[3] + 'x ' + ingr[2] 
                    txt += '<img height = 50px title= "' + alt_text + '" alt="' + alt_text + '" src="' + get_img_for_item(ingr[2] ) + '">'

        txt += '</TD><TD>' + get_workstation_nice_name(itm[6]) + '</TD>'
        txt += '</TR>'
    txt += '</table>\n'

    txt += '<H2>Built Items</H2>These are things that are built in place (houses, campfires) or spawnable objects that dont go into your inventory (like animals)<BR>'
    list_items = html_utils.read_csv_to_list(cfg.f_builtitem) # 
    txt += '<table><TR><TD>Built Item</TD><TD>Cost</TD></TR>'
    for itm in list_items:
        img_file = 'img' + os.sep + 'builtitem' + os.sep + itm[1] + '.png'
        txt += '<TR><TD><img align=left  width = 50px src="' + img_file  + '">'
        
        txt += '<div>' + itm[2] +  '</div>\n'
        txt += '</TD><TD>' + itm[3]
        
        txt += '</TD>'
        txt += '</TR>'
    txt += '</table>'

    txt += html_utils.get_footer('')
    with open(opfile, 'w') as fop:
        fop.write(txt)


def make_page_DevLog():
    """
    build a page showing dev log progress AND list of exceptions (missing items in recipes, etc) 
    """
    txt = html_utils.get_header('Sanct')
    txt += '<H1>Dev Log</H1><div id = content><BR>'

    txt += get_world_build_menu('Dev', 'Dev Log and list of errors')
    txt += mod_dev.get_stats()
    txt += mod_dev.get_progress_log()
    txt += mod_dev.get_missing_images()
    
 

    txt += html_utils.get_footer('')
    with open(cfg.op_file_dev, 'w') as fop:
        fop.write(txt)



def get_workstation_nice_name(raw_name):
    if raw_name == '':
        return ''
    if '_Kitchen' in raw_name:
        return 'Kitchen'
    if '_Workbench' in raw_name:
        return 'Workbench'

    if '_Furnace' in raw_name:
        return 'Furnace'

    if '_Pottery' in raw_name:
        return 'Pottery Wheel'

    if 'bucket' in raw_name:
        return 'Bucket'




    return 'UNKNOWN WORKSTATION'





def get_img_for_item(item_id):
    """
    gets the icon for an inventory item
    """
    list_inv = html_utils.read_csv_to_list(cfg.f_items) # 
    
    for inv in list_inv:
        if inv[1] == item_id:

            #img_file = os.path.join(cfg.op_folder, 'img', 'items',item_id + '.png')
            img_file = 'img' + os.sep + 'items' + os.sep + item_id + '.png'
            #print('img file = ' + img_file)
            return img_file
    return ''            





    return '1'


def get_short_coord(long_coord):
    """
    strips off the .0000 stuff from end of coords in UE4
    """

    return long_coord.strip('.000')


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


if __name__ == '__main__':
    main()

