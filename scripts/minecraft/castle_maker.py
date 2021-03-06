#!/usr/bin/python3
# -*- coding: utf-8 -*-
# castle_maker.py


import os
import sys
import minecraft_builder as mcb

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." )
pth = root_folder + os.sep + 'worldbuild'

sys.path.append(pth)

import mcrcon

mycon = None    # this is the network rcon object that will be set by calling program


style_stone = {'base':'stone 0', 'side':'cobblestone 0', 'corner':'stone 6'}
style_wood = {'base':'planks 1', 'side':'planks 2', 'corner':'stone 0'}
style_wool = {'base':'wool 1', 'side':'wool 2', 'corner':'wool 0'}
style_gate1 = {'base':'stonebrick 0', 'side':'cobblestone 0', 'corner':'stone 6'}


"""
start_x = 30
start_y = 63
start_z = 30
width = 16
height = 6
length = 28
"""


North = (1,0)
South = (-1, 0)
East = (0, 1)
West = (0, -1)

touchups = []  # must be done after all walls, structures complete to avoid overwrites



def TEST():
    """
    build a castle
    start_x = 30
    start_y = 63
    start_z = 30
    width = 12
    height = 4
    length = 18
    def wipe_area():
        res = []
        res.append('@Minecraft Server')
        res.append(mc_fill(start_x,start_y-1,start_z,start_x+width,start_y+height+2,start_z+length, 'minecraft:air 0'))
        mcb.make_from_list(res)

    """
    #make_castle_walls(30,63,30,12,4,18, 2)  # small walls
    #make_castle_walls(30,63,30,10,3,6, 0)  # tiny walls
    make_castle_walls(30,63,30,20,7,30, 4)  # large walls

def fill_area(x1,y1,z1,x2,y2,z2, item, myrcon=None):
    res = []
    res.append('@Minecraft Server')
    res.append(mc_fill(x1,y1,z1,x2,y2,z2,item))

    mcb.make_from_list(res, myrcon)

def plant(x1,z1,x2,z2,y1, item, myrcon=None): # 'wheat',
    res = []
    res.append('@Minecraft Server')
    res.append(mc_fill(x1,y1-2,z1,x2,y1+3,z2,'minecraft:air'))  # clear area vertically
    res.append(mc_fill(x1,y1-2,z1,x2,y1,z2,'minecraft:planks 0'))  # put dirt underneath to hold water

    # lay fence in lines
    res.append(mc_fill(x1,y1+1,z1,x1,y1+1,z2,'minecraft:fence 0 '))
    res.append(mc_fill(x2,y1+1,z1,x2,y1+1,z2,'minecraft:fence 0 '))
    res.append(mc_fill(x1,y1+1,z1,x2,y1+1,z1,'minecraft:fence 0 '))
    res.append(mc_fill(x1,y1+1,z2,x2,y1+1,z2,'minecraft:fence 0 '))

    res.append(mc_fill(x1+1,y1,z1+1,x2-1,y1,z2-1,'minecraft:farmland 7'))


    #fill_area(x1,y1-1,z1,x2,y2-1,z2, item)
    for z in range(z1+1, z2):
        for x in range(x1+1, x2):
            if x % 4 == 0 and z % 4 == 0:
                if x % 8 == 0:
                    res.append('/setblock ' + str(x) + ' ' + str(y1+1) + ' ' + str(z) + ' ' + 'fence')
                    res.append('/setblock ' + str(x) + ' ' + str(y1+1) + ' ' + str(z) + ' ' + 'torch 0')
                else:
                    res.append('/setblock ' + str(x) + ' ' + str(y1) + ' ' + str(z) + ' ' + 'water')
            else:
                res.append('/setblock ' + str(x) + ' ' + str(y1+1) + ' ' + str(z) + ' ' + item)

    mcb.make_from_list(res, myrcon)

def make_castle_walls(start_x, start_y, start_z, width, height, length, wall_width, rcon=None):
    touchups = []
    with open('last_build.log', 'w') as f:
        f.write('Building Castle - \n')
        f.write('start_x = ' + str(start_x)  + ', start_y = ' +  str(start_y)  + ', start_z = ' +  str(start_z)  + '\n' )
        f.write('width   = ' + str(width)    + ', height = ' +  str(height)  + ', length = ' +  str(length)  + '\n' )




    #mcb.make_from_list(castle_wall(start_x+wall_width,start_y,start_z+length,North, width ,height, style_wool))
    #mcb.make_from_list(castle_wall(start_x+width,start_y,start_z+wall_width, East, length, height, style_wood))

    mcb.make_from_list(castle_wall(start_x,start_y,start_z,North, width,height, style_stone, wall_width), rcon) # TOK
    mcb.make_from_list(castle_wall(start_x,start_y,start_z,East,  length,height, style_stone, wall_width), rcon) # TOK

    mcb.make_from_list(castle_wall(start_x,start_y,start_z+length-wall_width,North, width ,height, style_stone, wall_width), rcon)
    mcb.make_from_list(castle_wall(start_x+width-wall_width,start_y,start_z, East, length, height, style_stone, wall_width), rcon)

    mcb.make_from_list(touchups, rcon)


