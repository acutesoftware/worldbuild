# build_house.py
# this makes a build file for minecraft 
# this file is used by minecraft_builder.py to send the commands
# below to the minecraft server running on the PC via send_keys
# blank lines and lines starting with # are ignored
#
# Note - you need to use the @ symbol to decide whether to send 
# fill commands to client or server
#

import os
import sys
import minecraft_builder

style_wood = {'roof':'planks 1', 'walls':'planks 2', 'floor':'planks 3', 'posts':'planks 1'}
style_stone = {'roof':'planks 1', 'walls':'stone 0', 'floor':'stone 4', 'posts':'stone 0'}


def main():
    setup_house_bld(op_file='build_house.bld', x=-1540,y=88,z=1540,w=8,h=4,d=6, style=style_wood)
    setup_house_bld(op_file='build_cottage.bld', x=-1527,y=88,z=1530,w=6,h=3,d=4, style=style_stone)
    
    minecraft_builder.make_structure('build_house.bld')
    minecraft_builder.make_structure('build_cottage.bld')

    
def setup_house_bld(op_file, x,y,z,w,h,d, style):    
    """
    generates a build file for minecraft
    
    (x,y,z) ...==.....[ ]...==.... (x+w,y,z)
        .                               .
        .                               .
        .                               .
    (x,y,z+d) ......................(x+w,y,z+d)
    """
    res = []
    res.append('@Minecraft Server')
    res.append('/say hello from server, just building a house ~5 ~0 ~0')
    x1 = x-int((w+1)/2)-1
    y1 = y-1
    z1 = z-int((d+1)/2)-1
    x2 = x+int((w+1)/2)+1
    y2 = y+h
    z2 = z+int((d+1)/2)+1
    
    posts = style['posts'] # 'planks 1'
    roof = style['roof'] # 'planks 1'
    walls = style['walls'] # 'planks 2'
    floor = style['floor'] # 'planks 3'
    
    res.append(mc_fill(x1,y1,z1,x2,y2,z2, 'minecraft:air 0'))
    res.append(mc_fill(x1,y1,z1,x2,y2,z2, 'minecraft:' + walls + ' hollow'))
    res.append(mc_fill(x1,y1,z1,x2,y1,z2, 'minecraft:' + floor))  
    res.append(mc_fill(x1-1,y2+0,z1-1,x2+1,y2+0,z2+1, 'minecraft:' + roof))  # roof
    res.append(mc_fill(x1-1,y2+1,z1+1,x2+1,y2+1,z2-1, 'minecraft:' + roof))  # roof
    res.append(mc_fill(x1-1,y2+2,z1+3,x2+1,y2+2,z2-3, 'minecraft:' + roof))  # roof

    #posts in different wood
    dbl_width = 0  # set to 1 to have posts wide on short side of house
    res.append(mc_fill(x1,y1,z1,x1,y2-1,z1+dbl_width, 'minecraft:' + posts))  # post
    res.append(mc_fill(x2,y1,z1,x2,y2-1,z1+dbl_width, 'minecraft:' + posts))  # post
    res.append(mc_fill(x1,y1,z2,x1,y2-1,z2-dbl_width, 'minecraft:' + posts))  # post
    res.append(mc_fill(x2,y1,z2,x2,y2-1,z2-dbl_width, 'minecraft:' + posts))  # post
    
    
    # door on short wall
    res.append('/setblock ' + str(x1) + ' ' + str(y) + ' ' + str(z1 + int((d)/2)+1) + ' wooden_door')  # Side Door
    res.append('/setblock ' + str(x1) + ' ' + str(y+1) + ' ' + str(z1 + int((d)/2)+1) + ' wooden_door 8')  # Side Door
    
    
    # door on long wall
    res.append('/setblock ' + str(x1 + int((w+1)/2)+1) + ' ' + str(y) + ' ' + str(z1) + ' wooden_door')  # Door
    res.append('/setblock ' + str(x1 + int((w+1)/2)+1) + ' ' + str(y+1) + ' ' + str(z1) + ' wooden_door 8')  # Door
    
    """ 
    # Windows on short walls perpendicular to door
    # /fill 8 103 5 9 104 5 minecraft:glass 0 
    res.append(mc_fill(x1,y1+2,z1+2,x1,y2-2,z1+2, 'minecraft:glass 0'))  # windows
    res.append(mc_fill(x1,y1+2,z2-2,x1,y2-2,z2-2, 'minecraft:glass 0'))  # windows
    
    res.append(mc_fill(x2,y1+2,z1+2,x2,y2-2,z1+2, 'minecraft:glass 0'))  # windows
    res.append(mc_fill(x2,y1+2,z2-2,x2,y2-2,z2-2, 'minecraft:glass 0'))  # windows
    """
    
    # Windows on long walls parallel to door
    res.append(mc_fill(x1+2,y1+2,z1,x1+2,y2-2,z1, 'minecraft:glass 0'))  # windows
    res.append(mc_fill(x2-2,y1+2,z1,x2-2,y2-2,z1, 'minecraft:glass 0'))  # windows
    
    res.append(mc_fill(x1+2,y1+2,z2,x1+3,y2-2,z2, 'minecraft:glass 0'))  # windows
    res.append(mc_fill(x2-2,y1+2,z2,x2-3,y2-2,z2, 'minecraft:glass 0'))  # windows
    
 
    """  Torches and Decorations 
        0: Standing on the floor
        1: Pointing east
        2: Pointing west
        3: Pointing south
        4: Pointing north
    """    
    res.append('/setblock ' + str(x1+1) + ' ' + str(y2-2) + ' ' + str(z1+1) + ' torch 1')  # RHS of door
    res.append('/setblock ' + str(x1+1) + ' ' + str(y2-2) + ' ' + str(z2-1) + ' torch 1')  # LHS of door

    res.append('/setblock ' + str(x2-1) + ' ' + str(y2-2) + ' ' + str(z1+1) + ' torch 2')  # RHS back wall
    res.append('/setblock ' + str(x2-1) + ' ' + str(y2-2) + ' ' + str(z2-1) + ' torch 2')  # LHS back wall

    
    res.append('/setblock ' + str(x1-1) + ' ' + str(y2-1) + ' ' + str(z1) + ' torch 2')  # outside of side door (West)
    res.append('/setblock ' + str(x1-1) + ' ' + str(y2-1) + ' ' + str(z2) + ' torch 2')  # outside of side door (West)

    res.append('/setblock ' + str(x2+1) + ' ' + str(y2-1) + ' ' + str(z1) + ' torch 1')  # outside of narrow end wall (East)
    res.append('/setblock ' + str(x2+1) + ' ' + str(y2-1) + ' ' + str(z2) + ' torch 1')  # outside of narrow end wall (East)
    
    
    res.append('/setblock ' + str(x1) + ' ' + str(y2-1) + ' ' + str(z1-1) + ' torch 4')  # outside of N wall
    res.append('/setblock ' + str(x2) + ' ' + str(y2-1) + ' ' + str(z1-1) + ' torch 4')  # outside of N wall

    res.append('/setblock ' + str(x1) + ' ' + str(y2-1) + ' ' + str(z2+1) + ' torch 3')  # outside of S wall
    res.append('/setblock ' + str(x2) + ' ' + str(y2-1) + ' ' + str(z2+1) + ' torch 3')  # outside of S wall
    
    #res.append('/setblock ' + str(x2-3) + ' ' + str(y2-4) + ' ' + str(z2-1) + ' wall_sign 5 replace {Text1:\"hi\", Text2:\"\"}')
    
    """
    Furniture
    """
    res.append(mc_fill(x2-1,y1,z1+1,x2-3,y1,z1+3, 'minecraft:stained_hardened_clay 14'))  # red carpet in bedroom

    res.append('/setblock ' + str(x2-2) + ' ' + str(y1+1) + ' ' + str(z1+2) + ' bed 3')  # bed
    res.append('/setblock ' + str(x2-1) + ' ' + str(y1+1) + ' ' + str(z1+2) + ' bed 11') # bed head
    res.append(mc_fill(x2-1,y1+1,z2-1,x2-1,y1+1,z2-2, 'minecraft:bookshelf 0'))  # bookshelves next to bed

    res.append('/setblock ' + str(x1+3) + ' ' + str(y1+1) + ' ' + str(z1+1) + ' chest 3') 
    res.append('/setblock ' + str(x1+2) + ' ' + str(y1+1) + ' ' + str(z1+1) + ' chest 3') 
    res.append('/setblock ' + str(x1+1) + ' ' + str(y1+1) + ' ' + str(z1+1) + ' furnace 0')  # oven next to chest
 
    res.append('/setblock ' + str(x1+1) + ' ' + str(y1+1) + ' ' + str(z2-1) + ' crafting_table 4') 
    res.append('/setblock ' + str(x1+2) + ' ' + str(y1+1) + ' ' + str(z2-1) + ' anvil 4') 
    res.append('/setblock ' + str(x1+3) + ' ' + str(y1+1) + ' ' + str(z2-1) + ' enchanting_table 4')  # face north
     
    with open(op_file, 'w') as f:
        for line in res:
            f.write(line + '\n')
    
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
    
main()