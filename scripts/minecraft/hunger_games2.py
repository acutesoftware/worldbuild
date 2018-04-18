#!/usr/bin/python3
# -*- coding: utf-8 -*-
# hunger_games2.py
# this makes another style of arena map for minecraft

import os
import sys
import minecraft_builder
import castle_maker
import clear_area
import math

style_stone = {'roof':'planks 1', 'walls':'minecraft:stone 0', 'floor':'minecraft:stone 4', 'posts':'minecraft:stone 3'}

x_cent = -488
y_cent = 62
z_cent = 25
w = 1
h = 29
d = 1
r = 100

def main():

    myrcon = castle_maker.rcon_connection()

    # main ring wall
    make_circle(x_cent, y_cent, z_cent, r, h, w, d, style_stone['walls'],myrcon)
    make_circle(x_cent, y_cent, z_cent, r-1, h-1, w, d, style_stone['posts'],myrcon)
    make_circle(x_cent, y_cent, z_cent, r-3, h-2, w, d, style_stone['posts'],myrcon)
    make_circle(x_cent, y_cent, z_cent, r-1, h-3, w+1, d+1, style_stone['floor'],myrcon)
    make_circle(x_cent, y_cent, z_cent, r-1, h-3, w+2, d+2, style_stone['floor'],myrcon)

    # tall pillar in centre of arena
    make_circle(x_cent, y_cent-5, z_cent, 5, y_cent+2, 1, 1, style_stone['posts'],myrcon)

    # make the centre part for chests
    make_circle(x_cent, 69, z_cent, 8, 2, 5, 5, style_stone['posts'],myrcon)
    make_circle(x_cent, 68, z_cent, 9, 1, 5, 5, style_stone['posts'],myrcon)
    make_circle(x_cent, 67, z_cent, 11, 1, 5, 5, style_stone['posts'],myrcon)
    make_circle(x_cent, 66, z_cent, 13, 1, 5, 5, style_stone['posts'],myrcon)


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
