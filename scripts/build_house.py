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

x = -1540
y = 88
z = 1540

w = 6
h = 4
d = 4

def main():
    setup_house_bld()
    import minecraft_builder
    minecraft_builder.make_structure('build_house.bld')

    
def setup_house_bld():    
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
    res.append(mc_fill(x1,y1,z1,x2,y2,z2, 'minecraft:air 0'))
    res.append(mc_fill(x1,y1,z1,x2,y2,z2, 'minecraft:planks 1 hollow'))
    res.append(mc_fill(x1,y1,z1,x2,y1,z2, 'minecraft:planks 3'))  # floor
    res.append(mc_fill(x1-1,y2+0,z1-0,x2+1,y2+0,z2+0, 'minecraft:planks 2'))  # roof
    res.append(mc_fill(x1-1,y2+1,z1+1,x2+1,y2+1,z2-1, 'minecraft:planks 2'))  # roof
    res.append(mc_fill(x1-1,y2+2,z1+2,x2+1,y2+2,z2-2, 'minecraft:planks 2'))  # roof
    
    # door on short wall
    res.append('/setblock ' + str(x1) + ' ' + str(y) + ' ' + str(z1 + int((d)/2)+1) + ' wooden_door')  # Door
    res.append('/setblock ' + str(x1) + ' ' + str(y+1) + ' ' + str(z1 + int((d)/2)+1) + ' wooden_door 8')  # Door
    
    """ 
    # door on long wall
    res.append('/setblock ' + str(x1 + int((w)/2)+1) + ' ' + str(y) + ' ' + str(z1) + ' wooden_door')  # Door
    res.append('/setblock ' + str(x1 + int((w)/2)+1) + ' ' + str(y+1) + ' ' + str(z1) + ' wooden_door 8')  # Door
    
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



 
    
    print(res)
    with open('build_house.bld', 'w') as f:
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