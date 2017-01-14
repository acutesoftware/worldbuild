    # multi_level_castle.py
# Minecraft Server 1.11.2
# Seed: -7560993781265470572

import castle_maker
import clear_area
import time


def main():
    """
    .................................................................
    ....[back tower].................................................
    ................................[main keep]......................
    .................................................................
    .................................................................
    ..................................................[back right]...
    .................................................................
    ...............[courtyard].......................................
    ..............................---------------........................
    ..............................[  main town  ]........................
    ...............................-------------.........[front right]..
    .................................................................
    
    
    
    
    
    """
    myrcon = castle_maker.rcon_connection()
    castle_maker.teleport_player('craftandstore',227,76,197, myrcon)
    time.sleep(1) 

     #  town
    castle_base(230,74,200,270,78,254, myrcon)
        
     # courtyard
    castle_base(250,79,164,273,84,204, myrcon)
    clear_area.wipe_all(255, 80, 200, 12, 7, 12, myrcon)  # clear area
    
    time.sleep(1) 
    
    # Main Building (The Keep)
    castle_base(271,97,207,297,105,227, myrcon)
    clear_area.wipe_all(265, 97, 205, 10, 6, 10, myrcon)  # clear area
 
    castle_maker.tower_building(272, 103, 207, width=25, height=11, length=20, butt_height=8, myrcon=myrcon)
    
    castle_maker.tower_building(272, 113, 207, width=25, height=11, length=20, butt_height=8, myrcon=myrcon)
    
    castle_maker.make_castle_walls(267, 80, 188, 28, 7,43, 1, myrcon)  # base
    
    castle_maker.make_castle_walls(272, 122, 207, 24, 4,20, 0, myrcon) # top parapet
    # works - matches line  - castle_maker.make_castle_walls(273, 122, 208, 22, 3,18, 0) # top parapet
    time.sleep(1) 

    # lower area
    castle_maker.tower_building(267, 86, 189, width=28, height=16, length=41, butt_height=10, myrcon=myrcon)
    castle_maker.make_castle_walls(267, 93, 189, 28, 4,41, 0, myrcon) # lower parapet
   
    time.sleep(1) 
       
       
       
    # left tower
    castle_base(256,80,147,275,108,168, myrcon) 
    castle_maker.tower_building(258, 85, 148, width=14, height=20, length=14, butt_height=4, myrcon=myrcon)
    castle_maker.make_castle_walls(259, 103, 149, 11, 3,11, 0, myrcon) # parapet

    
    time.sleep(1) 
    
    
    # right tower
    castle_base(224,83,257,248,108,278, myrcon) 
    castle_maker.tower_building(228, 84, 262, width=14, height=20, length=10, butt_height=4, myrcon=myrcon)
    castle_maker.make_castle_walls(229, 103, 263, 11, 3,7, 0, myrcon) # parapet
    
    time.sleep(1) 
    
    # decorations, doors, gates, etc
    castle_maker.stairs_NS(x=256, z=204, width=6, y_base=74, y_top=79, step='minecraft:stone_brick_stairs 2', bannister='minecraft:air', step_spacing=1, myrcon=myrcon)

    time.sleep(1) 
    
    
    # buildings 
    
 
 
def castle_base(x1,y1,z1,x2,y2,z2, myrcon):
    w = x2 - x1
    h = y2 - y1
    d = z2 - z1
    clear_area.wipe_all(x1-1, y1, z1-1, w+1, h+40, d+1, myrcon)  # clear area
    castle_maker.fill_area(x1,y1,z1,x2,y1,z2, 'minecraft:grass', myrcon)
    castle_maker.make_castle_walls(x1, y1,z1, w, 5,d, 4, myrcon)
    
    
  


main()  