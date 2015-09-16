#!/usr/bin/python3
# -*- coding: utf-8 -*-
# wiki.py
import os
import sys
import config
import sample
import pprint
import shutil
import html_utils
import image_utils

def main():
    """
    manages the wiki pages
    To generate new pages, use the command 
    > python wiki.py samples
    """
    print('creating sample wiki from command line')
    source_path = os.path.join('samples','alrona')
    source_yaml = os.path.join(source_path,'alrona.yaml')
    wiki_folder = os.path.join(source_path,'wiki_op')
    create_wiki_from_yaml(source_path, source_yaml, wiki_folder)
    print('remember, to run from cmd line = > python wiki.py samples/filename.yaml')    

def create_wiki_from_yaml(src_fldr, fname, op_fldr):
    dat = sample._read_yaml(fname)
    if 'wiki' not in dat:
        print('missing wiki: Yes tag, so cant generate wiki for ' + fname)
        return
    if 'contents' not in dat:
        print('missing content tag, so cant generate wiki for ' + fname)
        return

    # first create the folder where the wiki files will live
    if not os.path.exists(op_fldr):
        print('Creating output folder ', op_fldr)
        os.makedirs(op_fldr)
    shutil.copyfile(os.path.join(src_fldr, dat['maps'][0]), os.path.join(op_fldr, 'map_full.jpg'))    
    shutil.copyfile(os.path.join(src_fldr, 'worldbuild.css'), os.path.join(op_fldr, 'worldbuild.css'))    
    shutil.copyfile(os.path.join(src_fldr, 'paper-texture.jpg'), os.path.join(op_fldr, 'paper-texture.jpg'))    
    
    # make a medium size image of the full map for main page
    image_utils.make_map_medium(os.path.join(src_fldr, dat['maps'][0]),  os.path.join(op_fldr, 'map_med.jpg'))
    
    
    # make the main page
    ndx_page = os.path.join(op_fldr, dat['world_name'] + '.html')
    with open(ndx_page, 'w') as f:
        f.write(html_utils.get_header(dat['world_name']))
        f.write(get_world_build_menu(dat, 'Welcome to ' + dat['world_name']))
        
        f.write('<div id = content><div id = "map">\n')
        f.write('<center><a href="map_full.jpg"><img src="map_med.jpg"></a></center><BR>') #YUCK - hard coded CSS - TODO
        f.write('<BR><BR><BR><BR><BR><BR><BR><BR><BR><BR></div>\n')

        
        f.write(html_utils.get_footer(''))
            
    # make the individual pages
    for chap in dat['contents']:
        op_file = os.path.join(op_fldr, chap + '.html')
        with open(op_file, 'w') as f2:
            f2.write(html_utils.get_header(dat['world_name']))
            f2.write(get_world_build_menu(dat, dat['world_name'] + ': ' + chap))
            f2.write(format_yaml_section(dat[chap], chap, dat, src_fldr, op_fldr))
            f2.write(html_utils.get_footer(''))
            
def get_world_build_menu(d, heading_str):
    lf = chr(13) + chr(10)
    txt = ''
    txt += '<H1>' + heading_str + '</H1>'
    txt += '<div id = "mainMenu"><UL>\n'
    page_name = heading_str[heading_str.find(':') + 1:].strip(' ')
    print(page_name)
    # home page
    if heading_str[0:11] == 'Welcome to ':
        txt += '<DIV ID=mainMenuItem-sel><LI><a href=' + d['world_name'] + '.html>Home</a></LI></DIV>'
    else:
        txt += '<DIV ID=mainMenuItem><LI><a href=' + d['world_name'] + '.html>Home</a></LI></DIV>'
    
    for chap in d['contents']:
        #print('heading_str = ',heading_str , 'chap = ', chap)
        if page_name == chap:
        
            txt += '<DIV ID=mainMenuItem-sel><LI><a href=' + chap + '.html>' + chap + '</a></LI></DIV>' + lf
        else:
            txt += '<DIV ID=mainMenuItem><LI><a href=' + chap + '.html>' + chap + '</a></LI></DIV>' + lf
    txt += '</UL></div>\n'
    
    return txt

def format_yaml_section(dct, nme, d, src_fldr, op_fldr):
    """
    takes a dictionary from the yaml file which is a section, and
    formats this as HTML
    nme is a fudge to determine if it is a settlement, meaning we 
    have to do some image crunching - TODO
    """
    print('creating wiki page for ', nme)
    txt = '<div id = content><BR>'
    orig_map = os.path.join(src_fldr, d['maps'][0])
    for entry in dct:
        txt += '<h2>' + entry['name'] + '</h2>'
        if nme == 'settlements':
            # split the map into chunks for pages
            map_subfile = os.path.join(op_fldr, 'map_' + entry['name'] + '.jpg')
            image_utils.extract_map_fragment(orig_map, entry['coords_x_y'], map_subfile)
    
            txt += '<img align=left width = 250px src="' + 'map_' + entry['name'] + '.jpg">'
            txt += '<p>' + entry['desc'] + '</p><BR><BR><HR>'
        else:    
            if 'desc' in entry:
                txt += '<p>' + entry['desc'] + '</p><BR><HR>'
            
            if 'file' in entry:
                txt += read_ext_file(os.path.join(src_fldr, entry['file']))
        
    return txt
    
def format_text(txt, op_format='MD', console=True):
    res = str(txt)
    if console == True:
        print(res)
    return res

def read_ext_file(fname):
    txt = '<h3>File: ' + os.path.basename(fname) + '</h3><p>'
    with open(fname, 'r') as f:
        for line in f:
            txt += line + '<BR>'
    txt += '</p><BR>'
    return txt


if __name__ == '__main__':    
    main()    
    
 