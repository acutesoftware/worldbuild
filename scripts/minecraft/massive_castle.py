# massive_castle.py

import castle_maker
import clear_area
"""
   30        44        76         <N>        104         130      150   
30  ....................                     ......................    
35  .|-------|         .                     .           |-------|.
    .|       |         .                     .           |       |.
    .|       |         .         /   \       .           |       |.
44  .|-------|         ........./     \.......           |-------|.
    .                                                            .
    .                                                            .
 <E>.                                                            .  <W>
    .                                                            .
75  .........          |---------[  ]--------|          ..........
80          .          |                     |          .
            .          |                     |          .
            .          |                     |          .
            .          |                     |          .
100         . |----|   |                     |    |----|.
105         . |    |   |---------[  ]--------|    |    |.
            . |    |                              |    |.
115         . |----|                              |----|.
120         .............................................
                                 <S>
"""

def main():
    do_garden()
    do_walls()
    do_castle()
    do_towers()
    
def do_garden():    
    # set the ground
    castle_maker.fill_area(30,62,30,150,62,120, 'minecraft:dirt 2')

    # path from gate to castle door
    castle_maker.fill_area(85,62,30,95,62,75, 'minecraft:stone 6')
    castle_maker.fill_area(88,62,54,92,62,70, 'minecraft:stone 4')
    for z in range(54, 71, 4):
        castle_maker.set_block(87, 63, z,'minecraft:stone 4')
        castle_maker.set_block(93, 63, z,'minecraft:stone 4')
        castle_maker.set_block(87, 64, z,'minecraft:fence')
        castle_maker.set_block(93, 64, z,'minecraft:fence')
        castle_maker.set_block(87, 65, z,'minecraft:torch 0')
        castle_maker.set_block(93, 65, z,'minecraft:torch 0')

    # plant some trees near main path
    castle_maker.set_block(79, 63, 54,'minecraft:sapling 2')
    castle_maker.set_block(79, 63, 61,'minecraft:sapling 2')
    castle_maker.set_block(79, 63, 68,'minecraft:sapling 2')
    castle_maker.set_block(101, 63, 54,'minecraft:sapling 2')
    castle_maker.set_block(101, 63, 61,'minecraft:sapling 2')
    castle_maker.set_block(101, 63, 68,'minecraft:sapling 2')

    # front left corner
    castle_maker.fill_area(33,62,33,68,62,71, 'minecraft:grass')
    castle_maker.plant(x1=38,z1=47,x2=50,z2=59,y1=62, item='minecraft:carrots 3') # 'wheat', 
    castle_maker.plant(x1=38,z1=59,x2=50,z2=71,y1=62, item='minecraft:potatoes 3') # 'wheat', 
    castle_maker.plant(x1=52,z1=47,x2=64,z2=59,y1=62, item='minecraft:wheat 4') # 'wheat', 
    castle_maker.plant(x1=52,z1=59,x2=64,z2=71,y1=62, item='minecraft:pumpkin 2') # 'wheat', 

    # front right corner
    castle_maker.fill_area(112,62,33,142,62,71, 'minecraft:grass')
    castle_maker.plant(x1=115,z1=47,x2=127,z2=59,y1=62, item='minecraft:wheat 4') # 'wheat', 
    castle_maker.plant(x1=115,z1=59,x2=127,z2=71,y1=62, item='minecraft:potatoes 3') # 'wheat', 
    castle_maker.plant(x1=129,z1=47,x2=141,z2=59,y1=62, item='minecraft:carrots 4') # 'wheat', 
    castle_maker.plant(x1=129,z1=59,x2=141,z2=71,y1=62, item='minecraft:pumpkin 4') # 'wheat', 


def do_walls():
    # make outer walls (make a BIG square, a smaller square, then wipe the corners to match
    castle_maker.make_castle_walls(30,63,30,120,4,90, 6)  # TOK massive outer wall
    castle_maker.make_castle_walls(70,63,30,40,4,20, 6)  # TOK gate inset wall
    castle_maker.make_castle_walls(30,63,74,20,4,46, 6)  # TOK lower left inset wall
    castle_maker.make_castle_walls(130,63,74,20,4,46, 6)  # TOK lower right inset wall
    clear_area.wipe_all(x = 30, y = 63, z = 81, w = 10, h = 7, d = 49)  # TOK clear bottom left corner
    clear_area.wipe_all(x = 137, y = 63, z = 81, w = 13, h = 7, d = 49) # clear bottom right corner
    clear_area.wipe_all(x = 77, y = 63, z = 30, w = 26, h = 7, d = 8) # clear front gate inset


    castle_maker.gate(x=86, y=63, z=43, width=8, height=8, length=8)
    
    # undercut on outer wall perimeter to stop spiders
    castle_maker.fill_area(30,63,30,150,66,30, 'minecraft:air')   # front wall across very front
    castle_maker.fill_area(76,63,30,76,66,44, 'minecraft:air')    # lhs inset near gate
    castle_maker.fill_area(104,63,30,104,66,44, 'minecraft:air')  # rhs inset near gate
    castle_maker.fill_area(76,63,44,104,66,44, 'minecraft:air')   # across front gate (todo - put torches back

    castle_maker.fill_area(30,63,30,30,66,80, 'minecraft:air')    # Left wall - front 
    castle_maker.fill_area(34,63,80,44,66,120, 'minecraft:air')   # Left wall - back 

    castle_maker.fill_area(150,63,30,150,66,80, 'minecraft:air')  # Right wall - front 
    castle_maker.fill_area(136,63,80,136,66,120, 'minecraft:air') # Right wall - back 

    castle_maker.fill_area(30,63,120,150,66,120, 'minecraft:air') # back wall - very back
    castle_maker.fill_area(30,63,80,44,66,80, 'minecraft:air')    # lhs inset
    castle_maker.fill_area(136,63,80,150,66,80, 'minecraft:air')  # rhs inset


