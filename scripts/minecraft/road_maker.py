#!/usr/bin/python3
# -*- coding: utf-8 -*-
# road_maker.py


import os
import sys
import minecraft_builder as mcb

style_stone = {'base':'stone 0', 'side':'stone 3'}
style_wood = {'base':'planks 1', 'side':'planks 2'}

North = (1,0)
South = (-1, 0)
East = (0, 1)
West = (0, -1)


def main():
    """
    trying different methods of making roads
    # works N/S    setup_road_bld(op_file='road.bld', x=10,y=62,z=10,direction=North, width=3,length=12, style=style_stone)
    #setup_road_bld(op_file='road.bld', x=10,y=70,z=10,direction=South, width=2,length=6, style=style_stone)
    setup_road_bld(op_file='road.bld', x=10,y=70,z=10,direction=West, width=2,length=6, style=style_stone)
    #setup_road_bld(op_file='road.bld', x=10,y=70,z=10,direction=North, width=2,length=6, style=style_stone)
    minecraft_builder.make_structure('road.bld')
    
    mcb.make_from_list(road(x=4,y=86,z=10,direction=South, width=4,length=12, style=style_stone))
    mcb.make_from_list(road(x=10,y=86,z=10,direction=West, width=3,length=6, style=style_wood))
    
    """
    
    # build multiple roads
    mcb.make_from_list(road(x=100,y=70,z=10,direction=North, width=5,length=30, style=style_wood))
    mcb.make_from_list(road(x=100,y=70,z=10,direction=East, width=4,length=12, style=style_stone))
    

    
def road(x,y,z,direction, width,length, style):    
    """
    creates a build list
    """
    base = style['base']
    side = style['side'] 
    res = []
    res.append('@Minecraft Server')
    
    if direction[0] == 0:   # North / South
        x1 = x
        z1 = z
        y1 = y
        x2 = x+width
        z2 = z+length * direction[1]
        res.append(mc_fill(x1,y-3,z1,x2,y,z2, 'minecraft:air 0'))
        res.append(mc_fill(x1,y,z1,x2,y,z2, 'minecraft:' + base))
        res.append(mc_fill(x1,y,z1,x1,y,z2, 'minecraft:' + side))
        res.append(mc_fill(x2,y,z1,x2,y,z2, 'minecraft:' + side))
        
        
    else:                   # East / West
        x1 = x
        z1 = z
        y1 = y
        x2 = x+length * direction[0]
        z2 = z+width
        res.append(mc_fill(x1,y1-3,z1,x2,y1,z2, 'minecraft:air 0'))
        res.append(mc_fill(x1,y1,z1,x2,y1,z2, 'minecraft:' + base))
        
        res.append(mc_fill(x1,y1,z1,x2,y1,z1, 'minecraft:' + side))
        res.append(mc_fill(x1,y1,z2,x2,y1,z2, 'minecraft:' + side))

    return res

    
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
    
    
    
def road_OLD(op_file, x,y,z,direction, width,length, style):    
    """
    generates a build file for minecraft
    """
    base = style['base']
    side = style['side'] 
    res = []
    res.append('@Minecraft Server')
    res.append('/say hello from server, just building a road')
    
    if direction[0] == 0:   # North / South
        x1 = x
        z1 = z
        x2 = x+width
        z2 = z+length * direction[1]
        res.append(mc_fill(x1,y-3,z1,x2,y,z2, 'minecraft:air 0'))
        res.append(mc_fill(x1,y,z1,x2,y,z2, 'minecraft:' + base))
        res.append(mc_fill(x1,y,z1,x1,y,z2, 'minecraft:' + side))
        res.append(mc_fill(x2,y,z1,x2,y,z2, 'minecraft:' + side))
        
        
    else:                   # East / West
        x1 = x
        z1 = z
        x2 = x+length * direction[0]
        z2 = z+width
        res.append(mc_fill(x1,y-3,z1,x2,y,z2, 'minecraft:air 0'))
        res.append(mc_fill(x1,y,z1,x2,y,z2, 'minecraft:' + base))
        
        res.append(mc_fill(x1,y,z1,x2,y,z1, 'minecraft:' + side))
        res.append(mc_fill(x1,y,z2,x2,y,z2, 'minecraft:' + side))

    

    with open(op_file, 'w') as f:
        for line in res:
            f.write(line + '\n')
            
    return res

    
    
main()