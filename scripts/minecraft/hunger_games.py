#!/usr/bin/python3
# -*- coding: utf-8 -*-
# hunger_games.py
# this makes an arena map for minecraft

import os
import sys
import minecraft_builder
import castle_maker
import clear_area

style_wood = {'roof':'planks 1', 'walls':'planks 2', 'floor':'planks 3', 'posts':'planks 1'}
style_stone = {'roof':'planks 1', 'walls':'stone 0', 'floor':'stone 4', 'posts':'stone 0'}

x = 12000
y = 90
z = 12000
w = 34+18
h = 6
d = 33


def main():

    myrcon = castle_maker.rcon_connection()
    castle_maker.teleport_player('craftandstore',x-10,y,z, myrcon)
    clear_area.wipe_all(x-1, y, z-1, w+3, h+50, d+3, myrcon)  # TOK clear bottom left corner

    castle_maker.fill_area(x,y,z,x+w,y,z+d, 'minecraft:grass', myrcon)

    # make_castle_walls(start_x, start_y, start_z, width, height, length, wall_width):
    castle_maker.make_castle_walls(x,y,z,w,h,d, 4, myrcon)  # outer wall


main()
