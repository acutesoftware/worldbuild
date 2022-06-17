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
    make_page_Commands()
    make_page_index()
    make_page_Places()
    make_page_NPCs()
    make_page_Items()
    make_page_Food()
    make_page_Item_list_filtered('Plants', 'plant_')
    make_page_Fish()
    make_page_Item_list_filtered('Animals', 'animal_')
    make_page_Item_list_filtered('Clothes', 'cloth_')
    make_page_Tools()
    make_page_Item_list_filtered('Materials', 'build_')

    make_page_crafting()
       
    make_page_DevLog()

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
            f.write('<a href="' + chap_html + '">' + chapter[0] + '</a> - ' + chapter[1] + '<BR>')

            # add short blurb or list based on each main heading
            if chapter[0] == 'Places':
                #f.write('Alrona has the following key locations<BR>')
                lvl_list = html_utils.read_csv_to_list(cfg.f_levels)
                for lvl in lvl_list:
                    if lvl[7] == 'True':  # is level playable
                        lvl_waypoints, lvl_spawners = get_data_levels(lvl[0])

                        #f.write(lvl[3] + ' : ' + lvl[4] + '<BR>')
                        pass
  


        
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
    txt += '<H1>Sanct Game</H1><div id = content><BR><BR>'
    txt += get_world_build_menu('Places', 'Sanct Places')
    lvl_list = html_utils.read_csv_to_list(cfg.f_levels) # ---,level_filename,full_filename,name,desc,image_med,image_icon,is_playable,is_home,is_locked,biome

    cur_txt = ''
    # first make a short list
    for lvl in lvl_list:
        if lvl[7] == 'True':  # is level playable
            txt += '<a href=Places.html#' + lvl[0] + '>' + lvl[4] + '><a/><BR>'
    txt += '<BR><BR>\n'

    # full details
    for lvl in lvl_list:
        if lvl[7] == 'True':  # is level playable
            lvl_waypoints, lvl_spawners = get_data_levels(lvl[0])
            cur_level_file = 'Places.html#' + lvl[0]
            img_file = 'img' + os.sep + 'places' + os.sep + lvl[0] + '.png'
            txt += '<div id=' + lvl[0] + '>\n' 
            txt += '<H2>' + lvl[3] + '</H3>'
            txt += '<a href=' + img_file + '><img align=center Title="' + lvl[4] + '" alt= ' + lvl[4] + ' height=240px width=320px src="' + img_file + '"><a/>'
            # make a section for each level

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
            txt += cur_txt

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
    txt += '<H1>Sanct Game</H1><div id = content><BR>NPCs in game<BR>'

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
    txt += '<H1>Sanct Game</H1><div id = content><BR>Table of all game items<BR>'

    txt += get_world_build_menu('Items', 'Items in the game')
    list_items = html_utils.read_csv_to_list(cfg.f_items) # 
    txt += '<div><table border=1><TR><TD>Item ID</TD><TD>Name</TD><TD>Description</TD><TD>Quality</TD><TD>Type</TD><TD>Stack size</TD><TD>Drops</TD><TD>Type</TD></TR>\n'
    for itm in list_items:
        txt += '<TR id=' + itm[1] + '><TD>'
        txt += '<div><a href=' + get_img_for_item(list_items, itm[1]) + '>'
        txt += itm[1] + '</a>' 
        txt += '<TD>' + itm[2] + '</TD>'
        txt += '<TD>' + itm[3] + '</TD>'
        txt += '<TD>' + itm[4] + '</TD>'  # quality
        txt += '<TD>' + itm[6] + '</TD>'  # type
        txt += '<TD>' + itm[9] + '</TD>'  # stack size
        txt += '<TD>' + itm[10] + '</TD>' # drops
        txt += '<TD>' + itm[16] + '</TD>' # equip type
        txt += '</TR>\n'
    txt += '</table>\n'
    txt += '</div>'

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
    txt += '<H1>Sanct Game</H1><div id = content><BR>'

    txt += get_world_build_menu(filter_list_desc, filter_list_desc + ' in the game')
    list_items = html_utils.read_csv_to_list(cfg.f_items) # 
    list_object_actions = html_utils.read_csv_to_list(cfg.f_object_actions) # 
    list_tool_types = html_utils.read_csv_to_list(cfg.f_tool_type)
    txt += '<DIV><table border=1><TR><TD>Item</TD><TD>Details</TD></TR>\n'

    for itm in list_items:
        #txt += '<H2>' + itm[2] + '</H2>'
        if filter_string.lower() in itm[0].lower():
            txt += '<TR><TD>'
            txt += '<img align=left  width = 50px src="' + get_img_for_item(list_items, itm[1]) + '">'
                    
            txt += '<div><a href="Items.html#' + itm[1] + '">' + itm[2] + '</a>'
            txt += '</td><TD>'
            txt +=  itm[3] + '<BR>'
            txt += '</TD></TR>\n'
    txt += '</table>\n'
    txt += '</div>'

    txt += html_utils.get_footer('')
    with open(opfile, 'w') as fop:
        fop.write(txt)
        


