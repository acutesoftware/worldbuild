#!/usr/bin/python3
# -*- coding: utf-8 -*-
# t_EXAMPLE.py
"""
python files with t_*.py are for use in the Tools menu of worldbuild.
You need to make sure your python tool has the following functions
res = run_tool(params) returns HTML_output showing the result of the tool
html = build_form(params, param_defaults)
param_values = get_form_results(params)

"""

import os
import sys

# TODO - if you need imports for your tool, add them here
# root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".."  )
# pth = os.path.join(root_folder, 'worldbuild', 'roguelike')
# sys.path.append(pth)
# import dungeon_generator as dg

def run_tool(params):
    param1 = params[0]
    param2 = params[1]
    param3 = params[2]
    html =''
    # code to run your tool goes here - it needs to return HTML
    
    html ='Example Tool : sum of params = ' + str( param1 + param2 + param3 ) + '<BR><BR>'


    html+= '<div>Welcome to the example Tool!<BR>You can have any number of tools, and add remove as you see fit.<BR>'
    html+= 'Note that these tools are all python programs and do NOT have and security or authentication implemented.</div>'
    html += '<div><I>This is designed for a desktop and should not be shared on a network</I></div>'

    html+= '<H3>How to configure your Example tool</h3>'
    html+= '<LI>Create a new python script called <code>t_[YOUR_TOOL].py</code> in the app folder (make a copy of t_EXAMPLE.py)'
    html+= '<LI>Implement the function: <code>run_tool</code>'
    html+= '<LI>Add an entry to <code>config_app.py</code> with the tool definition (?? or the SQLlite table)'
    html+= '<LI>Optional: create the following images <code>t_[YOUR_TOOL].jpg, t_[YOUR_TOOL]_icon.jpg, </code> and copy to /app/static/img'
    html+= '<LI>Go to the tools menu and run your tool'
    
    # return the HTML for the WorldBuild app
    return html
    
