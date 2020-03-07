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
    dat_town = make_town(3, 5)
    print_town(dat_town)


def make_town(sze_x, sze_y):
    """
    generates the town
    """
    #agt = mod_agt.ExploreAgent('TEST - exploring_agent',  os.getcwd(), 4, True)
    #grd = mod_grid.Grid(grid_height=3, grid_width=sze, pieces=buildings, spacing=2)   

    t = Town(0,0,sze_x,sze_y)

    t.add_building(1,1,Building(3,3,1))


    # add 1 pub near outskirts (even if one exists)
    tx = random.randint(1, sze_x)
    t.add_building(1,tx, 'P')


    # add one and only one town hall near the centre
    tx = random.randint(int(sze_x/2) - 2, int(sze_y/2) + 2)
    t.add_building(2,tx,'T')

    return t
    



def print_town(lgrd):
    """
    prints the town to console
    """
    print(lgrd)



class Building(object):
    def __init__(self, max_x, max_y, max_z, building_type = 'H'):
        self.x = random.randint(2, max_x)        
        self.y = random.randint(2, max_y)        
        self.z = random.randint(0, max_z)      
        self.current_building = random.choice(buildings)
        self.building_type = building_type 

    def __str__(self):
        res = 'building x=' + str(self.x) + ', y=' + str(self.y) + ', y=' + str(self.z) + '\n'    
        return res

class Town(object):
    def __init__(self, pos_x, pos_y, max_x, max_y):
        self.pos_x = pos_x
        self.pos_y =pos_y
        #self.size_x = random.randint(2, max_x)        
        #self.size_y = random.randint(2, max_y)        
        self.size_x = max_x  
        self.size_y =max_y
        self.grid =  mod_grid.Grid(grid_height=self.size_y, grid_width=self.size_x, pieces=buildings, spacing=2)   


    def __str__(self):
        res = 'Town located at  x=' + str(self.pos_x) + '/ y=' + str(self.pos_y) +  '\n' 
        res += str(self.grid)   
        return res

    def add_building(self, x,y, building_type):
        """
        adds type Building to the town at pos x,y
        """
        self.grid.set_tile(y, x, building_type)


if __name__ == '__main__':
    TEST()

