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

style_wood = {'roof':'planks 1', 'walls':'planks 2', 'floor':'planks 3', 'posts':'planks 1'}
style_stone = {'roof':'planks 1', 'walls':'stone 0', 'floor':'stone 4', 'posts':'stone 0'}

x = 12000
y = 58
z = 12000
w = 34+18
h = 12
d = 33
r = 75

def main():

    myrcon = castle_maker.rcon_connection()
    castle_maker.teleport_player('craftandstore',x-10,y,z, myrcon)

    PI = math.pi
    for angle in range(1, 360, 1):
        angle_rad = angle / PI
        cx = int(x + r * math.cos(angle_rad))
        cz = int(z + r * math.sin(angle_rad))
        print('angle=', angle, ' x=', cx, ', z = ', cz)
        castle_maker.fill_area(cx-2, y, cz-2, cx+2, y+h, cz+2, 'minecraft:stone 0',myrcon)



main()
