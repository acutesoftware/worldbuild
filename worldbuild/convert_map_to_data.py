#!/usr/bin/python3
# -*- coding: utf-8 -*-
# convert_map_to_data.py
import os
import sys
import config
import sample
import pprint
import shutil
import operator

import html_utils
import image_utils
import aikif.toolbox.image_tools as mod_img

def trace(fn):

    def build_trace_line(fn, args, ret_val):
        return "   " + fn.__name__ + str(args) + " -> " + str(ret_val) + "\n"

    def wrapper(*args):
        ret_val = fn(*args)
        trace_line = build_trace_line(fn, args, ret_val)
        print(trace_line.ljust(10))
        return ret_val

    return wrapper

@trace
def extract_data_from_map(fname):
    """
    read in a jpg file containing a map and attempt to 
    identify features such as sea, land, forest, roads 
    and towns using image recognition.
    """
    print('reading ', fname)
    from PIL import Image

    # size is width/height
    img = Image.open(fname)
    width, height = img.size
    print(img)
    pixels = img.load()
    all_pixels = []
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y]
            all_pixels.append(cpixel)
    
    print(all_pixels[0:10])
    
    # get a histogram of colours
    
    colours = {}
    for p in all_pixels:
        if p in colours:
            colours[p] += 1
        else:
            colours[p] = 1
    
    sorted_x = sorted(colours.items(), key=operator.itemgetter(1))
    for k, v in sorted_x:
        if v > 100:
            print(k,v)
    
    # identify sea - blue
    
    # identify land - Non blue
    
    # identify roads - brown
    
    # identify desert - yellow
    
    # identify forest - green
    
    # identify towns - small black circle, with brown roads leading out
    
if __name__ == '__main__':    
    extract_data_from_map(os.path.join(os.getcwd(), 'samples','alrona', 'wiki_op', 'map_Slyk.jpg'))