def make_page_Tools():
    """
    build a filtered list of items, but do NOT create pages (aalready done by 'make_page_Items')
    ---,ID,Name,Description,Quality,Icon,ItemType,Amount,IsStackable,MaxStackSize,IsDroppable,WorldMesh,Health,Duration,WeaponActorClass,EquipmentMesh,EquipmentType,EquipmentSlot,Damage,Armor,Strength,Dexterity,Intelligence

    """
    opfile = os.path.join(cfg.op_folder, 'Tools.html' )
    txt = html_utils.get_header('Sanct')
    txt += '<H1>Sanct Game</H1><div id = content><BR>'

    txt += get_world_build_menu('Tools', 'Tool Actions')
    list_items = html_utils.read_csv_to_list(cfg.f_items) # 
    list_object_actions = html_utils.read_csv_to_list(cfg.f_object_actions) # 
    list_tool_types = html_utils.read_csv_to_list(cfg.f_tool_type)
    list_object_types = html_utils.read_csv_to_list(cfg.f_object_type)
    txt += 'when a weilded tool is used on actors below, the functions below are called.<BR>'
    
    txt += '<table border=1><TR><TD>Item</TD><TD>Details</TD></TR>\n'

    for itm in list_items:
        #txt += '<H2>' + itm[2] + '</H2>'
        if 'Tool_' in itm[0]:
            txt += '<TR id=' + itm[1]  + '><TD>'
            txt += '<img align=left  width = 50px src="' + get_img_for_item(list_items, itm[1]) + '">'
                    
            txt += '<div><a href="Items.html#' + itm[1] + '">' + itm[2] + '</a>'
            txt += '</td><TD>'
            txt +=  itm[3] + '<BR>'
            txt += get_tool_actions(list_tool_types, list_object_actions, itm[1])
            txt += '</TD></TR>\n'
    txt += '</table>\n'


    txt += 'For generic objects that the tool can collect / harvest - the drop table is used to work out what items are dropped<BR>'
    txt += '<table border=1><TR><TD>Object Type</TD><TD>Description</TD><TD>If Object Name contains..</TD><TD>might Drop items on Destroy</TD></TR>\n'
    for itm in list_object_types: # ---,object_type,description,object_name_contains,drops_items_on_destroy
        #txt += '<H2>' + itm[2] + '</H2>'

            txt += '<TR><TD>' + itm[1] + '</td>'
            txt += '<TD>' + itm[2] + '</td>'           
            txt += '<TD>' + itm[3] + '</td>'            
            txt += '<TD>' + itm[4] + '</td>'            
            txt += '</TR>\n'
    txt += '</table>\n'


    txt += html_utils.get_footer('')
    with open(opfile, 'w') as fop:
        fop.write(txt)


def make_page_Fish():
    """
    build a filtered list of items, but do NOT create pages (aalready done by 'make_page_Items')
    ---,ID,Name,Description,Quality,Icon,ItemType,Amount,IsStackable,MaxStackSize,IsDroppable,WorldMesh,Health,Duration,WeaponActorClass,EquipmentMesh,EquipmentType,EquipmentSlot,Damage,Armor,Strength,Dexterity,Intelligence

    """
    opfile = os.path.join(cfg.op_folder, 'Fish.html' )
    txt = html_utils.get_header('Sanct')
    txt += '<H1>Sanct Game</H1><div id = content><BR>'

    txt += get_world_build_menu('Fish', 'Fishing and Water forage')
    list_items = html_utils.read_csv_to_list(cfg.f_items) # 
    list_fishing_loot = html_utils.read_csv_to_list(cfg.f_fishing_loot) # 
    list_recipes = html_utils.read_csv_to_list(cfg.f_recipes)
    list_recipe_ingred = html_utils.read_csv_to_list(cfg.f_recipe_ingred)
    txt += 'Make or buy yourself a fishing rod and catch fish for cooking and profit.<BR>'
    
    txt += '<table border=1><TR><TD>img</TD><TD>Fish</TD><TD>Desc</TD><TD>Drop chance</TD><TD>Lands Found</TD><TD>Water Type</TD><TD>Used in Recipes</TD></TR>\n'

    for itm in list_items:
        #txt += '<H2>' + itm[2] + '</H2>'
        if itm[0].startswith('fish_'):
            txt += '<TR id=' + itm[1]  + '><TD>'
            txt += '<img align=left  width = 50px src="' + get_img_for_item(list_items, itm[1]) + '">'
            txt += '</td><TD>'
            txt += '<a href="Items.html#' + itm[1] + '">' + itm[2] + '</a>'  # name
            txt += '</td><TD>'
            txt +=  itm[3]    # desc
            txt += '</td><TD>'
            
            has_loot = 'N'
            for loot in list_fishing_loot:
                if loot[1] == itm[1]:      # land locations
                    txt += loot[2] + '</td><TD>' + loot[3] + '</td><TD>' + loot[4] + '</td><TD>'
                    has_loot = 'Y'
            if has_loot == 'N':
                    txt += '<font color=red>no data</font></td><TD></td><TD></td><TD>'

            txt += get_recipes_for_item(list_items, list_recipes, list_recipe_ingred, itm[1])
            
            txt += '</TD></TR>\n'
    txt += '</table>\n'



    txt += html_utils.get_footer('')
    with open(opfile, 'w') as fop:
        fop.write(txt)



