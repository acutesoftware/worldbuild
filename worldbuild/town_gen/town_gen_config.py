#!/usr/bin/python3
# -*- coding: utf-8 -*-
# town_gen_config.py


##################################################
#  Building Specifications 
##################################################
# sizes are a tuple or x,y,z max sizes
# (each building fits in a grid cell, typically 10x10)
# z not used for now, but later in 3d render

road_size = (6, 10,0)
pub_size = (7,8,2)
shop_size = (3,5,1)
town_hall_size = (9,9,1)
house_small_size = (3,4,1)
house_big_size = (4,5,2)
empty_plot_size = (0,0,0)

# building types is the character used to display a 
# building in a simple ASCII map of the town

road_building_type = '='
pub_building_type =  'P'
shop_building_type = 'S'
town_hall_building_type = 'T'
house_small_building_type = 'h'
house_big_building_type = 'H'
empty_plot_building_type = '.'

# shops
num_shops_min = 1
num_shops_max = 6

# pubs
pub_add_if_size_x_greater = 10     # adds 2nd pub if map is wide enough (greater than x)
pub_add_if_sparse_perc_less = 50   # add another pub if sparse percentage less than this


 # 2D image variables
y_space_building = 100
x_space_building = 100

# draw building 2D
road_edge_y = 25
road_edge_colour = (181,101,29)
road_colour = "grey"
road_white_line_colour = "white"

house_border_colour = "grey"
house_body_colour = "peru"
house_roof_colour = "firebrick"

shop_border_colour = "red"
shop_colour = "yellow"

pub_border_colour = "white"
pub_colour = "blue"

town_hall_border_colour = "white"
town_hall_colour = "red"

empty_plot_chance_tree = 30    # percent chance of a tree showing in empty plot
tree_leaf_colour = "green"
tree_trunk_colour = "brown"
tree_chance_fruit = 90
tree_fruit_colours = ['red', 'red', 'red', 'yellow', 'orange', 'lime'] # multiple same values increase chance of that colour

