# clear_area.py

import minecraft_builder as mcb


def TEST():
    #wipe_all(x = 30-2, y = 63-2, z = 30-2, w = 100, h = 15, d = 100)
    wipe_all(x = 28, y = 63, z = 25, w = 275, h = 15, d = 150)
    
def wipe_all(x,y,z,w,h,d):
    res = []
    res.append('@Minecraft Server')
    res.append('/say hello from server, just clearing the area')
    for n in range(x, x + w, 5):
        res.append(mcb.mc_fill(n, y, z, n+5, y+h, z+d, 'minecraft:air 0'))
    mcb.make_from_list(res)
    

    
if __name__ == '__main__':     
    TEST()
