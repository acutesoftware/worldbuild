#!/usr/bin/python3
# -*- coding: utf-8 -*-
# castle_maker.py


import os
import sys
import minecraft_builder as mcb

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

def fill_area(x1,y1,z1,x2,y2,z2, item):
    res = []
    res.append('@Minecraft Server')
    res.append(mc_fill(x1,y1,z1,x2,y2,z2,item))

    mcb.make_from_list(res)
    
def plant(x1,z1,x2,z2,y1, item): # 'wheat',  
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

    mcb.make_from_list(res)
 
def make_castle_walls(start_x, start_y, start_z, width, height, length, wall_width):
    touchups = []
    with open('last_build.log', 'w') as f:
        f.write('Building Castle - \n')
        f.write('start_x = ' + str(start_x)  + ', start_y = ' +  str(start_y)  + ', start_z = ' +  str(start_z)  + '\n' )
        f.write('width   = ' + str(width)    + ', height = ' +  str(height)  + ', length = ' +  str(length)  + '\n' )
        
     
   
    # build outer walls
    mcb.make_from_list(castle_wall(start_x,start_y,start_z,North, width,height, style_stone, wall_width)) # TOK
    mcb.make_from_list(castle_wall(start_x,start_y,start_z,East,  length,height, style_stone, wall_width)) # TOK
    
    mcb.make_from_list(castle_wall(start_x,start_y,start_z+length-wall_width,North, width ,height, style_stone, wall_width))
    mcb.make_from_list(castle_wall(start_x+width-wall_width,start_y,start_z, East, length, height, style_stone, wall_width))
    
    #mcb.make_from_list(castle_wall(start_x+wall_width,start_y,start_z+length,North, width ,height, style_wool))
    #mcb.make_from_list(castle_wall(start_x+width,start_y,start_z+wall_width, East, length, height, style_wood))
     
    mcb.make_from_list(touchups)
    
    

    
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

            if n % 8 == 0:  # torches every 4*2 blocks
                res.append('/setblock ' + str(x1) + ' ' + str(y2+2) + ' ' + str(n) + ' torch 0')  # torch on inner wall
                res.append('/setblock ' + str(x2) + ' ' + str(y2+2) + ' ' + str(n) + ' torch 0')  # torch on outer wall
        
        # clear battlements on wall joins
        #if wall_width > 3:
        #    res.append(mc_fill(x1+2,y2+1,z1+2,x2,y2+2,z+wall_width, 'minecraft:air'))
        
        
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
        touchups.append(mc_fill(x1,y1+1,z1,x1+1,y1+1,z1, 'minecraft:' + corner))
        touchups.append(mc_fill(x1,y1+1,z1,x1+0,y1+2,z1, 'minecraft:' + corner))
        touchups.append(mc_fill(x2-1,y1+1,z1,x2,y1+1,z1, 'minecraft:' + corner))
        touchups.append(mc_fill(x2-0,y1+1,z1,x2,y1+2,z1, 'minecraft:' + corner))
        
        #battlements
        for n in range(x1, x2, 2):
            res.append(mc_fill(n,y2+1,z1,n,y2+1,z1, 'minecraft:' + side))
            res.append(mc_fill(n,y2+1,z2,n,y2+1,z2, 'minecraft:' + side))

            if n % 4 == 0:  # TODO - if length/width < 7 then torch every block ELSE torches every 4*2 blocks
                res.append('/setblock ' + str(n) + ' ' + str(y2+2) + ' ' + str(z1) + ' torch 0')  # torch on outer wall
                res.append('/setblock ' + str(n) + ' ' + str(y2+2) + ' ' + str(z2) + ' torch 0')  # torch on inner wall
        
         
    return res

def tower_building(x, y, z, width, height, length, butt_height, style=style_stone): 
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
    if width < 15:  # simple window with torch on normal towers (across vert axis)
        x_pos = x + (width/2)
        z_pos = z + (length/2)
        for y_pos in range(y+2, y+height, 5):
            res.append(mc_fill(x-1,y_pos,z_pos,x+length+1,y_pos+1,z_pos, 'minecraft:air'))  # windows right through
            res.append(mc_fill(x_pos,y_pos,z-1,x_pos,y_pos+1,z+width+1, 'minecraft:air'))
            res.append('/setblock ' + str(x+length-1) + ' ' + str(y_pos-1) + ' ' + str(z_pos) + ' torch 1')  # torch - 2 = E
            res.append('/setblock ' + str(x+length-1) + ' ' + str(y_pos-1) + ' ' + str(z_pos+width) + ' torch 2')  # torch - 2 = W
            res.append('/setblock ' + str(x_pos+0) + ' ' + str(y_pos-1) + ' ' + str(z_pos) + ' torch 3')  # torch - 3 = S
            res.append('/setblock ' + str(x_pos+length) + ' ' + str(y_pos-1) + ' ' + str(z_pos) + ' torch 4')  # torch - 4 = north (TOK)
            
        
    else:   # larger ornate glass windows for main building (across horiz axis)
         
        for x_pos in range(x+2, x+width-2, 8):
            res.append(mc_fill(x_pos,y+2,z-1,x_pos+2,y+6,z, 'minecraft:air'))  # make sure nothing in front of window
            res.append(mc_fill(x_pos,y+2,z,x_pos+2,y+6,z, 'minecraft:glass 0'))
    
    mcb.make_from_list(res)

 

def gate(x, y, z, width=5, height=5, length=7, style=style_gate1): 
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
    
    mcb.make_from_list(res)
 
    
def main_door(x=90, y=64, z=75):
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
    
    
    mcb.make_from_list(res)
    

def set_block(x,y,z,item):
    """
        set_block(x,y,z,'minecraft:sapling')
    """
   
    res = []
    res.append('@Minecraft Server')
    res.append('/setblock ' + str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + item) 
    
    mcb.make_from_list(res)
    
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
    
  
    
    
if __name__ == '__main__':     
    TEST()
