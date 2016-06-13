# build_flatworld.py
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

x = -1552
y = 88
z = 1520

w = 36
h = 9
d = 25

def main():
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
    res.append(mc_fill(x, y, z, x+w, y+h, z+d, 'minecraft:air 0'))
    #res.append(mc_fill(x, y-1, z, x+w, y-1, z+d, 'minecraft:grass 0'))
    print(res)
    with open('build_flatworld.bld', 'w') as f:
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