def castle_wall(x,y,z,direction, length, height, style, wall_width):
    """
    creates a build list
    """
    base = style['base']
    corner = style['corner']
    side = style['side']
    res = []
    res.append('@Minecraft Server')



    if direction[0] == 0:   # East / West
        x1 = x
        z1 = z
        y1 = y
        x2 = x+wall_width
        y2 = y+height
        z2 = z+length * direction[1]
        res.append(mc_fill(x1,y1,z1,x2,y2,z2, 'minecraft:' + side))
        res.append(mc_fill(x1,y1,z1,x2,y1+0,z2, 'minecraft:' + base))

        # corner base support
        touchups.append(mc_fill(x1,y1+1,z1,x1,y1+1,z1+1, 'minecraft:' + corner))
        touchups.append(mc_fill(x1,y1+1,z1,x1,y1+2,z1+0, 'minecraft:' + corner))

        touchups.append(mc_fill(x1,y1+1,z2-1,x1,y1+1,z2, 'minecraft:' + corner))
        touchups.append(mc_fill(x1,y1+1,z2-0,x1,y1+2,z2, 'minecraft:' + corner))



        # battlements (also known as crenellations)
        for n in range(z1, z2, 2):
            res.append(mc_fill(x1,y2+1,n,x1,y2+1,n, 'minecraft:' + side))
            res.append(mc_fill(x2,y2+1,n,x2,y2+1,n, 'minecraft:' + side))

            if n % 4 == 0:  # torches every 4*2 blocks
                res.append('/setblock ' + str(x1) + ' ' + str(y2+2) + ' ' + str(n) + ' torch 0')  # torch on inner wall
                res.append('/setblock ' + str(x2) + ' ' + str(y2+2) + ' ' + str(n) + ' torch 0')  # torch on outer wall

        # corner pillars - stone pillars on inside
        res.append(mc_fill(x1,y1-2,z1,x1,y2,z1, 'minecraft:' + corner))
        res.append(mc_fill(x1,y1-2,z2,x1,y2,z2, 'minecraft:' + corner))

        res.append(mc_fill(x2,y1-2,z1,x2,y2,z1, 'minecraft:' + corner))
        res.append(mc_fill(x2,y1-2,z2,x2,y2,z2, 'minecraft:' + corner))
        """
        # now top inverted stair on top rail all the way around
        # Bits	Description
        0x1
        0x2	A two-bit field containing a value from 0 to 3 specifying the direction of the stairs' full-block side:
        0: East
        1: West
        2: South
        3: North
        0x4	Set if stairs are upside-down
        """
        #castle_maker.fill_area(30,63,30,150,66,30, 'minecraft:air')   # front wall across very front

        # front wall lip
        #res.append(mc_fill(x1,y1,z1,x2,y2-1,z1, 'minecraft:air'))  # make the lower wall insetted  (NO -
        res.append(mc_fill(x1,y2-1,z1-1,x2,y2-1,z1-1, 'minecraft:stone_brick_stairs 6'))  # front wall (need to tidy over gate)
        res.append(mc_fill(x1,y2-1,z2+1,x2,y2-1,z2+1, 'minecraft:stone_brick_stairs 7'))
        res.append(mc_fill(x1-1,y2-1,z1,x1-1,y2-1,z2, 'minecraft:stone_brick_stairs 4'))
        res.append(mc_fill(x2+1,y2-1,z1,x2+1,y2-1,z2, 'minecraft:stone_brick_stairs 5'))




    else:                   # North / South
        x1 = x
        z1 = z
        y1 = y
        x2 = x+length * direction[0]
        y2 = y+height
        z2 = z+wall_width

        res.append(mc_fill(x1,y1,z1,x2,y2,z2, 'minecraft:' + side))
        res.append(mc_fill(x1,y1,z1,x2,y1+0,z2, 'minecraft:' + base))

        # corner base support
        touchups.append(mc_fill(x1,y1+1,z1,x1+1,y1+1,z1, 'minecraft:' + corner)) #
        touchups.append(mc_fill(x1,y1+1,z1,x1+0,y1+2,z1, 'minecraft:' + corner))
        touchups.append(mc_fill(x2-1,y1+1,z1,x2,y1+1,z1, 'minecraft:' + corner))
        touchups.append(mc_fill(x2-0,y1+1,z1,x2,y1+2,z1, 'minecraft:' + corner))


        #battlements
        for n in range(x1, x2, 2):
            res.append(mc_fill(n,y2+1,z1,n,y2+1,z1, 'minecraft:' + side))
            res.append(mc_fill(n,y2+1,z2,n,y2+1,z2, 'minecraft:' + side))
            #res.append('/setblock ' + str(n) + ' ' + str(y2+2) + ' ' + str(z1) + ' torch 0')  # torch on inner wall

            if n % 4 == 0:  # TODO - if length/width < 7 then torch every block ELSE torches every 4*2 blocks
                res.append('/setblock ' + str(n) + ' ' + str(y2+2) + ' ' + str(z1) + ' torch 0')  # torch on outer wall
                res.append('/setblock ' + str(n) + ' ' + str(y2+2) + ' ' + str(z2) + ' torch 0')  # torch on inner wall

        # corner pillars - stone pillars on inside
        res.append(mc_fill(x1,y1-2,z1,x1,y2,z1, 'minecraft:' + corner)) #'minecraft:wool 1')) # corner))
        res.append(mc_fill(x1,y1-2,z2,x1,y2,z2, 'minecraft:' + corner)) #'minecraft:wool 2')) # corner))

        res.append(mc_fill(x2,y1-2,z1,x2,y2,z1, 'minecraft:' + corner)) #'minecraft:wool 3')) #corner))
        res.append(mc_fill(x2,y1-2,z2,x2,y2,z2, 'minecraft:' + corner)) #'minecraft:wool 4')) #corner))

        # front wall lip
        #res.append(mc_fill(x1,y1,z1,x2,y2-1,z1, 'minecraft:air'))  # make the lower wall insetted  (NO -
        res.append(mc_fill(x1,y2-1,z1-1,x2,y2-1,z1-1, 'minecraft:stone_brick_stairs 6'))  # front wall (need to tidy over gate)
        res.append(mc_fill(x1,y2-1,z2+1,x2,y2-1,z2+1, 'minecraft:stone_brick_stairs 7'))
        res.append(mc_fill(x1-1,y2-1,z1,x1-1,y2-1,z2, 'minecraft:stone_brick_stairs 4'))
        res.append(mc_fill(x2+1,y2-1,z1,x2+1,y2-1,z2, 'minecraft:stone_brick_stairs 5'))


    return res

