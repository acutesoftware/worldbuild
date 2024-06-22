#!/usr/bin/python3
# -*- coding: utf-8 -*-
# t_dungeon.py
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

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".."  )
pth = os.path.join(root_folder, 'worldbuild', 'town_gen')
fldr_img =  os.path.join(root_folder, 'worldbuild', 'app', 'static', 'img')

print ('TOWN_GEN WORLDBUILD PATH = ' + pth)
sys.path.append(pth)


from town_gen import town_gen as mod_tool     

def run_tool(params):
    X_pos = params[0]
    Y_pos = params[1]
    width = params[2]
    length = params[3]
    sparseness  = params[4]

    base_img = fldr_img + os.sep + '2D_town_gen_'
    img_file = base_img + dte() + '.png'
    import glob
    for f in glob.glob(base_img + "*.png"):
        os.remove(f)

    
    res = mod_tool.make_town( 'Starting Town - dense', X_pos, Y_pos, width, length, sparseness)
    res.output_detail(img_file, show_grid='N', launch_image='N')
    content_html =  res.str_as_html()

    img_file_static =  img_file[53:]
    print('img_file_static = ' + img_file_static)
    content_html = '<img width=800px src=' +img_file_static + '>'
    return content_html


def dte():
    from datetime import datetime
    now = datetime.today().isoformat().replace(':','_').replace('.', '_')
    print(now)  # '2018-12-05T11:15:55.126382'    
    return now
