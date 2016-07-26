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

clear_area.wipe_all(x = 77, y = 63, z = 30, w = 22, h = 7, d = 8) # clear front gate inset




castle_maker.make_castle_walls(35, 63,35,14,9,10, 2)  # top left tower
castle_maker.make_castle_walls(130,63,35,14,9,10, 2)  # top right tower
castle_maker.make_castle_walls(70,63,75,40,7,30, 2)  # main building 
castle_maker.make_castle_walls(55, 63,100,6,12, 6, 0)  # bottom left tower
castle_maker.make_castle_walls(120,63,100,6,12,6, 0)  # bottom right tower









"""
    # build outer walls
    mcb.make_from_list(castle_wall(start_x,start_y,start_z,North, width,height, style_stone, wall_width)) # TOK
    mcb.make_from_list(castle_wall(start_x,start_y,start_z,East,  length,height, style_stone, wall_width)) # TOK
    
    mcb.make_from_list(castle_wall(start_x,start_y,start_z+length-wall_width,North, width ,height, style_stone, wall_width))
    mcb.make_from_list(castle_wall(start_x+width-wall_width,start_y,start_z, East, length, height, style_stone, wall_width))
"""