def tower_building(x, y, z, width, height, length, butt_height, style=style_stone, myrcon=None):
    """
    make a tower building with some multi width blocks to give
    some detail
    """
    res = []
    res.append('@Minecraft Server')

    # ground floor
    res.append(mc_fill(x,y,z,x+width,y+butt_height,z+length, 'minecraft:' + style['side'] + ' hollow'))

    # top floor - remaining height
    res.append(mc_fill(x+1,y+butt_height,z+1,x+width-2,y + height,z+length-2, 'minecraft:' + style['corner'] + ' hollow'))

    # windows
    torch_name = ' wool ' # ' torch '   # to switch between floating wool colours and torchs (painful to set)
    if width < 15:  # simple window with torch on normal towers (across vert axis)
        x_pos = x + (width/2)
        z_pos = z + (length/2)
        floor_height = 0
        for y_pos in range(y+2, y+height-2, 5):
            # floor
            if floor_height == 0:
                floor_height = y_pos-y+2  # take the first iteration as floor height of tower
            res.append(mc_fill(x+2,y_pos-2,z+2,x+width-3,y_pos-2,z+length-3, 'minecraft:planks 1'))

            # windows
            res.append(mc_fill(x-1,y_pos-1,z_pos,x+length+1,y_pos,z_pos, 'minecraft:air'))  # windows right through
            res.append(mc_fill(x_pos,y_pos-1,z-1,x_pos,y_pos,z+width+1, 'minecraft:air'))

            # torches
            res.append('/setblock ' + str(x)        + ' ' + str(y_pos+1) + ' ' + str(z_pos)    + ' torch 2')
            res.append('/setblock ' + str(x+length) + ' ' + str(y_pos+1) + ' ' + str(z_pos)    + ' torch 1')
            res.append('/setblock ' + str(x_pos)    + ' ' + str(y_pos+1) + ' ' + str(z)        + ' torch 4')
            res.append('/setblock ' + str(x_pos)    + ' ' + str(y_pos+1) + ' ' + str(z+length) + ' torch 3')

        # now loop through floors AGAIN, and put in the stairs
        for y_pos in range(y+2, y+height-2, 5):
            # stairs
            #res.append(tower_stairs_as_list(x+3, z+2, width=1, y_base=y_pos-2, y_top=y_pos+2, step='minecraft:stone 0', bannister='minecraft:air', step_spacing=1))
            step_num = 0
            for stair_y in range(y_pos-1, y_pos+floor_height):
                res.append(mc_fill(x+2,stair_y,z+2+step_num,x+2,stair_y+4,z+2+step_num, 'minecraft:air')) # clear headroom
                res.append(mc_fill(x+2,stair_y,z+2+step_num,x+2,stair_y,z+2+step_num, 'minecraft:oak_stairs 2')) # planks 1
                step_num +=1
            #torches and bed on each floor
            res.append('/setblock ' + str(x+5) + ' ' + str(y_pos-1) + ' ' + str(z+3) + ' bed 3')  # bed
            res.append('/setblock ' + str(x+6) + ' ' + str(y_pos-1) + ' ' + str(z+3) + ' bed 11') # bed head
            res.append('/setblock ' + str(x+5) + ' ' + str(y_pos-1) + ' ' + str(z+5) + ' bed 3')  # bed
            res.append('/setblock ' + str(x+6) + ' ' + str(y_pos-1) + ' ' + str(z+5) + ' bed 11') # bed head

            res.append('/setblock ' + str(x+3) + ' ' + str(y_pos-1) + ' ' + str(z+4) + ' torch 0') # torch
            res.append('/setblock ' + str(x+6) + ' ' + str(y_pos-1) + ' ' + str(z+4) + ' torch 0') # torch

    else:   # larger ornate glass windows for main building (across horiz axis)
        if butt_height > 5:
            for x_pos in range(x+2, x+width-3, 8):
                res.extend(window_NS(x_pos,y+2,z,       width=2,height=3)) # front Windows
                res.extend(window_NS(x_pos,y+3,z+length,width=1,height=2)) # Back wall windows
            for z_pos in range(z+3, z+length-4, 6):
                res.extend(window_EW(x+width,y+2,z_pos,width=1,height=3)) # LHS Windows
                res.extend(window_EW(x,      y+2,z_pos,width=1,height=3)) # RHS windows
        else:   # Top master tower - LOTS of glass
            for x_pos in range(x+2, x+width-2, 6):
                res.extend(window_NS(x_pos,y+butt_height+2,z+1,       width=4,height=12)) # front Windows
                res.extend(window_NS(x_pos,y+butt_height+2,z+length-2,width=3,height=12)) # back Windows

    mcb.make_from_list(res, myrcon)

