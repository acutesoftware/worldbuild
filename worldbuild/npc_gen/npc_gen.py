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
    npcs = make_npcs(5)
    save_list_to_csv(npcs, 'random_npc.csv')

    relationships = estimate_npc_relationships(npcs)
    save_list_to_csv(relationships, 'npc_relationships.csv')
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

def get_attitude_id_from_name(nme):
    for att in attitudes:
        if nme == att[1]:
            return att[0]
    return 0

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


def estimate_npc_relationships(npcs):
    """
    does a cartesian product of all npcs to see how they might
    relate to each other based on location, background, etc
    """
    res = []
    for npc1 in npcs[1:]:
        for npc2 in npcs[1:]:
            if npc1 != npc2:
                relationship_score = find_relationship(npc1, npc2)
                msg = get_welcome_message(relationship_score)
                relationship = [npc1[0], npc2[0], str(relationship_score), msg]
                res.append(relationship)
    return res

def find_relationship(npc1, npc2):
    """
    returns a score from -100 to 100 between 2 npcs
    """
    score = 50

    #print('npc1 = ' + str(npc1) + '  npc2 = ' + str(npc2))

    att1 = get_attitude_id_from_name(npc1[4])
    att2 = get_attitude_id_from_name(npc2[4])
    #print('att1 = ' + str(att1) + '  att2 = ' + str(att2))
    score += att1 # assume niceness or nastiness affects relationships in general
    score += att2 # assume niceness or nastiness affects relationships in general
    
    age_diff = abs(npc1[1] - npc2[1])

    if age_diff == 0 :
        score += 10     # wow, we are the same age!
    elif age_diff < 10:
        score += age_diff    
    else:
        score -= age_diff    
        

    if npc2[1] - npc1[1] < 5:
        score += 10
    if npc2[1] - npc1[1] < 15:
        score += 5
    
    if npc1[1] - npc2[1] < 5:
        score += 10
    if npc1[1] - npc2[1] < 15:
        score += 5
        
    return score


def get_welcome_message(relationship_score):
    
    if relationship_score < 60:
        return "hey"
    if relationship_score < 80:
        return "Hi, hows it going"
    if relationship_score < 100:
        return "Hey, great to see you again"
        
    return "Hi love"


if __name__ == '__main__':
    TEST()

