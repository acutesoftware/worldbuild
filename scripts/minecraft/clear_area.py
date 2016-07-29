# clear_area.py

import minecraft_builder as mcb


def TEST():
    print('clearing castle area')
    # TOK - clears all walls (all inner area of castle 
    wipe_all(x = 28, y = 63, z = 25, w = 235, h = 75, d = 150)
    
    # TOK - clears main castle building
    wipe_all(x=72, y=63, z=77,w=36,h=30,d=26)
    wipe_all(x=70, y=74, z=70,w=46,h=50,d=36)
    wipe_all(x=30, y=74, z=30,w=126,h=110,d=80)  # 37,96,36,11,3,8, 0)  
    
    
def wipe_all(x,y,z,w,h,d):
    res = []
    res.append('@Minecraft Server')
    res.append('/say hello from server, just clearing the area')
    for n in range(x, x + w, 1):
        res.append(mcb.mc_fill(n, y, z, n+1, y+h, z+d, 'minecraft:air 0'))
    mcb.make_from_list(res)
    

    
if __name__ == '__main__':     
    TEST()