def window_NS(x,y,z,width=2,height=4):
    """
    place a window on N/S axis and put lighting around it
    """
    res = []
    res.append(mc_fill(x,y,z-1,x+width,y+height,z, 'minecraft:air'))  # make sure nothing in front of window
    res.append(mc_fill(x,y,z,x+width,y+height,z, 'minecraft:glass 0'))
    res.append('/setblock ' + str(x-1) + ' ' + str(y+1) + ' ' + str(z-1) + ' torch 4') # lower torch - outer LHS
    res.append('/setblock ' + str(x-1) + ' ' + str(y+1) + ' ' + str(z+1) + ' torch 3') # lower torch - inner LHS
    res.append('/setblock ' + str(x+width+1) + ' ' + str(y+1) + ' ' + str(z-1) + ' torch 4') # lower torch - outer RHS
    res.append('/setblock ' + str(x+width+1) + ' ' + str(y+1) + ' ' + str(z+1) + ' torch 3') # lower torch - inner RHS
    res.append('/setblock ' + str(x-1) + ' ' + str(y+height) + ' ' + str(z-1) + ' torch 4') # upper torch - outer LHS
    res.append('/setblock ' + str(x-1) + ' ' + str(y+height) + ' ' + str(z+1) + ' torch 3') # upper torch - inner LHS
    res.append('/setblock ' + str(x+width+1) + ' ' + str(y+height) + ' ' + str(z-1) + ' torch 4') # upper torch - outer RHS
    res.append('/setblock ' + str(x+width+1) + ' ' + str(y+height) + ' ' + str(z+1) + ' torch 3') # upper torch - inner RHS
    return res

def window_EW(x,y,z,width=2,height=4):
    """
    place a window on N/S axis and put lighting around it
    """
    res = []
    res.append(mc_fill(x,y,z,x,y+height,z+width, 'minecraft:air'))  # make sure nothing in front of window
    res.append(mc_fill(x,y,z,x,y+height,z+width, 'minecraft:glass 0'))
    res.append('/setblock ' + str(x+1) + ' ' + str(y+1) + ' ' + str(z-1) + ' torch 2') # lower torch - outer LHS
    res.append('/setblock ' + str(x-1) + ' ' + str(y+1) + ' ' + str(z+width+1) + ' torch 1') # lower torch - inner LHS
    res.append('/setblock ' + str(x+1) + ' ' + str(y+1) + ' ' + str(z-1) + ' torch 1') # lower torch - outer RHS
    res.append('/setblock ' + str(x-1) + ' ' + str(y+1) + ' ' + str(z+width+1) + ' torch 2') # lower torch - inner RHS

    res.append('/setblock ' + str(x+1) + ' ' + str(y+height-0) + ' ' + str(z-1) + ' torch 2') # upper torch - outer LHS
    res.append('/setblock ' + str(x-1) + ' ' + str(y+height-0) + ' ' + str(z+width+1) + ' torch 1') # upper torch - inner LHS
    res.append('/setblock ' + str(x+1) + ' ' + str(y+height-0) + ' ' + str(z-1) + ' torch 1') # upper torch - outer RHS
    res.append('/setblock ' + str(x-1) + ' ' + str(y+height-0) + ' ' + str(z+width+1) + ' torch 2') # upper torch - inner RHS
    return res



