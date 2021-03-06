# medium_castle.py

import castle_maker
import clear_area


x = 1208
y = 98
z = -1924
w = 34+18
h = 6
d = 33

def main():
    
    myrcon = castle_maker.rcon_connection()
    castle_maker.teleport_player('craftandstore',x-10,y,z, myrcon)
    clear_area.wipe_all(x-1, y, z-1, w+3, h+50, d+3, myrcon)  # TOK clear bottom left corner

    castle_maker.fill_area(x,y,z,x+w,y,z+d, 'minecraft:grass', myrcon)
    
    # make_castle_walls(start_x, start_y, start_z, width, height, length, wall_width):
    castle_maker.make_castle_walls(x,y,z,w,h,d, 4, myrcon)  # outer wall
    
    """
    castle_maker.gate(1239, y+1, -1925, width=7, height=9, length=6, myrcon)
    
    castle_maker.tower_building(x+3, y+0, z+6, width=25, height=8, length=21, butt_height=6, myrcon)
    castle_maker.tower_building(x+3, y+9, z+6, width=25, height=8, length=21, butt_height=7, myrcon)
 
    castle_maker.make_castle_walls(x+3, y+16,z+6, 25, 4,21, 1, myrcon)  # TOK 
    """
    
main()