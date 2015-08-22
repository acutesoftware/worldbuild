# build_world.py

import os
import sys
import math
from random import randint 
import aikif.environments.worlds as my_world
import aikif.agents.explore.agent_explore_grid as agt

temp_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'temp') + os.sep
fldr = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
LOG_LEVEL = 2

#print('temp_folder = ', temp_folder)

def main():
    """
    generates a random world, sets terrain and runs agents in it
    """
    width       =   79  # grid width  (takes about 5 minutes to generate 500x400 grid with 8% blockages)
    height      =   50  # grid height
    num_seeds   =    4   # number of seed points to start land generation
    perc_land   =   15   # % of world that is land
    perc_sea    =   85   # % of world that is sea
    perc_blocked=    2   # % of world that is blocked
    
    myWorld = my_world.World( height, width, [' ','x','#']) 
    myWorld.build_random( num_seeds, perc_land, perc_sea, perc_blocked)
    myWorld.grd.save(fldr + os.sep + 'sample_world.txt')
    
    #Create some agents to walk the grid
    iterations  = 50   # how many simulations to run
    num_agents  =  5   # number of agents to enter the world
    target_coords = [math.floor(myWorld.grd.grid_height/2) + randint(1, math.floor(myWorld.grd.grid_height/2)) - 3, \
                     math.floor(myWorld.grd.grid_width /2) + randint(1, math.floor(myWorld.grd.grid_width/2)) - 5]
    agt_list = []
    for agt_num in range(0,num_agents):
        ag = agt.ExploreAgent( 'wb_agent' + str(agt_num),  temp_folder, False, LOG_LEVEL)
        start_y, start_x = myWorld.grd.find_safe_starting_point()
        ag.set_world(myWorld.grd, [start_y, start_x], target_coords)
        agt_list.append(ag)
    sim = my_world.WorldSimulation(myWorld, agt_list, LOG_LEVEL)
    sim.run(iterations, 'Y', temp_folder)
    
    #print('saving sim to ', fldr + os.sep + 'world_traversed.txt')
    sim.world.grd.save(fldr + os.sep + 'world_traversed.txt')
 