def catapult(x,y, z, myrcon):
    """
    makes a catapult with small footprint to fit on tower or walls
    x = centre, y = base, z = front centre
    Bits    Values
    0x1  0x2    A two-bit field storing a value of 0 to 3 specifying the type of wood:
        0:  Oak Wood   (oak up/dn = 0, oak EW = 4, oak NS = 8
        1:  Spruce Wood
        2:  Birch Wood
        3:  Jungle Wood
    0x4 0x8 A two-bit field storing a value of 0 to 3 specifying the orientation of the wood:
        0:  Facing Up/Down
        1:  Facing East/West
        2:  Facing North/South
        3:  Only bark
    """

    height = 8
    arm_fr = 3
    arm_bk = 8
    #fill_area(x-3,y,z-10,x+3,y+height+5,z+10, 'minecraft:air')

    res = []
    res.append('@Minecraft Server')

    res.append(mc_fill(x-2,y,z,x-2,y+height-1,z, 'minecraft:log 0'))  # LHS post
    res.append(mc_fill(x+2,y,z,x+2,y+height-1,z, 'minecraft:log 0'))  # RHS post
    res.append(mc_fill(x-2,y+height,z,x+2,y+height,z, 'minecraft:log 4'))  # main support beam
    res.append(mc_fill(x,y+height+1,z-arm_fr,x,y+height+1,z+arm_bk, 'minecraft:iron_block'))  # catapult arm - log 9
    res.append(mc_fill(x,y+height+2,z,x,y+height+2,z, 'minecraft:rail 1'))
    res.append(mc_fill(x-1,y+height+1,z,x-1,y+height+1,z, 'minecraft:rail 2'))
    res.append(mc_fill(x+1,y+height+1,z,x+1,y+height+1,z, 'minecraft:rail 3'))




    res.append(mc_fill(x-1,y,z+2,x-1,y+2,z+4, 'minecraft:stone 0'))  # support base to hold winder
    res.append(mc_fill(x+1,y,z+2,x+1,y+2,z+4, 'minecraft:stone 0'))  # support base to hold winder
    res.append(mc_fill(x-1,y+2,z+2,x+1,y+2,z+2, 'minecraft:air'))  # make corners nice
    res.append(mc_fill(x-1,y+2,z+4,x+1,y+2,z+4, 'minecraft:air'))  # make corners nice
    res.append(mc_fill(x+1,y+2,z+2,x+1,y+2,z+2, 'minecraft:air'))  # make corners nice
    res.append(mc_fill(x+1,y+2,z+4,x+1,y+2,z+4, 'minecraft:air'))  # make corners nice

    res.append(mc_fill(x-2,y+1,z+3,x+2,y+1,z+3, 'minecraft:iron_block'))  # beam to support winding - log 4
    res.append(mc_fill(x+3,y,z+3,x+3,y+2,z+3, 'minecraft:fence'))  # handle to wind down beam
    res.append(mc_fill(x,y+2,z+3,x,y+height,z+3, 'minecraft:fence'))  # rope to top catapult arm

    # counterweight
    # simple rope res.append(mc_fill(x,y+height-1,z-3,x,y+height,z-3, 'minecraft:fence'))  # rope to hold counterweight
    res.append(mc_fill(x-1,y+height,z-3,x-1,y+height+1,z-3, 'minecraft:nether_brick_fence'))  # rope to hold counterweight
    res.append(mc_fill(x+1,y+height,z-3,x+1,y+height+1,z-3, 'minecraft:nether_brick_fence'))  # rope to hold counterweight
    res.append(mc_fill(x-1,y+height-2,z-2,x+1,y+height-1,z-4, 'minecraft:cobblestone 0'))  # stone mass as counterweight
    res.append(mc_fill(x-1,y+height-3,z-2,x+1,y+height-3,z-4, 'minecraft:planks 3'))  # wood base for counterweight

    # lighting
    res.append('/setblock ' + str(x+1) + ' ' + str(y+3) + ' ' + str(z+3) + ' torch 0')
    res.append('/setblock ' + str(x-1) + ' ' + str(y+3) + ' ' + str(z+3) + ' torch 0')
    res.append('/setblock ' + str(x+1) + ' ' + str(y+2) + ' ' + str(z+2) + ' torch 0')
    res.append('/setblock ' + str(x-1) + ' ' + str(y+2) + ' ' + str(z+2) + ' torch 0')
    res.append('/setblock ' + str(x+1) + ' ' + str(y+2) + ' ' + str(z+4) + ' torch 0')
    res.append('/setblock ' + str(x-1) + ' ' + str(y+2) + ' ' + str(z+4) + ' torch 0')

    res.append('/setblock ' + str(x-2) + ' ' + str(y+height+1) + ' ' + str(z) + ' torch 0')
    res.append('/setblock ' + str(x+2) + ' ' + str(y+height+1) + ' ' + str(z) + ' torch 0')


    res.append('/setblock ' + str(x) + ' ' + str(y+height+2) + ' ' + str(z-3) + ' torch 0')  # torch on counterweight
    res.append('/setblock ' + str(x) + ' ' + str(y+height) + ' ' + str(z-3) + ' torch 0')  # torch on counterweight


    # payload
    res.append(mc_fill(x-1,y+height,z+arm_bk-1,x+1,y+height,z+arm_bk+2, 'minecraft:stone_slab 8'))  # catapult tray
    res.append(mc_fill(x-1,y+height+1,z+arm_bk,x+1,y+height+1,z+arm_bk+1, 'minecraft:netherrack 1'))  # payload to launch
    res.append('/setblock ' + str(x-1) + ' ' + str(y+height+2) + ' ' + str(z+arm_bk+1) + ' fire')
    res.append('/setblock ' + str(x+1) + ' ' + str(y+height+2) + ' ' + str(z+arm_bk+1) + ' fire')
    res.append('/setblock ' + str(x) + ' ' + str(y+height+2) + ' ' + str(z+arm_bk) + ' fire')

    mcb.make_from_list(res, myrcon)


