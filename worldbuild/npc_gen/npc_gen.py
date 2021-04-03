#!/usr/bin/python3
# -*- coding: utf-8 -*-
# town_gen.py

import os 
import sys
import random 

import os
import sys 

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." )
pth = root_folder #+ os.sep + 'worldbuild'
sys.path.append(pth)

import worldbuild.town_gen.town_gen_config as cfg

import rawdata.generate as generate
import random

locations = [  # name,desc,coord_x,coord_y
['home','your home',0,0],
['road','main street',1,0],
['shop','General Store', 1,1],
['town_square','Town square with a nice fountain', 2,0],
['weapons', 'Weapons shop', 3,0],
['tavern','Old Tavern',4,0],
['old_house','Abandoned House',5,1 ],
]

def TEST():
    print('generating NPC list...')
    make_npcs(10)


def make_npcs(num_npcs):
    """
    generates the NPC list
    """
    list_names = generate.get_list_people()
    npcs = []
    for i in range(1, num_npcs):
        nme = random.choice(list_names)
        age = random.randint(16,60)
        location = random.choice(locations[1:])[0]

        npcs.append([nme, age, location])

    print(npcs)
    

if __name__ == '__main__':
    TEST()

