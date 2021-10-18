#!/usr/bin/python3
# -*- coding: utf-8 -*-
# simulate_npc.py

import os
import random 

import quest 

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )

# setup simulation
locations = quest.Locations()
locations.fill_from_csv(os.path.join(root_folder,'data', 'locations_town.csv'))
locations.rebuild_list()

items = quest.Items()
items.fill_from_csv(os.path.join(root_folder,'data', 'items.csv'))

npcs = quest.NPCs()
npcs.fill_from_csv(os.path.join(root_folder,'data', 'npcs.csv'))
npcs.rebuild_list()

def main():
    cmd = 'start'
    while cmd != '':
        cmd = get_command()
        if cmd == '1':
            command_move()
        if cmd == '2':
            command_help()
        if cmd == 'n':
            command_list_npc()
        if cmd == 'l':
            command_list_location()


def get_command():
    # press enter manually for now, but game loop
    print('commands are:')
    print('1 = move (EventTick - all NPCs do their next move [may not be to timescale])')
    print('2 = help')
    print('n = list NPCs')
    print('l = list locations')
 
    
    cmd = input("enter command: ")
    return cmd

def command_move():
    """
    move the NPCs
    """

    print('moving NPCs')

    for npc_num, n in enumerate(npcs.object_list):
        new_location = get_new_location(n)
        if new_location is None:
            print(str(n.name) + ' is idle at ' + str(n.location) )    
        else:
            print(str(n.name) + ' moving to ' + new_location.name + ' (' + new_location.desc + ')')
            n.location = new_location
            npcs.object_list[npc_num] = n


def get_new_location(npc):
    """
    uses an NPC current location and goals to find thier new location
    """
    if random.randint(1,100) > 50:
        new_location = locations.object_list[random.randint(0,len(locations.object_list) - 1)]
        return new_location    
    else:
        return None

def command_help():
    """
    help the NPCs
    """
    print('Help Screen')
    print(' - modify the locations_town.csv for different coords')
    print(' - modify this file for different NPCs')
    
    

def command_list_npc():
    """
    List NPCs - location and goals
    """
    for n in npcs.object_list:
        print(str(n))


def command_list_location():
    for l in locations.object_list:
        print(str(l))




if __name__ == '__main__':
	main()
