#!/usr/bin/python3
# -*- coding: utf-8 -*-
# hunger_games.py
# this makes an arena map for minecraft

import os
import sys
import minecraft_builder
import castle_maker
import clear_area
import math

style_stone = {'roof':'planks 1', 'walls':'minecraft:stone 0', 'floor':'minecraft:stone 4', 'posts':'minecraft:stone 3'}

x_cent = -351
y_cent = 62
z_cent = 300 #10000
w = 1 #34+18
h = 29
d = 1
r = 50

def main():

    myrcon = castle_maker.rcon_connection()
    #make_circle(x_cent, y_cent, z_cent, r, h, w, d, style_stone['walls'],myrcon)
    #make_circle(x_cent, y_cent, z_cent, r, h, w-1, d, style_stone['posts'],myrcon)
    #make_circle(x_cent, y_cent, z_cent, r, h, w+1, d, style_stone['posts'],myrcon)

    # make the top parapet
    # clear mistake  make_circle(x_cent-1, y_cent+h, z_cent-1, r, h+1, w+1, d+1, 'minecraft:air',myrcon)
    make_circle(x_cent-2, y_cent+h, z_cent-2, r, 2, w+2, d+2, 'minecraft:air',myrcon)
    make_circle(x_cent, y_cent+h, z_cent, r, 2, w+2, d+2, style_stone['posts'],myrcon)
    

def make_circle(x, y, z, radius, height, width, depth, style,myrcon):
    """
    makes a circluar wall
    """
    PI = math.pi
    for angle in range(1, 360, 1):
        angle_rad = angle / PI
        cx = int(x + radius * math.cos(angle_rad))
        cz = int(z + radius * math.sin(angle_rad))
        castle_maker.fill_area(cx, y, cz, cx+width, y+height, cz+depth,style,myrcon)



main()