def make_page_Food():
    """
    build a filtered list of items, but do NOT create pages (aalready done by 'make_page_Items')
    ---,ID,Name,Description,Quality,Icon,ItemType,Amount,IsStackable,MaxStackSize,IsDroppable,WorldMesh,Health,Duration,WeaponActorClass,EquipmentMesh,EquipmentType,EquipmentSlot,Damage,Armor,Strength,Dexterity,Intelligence

    """
    opfile = os.path.join(cfg.op_folder, 'Food.html' )
    txt = html_utils.get_header('Sanct')
    txt += '<H1>Sanct Game</H1><div id = content><BR>'

    txt += get_world_build_menu('Food', 'Cooking and Eating')
    list_items = html_utils.read_csv_to_list(cfg.f_items) # 
    list_recipes = html_utils.read_csv_to_list(cfg.f_recipes)
    list_recipe_ingred = html_utils.read_csv_to_list(cfg.f_recipe_ingred)
    list_npcs = html_utils.read_csv_to_list(cfg.f_npcs)
    txt += '<table border=1><TR><TD>img</TD><TD>Food</TD><TD>Desc</TD><TD>Crafted via</TD><TD>Sold by Vendors</TD><TD>Health</TD><TD>Used in Recipes</TD></TR>\n'

    for itm in list_items:
        #txt += '<H2>' + itm[2] + '</H2>'
        if itm[0].lower().startswith('food_'):
            txt += '<TR id=' + itm[1]  + '><TD>'
            txt += '<img align=left  width = 50px src="' + get_img_for_item(list_items, itm[1]) + '">'
            txt += '</td><TD>'
            txt += '<a href="Items.html#' + itm[1] + '">' + itm[2] + '</a>'  # name
            txt += '</td><TD>'
            txt +=  itm[3]    # desc
            txt += '</td><TD>'
            txt += get_item_crafted_via(list_recipes,  itm[1])    # Crafted by
            txt += '</td><TD>'
            txt += get_item_sold_by(list_npcs, itm[1])    # Sold by Vendors
            txt += '</td><TD>'
            txt +=  itm[12]    # health
            txt += '</td><TD>'
            
            txt += get_recipes_for_item(list_items, list_recipes, list_recipe_ingred, itm[1])
            
            txt += '</TD></TR>\n'
    txt += '</table>\n'



    txt += html_utils.get_footer('')
    with open(opfile, 'w') as fop:
        fop.write(txt)




def get_item_crafted_via(lstRecipes, item_id):
    """
    gets the recipe used to craft an inventory item
    """
    txt = ''
    for recipe in lstRecipes:
        if recipe[1] == item_id:
            if recipe[2]  == '':
                workstation = 'Hand'
            else:
                workstation = recipe[6]
            txt += '<a href=Crafting.html#' + recipe[1] + '>' + recipe[2] + 'recipe </a>'
            txt += ' (makes = ' + recipe[5] + ')<BR>'
            txt += ' via ' + workstation + '<BR>'

            
    return txt            

def get_item_sold_by(lstNPCs, item_id):
    """
    gets the recipe used to craft an inventory item
    """
    txt = ''
    for npc in lstNPCs:
        if npc[9] == 'True':
            if npc[10] in item_id or npc[10] == '':
                txt += '<a href=NPC.html#' + npc[1] + '>' + npc[2] + '</a>'  + ' in ' + npc[5] + '<BR>'
            
    return txt            



