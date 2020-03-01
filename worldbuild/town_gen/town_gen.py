#!/usr/bin/python3
# -*- coding: utf-8 -*-
# town_gen.py

import os 
import sys
import random 



#import aikif.agents.explore.agent_explore_grid as mod_agt

import aikif.toolbox.cls_grid as mod_grid


buildings = ['H','h', 'P', 'S', 'T']
build_specs = {
    'H':99, 'h':99, 'P':2, 'S':5, 'T':1
}

def TEST():
    print('generating town...')
    dat_town = make_town(4)
    print_town(dat_town)


def make_town(sze):
    """
    generates the town
    [1,1,1,1,1,1,1]
    """
    #agt = mod_agt.ExploreAgent('TEST - exploring_agent',  os.getcwd(), 4, True)
    grd = mod_grid.Grid(grid_height=3, grid_width=sze, pieces=buildings, spacing=2)   

    #grd.new_tile()
    #grd.new_tile()
    #agt.set_world( grd, [3,4], [6,6])
    print(grd)


    for col in range(sze):

        current_building = random.choice(buildings)
       # if build_specs[current_building] > 1
        grd.set_tile(0, col, current_building)
        grd.set_tile(1, col, '-')
        if current_building in ['P','S','T']:
            grd.set_tile(2, col, '.')
        else:
            grd.set_tile(2, col, 'H')
        


    return grd
    



def print_town(dat_town):
    """
    prints the town to console
    """
    print(dat_town)




if __name__ == '__main__':
    TEST()

