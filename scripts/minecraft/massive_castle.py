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

#clear_area.wipe_all(x = 28, y = 63, z = 25, w = 275, h = 15, d = 150)
# make_castle_walls(start_x, start_y, start_z, width, height, length, wall_width)

def main():
    #do_walls()
    #do_castle()
    do_towers()
    #do_garden()
    
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


    # front left corner
    castle_maker.fill_area(33,62,33,68,62,71, 'minecraft:grass')
    castle_maker.plant(x1=38,z1=47,x2=50,z2=59,y1=62, item='minecraft:carrots 3') # 'wheat', 
    castle_maker.plant(x1=38,z1=59,x2=50,z2=71,y1=62, item='minecraft:potatoes 3') # 'wheat', 
    castle_maker.plant(x1=52,z1=47,x2=64,z2=59,y1=62, item='minecraft:wheat 4') # 'wheat', 
    castle_maker.plant(x1=52,z1=59,x2=64,z2=71,y1=62, item='minecraft:pumpkin 2') # 'wheat', 

    #castle_maker.fill_area(49,65,53,55,62,59, 'minecraft:wheat_seeds 2')



    # front right corner
    castle_maker.fill_area(112,62,33,142,62,71, 'minecraft:grass')

    castle_maker.plant(x1=115,z1=47,x2=127,z2=59,y1=62, item='minecraft:wheat 4') # 'wheat', 
    castle_maker.plant(x1=115,z1=59,x2=127,z2=71,y1=62, item='minecraft:potatoes 3') # 'wheat', 

    castle_maker.plant(x1=129,z1=47,x2=141,z2=59,y1=62, item='minecraft:carrots 4') # 'wheat', 
    castle_maker.plant(x1=129,z1=59,x2=141,z2=71,y1=62, item='minecraft:pumpkin 4') # 'wheat', 



    # plant some trees
    castle_maker.set_block(79, 63, 54,'minecraft:sapling 2')
    castle_maker.set_block(79, 63, 61,'minecraft:sapling 2')
    castle_maker.set_block(79, 63, 68,'minecraft:sapling 2')
    castle_maker.set_block(101, 63, 54,'minecraft:sapling 2')
    castle_maker.set_block(101, 63, 61,'minecraft:sapling 2')
    castle_maker.set_block(101, 63, 68,'minecraft:sapling 2')


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

    castle_maker.main_door(x=90, y=64, z=75)  # coords for door are bottom centre - ornate stuff built out from there

    # Tower battlements - mid height
    #clear_area.wipe_all(x = 28, y = 63, z = 25, w = 275, h = 15, d = 150)
    # make_castle_walls(start_x, start_y, start_z, width, height, length, wall_width)

    castle_maker.make_castle_walls(35, 63,35,14,9,10, 2)  # top left tower
    castle_maker.make_castle_walls(130,63,35,14,9,10, 2)  # top right tower
    castle_maker.make_castle_walls(70,63,75,40,7,30, 2)  # main building 

def do_towers():
        
    #      tower_building(x, y, z, width, height, length, butt_height, style=style_stone)
    castle_maker.make_castle_walls(35, 63,35,14,9,10, 3)  # top left tower
    castle_maker.tower_building(   37, 72,37,10,25,8, 3)  # top left tower
    castle_maker.make_castle_walls(37, 96,37, 9, 2,7, 0) 
    
    castle_maker.make_castle_walls(130,63,35,14,9,10, 2)  # top right tower
    castle_maker.tower_building(   132, 72,37,10,25,8, 3)  # top right tower
    castle_maker.make_castle_walls(132, 96,37, 9, 2,7, 0) 
    
    #castle_maker.make_castle_walls(50, 63,108,14,9, 10, 3)  # bottom left tower
    castle_maker.tower_building(   50, 63,106,9,34,9, 0)  # bottom left tower
    castle_maker.make_castle_walls(50, 96,106,8,2, 8, 0)  # bottom left tower

    #castle_maker.make_castle_walls(124,63,108,14,9,6, 3)  # bottom right tower
    castle_maker.tower_building(   122,63,106,9,34,9, 0)  # bottom left tower
    castle_maker.make_castle_walls(122,96,106,8,2,8, 0)  # bottom right tower

    # tower buildings


 

if __name__ == '__main__':                
    main()            