def gate(x, y, z, width=5, height=5, length=7, style=style_gate1, myrcon=None):
    """
    make a gate on the main wall
      FRONT                SIDE                TOP
       ####              #########        -----######------
      ##  ##             |       |             ######
      #    #             |       |             ######
      #    #             |       |             ######
   ___#    #____      ___|       |___          ######
                                               ######
                                          -----######-----


    """
    res = []
    res.append('@Minecraft Server')

    # clear area
    #res.append(mc_fill(x,y-1,z-4,x+width,y+height+9,z+length+4, 'minecraft:air'))
    res.append(mc_fill(x-3,y,z-2,x+width+2,y+height,z+length+1, 'minecraft:air'))


    # gradient walls up and over the gate - style_stone
    res.append(mc_fill(x-3,y,z+1,x+width+2,y+height-4,z+length-1, 'minecraft:' + style_stone['side']))

    res.append(mc_fill(x-2,y,z+1,x+width+2,y+height-3,z+length-1, 'minecraft:' + style_stone['side']))
    res.append(mc_fill(x,y,z+1,x+width+0,y+height-2,z+length-1, 'minecraft:' + style_stone['side']))
    res.append(mc_fill(x+2,y,z+1,x+width-2,y+height-1,z+length-1, 'minecraft:' + style_stone['side']))

    # basic outline of stone
    res.append(mc_fill(x+1,y,z+1,x+width-1,y+height-3,z+length-1, 'minecraft:' + style_gate1['base'] + ' hollow'))
    res.append(mc_fill(x+2,y,z-0,x+width-2,y+height-4,z+length+0, 'minecraft:air'))
    res.append(mc_fill(x+2,y,z+2,x+width-2,y+height-4,z+length-2, 'minecraft:' + style_gate1['base'] + ' hollow'))
    res.append(mc_fill(x+3,y,z-1,x+width-3,y+height-5,z+length+1, 'minecraft:air'))


    # make a gate, shown open via iron bars on top of walkway
    #res.append('/setblock ' + str(x+2) + ' ' + str(y-5) + ' ' + str(z) + ' iron_bars 0')
    res.append(mc_fill(x+2,y+3,z+1,x+width-2,y+height-4,z+1, 'minecraft:iron_bars'))

    # put a glowstone in the underside of the roof of the walkway
    res.append('/setblock ' + str(x+(width/2)) + ' ' + str(y+4) + ' ' + str(z+3) + ' glowstone 0')

    # torches on outside of gate
    res.append('/setblock ' + str(x+1) + ' ' + str(y+5) + ' ' + str(z) + ' torch 4')  # torch on outer wall
    res.append('/setblock ' + str(x+width-1) + ' ' + str(y+5) + ' ' + str(z) + ' torch 4')  # torch on outer wall
    res.append('/setblock ' + str(x+1) + ' ' + str(y+2) + ' ' + str(z) + ' torch 4')  # torch on outer wall
    res.append('/setblock ' + str(x+width-1) + ' ' + str(y+2) + ' ' + str(z) + ' torch 4')  # torch on outer wall

    mcb.make_from_list(res, myrcon)


