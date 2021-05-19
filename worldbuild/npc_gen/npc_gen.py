#!/usr/bin/python3
# -*- coding: utf-8 -*-
# npc_gen.py

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

attitudes = [[-9,'nasty'], [-5,'dismissmive'], [0,'neutral'], [5,'helpful'], [9, 'caring']]
professions = ['cook', 'farmer', 'builder', 'vet', 'woodworker', 'helper']
childhoods = ['poor', 'normal', 'privileged']

def TEST():
    print('generating NPC list...')
    res = make_npcs(50)
    save_list_to_csv(res, 'random_npc.csv')
    print("Done")

def make_npcs(num_npcs):
    """
    generates the NPC list
    """
    list_names = generate.get_list_people()
    npcs = [['npc_name', 'age', 'location', 'born', 'attitude', 'profession', 'work_location', 'childhood']]
    for i in range(1, num_npcs):
        nme = random.choice(list_names)
        age = get_random_age()
        location = random.choice(locations[1:])[1]
        born =  random_fantasy_name() #random.choice(generate.get_list_places())
        attitude = get_random_attitude() # random.choice(attitudes)[1]
        profession = random.choice(professions)
        work_location =  random_fantasy_name() #random.choice(locations[1:])[1]
        childhood = random.choice(childhoods)
        this_npc = [nme, age, location, born, attitude, profession, work_location, childhood]
        describe_npc(this_npc)
        npcs.append(this_npc)

    return npcs

def get_random_attitude():
    """
    mostly gets a nice attitude, but occasionally random
    """
    att = random.choice(attitudes)
    if att[0] < 3 :
        att =random.choice(attitudes)
    if att[0] < 3 :
        att =random.choice(attitudes)
    if att[0] < 3 :
        att =random.choice(attitudes)
    if att[0] < 3 :
        att =random.choice(attitudes)
    return att[1]    


def random_fantasy_name():
    pre = ['Al', 'El', 'Prom', 'Wec', 'Plab', 'Son', 'Isa', 'Wol']
    post = ['form', 'lest', 'gorn', 'sed', 'ard', 'stand', 'kite']

    return random.choice(pre) + random.choice(post)

def get_random_age():
    """
    mostly gets a young person, but occasionally random
    """
    age = random.randint(16,50)
    if age > 30:
        age = random.randint(16,50)
    else:
        return age
    if age > 25:
        age = random.randint(16,50)
    else:
        return age
    if age > 20:
        age = random.randint(16,50)
    return age


def describe_npc(npc_spec):
    """
    using the spec and reference tables, gives a short narrative about an NPC
    """
    #print('npc spec for ....' + str(npc_spec))
    nme = npc_spec[0]
    age = str(npc_spec[1])
    location = npc_spec[2] 
    born = npc_spec[3] 
    pers = npc_spec[4] 
    prof = npc_spec[5] 
    work = npc_spec[6] 
    childhood = npc_spec[7] 
    res = ''
    res += '------------------------------------------------\n'
    res += nme + ' was born ' + age + ' years ago in ' + born + '\n'
    res += 'They work as ' + prof + ' in ' + work + '\n'
    res += nme + ' had a ' + childhood + ' childhood and have a ' + pers + ' personality.'

    print(res)
    
    

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

