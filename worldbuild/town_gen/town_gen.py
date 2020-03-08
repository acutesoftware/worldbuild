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

    empty_plot = Building(0,0,0,  building_type = '.')
    road = Building(5,5,0,  building_type = '=')
    house_small = Building(2,3,1,  building_type = 'h')
    house_big = Building(4,5,2,  building_type = 'H')
    pub = Building(7,8,2,  building_type = 'P')
    town_hall = Building(9,9,1,  building_type = 'T')
    

    t = Town(0,0,sze_x,sze_y, empty_plot)

    # put a road down the middle
    for x in range(t.size_x):
        t.add_building(x,1,road)    

    t.add_building(1,0,house_small)
    t.add_building(4,0,house_small)
    t.add_building(8,2,house_big)



    t.add_building(0,0,pub)
    t.add_building(1,2,town_hall)

    


    '''
    # add 1 pub near outskirts (even if one exists)
    tx = random.randint(1, sze_x)
    t.add_building(1,tx, 'P')


    # add one and only one town hall near the centre
    tx = random.randint(int(sze_x/2) - 2, int(sze_y/2) + 2)
    t.add_building(2,tx,'T')
    '''

    print(t)

    return t
    



def print_town(lgrd):
    """
    prints the town to console
    """
    print(lgrd)



class Building(object):
    def __init__(self, max_x, max_y, max_z, building_type):
        if max_x == 0:
            self.x = 0        
            self.y = 0        
            self.z = 0      
        else:
            self.x = random.randint(1, max_x)        
            self.y = random.randint(1, max_y)        
            self.z = random.randint(0, max_z)      
        self.current_building = random.choice(buildings)
        self.building_type = building_type 
        #print(self)

    def __str__(self):
        res = 'building x=' + str(self.x) + ', y=' + str(self.y) + ', y=' + str(self.z) + '\n'    
        return res

class Town(object):
    """
    A town has a grid of size_y / size_x and each cell contains a plot.
    The plot is arbitralily 8x8 so a building can be up to 8x8. 
    This allows for random size buildings (most will be 3x3) to be 
    fitted onto a plot without worrying about space fitting algorithms.
    """
    def __init__(self, pos_y, pos_x, size_y, size_x,empty_plot):
        self.pos_x = pos_x
        self.pos_y =pos_y
        #self.size_x = random.randint(2, max_x)        
        #self.size_y = random.randint(2, max_y)        
        self.size_x = size_x  
        self.size_y =size_y
        self.empty_plot = empty_plot
        
        self.town_grid = [ [ empty_plot for dummy_x in range( size_x ) ] for dummy_y in range( size_y ) ]
        #print('town_grid = ', self.town_grid)
        #print(self)

    def __str__(self):
        res = 'Town located at  x=' + str(self.pos_x) + '/ y=' + str(self.pos_y) +  '\n' 
        res = 'SIZE:  x=' + str(self.size_x) + '/ y=' + str(self.size_y) +  '\n' 
        #res += str(self.grid)  
        for y in range(self.size_y ):
            for x in range(self.size_x):
                #print('town: y=', y, ', x=', x)
                if self.town_grid[y][x]:
                    res += self.town_grid[y][x].building_type
                else:
                    res += '.'                   
            res += '\n'
            
        return res

    def add_building(self, x,y, building):
        """
        adds type Building to the town at pos x,y
        """
        #self.grid.set_tile(y, x, building_type)
        self.town_grid[y][x] = building


if __name__ == '__main__':
    TEST()

