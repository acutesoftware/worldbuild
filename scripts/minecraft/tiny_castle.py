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
"""

def main():
    # make_castle_walls(start_x, start_y, start_z, width, height, length, wall_width)
    clear_area.wipe_all(x = 65, y = 63, z = -67, w = 80, h = 7, d = 39)  # TOK clear bottom left corner

    castle_maker.make_castle_walls(67,63,-67,30,4,34, 6)  # big wall
    castle_maker.gate(x=78, y=63, z=-68, width=8, height=8, length=8)
    
    
    #castle_maker.make_castle_walls(75,63,-57,15,4,5, 2)  # little wall
    #castle_maker.make_castle_walls(30,63,74,20,4,46, 6)  # castle

    #castle_maker.gate(x=86, y=63, z=43, width=8, height=8, length=8)
    
    # undercut on outer wall perimeter to stop spiders
    #castle_maker.fill_area(30,63,30,150,66,30, 'minecraft:air')   # front wall across very front
    #castle_maker.fill_area(76,63,30,76,66,44, 'minecraft:air')    # lhs inset near gate

main()