def do_castle():

    # main building- - multi layers
    castle_maker.tower_building(x=71, y=63, z=76, width=38, height=11, length=30, butt_height=7)
    castle_maker.make_castle_walls(70, 70,75, 40, 1,32, 0)  # TOK 

    castle_maker.tower_building(x=71, y=74, z=76, width=38, height=12, length=30, butt_height=6)
    castle_maker.make_castle_walls(70, 80,75, 40, 1,32, 0)  # TOK 

    castle_maker.tower_building(x=71, y=86, z=76, width=38, height=24, length=30, butt_height=12)
    castle_maker.make_castle_walls(70, 98,75, 40, 1,32, 0)  # TOK 

    castle_maker.tower_building(x=81, y=110, z=78, width=16, height=18, length=14, butt_height=2)  # front tower on top of main
    castle_maker.tower_building(x=73, y=110, z=93, width=10, height=22, length=10, butt_height=0)  # back right tower on top of main
    castle_maker.tower_building(x=97, y=110, z=93, width=10, height=22, length=10, butt_height=0)  # back left tower on top of main


    # merge 1st and 2nd floors
    castle_maker.fill_area(73,70,78,106,70,103, 'minecraft:air')
    # merge 2nd and 3rd floors
    castle_maker.fill_area(73,80,78,106,80,103, 'minecraft:air')
    
    # floor
    castle_maker.fill_area(72,63,77,109,63,105, 'minecraft:stone 4')
    
    # floor lighting (and roof of above floor using glowstones)
    castle_maker.tile_block(74, 63, 78, 106, 105, 5, 'minecraft:glowstone 0')
    castle_maker.tile_block(74, 74, 78, 106, 103, 5, 'minecraft:glowstone 0')
    castle_maker.tile_block(74, 86, 78, 106, 103, 5, 'minecraft:glowstone 0')
    castle_maker.tile_block(74, 98, 78, 106, 103, 5, 'minecraft:glowstone 0')
    castle_maker.tile_block(74, 110, 78, 106, 103, 5, 'minecraft:glowstone 0')
    
    castle_maker.main_door(x=90, y=63, z=75)  # coords for door are bottom centre - ornate stuff built out from there

    castle_maker.stairs_NS(x=88, z=87, width=4, y_base=64, y_top=74, step='minecraft:quartz_stairs 2', bannister='minecraft:quartz_block 2', step_spacing=1)

    # 2nd floor
    castle_maker.stairs_NS(x=74, z=90, width=2, y_base=74, y_top=87, step='minecraft:stone 4', bannister='minecraft:stone 4', step_spacing=1)
    castle_maker.stairs_NS(x=101, z=90, width=2, y_base=74, y_top=87, step='minecraft:stone 4', bannister='minecraft:stone 4', step_spacing=1)
    
    # 3rd floor 90,86,90 --> 98 
    castle_maker.stairs_NS(x=90, z=85, width=2, y_base=87, y_top=99, step='minecraft:quartz_stairs 2', bannister='minecraft:quartz_block 2', step_spacing=1)
    
    # 4th floor - 90 90 (y=98 -> 110
    castle_maker.stairs_NS(x=90, z=85, width=2, y_base=99, y_top=111, step='minecraft:quartz_stairs 2', bannister='minecraft:quartz_block 2', step_spacing=1)
    
    
def do_towers():
    castle_maker.make_castle_walls(35, 63,35,14,9,10, 3)  # top left tower
    castle_maker.tower_building(   37, 72,37,10,25,9, 0)  # top left tower
    castle_maker.make_castle_walls(37, 96,37, 9, 2,8, 0) 
    
    castle_maker.make_castle_walls(130,63,35,14,9,10, 2)  # top right tower
    castle_maker.tower_building(   132, 72,37,10,25,9, 0)  # top right tower
    castle_maker.make_castle_walls(132, 96,37, 9, 2,8, 0) 
    
    #castle_maker.make_castle_walls(50, 63,108,14,9, 10, 3)  # bottom left tower
    castle_maker.tower_building(   50, 63,106,9,34,9, 0)  # bottom left tower
    castle_maker.make_castle_walls(50, 96,106,8,2, 8, 0)  # bottom left tower

    #castle_maker.make_castle_walls(124,63,108,14,9,6, 3)  # bottom right tower
    castle_maker.tower_building(   122,63,106,9,34,9, 0)  # bottom left tower
    castle_maker.make_castle_walls(122,96,106,8,2,8, 0)  # bottom right tower


if __name__ == '__main__':                
    main()            






