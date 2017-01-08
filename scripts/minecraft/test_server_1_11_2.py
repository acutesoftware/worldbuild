# test_server_1_11_2.py

import castle_maker
import clear_area


x = 56
y = 64
z = 224
w = 11
h = 6
d = 8

clear_area.wipe_all(x, y, z, w, h+10, d)
castle_maker.tower_building(x, y, z, w, h, d, butt_height=5)
