#!/usr/bin/python3
# -*- coding: utf-8 -*-
# simulate_npc.py

import os
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
        if cmd == '3':
            command_fight()


def get_command():
    # press enter manually for now, but game loop
    print('commands are:')
    print('1 = move')
    print('2 = help')
    print('3 = fight')
 
    
    cmd = input("enter command: ")
    return cmd

def command_move():
    """
    move the NPCs
    """
    import random 

    print('moving NPCs')

    for n in npcs.object_list:
        new_location = locations.object_list[random.randint(1,3)]
        print(str(n.name) + ' moving to ' + new_location.name + ' (' + new_location.desc + ')')
    


def command_help():
    """
    help the NPCs
    """
    print('Help Screen')
    print(' - modify the locations_town.csv for different coords')
    print(' - modify this file for different NPCs')
    
    

def command_fight():
    """
    NPCs attack
    """
    print('not yet implemented')


if __name__ == '__main__':
	main()
