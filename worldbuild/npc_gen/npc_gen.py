#!/usr/bin/python3
# -*- coding: utf-8 -*-
# npc_gen.py

import os 
import sys
import random 

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." )
pth = root_folder #+ os.sep + 'worldbuild'
sys.path.append(pth)



### LOCAL PC (rawdata)
rawdata_folder = os.path.abspath(os.path.dirname(root_folder  + os.sep + ".." + os.sep + ".." ))  + os.sep + "rawdata"  + os.sep + "rawdata"
print('rawdata_folder = ' + rawdata_folder)
sys.path.append(rawdata_folder)
import generate as generate


### Public (when rawdata updated via pip install)
#import rawdata.generate as generate

"""
locations = [  # name,desc,coord_x,coord_y
['home','your home',0,0],
['road','main street',1,0],
['shop','General Store', 1,1],
['town_square','Town square with a nice fountain', 2,0],
['weapons', 'Weapons shop', 3,0],
['tavern','Old Tavern',4,0],
['old_house','Abandoned House',5,1 ],
]
"""

attitudes = [[-2,'negative'], [-1,'dismissmive'], [0,'neutral'], [1,'helpful'], [2, 'caring']]
professions = ['cook', 'farmer', 'builder', 'vet', 'woodworker', 'angler']
childhoods = ['poor', 'normal', 'privileged']

def TEST():
    column_headings, locations_data = read_csv_to_list(get_fullname('locations_world.csv'))
    print('generating NPC list...')

    npcs = make_npcs(10, locations_data)
    save_list_to_csv(npcs, 'random_npc.csv')

    relationships = estimate_npc_relationships(npcs)
    save_list_to_csv(relationships, 'npc_relationships.csv')

    
    print("Done")

def make_npcs(num_npcs, locations):
    """
    generates the NPC list
    """
    list_names = generate.get_list_people()
    npcs = [['npc_name', 'age', 'location', 'born', 'attitude', 'profession',  'childhood']]
    for i in range(1, num_npcs):
        nme = random.choice(list_names)
        age = get_random_age()
        location = random.choice(locations)[0]
        born =  generate.get_fantasy_name() #random.choice(generate.get_list_places())
        attitude = get_random_attitude() # random.choice(attitudes)[1]
        profession = random.choice(professions)
        childhood = random.choice(childhoods)
        this_npc = [nme, age, location, born, attitude, profession, childhood]
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
    return str(att[0]    )



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
    pers =  get_pers_desc(int(npc_spec[4]))
    prof = npc_spec[5] 
    childhood = npc_spec[6] 
    res = ''
    res += '------------------------------------------------\n'
    res += nme + ' is ' + age + ' years old and lives in ' + location + ', '
    res += 'where they work as a ' + prof + '\n'
    #res += nme + ' had a ' + childhood + ' childhood and have a ' + pers + ' personality.'

    print(res)

def get_pers_desc(pers_index):
    if pers_index == -2:
        return 'grumpy'
    elif pers_index == -1:
        return 'bored'
    if pers_index == 0:
        return 'normal'
    if pers_index == 1:
        return 'happy'
    if pers_index == 2:
        return 'helpful'
        

def get_fullname(fname):
    """
    gets full filename of crafting data from this folder
    """
    return os.path.join(root_folder,'worldbuild', 'data', fname)

def read_csv_to_list(fname):
    raw_data = []
    column_headings = []
    clean_data = []
    with open(fname, 'r') as fip:
        for line in fip:
            raw_data.append(line.strip('\n'))
    
    for line_num, raw_line in enumerate(raw_data):
        if raw_line.strip(' ') != '':
            cols = raw_line.split(',')
            if line_num == 0:
                column_headings = cols
            else:
                clean_data.append(cols)
    return column_headings, clean_data


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

def append_list_to_csv(lst, filename):
    """
    takes a list and saves to CSV
    """

    with open(filename, 'a', encoding='UTF-8') as f:
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
    res = [['npc1', 'npc2', 'relationship_score','welcome_message']]
    for npc1 in npcs[1:]:
        for npc2 in npcs[1:]:
            if npc1 != npc2:
                relationship_score = find_relationship_score(npc1, npc2)
                msg = get_welcome_message(npc1,npc2, relationship_score)
                relationship = [npc1[0], npc2[0], str(relationship_score), msg]
                res.append(relationship)
    return res

def find_relationship_score(npc1, npc2):
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
        
    # check professions
    if npc1[5] == npc2[5]:
        score += 20

    # bonus if we come from the same place
    if npc1[2] == npc2[2]:
        score += 20

    # modify THIS Npcs score based on their attitude
    score += int(npc1[4]) * 5


    return score


def get_welcome_message(npc1,npc2, relationship_score):
    

    msg = ''
    if npc1[5] == npc2[5]:
        msg = 'Oh, cool another ' + npc1[5]

        if npc1[2] == npc2[2]:
            msg += ' from ' + npc1[2] + ' as well! '
        else:
            msg +=  '! '
    else:
        if npc1[2] == npc2[2]:
            msg += 'Oh , you are from ' + npc1[2] + ' as well! '




    if relationship_score < 40:
        return msg + " What do you want!"
    if relationship_score < 50:
        return  msg + " <mutters to themselves>"
    if relationship_score < 60:
        return  msg + " hey"
    if relationship_score < 80:
        return  msg + " Hi, hows it going"
    if relationship_score < 100:
        return  msg + " Hey, great to see you again"
        
    return  msg + " *hugs*"


if __name__ == '__main__':
    TEST()

