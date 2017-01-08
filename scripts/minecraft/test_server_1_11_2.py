# test_server_1_11_2.py

import castle_maker
import clear_area



# make a small tower room at spawn point (done)

# x = 56
# y = 64
# z = 224
# w = 11
# h = 6
# d = 8
# TOK - clear_area.wipe_all(x, y, z, w, h+10, d)
# TOK - castle_maker.tower_building(x, y, z, w, h, d, butt_height=5)

# make a castle at 235,77,200
x = 230
y = 74
z = 200
w = 40
h = 6
d = 35

clear_area.wipe_all(x-0, y, z-0, w+0, h+50, d+0)  # TOK clear bottom left corner

castle_maker.fill_area(x,y,z,x+w,y,z+d, 'minecraft:grass')
    
    
    
    