#!/usr/bin/python3
# -*- coding: utf-8 -*-
# t_gen_world.py
"""
python files with t_*.py are for use in the Tools menu of worldbuild.
You need to make sure your python tool has the following functions
res = run_tool(params) returns HTML_output showing the result of the tool
(NO - this is in mod_wb) html = build_form(params, param_defaults)
(NOT NEEDED) param_values = get_form_results(params)

"""

import os
import sys
import time

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + ".." )
pth = root_folder + os.sep + 'virtual-AI-simulator' + os.sep + 'vais'
sys.path.append(pth)
import world_generator as mod_wrld
import worlds as my_world
output_folder = r'/home/duncan/dev/src/python/worldbuild/worldbuild/app/static/img/'
temp_file_image = os.path.join(output_folder, 'gridworld_latest.png')

base_img = r'/home/duncan/dev/src/python/worldbuild/worldbuild/app/static/img/gridworld_'

import glob
for f in glob.glob(base_img + "*.png"):
    os.remove(f)


def run_tool(params):
    width       =  params[0] # int(get_val('width', params))
    height      =  params[1] # int(get_val('height', params))
    num_seeds   =  params[2] # int(get_val('num_seeds', params))
    perc_land   =  params[3] # int(get_val('perc_land', params))
    perc_sea    =  params[4] # int(get_val('perc_sea', params))
    perc_blocked=  params[5] # int(get_val('perc_blocked', params))
        
    iterations  =  params[6] #int(get_val('iterations', params))
    num_agents  =  params[7] #int(get_val('num_agents', params))

    img_file = base_img + dte() + '.png'
    w = mod_wrld.build_world(height, width, num_seeds, perc_land, perc_sea, perc_blocked)
    for i in range(1, iterations):
        w.add_mountains()

    w.save_grid_to_image(img_file, 'N')

    img_file_static =  img_file[53:]
    #print('img_file_static = ' + img_file_static)
    #content_html = '<img width=800px src=' + img_file_static + '>'
    content_html = '<img src=' + img_file_static + '>'
    return content_html    
    


def dte():
    from datetime import datetime
    now = datetime.today().isoformat().replace(':','_').replace('.', '_')
    return now
    
