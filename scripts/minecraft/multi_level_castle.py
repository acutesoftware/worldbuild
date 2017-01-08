    # multi_level_castle.py
# Minecraft Server 1.11.2
# Seed: -7560993781265470572

import castle_maker
import clear_area


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
    

     #  town
    castle_base(230,74,200,270,78,254)
        
     # courtyard
    castle_base(250,79,164,273,84,204)
    clear_area.wipe_all(253, 80, 200, 12, 7, 12)  # clear area
    
    
    # Main Building (The Keep)
    castle_base(271,97,207,297,105,227)
    clear_area.wipe_all(265, 97, 205, 10, 6, 10)  # clear area
 
    castle_maker.tower_building(272, 103, 207, width=25, height=11, length=20, butt_height=8)
    
    castle_maker.tower_building(272, 113, 207, width=25, height=11, length=20, butt_height=8)
    
    castle_maker.make_castle_walls(267, 80, 188, 28, 7,43, 1)  # base
    
    castle_maker.make_castle_walls(273, 122, 207, 22, 3,18, 0) # top parapet

    castle_maker.tower_building(267, 86, 189, width=28, height=16, length=41, butt_height=10)
       
       
       
       
    # left tower
    castle_base(256,80,147,275,108,168) 
    castle_maker.tower_building(258, 85, 148, width=14, height=20, length=14, butt_height=4)
    castle_maker.make_castle_walls(259, 103, 149, 11, 3,11, 0) # parapet

    
    
    
    # right tower
    castle_base(224,83,257,248,108,278) 
    castle_maker.tower_building(228, 84, 262, width=14, height=20, length=10, butt_height=4)
    castle_maker.make_castle_walls(229, 103, 263, 11, 3,7, 0) # parapet
    
    
    # decorations, doors, gates, etc
    
    
    
    # buildings 
    
 
 
def castle_base(x1,y1,z1,x2,y2,z2):
    w = x2 - x1
    h = y2 - y1
    d = z2 - z1
    clear_area.wipe_all(x1-1, y1, z1-1, w+1, h+40, d+1)  # clear area
    castle_maker.fill_area(x1,y1,z1,x2,y1,z2, 'minecraft:grass')
    castle_maker.make_castle_walls(x1, y1,z1, w, 5,d, 4)
    
    
  


main()  