def main_door(x=90, y=64, z=75, myrcon=None):
    """
    Makes a fancy main door at the entrance of the castle building
    coords for door are bottom centre - ornate stuff built out from there



    """
    res = []
    res.append('@Minecraft Server')


    # outer frame
    res.append(mc_fill(x-5,y,z-2,x+5,y+7,z+1, 'minecraft:air'))
    res.append(mc_fill(x-4,y,z-2,x+4,y+7,z+1, 'minecraft:stone 6'))
    res.append(mc_fill(x-5,y,z-1,x+5,y+6,z+1, 'minecraft:stone 6'))

    res.append(mc_fill(x-3,y,z-2,x+3,y+6,z+1, 'minecraft:air'))
    res.append(mc_fill(x-3,y,z-1,x+3,y+6,z+1, 'minecraft:stone 6'))

    res.append(mc_fill(x-2,y,z-2,x+2,y+5,z+1, 'minecraft:air'))
    res.append(mc_fill(x-2,y,z-0,x+2,y+5,z+0, 'minecraft:stone 4'))

    res.append(mc_fill(x-1,y+1,z-5,x+1,y+3,z+1, 'minecraft:air'))

    # fix for lower ground floor
    res.append(mc_fill(x-2,y,z-4,x+2,y,z+1, 'minecraft:stone 4'))

    # door
    res.append('/setblock ' + str(x-1) + ' ' + str(y+1) + ' ' + str(z) + ' acacia_door 4')  # Door
    res.append('/setblock ' + str(x-1) + ' ' + str(y+2) + ' ' + str(z) + ' acacia_door 8')  # Door
    res.append('/setblock ' + str(x) + ' ' + str(y+1) + ' ' + str(z) + ' acacia_door 4')  # Door
    res.append('/setblock ' + str(x) + ' ' + str(y+2) + ' ' + str(z) + ' acacia_door 8')  # Door
    res.append('/setblock ' + str(x+1) + ' ' + str(y+1) + ' ' + str(z) + ' acacia_door 4')  # Door
    res.append('/setblock ' + str(x+1) + ' ' + str(y+2) + ' ' + str(z) + ' acacia_door 8')  # Door

    # corners for aesthetics
    res.append('/setblock ' + str(x-2) + ' ' + str(y+5) + ' ' + str(z-1) + ' minecraft:stone 6')
    res.append('/setblock ' + str(x+2) + ' ' + str(y+5) + ' ' + str(z-1) + ' minecraft:stone 6')
    res.append('/setblock ' + str(x-3) + ' ' + str(y+6) + ' ' + str(z-2) + ' minecraft:stone 6')
    res.append('/setblock ' + str(x+3) + ' ' + str(y+6) + ' ' + str(z-2) + ' minecraft:stone 6')

    res.append('/setblock ' + str(x-4) + ' ' + str(y+7) + ' ' + str(z-2) + ' minecraft:air')
    res.append('/setblock ' + str(x+4) + ' ' + str(y+7) + ' ' + str(z-2) + ' minecraft:air')


    # lighting
    #res.append('/setblock ' + str(x-1) + ' ' + str(y+4) + ' ' + str(z-1) + ' torch 4')  # torch on outer wall
    #res.append('/setblock ' + str(x+1) + ' ' + str(y+4) + ' ' + str(z-1) + ' torch 4')  # torch on outer wall
    res.append('/setblock ' + str(x) + ' ' + str(y+5) + ' ' + str(z) + ' glowstone 0')  #

    res.append('/setblock ' + str(x-2) + ' ' + str(y+5) + ' ' + str(z-2) + ' torch 4')  # torch on outer wall
    res.append('/setblock ' + str(x+2) + ' ' + str(y+5) + ' ' + str(z-2) + ' torch 4')  # torch on outer wall

    res.append('/setblock ' + str(x-3) + ' ' + str(y+6) + ' ' + str(z-3) + ' torch 4')  # torch on outer wall
    res.append('/setblock ' + str(x+3) + ' ' + str(y+6) + ' ' + str(z-3) + ' torch 4')  # torch on outer wall


    # inside of door
    res.append('/setblock ' + str(x-1) + ' ' + str(y+4) + ' ' + str(z+1) + ' torch 3')  # torch on inner wall
    res.append('/setblock ' + str(x+1) + ' ' + str(y+4) + ' ' + str(z+1) + ' torch 3')  # torch on inner wall


    mcb.make_from_list(res, myrcon)

