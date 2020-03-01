#!/usr/bin/python3
# -*- coding: utf-8 -*-
# town_gen.py

import os 
import sys
import random 



#import aikif.agents.explore.agent_explore_grid as mod_agt

import aikif.toolbox.cls_grid as mod_grid


buildings = [ 'H','h', 'H','h', 'H','h', 'P', 'S', 'S', 'S']
build_specs = {
    'H':99, 'h':99, 'P':2, 'S':5, 'T':1
}

def TEST():
    print('generating town...')
    dat_town = make_town(14)
    print_town(dat_town)


def make_town(sze):
    """
    generates the town
    [1,1,1,1,1,1,1]
    """
    #agt = mod_agt.ExploreAgent('TEST - exploring_agent',  os.getcwd(), 4, True)
    grd = mod_grid.Grid(grid_height=3, grid_width=sze, pieces=buildings, spacing=2)   



    for col in range(sze):

        current_building = random.choice(buildings)
       # if build_specs[current_building] > 1
        grd.set_tile(0, col, current_building)
        grd.set_tile(1, col, '-')
        if current_building in ['P','S']:
            grd.set_tile(2, col, '.')
        else:
            grd.set_tile(2, col, 'H')
        
    # add 1 pub near outskirts (even if one exists)
    tx = random.randint(0, 3)
    grd.set_tile(2, tx, 'P')

    # add one and only one town hall near the centre
    tx = random.randint(int(sze/2) - 2, int(sze/2) + 2)
    grd.set_tile(2, tx, 'T')

    return grd
    



def print_town(lgrd):
    """
    prints the town to console
    """
    print(lgrd)




if __name__ == '__main__':
    TEST()

