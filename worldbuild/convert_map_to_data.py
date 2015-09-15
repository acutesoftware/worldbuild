#!/usr/bin/python3
# -*- coding: utf-8 -*-
# convert_map_to_data.py
import os
import sys
import config
import sample
import pprint
import shutil
import html_utils
import image_utils
import aikif.toolbox.image_tools as mod_img


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
    
    # identify sea - blue
    
    # identify land - Non blue
    
    # identify roads - brown
    
    # identify desert - yellow
    
    # identify forest - green
    
    # identify towns - small black circle, with brown roads leading out
    
extract_data_from_map(os.path.join(os.getcwd(), 'samples','alrona', 'wiki_op', 'map_Slyk.jpg'))