def stairs_as_list(x, z, width, y_base, y_top, step='minecraft:stone 4', bannister='minecraft:air', step_spacing=1):
    res = []
    step_num = 0
    res.append('@Minecraft Server')
    for y in range(y_base, y_top):
        #for z_pos in (z, z+width):
        res.append(mc_fill(x,y,z+step_num,x+width,y+5,z+step_num+step_spacing, 'minecraft:air')) # clear headroom
        res.append(mc_fill(x,y,z+step_num+step_spacing,x+width,y,z+step_num+step_spacing, step))

        # bannister
        if bannister != 'minecraft:air':  # torches on edge of stairs (NO - because most are on walls)
            res.append(mc_fill(x-1,y+1,z+step_num,x+width+1,y+5,z+step_num+step_spacing, 'minecraft:air')) # clear headroom
            res.append(mc_fill(x-1,y,z+step_num,x-1,y+2,z+step_num+step_spacing, bannister))
            res.append(mc_fill(x+width+1,y,z+step_num,x+width+1,y+2,z+step_num+step_spacing, bannister))
            res.append('/setblock ' + str(x-1) + ' ' + str(y+3) + ' ' + str(z+step_num) + ' torch 0')  # torch on right bannister
            res.append('/setblock ' + str(x+width+1) + ' ' + str(y+3) + ' ' + str(z+step_num) + ' torch 0') # torch on left bannister
        else:
            if y > y_base and y< y_top:
                res.append('/setblock ' + str(x+width) + ' ' + str(y+1) + ' ' + str(z+step_num) + ' torch 2')
                res.append('/setblock ' + str(x+width-1) + ' ' + str(y+1) + ' ' + str(z+step_num) + ' torch 1')

        step_num +=step_spacing

    # plus a torch under the stairs
    res.append('/setblock ' + str(x+width) + ' ' + str(y_base) + ' ' + str(z+3) + ' torch 0')
    res.append('/setblock ' + str(x+width-1) + ' ' + str(y_base) + ' ' + str(z+3) + ' torch 0')


    return res

def stairs_NS(x, z, width, y_base, y_top, step='minecraft:stone 4', bannister='minecraft:air', step_spacing=1, myrcon=None):
    """
    make a staircase to join floor to roof
    """
    res = []
    res = stairs_as_list(x, z, width, y_base, y_top, step, bannister, step_spacing)
    mcb.make_from_list(res, myrcon)


def tile_block(start_x, y, start_z, end_x, end_z, spacing, block, myrcon=None):
    """
    used for lighting, puts a block (torch or glowstone) every 'spacing'
    blocks on a floor or roof
    """
    res = []
    res.append('@Minecraft Server')
    for z in range(start_z, end_z, spacing):
        for x in range(start_x, end_x, spacing):
            res.append('/setblock ' + str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + block)
    mcb.make_from_list(res, myrcon)

def set_block(x,y,z,item, myrcon=None):
    """
        set_block(x,y,z,'minecraft:sapling')
    """

    res = []
    res.append('@Minecraft Server')
    res.append('/setblock ' + str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + str(item))

    mcb.make_from_list(res, myrcon)

def mc_fill(x1, y1, z1, x2, y2, z2, item):
    """
    formats the fill params to a minecraft command
    /fill 1 79 1 9 88 9 minecraft:air 0
    /fill 1 80 1 4 84 4 minecraft:sandstone 0 hollow
    /fill 1 79 1 4 79 4 minecraft:stone 0
    /fill 1 85 1 4 85 4 minecraft:wool 3
    /fill 1 81 2 1 83 3 minecraft:air 0


    """
    r = '/fill '
    r += str(x1) + ' '
    r += str(y1) + ' '
    r += str(z1) + ' '
    r += str(x2) + ' '
    r += str(y2) + ' '
    r += str(z2) + ' '
    r += item
    return r

def rcon_connection():
    """
    function to handle connection to local minecraft server
    and return the rcon connection for use in minecraft_builder
    """

    #f = open('T:\\user\\AIKIF\\pers_data\\credentials\\minecraft_server.cred')
    f = open('/home/duncan/AIKIF/pers_data/credentials/minecraft_server.cred')
    pwd = f.read()
    f.close()


    rcon = mcrcon.MCRcon('192.168.1.5', pwd, port=25576)
    rcon.connect()
    #rcon.login(pwd)  :25576
    return rcon

def teleport_player(player_name,x,y,z, myrcon):
    if myrcon == None: # use sendkeys
        res = []
        res.append('@Minecraft Server')
        res.append('/tp ' + player_name + ' ' + str(x) + ' ' + str(y) + ' ' + str(z))
        mcb.make_from_list(res)

    else: # using network rcon
        myrcon.command('/tp ' + player_name + ' ' + str(x) + ' ' + str(y) + ' ' + str(z))


if __name__ == '__main__':
    TEST()
