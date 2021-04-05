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
    res = make_npcs(20)
    save_list_to_csv(res, 'random_npc.csv')
    print("Done")

def make_npcs(num_npcs):
    """
    generates the NPC list
    """
    list_names = generate.get_list_people()
    npcs = [['npc_name', 'age', 'location']]
    for i in range(1, num_npcs):
        nme = random.choice(list_names)
        age = random.randint(16,60)
        location = random.choice(locations[1:])[0]

        npcs.append([nme, age, location])

    return npcs
    

def save_list_to_csv(lst, filename):
    """
    takes a list and saves to CSV
    """

    with open(filename, 'w', encoding='UTF-8') as f:
        for row in lst:
            for col in row:
                if col:
                    f.write( '"' + str(col) + '",')
                else:
                    f.write('"",')
            f.write('\n')


if __name__ == '__main__':
    TEST()

