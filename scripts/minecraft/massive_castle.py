# massive_castle.py

import castle_maker
import clear_area
"""
   30        50        70                   110         130      150   
30  ....................                     ......................    
35  .|-------|         .                     .           |-------|.
    .|       |         .                     .           |       |.
    .|       |         .         /   \       .           |       |.
50  .|-------|         ........./     \.......           |-------|.
    .                                                            .
    .                                                            .
    .                                                            .
    .                                                            .
75  .........          |---------[  ]--------|          ..........
            .          |                     |          .
            .          |                     |          .
            .          |                     |          .
            .          |                     |          .
100         . |----|   |                     |    |----|.
105         . |    |   |---------[  ]--------|    |    |.
            . |    |                              |    |.
115         . |----|                              |----|.
120         .............................................

"""

#clear_area.wipe_all(x = 28, y = 63, z = 25, w = 275, h = 15, d = 150)
# make_castle_walls(start_x, start_y, start_z, width, height, length, wall_width)


# make outer walls (make a BIG square, a smaller square, then wipe the corners to match
castle_maker.make_castle_walls(30,63,30,120,4,90, 6)  # TOK massive outer wall
castle_maker.make_castle_walls(70,63,30,40,4,20, 6)  # TOK gate inset wall
castle_maker.make_castle_walls(30,63,74,20,4,46, 6)  # TOK lower left inset wall
castle_maker.make_castle_walls(130,63,74,20,4,46, 6)  # TOK lower right inset wall
clear_area.wipe_all(x = 30, y = 63, z = 81, w = 10, h = 7, d = 49)  # TOK clear bottom left corner
clear_area.wipe_all(x = 137, y = 63, z = 81, w = 13, h = 7, d = 49) # clear bottom right corner
clear_area.wipe_all(x = 77, y = 63, z = 30, w = 26, h = 7, d = 8) # clear front gate inset

# Tower battlements - mid height
castle_maker.make_castle_walls(35, 63,35,14,9,10, 2)  # top left tower
castle_maker.make_castle_walls(130,63,35,14,9,10, 2)  # top right tower
castle_maker.make_castle_walls(70,63,75,40,7,30, 2)  # main building 
castle_maker.make_castle_walls(55, 63,100,6,22, 6, 0)  # bottom left tower
castle_maker.make_castle_walls(120,63,100,6,22,6, 0)  # bottom right tower


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


# tower buildings
castle_maker.tower_building(   37, 72,37,10,25,8, 3)  # top left tower
castle_maker.make_castle_walls(37, 96,37, 9, 3,7, 1)  # TOK lower left inset wall


castle_maker.tower_building(   132, 72,37,10,25,8, 3)  # top right tower
castle_maker.make_castle_walls(132, 96,37, 9, 3,7, 1)  # TOK lower left inset wall


