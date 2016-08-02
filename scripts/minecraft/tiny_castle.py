# tiny_castle.py

import castle_maker
import clear_area
"""
    67        75       80    
-67 ....................       
    .                  .
35  . |-------|        .         
    . |       |        .        
    . |       |        .      
    . |-------|        .
-57 ............       .
               .       .
-52            .../  \..
       <S>
       
tower_building(x, y, z, width, height, length, butt_height, style=style_stone)       
make_castle_walls(start_x, start_y, start_z, width, height, length, wall_width)       
gate(x=78, y=63, z=-68, width=8, height=8, length=8)
fill_area(x1,y1,z1,x2,y2,z2, item)
"""

def main():
    clear_area.wipe_all(x = 65, y = 63, z = -71, w = 80, h = 15, d = 49)  # TOK clear bottom left corner

    # TO TEST SAME SIZE WALLS
    # castle_maker.make_castle_walls(67,63,-67,30,4,34, 6)  # big wall
    # castle_maker.gate(x=78, y=63, z=-68, width=8, height=8, length=8)
    
    castle_maker.fill_area(70,62,-77,110,62,-34, 'minecraft:grass')
    
    # really tiny castle
    castle_maker.make_castle_walls(70,63,-67,34,4,32, 2)  # outer wall
    castle_maker.gate(x=81, y=63, z=-68, width=3, height=6, length=4)
    castle_maker.tower_building(x=78, y=62, z=-55, width=11, height=5, length=10, butt_height=0)
    castle_maker.make_castle_walls(78,67,-55,10,1,9, 0)  # top parapet
 

main()