def get_recipes_for_item(list_items, lstRecipes, lstRecipeIngred, item_id):
    """
    gets details of all recipes used by item
    """
    txt = ''
    recipe_id = ''
    for tpe in sorted(lstRecipeIngred):
        if tpe[2] in item_id:
            recipe_id = tpe[1]
            for lst in lstRecipes:
                if lst[1] == recipe_id:
                    txt += '<img width = 50px src="' + get_img_for_item(list_items, recipe_id) + '">' 
                    txt += '<a href=Crafting.html#' + recipe_id + '>' + lst[1] + '</a><BR>'
    
    return txt

def get_tool_actions(lstToolTypes, lstObjActions, item_id):
    """
    gets a list of tool actions for the tools page (filtered item list)
    """
    txt = ''
    tool_type = 'None'
    for tpe in sorted(lstToolTypes):
        if tpe[4] in item_id:
            tool_type = tpe[1]
    for lst in lstObjActions:
        if lst[2] == tool_type:
            txt += 'when used on "' + lst[1] + '", it calls ' +lst[3] + '<BR>'
    
    return txt

def make_page_crafting(view_type='ICON'):
    """
    crafting page with recipes AND built items
    recipe data = ---,recipe_id,recipe_name,base_time_to_build,base_cost_to_build,num_produced_per_craft,tools_or_workbench_required
    recipe ingred data = ---,recipe_id,item_id,quantity,crafting_method_id
    builtitem data = ---,built_item_id,Built Item Name,level_required,icon,floorplan_img,SM_foundation_for_placing,building_size

    """
    opfile = cfg.op_file_crafting
    txt = html_utils.get_header('Sanct')
    txt += '<H1>Sanct Game</H1><div id = content><BR>'

    txt += '<BR><div id = content><BR>'

    txt += get_world_build_menu('Crafting', 'Crafting recipes')
    list_items = html_utils.read_csv_to_list(cfg.f_recipes) # 
    list_item_ingred = html_utils.read_csv_to_list(cfg.f_recipe_ingred) # 
    txt += '<table border=1><TR><TD>Recipe</TD><TD>Ingredients</TD><TD>Workstation</TD></TR>\n'
    for itm in list_items:
        txt += '<TR id=' + itm[1]  + '><TD valign=top>\n'
        
        # get icon for main recipe
        txt += '<img align=left  width = 50px src="' + get_img_for_item(list_items, itm[1]) + '">'
        txt += '<div><a href="Items.html#' + itm[1] + '">' + itm[2] + '</a>'
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
                    txt += '<img height = 50px title= "' + alt_text + '" alt="' + alt_text + '" src="' + get_img_for_item(list_items, ingr[2] ) + '">'

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
    txt += '<H1>Sanct Game</H1><div id = content><BR>'

    txt += get_world_build_menu('Dev', 'Dev Log and list of errors')
    txt += mod_dev.get_stats()
    txt += mod_dev.get_progress_log()
    txt += mod_dev.get_missing_images()
    
 

    txt += html_utils.get_footer('')
    with open(cfg.op_file_dev, 'w') as fop:
        fop.write(txt)


def make_page_Commands():
    """
    generate the help file with list of commands. NOTE you need
    to run the UE4 GOD mode, then DEV UI, then make help files 
    which generates a CSV list of all commands with subheadings.
    """
    txt = html_utils.get_header('Sanct')
    txt += '<H1>Sanct Game</H1><div id = content><BR>'
    txt += get_world_build_menu('Game', 'Game Play')
    txt += '<div>Explore the lands of Alrona and discover tamable animals in this Open world map (you can go anywhere - like even off the edge of the world if you want)<div>\n'
    txt += '<div>Train and practice crafting recipes to build quality items for sale<div>\n'
    txt += '<div>Compete in Leaderboard challenges for best item, most money earned<div>\n'
    txt += '<div>Decorate your house, make a nice shed and hang out with your pets<div><BR>\n'
    list_items = html_utils.read_csv_to_list(cfg.f_game_help)
    txt += '<table border=0>\n'  # <TR><TD>Command</TD><TD>Description</TD></TR>
    for itm in list_items:
        txt += '<TR><TD valign=top>\n' + itm[0] + '</td><td valign=top>' + itm[1] + '</td></tr>\n'
    txt += '</table>\n'
        
    txt += html_utils.get_footer('')
    with open(cfg.op_file_game_help, 'w') as fop:
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





def get_img_for_item(list_inv, item_id):
    """
    gets the icon for an inventory item
    """
    #list_inv = html_utils.read_csv_to_list(cfg.f_items) # 
    
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

